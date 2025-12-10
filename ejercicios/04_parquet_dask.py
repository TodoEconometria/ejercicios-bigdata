import os
import dask.dataframe as dd
import pandas as pd

# --- CONFIGURACIÓN DE RUTAS ---
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
RUTA_LIMPIO = os.path.join(BASE_DIR, "ejercicios_bigdata", "datos", "taxi_limpio.csv")
RUTA_PARQUET = os.path.join(BASE_DIR, "ejercicios_bigdata", "datos", "taxi.parquet")

def csv_a_parquet():
    """
    Convierte CSV a Parquet.
    ¿Por qué?
    - CSV: Texto plano, lento de leer, ocupa mucho espacio.
    - Parquet: Binario, comprimido, organizado por columnas. ¡Mucho más rápido para Big Data!
    """
    if not os.path.exists(RUTA_LIMPIO):
        print(f"❌ Error: No encuentro {RUTA_LIMPIO}. Ejecuta el ejercicio 02 primero.")
        return

    print(f"📖 Leyendo CSV limpio con Dask: {RUTA_LIMPIO}")
    # Dask funciona igual que Pandas, pero "perezoso" (lazy).
    # No lee todo el archivo de golpe, solo prepara el plan de ejecución.
    ddf = dd.read_csv(RUTA_LIMPIO)

    print(f"💾 Convirtiendo a formato Parquet: {RUTA_PARQUET} ...")
    # Aquí es donde Dask realmente trabaja. Lee trozos del CSV y escribe trozos de Parquet en paralelo.
    ddf.to_parquet(RUTA_PARQUET, engine='pyarrow', write_index=False)
    print("✅ Conversión completada.")

def analisis_con_dask():
    """
    Ejemplo de análisis distribuido con Dask.
    """
    print("\n--- Análisis con Dask ---")
    print(f"📖 Leyendo Parquet desde: {RUTA_PARQUET}")
    # Leer Parquet es instantáneo porque solo lee los metadatos, no los datos enteros.
    ddf = dd.read_parquet(RUTA_PARQUET, engine='pyarrow')

    # Vamos a calcular el precio promedio del viaje según el tipo de pago.
    # payment_type: 1=Tarjeta de crédito, 2=Efectivo, etc.
    print("🧠 Planificando cálculo: Promedio de 'fare_amount' por 'payment_type'...")
    
    # Esta línea NO calcula nada todavía. Solo construye el grafo de tareas.
    calculo_perezoso = ddf.groupby('payment_type')['fare_amount'].mean()

    print("🚀 Ejecutando cálculo (compute)...")
    # .compute() dispara el procesamiento real. Dask usará todos los núcleos de tu CPU.
    resultado = calculo_perezoso.compute()

    print("\n📊 Resultado (Precio promedio por tipo de pago):")
    print(resultado)
    print("\nNota: Observa que el resultado es una Serie de Pandas normal.")
    print("Dask maneja lo 'grande' y te devuelve algo 'pequeño' y manejable.")

if __name__ == "__main__":
    csv_a_parquet()
    analisis_con_dask()
