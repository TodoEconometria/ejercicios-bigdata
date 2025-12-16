

import pandas as pd
import glob
import os
from pathlib import Path
from datetime import datetime


def analizar_csv(ruta_csv):
    """
    Analiza un archivo CSV individual y retorna estadísticas completas.

    Args:
        ruta_csv (str): Ruta al archivo CSV

    Returns:
        dict: Diccionario con estadísticas del CSV
    """
    try:
        # Leer el CSV
        df = pd.read_csv(ruta_csv)

        # Nombre del archivo sin extensión
        nombre_archivo = Path(ruta_csv).stem

        # Información básica
        num_filas, num_columnas = df.shape

        # Análisis de columnas
        columnas_info = []
        for col in df.columns:
            columnas_info.append({
                'nombre': col,
                'tipo': str(df[col].dtype),
                'nulos': df[col].isna().sum(),
                'nulos_pct': (df[col].isna().sum() / num_filas) * 100,
                'unicos': df[col].nunique()
            })

        # Filas duplicadas
        duplicados = df.duplicated().sum()

        # Primeras 3 filas
        primeras_filas = df.head(3).to_dict('records')

        return {
            'nombre_archivo': nombre_archivo,
            'ruta': ruta_csv,
            'num_filas': num_filas,
            'num_columnas': num_columnas,
            'columnas': list(df.columns),
            'columnas_info': columnas_info,
            'duplicados': duplicados,
            'primeras_filas': primeras_filas,
            'dataframe': df  # Guardamos el df para análisis posteriores
        }

    except Exception as e:
        print(f"[ERROR] No se pudo analizar {ruta_csv}: {e}")
        return None


def extraer_fabricantes(dataframe, columna_nombre='name'):
    """
    Extrae fabricantes únicos del nombre del producto.

    Asume que el fabricante es la primera palabra del nombre.
    Ejemplo: "AMD Ryzen 5 3600" -> "AMD"

    Args:
        dataframe (pd.DataFrame): DataFrame con columna de nombres
        columna_nombre (str): Nombre de la columna que contiene nombres de productos

    Returns:
        set: Conjunto de fabricantes únicos
    """
    fabricantes = set()

    if columna_nombre not in dataframe.columns:
        return fabricantes

    # Extraer primera palabra de cada nombre
    for nombre in dataframe[columna_nombre].dropna():
        primera_palabra = str(nombre).split()[0] if str(nombre).split() else None
        if primera_palabra:
            fabricantes.add(primera_palabra)

    return fabricantes


def extraer_colores(dataframe):
    """
    Extrae colores únicos si existe una columna de color.

    Args:
        dataframe (pd.DataFrame): DataFrame

    Returns:
        set: Conjunto de colores únicos
    """
    colores = set()

    # Buscar columnas que contengan "color" en el nombre
    columnas_color = [col for col in dataframe.columns if 'color' in col.lower()]

    for col in columnas_color:
        # Extraer valores únicos de la columna de colores
        valores_color = dataframe[col].dropna().unique()
        colores.update(valores_color)

    return colores


def analizar_calidad_datos(dataframe):
    """
    Analiza calidad de datos: nulos, duplicados, rangos.

    Args:
        dataframe (pd.DataFrame): DataFrame a analizar

    Returns:
        dict: Diccionario con métricas de calidad
    """
    analisis = {
        'total_filas': len(dataframe),
        'filas_duplicadas': dataframe.duplicated().sum(),
        'columnas_con_nulos': [],
        'rangos_numericos': {}
    }

    # Análisis de valores nulos por columna
    for col in dataframe.columns:
        nulos = dataframe[col].isna().sum()
        if nulos > 0:
            analisis['columnas_con_nulos'].append({
                'columna': col,
                'nulos': nulos,
                'porcentaje': (nulos / len(dataframe)) * 100
            })

    # Análisis de rangos numéricos (especialmente precios)
    for col in dataframe.columns:
        if dataframe[col].dtype in ['int64', 'float64']:
            analisis['rangos_numericos'][col] = {
                'min': dataframe[col].min(),
                'max': dataframe[col].max(),
                'promedio': dataframe[col].mean(),
                'mediana': dataframe[col].median()
            }

    return analisis


def identificar_columnas_comunes(lista_analisis):
    """
    Identifica columnas que son comunes a todos los CSVs.

    Args:
        lista_analisis (list): Lista de diccionarios con análisis de CSVs

    Returns:
        set: Conjunto de columnas comunes
    """
    if not lista_analisis:
        return set()

    # Empezar con las columnas del primer CSV
    columnas_comunes = set(lista_analisis[0]['columnas'])

    # Intersección con columnas de los demás CSVs
    for analisis in lista_analisis[1:]:
        columnas_comunes = columnas_comunes.intersection(set(analisis['columnas']))

    return columnas_comunes


