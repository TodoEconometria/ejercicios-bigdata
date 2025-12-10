import os
import sys
from pyspark.sql import SparkSession

# --- CORRECCIÓN PARA WINDOWS ---
# Aseguramos que PySpark use el mismo Python que está ejecutando este script.
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

# --- CONFIGURACIÓN DE RUTAS ---
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
RUTA_PARQUET = os.path.join(BASE_DIR, "ejercicios_bigdata", "datos", "taxi.parquet")

def consulta_spark():
    """
    Ejemplo de consulta SQL usando Apache Spark.
    """
    if not os.path.exists(RUTA_PARQUET):
        print(f"❌ Error: No encuentro {RUTA_PARQUET}. Ejecuta el ejercicio 03 primero.")
        return

    print("⚡ Iniciando SparkSession...")
    print("   (Si estás en Windows y ves advertencias sobre 'winutils', no te preocupes, es normal en local)")
    
    try:
        spark = SparkSession.builder \
            .appName("EjercicioBigDataSpark") \
            .master("local[*]") \
            .config("spark.ui.showConsoleProgress", "false") \
            .getOrCreate()
        
        # Reducir el nivel de log para no asustar al usuario con warnings de Hadoop
        spark.sparkContext.setLogLevel("ERROR")

        print(f"📖 Leyendo Parquet con Spark: {RUTA_PARQUET}")
        df = spark.read.parquet(RUTA_PARQUET)
        
        df.createOrReplaceTempView("tabla_taxis")
        
        print("🧠 Ejecutando consulta SQL...")
        query = """
        SELECT 
            payment_type,
            count(*) as total_viajes,
            ROUND(AVG(fare_amount), 2) as tarifa_promedio,
            ROUND(AVG(trip_distance), 2) as distancia_promedio
        FROM tabla_taxis
        GROUP BY payment_type
        ORDER BY payment_type
        """
        
        resultado = spark.sql(query)
        
        print("\n📊 Resultados de la consulta:")
        resultado.show()
        
        print("🛑 Deteniendo SparkSession...")
        spark.stop()
        print("✅ Fin del ejercicio.")
        
    except Exception as e:
        print("\n❌ Ocurrió un error al ejecutar Spark.")
        print("Posible causa: En Windows, Spark necesita 'winutils.exe' para algunas operaciones de disco.")
        print(f"Detalle del error: {e}")

if __name__ == "__main__":
    consulta_spark()
