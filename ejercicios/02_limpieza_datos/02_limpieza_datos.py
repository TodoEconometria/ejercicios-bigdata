import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- CONFIGURACIÓN DE RUTAS ---
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
RUTA_CSV = os.path.join(BASE_DIR, "ejercicios_bigdata", "datos", "nyc_taxi.csv")
RUTA_LIMPIO = os.path.join(BASE_DIR, "ejercicios_bigdata", "datos", "taxi_limpio.csv")
RUTA_GRAFICO = os.path.join(BASE_DIR, "ejercicios_bigdata", "datos", "distribucion_distancia.png")

def limpiar_datos():
    """
    Carga datos sucios, los limpia y genera nuevas características.
    """
    if not os.path.exists(RUTA_CSV):
        print(f"❌ Error: No encuentro {RUTA_CSV}")
        return

    print(f"🧹 Leyendo datos crudos desde: {RUTA_CSV}")
    df = pd.read_csv(RUTA_CSV)
    
    # --- 1. INSPECCIÓN INICIAL ---
    print("\n--- Antes de limpiar ---")
    print(df.info()) # Muestra tipos de datos y valores nulos
    
    # --- 2. LIMPIEZA DE NULOS ---
    # En el mundo real, los datos vienen incompletos.
    # Eliminamos filas donde falten datos críticos (fechas, distancia, precio).
    columnas_criticas = ["tpep_pickup_datetime", "tpep_dropoff_datetime", "trip_distance", "fare_amount"]
    # Nota: Los nombres de columnas en el CSV pueden variar, ajustamos a los nombres reales del dataset NYC Taxi.
    # Si el CSV tiene nombres diferentes, pandas dará error, así que es bueno inspeccionar primero.
    # Asumimos nombres estándar del dataset amarillo de NYC.
    
    print(f"\nEliminando filas con valores nulos en: {columnas_criticas}")
    df_limpio = df.dropna(subset=columnas_criticas).copy()
    
    # --- 3. CONVERSIÓN DE TIPOS ---
    # Las fechas suelen leerse como texto (object). Hay que convertirlas a 'datetime' para poder operar con ellas.
    print("Convirtiendo columnas de fecha...")
    df_limpio["tpep_pickup_datetime"] = pd.to_datetime(df_limpio["tpep_pickup_datetime"])
    df_limpio["tpep_dropoff_datetime"] = pd.to_datetime(df_limpio["tpep_dropoff_datetime"])
    
    # --- 4. INGENIERÍA DE CARACTERÍSTICAS (Feature Engineering) ---
    # Crear nuevos datos a partir de los existentes.
    # Calculamos la duración del viaje en minutos.
    print("Calculando duración del viaje...")
    df_limpio["duracion_minutos"] = (df_limpio["tpep_dropoff_datetime"] - df_limpio["tpep_pickup_datetime"]).dt.total_seconds() / 60
    
    # --- 5. FILTRADO DE ERRORES LÓGICOS ---
    # A veces hay datos que no tienen sentido (ej. distancias negativas o 0, precios negativos).
    print("Filtrando datos erróneos (distancias <= 0, precios <= 0)...")
    df_limpio = df_limpio[ (df_limpio["trip_distance"] > 0) & (df_limpio["fare_amount"] > 0) ]

    print(f"\n--- Después de limpiar ---")
    print(f"Filas originales: {len(df)}")
    print(f"Filas limpias:    {len(df_limpio)}")
    print(f"Datos eliminados: {len(df) - len(df_limpio)}")

    # --- 6. GUARDADO ---
    print(f"\n💾 Guardando datos limpios en: {RUTA_LIMPIO}")
    df_limpio.to_csv(RUTA_LIMPIO, index=False)
    
    # --- 7. VISUALIZACIÓN (Bonus) ---
    # Una imagen vale más que mil tablas.
    print(f"📊 Generando gráfico en: {RUTA_GRAFICO}")
    plt.figure(figsize=(10, 6))
    # Usamos seaborn para un histograma bonito. Limitamos a viajes de menos de 10 millas para ver mejor.
    sns.histplot(df_limpio[df_limpio["trip_distance"] < 10]["trip_distance"], bins=30, kde=True)
    plt.title("Distribución de Distancias de Viajes (menores a 10 millas)")
    plt.xlabel("Distancia (millas)")
    plt.ylabel("Frecuencia")
    plt.savefig(RUTA_GRAFICO)
    print("✅ ¡Limpieza y visualización completadas!")

if __name__ == "__main__":
    limpiar_datos()