def generar_reporte_completo(ruta_carpeta_csv):
    """
    Genera reporte completo de todos los CSVs en la carpeta.

    Args:
        ruta_carpeta_csv (str): Ruta a la carpeta con los CSVs
    """
    print("=" * 80)
    print("ANÁLISIS EXPLORATORIO DE DATOS (EDA)")
    print("Tienda de Componentes Informáticos")
    print("=" * 80)
    print(f"\nFecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Carpeta analizada: {ruta_carpeta_csv}\n")

    # Buscar todos los archivos CSV
    patron_busqueda = os.path.join(ruta_carpeta_csv, "*.csv")
    archivos_csv = glob.glob(patron_busqueda)

    if not archivos_csv:
        print(f"[ERROR] No se encontraron archivos CSV en: {ruta_carpeta_csv}")
        return

    print(f"[INFO] Encontrados {len(archivos_csv)} archivos CSV\n")

    # Analizar cada CSV
    lista_analisis = []
    todos_fabricantes = set()
    todos_colores = set()

    for ruta_csv in sorted(archivos_csv):
        print(f"Analizando: {Path(ruta_csv).name}...")
        analisis = analizar_csv(ruta_csv)

        if analisis:
            lista_analisis.append(analisis)

            # Extraer fabricantes y colores
            df = analisis['dataframe']
            fabricantes = extraer_fabricantes(df)
            colores = extraer_colores(df)

            todos_fabricantes.update(fabricantes)
            todos_colores.update(colores)

    print(f"\n[OK] Análisis completado: {len(lista_analisis)} archivos procesados\n")

    # --- SECCIÓN 1: RESUMEN EJECUTIVO ---
    print("=" * 80)
    print("1. RESUMEN EJECUTIVO")
    print("=" * 80)

    total_productos = sum(a['num_filas'] for a in lista_analisis)
    total_categorias = len(lista_analisis)

    print(f"\nArchivos CSV analizados: {len(lista_analisis)}")
    print(f"Total de productos (filas): {total_productos:,}")
    print(f"Categorías diferentes: {total_categorias}")
    print(f"Fabricantes únicos identificados: {len(todos_fabricantes)}")
    print(f"Colores únicos identificados: {len(todos_colores)}")

    # --- SECCIÓN 2: ANÁLISIS POR ARCHIVO ---
    print("\n" + "=" * 80)
    print("2. ANÁLISIS POR ARCHIVO CSV")
    print("=" * 80)

    for analisis in lista_analisis:
        print(f"\n--- {analisis['nombre_archivo']} ---")
        print(f"  Filas: {analisis['num_filas']}")
        print(f"  Columnas: {analisis['num_columnas']}")
        print(f"  Columnas: {', '.join(analisis['columnas'])}")
        print(f"  Duplicados: {analisis['duplicados']}")

        # Mostrar primeras 3 filas (solo nombres de producto si existe)
        if 'name' in analisis['columnas']:
            df = analisis['dataframe']
            print(f"  Ejemplos de productos:")
            for i, nombre in enumerate(df['name'].head(3), 1):
                print(f"    {i}. {nombre}")

    # --- SECCIÓN 3: ANÁLISIS DE CALIDAD ---
    print("\n" + "=" * 80)
    print("3. ANÁLISIS DE CALIDAD DE DATOS")
    print("=" * 80)

    for analisis in lista_analisis:
        df = analisis['dataframe']
        calidad = analizar_calidad_datos(df)

        if calidad['columnas_con_nulos'] or calidad['filas_duplicadas'] > 0:
            print(f"\n--- {analisis['nombre_archivo']} ---")

            if calidad['filas_duplicadas'] > 0:
                print(f"  [!] Filas duplicadas: {calidad['filas_duplicadas']}")

            if calidad['columnas_con_nulos']:
                print(f"  [!] Columnas con valores nulos:")
                for col_info in calidad['columnas_con_nulos']:
                    print(f"      - {col_info['columna']}: {col_info['nulos']} ({col_info['porcentaje']:.1f}%)")

            # Mostrar rangos de precios si existe
            if 'price' in calidad['rangos_numericos']:
                precios = calidad['rangos_numericos']['price']
                print(f"  Rango de precios:")
                print(f"      Min: ${precios['min']:.2f}")
                print(f"      Max: ${precios['max']:.2f}")
                print(f"      Promedio: ${precios['promedio']:.2f}")

    # --- SECCIÓN 4: COLUMNAS COMUNES ---
    print("\n" + "=" * 80)
    print("4. ANÁLISIS DE ESTRUCTURA")
    print("=" * 80)

    columnas_comunes = identificar_columnas_comunes(lista_analisis)
    print(f"\nColumnas comunes a TODOS los CSVs: {len(columnas_comunes)}")
    if columnas_comunes:
        print(f"  {', '.join(sorted(columnas_comunes))}")
    else:
        print("  [!] No hay columnas comunes a todos los archivos")

    # Tabla resumen
    print("\nTabla resumen (archivo → filas):")
    print(f"{'Archivo':<30} {'Filas':>10}")
    print("-" * 42)
    for analisis in sorted(lista_analisis, key=lambda x: x['num_filas'], reverse=True):
        print(f"{analisis['nombre_archivo']:<30} {analisis['num_filas']:>10,}")

    # --- SECCIÓN 5: ENTIDADES IDENTIFICADAS ---
    print("\n" + "=" * 80)
    print("5. IDENTIFICACIÓN DE ENTIDADES")
    print("=" * 80)

    print(f"\nCategorías (basado en nombres de archivos): {total_categorias}")
    for analisis in lista_analisis:
        print(f"  - {analisis['nombre_archivo']}")

    print(f"\nFabricantes únicos encontrados: {len(todos_fabricantes)}")
    if todos_fabricantes:
        fabricantes_ordenados = sorted(list(todos_fabricantes))[:20]  # Primeros 20
        print(f"  {', '.join(fabricantes_ordenados)}")
        if len(todos_fabricantes) > 20:
            print(f"  ... y {len(todos_fabricantes) - 20} más")

    print(f"\nColores únicos encontrados: {len(todos_colores)}")
    if todos_colores:
        print(f"  {', '.join(sorted(list(todos_colores)))}")

    # --- SECCIÓN 6: CONCLUSIONES ---
    print("\n" + "=" * 80)
    print("6. CONCLUSIONES PARA EL DISEÑO DE BASE DE DATOS")
    print("=" * 80)

    print("\nEntidades identificadas para Modelo B (normalizado):")
    print("  1. CATEGORIAS - Una tabla con las categorías de productos")
    print("  2. FABRICANTES - Una tabla con fabricantes únicos")
    print("  3. PRODUCTOS - Tabla central con todos los productos")
    if todos_colores:
        print("  4. COLORES - Tabla con colores disponibles")
        print("  5. PRODUCTOS_COLORES - Relación M:N entre productos y colores")

    print("\nRelaciones identificadas:")
    print("  - CATEGORIAS 1:N PRODUCTOS (una categoría tiene muchos productos)")
    print("  - FABRICANTES 1:N PRODUCTOS (un fabricante fabrica muchos productos)")
    if todos_colores:
        print("  - PRODUCTOS M:N COLORES (un producto puede tener varios colores)")

    print("\nProblema del Modelo A (desnormalizado):")
    print("  - 26 tablas independientes sin relaciones")
    print("  - Fabricantes duplicados en cada tabla")
    print("  - Difícil realizar consultas entre categorías")
    print("  - Redundancia de información")

    # --- GUARDAR REPORTE EN ARCHIVO MARKDOWN ---
    ruta_salida = os.path.join(os.path.dirname(__file__), "resumen_eda.md")

    print(f"\n{'=' * 80}")
    print(f"[OK] Análisis completado exitosamente")
    print(f"[OK] Reporte guardado en: {ruta_salida}")
    print(f"{'=' * 80}\n")

    # Guardar en archivo formato Markdown
    with open(ruta_salida, 'w', encoding='utf-8') as f:
        f.write("# Resumen - Análisis Exploratorio de Datos (EDA)\n\n")
        f.write("**Ejercicio:** 1.1 - Introducción a SQLite\n")
        f.write(f"**Fecha:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"**Generado por:** `eda_exploratorio.py`\n\n")
        f.write("---\n\n")

        # Resumen Ejecutivo
        f.write("## 1. Resumen Ejecutivo\n\n")
        f.write(f"- **Archivos CSV analizados:** {len(lista_analisis)}\n")
        f.write(f"- **Total de productos:** {total_productos:,}\n")
        f.write(f"- **Categorías diferentes:** {total_categorias}\n")
        f.write(f"- **Fabricantes únicos:** {len(todos_fabricantes)}\n")
        f.write(f"- **Colores únicos:** {len(todos_colores)}\n\n")

        # Tabla Resumen
        f.write("---\n\n")
        f.write("## 2. Tabla Resumen de Archivos\n\n")
        f.write("| Archivo | Filas | Columnas |\n")
        f.write("|---------|------:|---------:|\n")
        for analisis in sorted(lista_analisis, key=lambda x: x['num_filas'], reverse=True):
            f.write(f"| {analisis['nombre_archivo']} | {analisis['num_filas']:,} | {analisis['num_columnas']} |\n")

        # Columnas Comunes
        f.write("\n---\n\n")
        f.write("## 3. Columnas Comunes\n\n")
        columnas_comunes = identificar_columnas_comunes(lista_analisis)
        if columnas_comunes:
            f.write(f"Columnas presentes en **TODOS** los archivos CSV ({len(columnas_comunes)}):\n\n")
            for col in sorted(columnas_comunes):
                f.write(f"- `{col}`\n")
        else:
            f.write("No hay columnas comunes a todos los archivos.\n")

        # Fabricantes
        f.write("\n---\n\n")
        f.write("## 4. Fabricantes Identificados\n\n")
        f.write(f"**Total:** {len(todos_fabricantes)} fabricantes únicos\n\n")
        if todos_fabricantes:
            fabricantes_ordenados = sorted(list(todos_fabricantes))
            # Mostrar en formato de lista con columnas
            f.write("```\n")
            for i in range(0, len(fabricantes_ordenados), 5):
                f.write("  ".join(f"{fab:<15}" for fab in fabricantes_ordenados[i:i+5]))
                f.write("\n")
            f.write("```\n")

        # Colores
        f.write("\n---\n\n")
        f.write("## 5. Colores Identificados\n\n")
        if todos_colores:
            f.write(f"**Total:** {len(todos_colores)} colores únicos\n\n")
            for color in sorted(todos_colores):
                f.write(f"- {color}\n")
        else:
            f.write("No se encontraron columnas de color en los datos.\n")

        # Análisis de Calidad
        f.write("\n---\n\n")
        f.write("## 6. Análisis de Calidad de Datos\n\n")

        archivos_con_problemas = []
        for analisis in lista_analisis:
            df = analisis['dataframe']
            calidad = analizar_calidad_datos(df)

            if calidad['columnas_con_nulos'] or calidad['filas_duplicadas'] > 0:
                archivos_con_problemas.append({
                    'nombre': analisis['nombre_archivo'],
                    'duplicados': calidad['filas_duplicadas'],
                    'nulos': calidad['columnas_con_nulos']
                })

        if archivos_con_problemas:
            f.write("### Archivos con Problemas de Calidad\n\n")
            for archivo in archivos_con_problemas:
                f.write(f"#### {archivo['nombre']}\n\n")
                if archivo['duplicados'] > 0:
                    f.write(f"- **Filas duplicadas:** {archivo['duplicados']}\n")
                if archivo['nulos']:
                    f.write(f"- **Columnas con valores nulos:**\n")
                    for col_info in archivo['nulos']:
                        f.write(f"  - `{col_info['columna']}`: {col_info['nulos']} ({col_info['porcentaje']:.1f}%)\n")
                f.write("\n")
        else:
            f.write("No se encontraron problemas significativos de calidad en los datos.\n\n")

        # Conclusiones
        f.write("---\n\n")
        f.write("## 7. Conclusiones\n\n")
        f.write("### Entidades Identificadas para Modelo B (Normalizado)\n\n")
        f.write("1. **CATEGORIAS** - Una tabla con las categorías de productos\n")
        f.write("2. **FABRICANTES** - Una tabla con fabricantes únicos\n")
        f.write("3. **PRODUCTOS** - Tabla central con todos los productos\n")
        if todos_colores:
            f.write("4. **COLORES** - Tabla con colores disponibles\n")
            f.write("5. **PRODUCTOS_COLORES** - Relación M:N entre productos y colores\n")

        f.write("\n### Relaciones Identificadas\n\n")
        f.write("- `CATEGORIAS` 1:N `PRODUCTOS` (una categoría tiene muchos productos)\n")
        f.write("- `FABRICANTES` 1:N `PRODUCTOS` (un fabricante fabrica muchos productos)\n")
        if todos_colores:
            f.write("- `PRODUCTOS` M:N `COLORES` (un producto puede tener varios colores)\n")

        f.write("\n### Problema del Modelo A (Desnormalizado)\n\n")
        f.write(f"- {len(lista_analisis)} tablas independientes sin relaciones\n")
        f.write("- Fabricantes duplicados en cada tabla\n")
        f.write("- Difícil realizar consultas entre categorías\n")
        f.write("- Alta redundancia de información\n\n")

        f.write("---\n\n")
        f.write("**Próximo paso:** Completar `ANALISIS_DATOS.md` con estos hallazgos y crear los diagramas ER.\n")


if __name__ == "__main__":
    # Ruta a los datos (ajustar según tu estructura)
    ruta_datos = "../../../datos/csv_tienda_informatica/csv_tienda_informatica/"

    # Verificar si la ruta existe
    if not os.path.exists(ruta_datos):
        print(f"[ERROR] La ruta no existe: {ruta_datos}")
        print("\nPor favor, ajusta la variable 'ruta_datos' en el script.")
        print("Debe apuntar a la carpeta con los archivos CSV.")
    else:
        generar_reporte_completo(ruta_datos)
