# pipeline.py
# Trabajo Final: Pipeline Completo (Descarga -> ETL Spark -> Análisis EDA/Visual)
# Tema: Desarrollo Político-Económico en el Magreb: Autoritarismo vs Democracia
# Autor: Carlos Rivasplata

import sys
import os
import requests
from pathlib import Path

# --- CONFIGURACIÓN DE RUTAS PARA SPARK (DOCKER) ---
spark_home = os.environ.get('SPARK_HOME', '/opt/spark')
sys.path.append(os.path.join(spark_home, 'python'))
py4j_path = os.path.join(spark_home, 'python', 'lib')
if os.path.exists(py4j_path):
    py4j_zips = [f for f in os.listdir(py4j_path) if f.startswith("py4j") and f.endswith(".zip")]
    if py4j_zips:
        sys.path.append(os.path.join(py4j_path, py4j_zips[0]))
# --------------------------------------------------

from pyspark.sql import SparkSession, functions as F
from pyspark.sql.types import DoubleType, StringType
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# --- CONFIGURACIÓN GLOBAL ---
URL_QOG = "https://www.qogdata.pol.gu.se/data/qog_std_cs_jan26.csv"
RUTA_BASE = "/workspace"
RUTA_CSV = f"{RUTA_BASE}/datos/qog/qog_std_cs_jan26.csv"
RUTA_PARQUET = f"{RUTA_BASE}/outputs/parquet/magreb_qog_analisis"
RUTA_GRAFICOS = f"{RUTA_BASE}/outputs/graficos"

# Países del Magreb (Marruecos, Argelia, Túnez, Libia, Mauritania)
PAISES_SELECCIONADOS = ["MAR", "DZA", "TUN", "LBY", "MRT"]

def asegurar_directorio(ruta):
    if not os.path.exists(ruta):
        os.makedirs(ruta)

# ==========================================
# 1. DESCARGA DE DATOS
# ==========================================
def descargar_datos():
    print("\n[PASO 1] Descargando datos QoG...")
    # Aseguramos que exista la carpeta
    carpeta_destino = os.path.dirname(RUTA_CSV)
    asegurar_directorio(carpeta_destino)
    
    print(f"==> URL: {URL_QOG}")
    print(f"==> Destino: {RUTA_CSV}")
    
    try:
        r = requests.get(URL_QOG, timeout=120)
        r.raise_for_status()
        with open(RUTA_CSV, 'wb') as f:
            f.write(r.content)
        print("✅ Descarga completada y archivo sobrescrito.")
    except Exception as e:
        print(f"❌ Error en la descarga: {e}")
        sys.exit(1)

# ==========================================
# 2. ETL CON SPARK
# ==========================================
def crear_spark() -> SparkSession:
    return SparkSession.builder.appName("QoG-Magreb-Pipeline").getOrCreate()

def run_etl():
    print("\n[PASO 2] Iniciando ETL con Spark...")
    spark = crear_spark()

    # Leer CSV
    print(f"==> Leyendo CSV desde: {RUTA_CSV}")
    df = spark.read.option("header", True).option("inferSchema", True).csv(RUTA_CSV)

    # Mapeo de variables clave con ALTERNATIVAS
    # Si la principal no existe, buscamos la alternativa
    cols_config = [
        {"alias": "pais_iso",       "candidates": ["ccodealp", "ccode"], "type": StringType()},
        {"alias": "pais_nombre",    "candidates": ["cname", "cname_qog"], "type": StringType()},
        {"alias": "democracia",     "candidates": ["vdem_polyarchy", "polity2", "fh_pr"], "type": DoubleType()},
        {"alias": "pib_pc",         "candidates": ["wdi_gdppc", "mad_gdppc", "wdi_gdpc"], "type": DoubleType()},
        {"alias": "corrupcion",     "candidates": ["ti_cpi", "vdem_corr", "icrg_qog"], "type": DoubleType()},
        {"alias": "estabilidad",    "candidates": ["wgi_pv", "icrg_stability", "gpi_gpi"], "type": DoubleType()},
        {"alias": "esperanza_vida", "candidates": ["wdi_lifexp", "undp_hdi"], "type": DoubleType()}
    ]
    
    available_cols = df.columns
    select_exprs = []

    for item in cols_config:
        found = False
        for cand in item["candidates"]:
            if cand in available_cols:
                print(f"   -> Variable '{item['alias']}' encontrada como: {cand}")
                select_exprs.append(F.col(cand).cast(item["type"]).alias(item["alias"]))
                found = True
                break
        
        if not found:
            print(f"⚠️ Variable '{item['alias']}' NO encontrada. Se llenará con NULL (tipo {item['type']}).")
            # AQUÍ ESTÁ LA CORRECCIÓN: Casteamos el NULL al tipo correcto
            select_exprs.append(F.lit(None).cast(item["type"]).alias(item["alias"]))

    df_clean = df.select(*select_exprs)

    # Filtrar Países (Magreb)
    # Nota: Si pais_iso terminó siendo numérico (ccode), el filtro por strings fallará.
    # Intentamos detectar si es string o no.
    # Pero para simplificar, asumimos que si se encontró ccodealp es string.
    
    # Verificamos si pais_iso es string o double en el esquema actual
    iso_type = [f.dataType for f in df_clean.schema.fields if f.name == "pais_iso"][0]
    
    if isinstance(iso_type, StringType):
        df_clean = df_clean.filter(F.col("pais_iso").isin(PAISES_SELECCIONADOS))
    else:
        print("⚠️ 'pais_iso' parece ser numérico. No se puede filtrar por códigos ISO-3 (MAR, DZA...).")
        print("   Se omitirá el filtro de países para evitar errores (se procesarán todos).")

    # Variables Derivadas
    # 1. Categoría de Régimen
    df_clean = df_clean.withColumn(
        "categoria_regimen",
        F.when(F.col("democracia") > 0.7, "Democracia")
         .when(F.col("democracia") > 0.4, "Híbrido")
         .otherwise("Autoritario")
    )

    # 2. Índice de Desarrollo Institucional (PIB ajustado por corrupción)
    # Normalizamos PIB (log) * (Corrupción/100)
    df_clean = df_clean.withColumn(
        "indice_inst",
        (F.log(F.col("pib_pc")) * (F.col("corrupcion") / 100))
    )

    # Guardar Parquet
    print(f"==> Guardando resultado ETL en: {RUTA_PARQUET}")
    df_clean.write.mode("overwrite").parquet(RUTA_PARQUET)
    
    print("==> Preview de datos procesados:")
    df_clean.show()
    spark.stop()
    print("✅ ETL Finalizado.")

# ==========================================
# 3. ANÁLISIS EDA Y VISUALIZACIÓN
# ==========================================
def run_analysis():
    print("\n[PASO 3] Iniciando Análisis EDA y Visualización...")
    asegurar_directorio(RUTA_GRAFICOS)

    # Cargar datos procesados
    try:
        df = pd.read_parquet(RUTA_PARQUET)
        print(f"==> Datos cargados: {len(df)} registros.")
    except Exception as e:
        print(f"❌ Error leyendo Parquet: {e}")
        return

    # --- JUSTIFICACIÓN DE MODELO ---
    print("\n--- JUSTIFICACIÓN DE MODELO ---")
    print("El dataset utilizado es de tipo 'Cross-Section' (Corte Transversal), conteniendo datos de un solo año reciente.")
    print("Por esta razón, se descartan los siguientes modelos:")
    print("1. Series Temporales (Panel Data): No hay evolución temporal (años) para analizar tendencias.")
    print("2. Clustering Complejo: Con solo 5 observaciones (países), un algoritmo como K-Means no tiene suficiente varianza.")
    print("SELECCIÓN: Se procede con un ANÁLISIS COMPARATIVO y CORRELACIONAL (EDA Visual).")
    print("-------------------------------\n")

    # --- EDA BÁSICO ---
    print("--- ESTADÍSTICAS DESCRIPTIVAS ---")
    print(df.describe())
    print("\n--- CONTEO DE NULOS ---")
    print(df.isnull().sum())
    print("---------------------------------\n")

    # Ordenar por democracia para gráficos
    if "democracia" in df.columns and not df["democracia"].isnull().all():
        df = df.sort_values("democracia", ascending=False)

    # --- GRÁFICO 1: Comparación de Democracia (Barras) ---
    if "democracia" in df.columns and "pais_iso" in df.columns:
        plt.figure(figsize=(10, 6))
        sns.barplot(data=df, x="pais_iso", y="democracia", palette="viridis")
        plt.title("Nivel de Democracia en el Magreb (V-Dem)", fontsize=14)
        plt.ylabel("Índice (0=Autocracia, 1=Democracia)")
        plt.axhline(0.5, color='red', linestyle='--', label="Umbral Democrático")
        plt.legend()
        plt.savefig(os.path.join(RUTA_GRAFICOS, "01_comparacion_democracia.png"))
        plt.close()
        print("✅ Gráfico 1 guardado: Comparación Democracia")

    # --- GRÁFICO 2: Democracia vs PIB (Scatter) ---
    if "democracia" in df.columns and "pib_pc" in df.columns:
        # Eliminar nulos para el scatter
        df_scatter = df.dropna(subset=["pib_pc", "democracia"])
        if not df_scatter.empty:
            plt.figure(figsize=(10, 6))
            sns.scatterplot(data=df_scatter, x="pib_pc", y="democracia", hue="pais_iso", s=300, palette="deep")
            
            # Etiquetas
            for i in range(len(df_scatter)):
                plt.text(df_scatter.iloc[i]["pib_pc"]+100, df_scatter.iloc[i]["democracia"], df_scatter.iloc[i]["pais_iso"])

            plt.title("Relación Riqueza (PIB pc) vs Democracia", fontsize=14)
            plt.xlabel("PIB per Cápita (USD)")
            plt.ylabel("Índice de Democracia")
            plt.grid(True, alpha=0.3)
            plt.savefig(os.path.join(RUTA_GRAFICOS, "02_democracia_vs_pib.png"))
            plt.close()
            print("✅ Gráfico 2 guardado: Scatter Plot")
        else:
            print("⚠️ No hay datos suficientes (sin nulos) para el Scatter Plot.")

    # --- GRÁFICO 3: Mapa de Calor de Correlación ---
    # Seleccionamos solo columnas numéricas relevantes
    cols_corr = ["democracia", "pib_pc", "corrupcion", "estabilidad", "esperanza_vida"]
    # Filtramos las que existen en el df
    cols_existentes = [c for c in cols_corr if c in df.columns]
    
    if len(cols_existentes) > 1:
        plt.figure(figsize=(8, 6))
        # Calculamos matriz de correlación
        corr_matrix = df[cols_existentes].corr()
        
        sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", vmin=-1, vmax=1, fmt=".2f")
        plt.title("Mapa de Calor de Correlación (Variables Clave)", fontsize=14)
        plt.tight_layout()
        plt.savefig(os.path.join(RUTA_GRAFICOS, "03_heatmap_correlacion.png"))
        plt.close()
        print("✅ Gráfico 3 guardado: Heatmap Correlación")
    else:
        print("⚠️ No hay suficientes variables numéricas para el Heatmap.")

    # --- GRÁFICO 4: Estabilidad vs Corrupción (Barras Agrupadas) ---
    if "estabilidad" in df.columns and "corrupcion" in df.columns:
        # Normalizamos para que estén en escalas comparables (0-1)
        # Estabilidad suele ir de -2.5 a 2.5 -> Normalizamos a 0-1 aprox
        # Corrupción va de 0 a 100 -> Dividimos por 100
        df_norm = df.copy()
        df_norm["estabilidad_norm"] = (df_norm["estabilidad"] - df_norm["estabilidad"].min()) / (df_norm["estabilidad"].max() - df_norm["estabilidad"].min())
        df_norm["corrupcion_norm"] = df_norm["corrupcion"] / 100
        
        df_melt = df_norm.melt(id_vars=["pais_iso"], value_vars=["estabilidad_norm", "corrupcion_norm"], 
                               var_name="Indicador", value_name="Valor Normalizado")
        
        plt.figure(figsize=(10, 6))
        sns.barplot(data=df_melt, x="pais_iso", y="Valor Normalizado", hue="Indicador", palette="magma")
        plt.title("Comparativa: Estabilidad Política vs Control de Corrupción (Normalizado)", fontsize=14)
        plt.ylabel("Índice Normalizado (0-1)")
        plt.legend(title="Indicador")
        plt.savefig(os.path.join(RUTA_GRAFICOS, "04_estabilidad_vs_corrupcion.png"))
        plt.close()
        print("✅ Gráfico 4 guardado: Estabilidad vs Corrupción")

    # --- GRÁFICO 5: Bubble Plot (Esperanza Vida vs PIB, tamaño=Democracia) ---
    if "esperanza_vida" in df.columns and "pib_pc" in df.columns and "democracia" in df.columns:
        plt.figure(figsize=(10, 6))
        # Multiplicamos democracia por 1000 para que las burbujas sean visibles
        sns.scatterplot(data=df, x="pib_pc", y="esperanza_vida", size="democracia", sizes=(100, 1000), 
                        hue="pais_iso", palette="cool", alpha=0.7)
        
        # Etiquetas
        for i in range(len(df)):
            plt.text(df.iloc[i]["pib_pc"]+200, df.iloc[i]["esperanza_vida"], df.iloc[i]["pais_iso"])
            
        plt.title("Impacto Social: Esperanza de Vida vs Riqueza (Tamaño = Democracia)", fontsize=14)
        plt.xlabel("PIB per Cápita (USD)")
        plt.ylabel("Esperanza de Vida (años)")
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        plt.savefig(os.path.join(RUTA_GRAFICOS, "05_bubble_social.png"))
        plt.close()
        print("✅ Gráfico 5 guardado: Bubble Plot Social")

    print("\n[PASO 3] Análisis Finalizado Exitosamente ✅")

if __name__ == "__main__":
    # Ejecución secuencial completa
    descargar_datos()
    run_etl()
    run_analysis()
