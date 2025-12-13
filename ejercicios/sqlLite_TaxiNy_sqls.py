# ------------------------------------------------------------------------------
# PASO 1: Importación de librerías y configuración de rutas
# ------------------------------------------------------------------------------
# - os: Para construir rutas de archivos de forma que funcionen en cualquier
#       sistema operativo (Windows, Mac, Linux).
# - pandas: La librería fundamental para la manipulación de datos en Python.
#           Nos proporciona los DataFrames.
# - sqlalchemy: El "traductor" universal de Python para hablar con casi
#               cualquier base de datos SQL. Usaremos su función 'create_engine'.

import os
import pandas as pd
from sqlalchemy import create_engine

print("========================================================")
print("== CONSULTAS ==")
print("========================================================")

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

# Ruta a la base de datos SQLite (la forma "nueva")
RUTA_DB = os.path.join(BASE_DIR,"ejercicios-bigdata", "taxi.db")

# Nombre de la tabla donde se guardaron los datos
NOMBRE_TABLA = "viajes_taxi"

print(f"\n[CONFIG] Raíz del proyecto detectada en: {BASE_DIR}")

print(f"[CONFIG] Ruta de la BD SQLite de destino: {RUTA_DB}")

# ------------------------------------------------------------------------------
# PASO 3: La forma "nueva" y profesional - Cargar datos desde SQLite
# ------------------------------------------------------------------------------
# Esta es la versión mejorada. Se conecta a la base de datos y ejecuta una
# consulta SQL para traer los datos.

def cargar_datos_desde_sqlite():
    """
    Se conecta a la base de datos SQLite y lee los datos de la tabla de taxis.

    Ventajas:
    - Eficiente: La base de datos puede hacer filtros, agregaciones y uniones
      de forma optimizada antes de enviar los datos a Python.
    - Escalable: Podemos cambiar la consulta para traer solo un subconjunto
      de datos (ej: los últimos 1000 viajes) sin cargar todo.
    - Profesional: Es el estándar de la industria para cualquier aplicación seria.

    Desventajas:
    - Requiere un paso previo de configuración (crear la base de datos).
    """
    print("\n--------------------------------------------------------")
    print("--- MÉTODO 2: Consultando desde la base de datos SQLite ---")
    print("--------------------------------------------------------")

    if not os.path.exists(RUTA_DB):
        print(f"❌ ERROR: No se encontró la base de datos en {RUTA_DB}")
        print("   Asegúrate de haber ejecutado '01_cargar_sqlite.py' primero.")
        return None

    # 1. Crear el "motor" de conexión:
    #    SQLAlchemy usa un 'engine' para gestionar la comunicación.
    #    La cadena de conexión 'sqlite:///<ruta_al_archivo>' le dice
    #    que estamos usando una base de datos SQLite local.
    print(f"🔌 Creando conexión a la base de datos '{os.path.basename(RUTA_DB)}'...")
    motor_db = create_engine(f"sqlite:///{RUTA_DB}")

    # 2. Definir la consulta SQL:
    #    Por ahora, traemos toda la tabla, que es equivalente a leer el CSV.
    #    Pero aquí es donde reside el poder: podríamos cambiar esta consulta
    #    por algo como "SELECT * FROM viajes_taxi WHERE passenger_count > 2"
    #    y la base de datos haría el filtrado por nosotros.
    consulta_sql = f"SELECT * FROM {NOMBRE_TABLA};"
    print(f"🔍 Ejecutando consulta SQL: \"{consulta_sql}\"")

    # 3. Leer los datos con Pandas:
    #    pd.read_sql() toma la consulta y el motor de conexión, y devuelve
    #    un DataFrame, igual que pd.read_csv().
    df = pd.read_sql(consulta_sql, motor_db)
    print(f"✅ ¡Éxito! Se han cargado {len(df)} filas en un DataFrame desde la BD.")
    return df


# ------------------------------------------------------------------------------
# PASO 4: La magia de la abstracción - Analizando los datos
# ------------------------------------------------------------------------------
# Esta función representa la lógica de nuestro dashboard (crear gráficos,
# calcular estadísticas, etc.).
#
# ¡OBSERVA! A esta función no le importa de dónde vienen los datos.
# Solo necesita recibir un DataFrame de Pandas para funcionar.
#
# Esta separación de responsabilidades (una parte del código carga los datos,
# otra parte los analiza) es un principio clave del buen diseño de software.

def analizar_dataframe(df, fuente_de_datos):
    """
    Realiza un análisis simple sobre un DataFrame y muestra los resultados.
    """
    print(f"\n--- Analizando DataFrame cargado desde: {fuente_de_datos} ---")
    if df is None:
        print("El DataFrame está vacío, no se puede analizar.")
        return

    # Calculamos algunas estadísticas simples
    num_filas = len(df)
    num_columnas = len(df.columns)
    distancia_media = df['trip_distance'].mean() if 'trip_distance' in df.columns else 'N/A'
    tarifa_maxima = df['fare_amount'].max() if 'fare_amount' in df.columns else 'N/A'

    print(f"  - Número de registros: {num_filas}")
    print(f"  - Número de columnas: {num_columnas}")
    print(f"  - Distancia media del viaje: {distancia_media:.2f} millas")
    print(f"  - Tarifa máxima registrada: ${tarifa_maxima:.2f}")
    print("--------------------------------------------------------\n")

def ejecutar_consultas_sql(motor_db):
    """
    Ejecuta un conjunto de consultas SQL útiles sobre la tabla viajes_taxi
    y muestra resultados (head) en pantalla.
    """
    consultas = {
        # 1) Muestra rápida
        "Muestra 5 filas": f"""
            SELECT * FROM {NOMBRE_TABLA}
            LIMIT 5;
        """,

        # 2) Conteo total de registros
        "Total de viajes": f"""
            SELECT COUNT(*) AS total_viajes
            FROM {NOMBRE_TABLA};
        """,

        # 3) Top 10 viajes más largos
        "Top 10 distancias": f"""
            SELECT tpep_pickup_datetime, tpep_dropoff_datetime, passenger_count, trip_distance
            FROM {NOMBRE_TABLA}
            WHERE trip_distance IS NOT NULL
            ORDER BY trip_distance DESC
            LIMIT 10;
        """,

        # 4) Distancia media y percentiles aproximados no (SQLite no tiene percentile nativo),
        # pero sí stats básicas:
        "Stats de distancia": f"""
            SELECT
                MIN(trip_distance) AS min_dist,
                AVG(trip_distance) AS avg_dist,
                MAX(trip_distance) AS max_dist
            FROM {NOMBRE_TABLA}
            WHERE trip_distance IS NOT NULL;
        """,

        # 5) Viajes por número de pasajeros
        "Viajes por passenger_count": f"""
            SELECT passenger_count, COUNT(*) AS num_viajes
            FROM {NOMBRE_TABLA}
            GROUP BY passenger_count
            ORDER BY num_viajes DESC;
        """,

        # 6) Ingresos por forma de pago (si existe payment_type)
        "Ingresos por payment_type": f"""
            SELECT payment_type,
                   COUNT(*) AS num_viajes,
                   AVG(fare_amount) AS fare_media,
                   SUM(fare_amount) AS total_fare
            FROM {NOMBRE_TABLA}
            WHERE fare_amount IS NOT NULL
            GROUP BY payment_type
            ORDER BY total_fare DESC;
        """,

        # 7) Tarifa media por distancia (buckets)
        "Tarifa media por tramo de distancia": f"""
            SELECT
                CASE
                    WHEN trip_distance < 1 THEN '0-1'
                    WHEN trip_distance < 3 THEN '1-3'
                    WHEN trip_distance < 5 THEN '3-5'
                    WHEN trip_distance < 10 THEN '5-10'
                    ELSE '10+'
                END AS tramo_distancia,
                COUNT(*) AS num_viajes,
                AVG(fare_amount) AS fare_media
            FROM {NOMBRE_TABLA}
            WHERE trip_distance IS NOT NULL AND fare_amount IS NOT NULL
            GROUP BY tramo_distancia
            ORDER BY num_viajes DESC;
        """,

        # 8) Viajes por día (si tpep_pickup_datetime es texto ISO o similar)
        "Viajes por día (pickup)": f"""
            SELECT
                date(tpep_pickup_datetime) AS dia,
                COUNT(*) AS num_viajes,
                AVG(trip_distance) AS dist_media
            FROM {NOMBRE_TABLA}
            WHERE tpep_pickup_datetime IS NOT NULL
            GROUP BY dia
            ORDER BY dia
            LIMIT 15;
        """,

        # 9) Duración del viaje en minutos (requiere datetime parseable por SQLite)
        "Top 10 duraciones (min)": f"""
            SELECT
                tpep_pickup_datetime,
                tpep_dropoff_datetime,
                trip_distance,
                ROUND((julianday(tpep_dropoff_datetime) - julianday(tpep_pickup_datetime)) * 24 * 60, 2) AS duracion_min
            FROM {NOMBRE_TABLA}
            WHERE tpep_pickup_datetime IS NOT NULL
              AND tpep_dropoff_datetime IS NOT NULL
            ORDER BY duracion_min DESC
            LIMIT 10;
        """,

        # 10) Calidad: detecta viajes raros (distancia negativa o cero con tarifa alta)
        "Viajes sospechosos": f"""
            SELECT trip_distance, fare_amount, passenger_count, tpep_pickup_datetime
            FROM {NOMBRE_TABLA}
            WHERE (trip_distance <= 0 AND fare_amount > 20)
               OR (trip_distance > 50)
            ORDER BY fare_amount DESC
            LIMIT 20;
        """,
    }

    print("\n" + "="*70)
    print("🔎 EJECUTANDO CONSULTAS SQL")
    print("="*70)

    for titulo, sql in consultas.items():
        print(f"\n🧾 {titulo}")
        print("-"*70)
        try:
            dfq = pd.read_sql(sql, motor_db)
            # mostramos poco para no petar la consola
            print(dfq.head(10))
        except Exception as e:
            print(f"❌ Error en consulta '{titulo}': {e}")


# ------------------------------------------------------------------------------
# PASO 5: Ejecución principal del script
# ------------------------------------------------------------------------------
# Aquí orquestamos todo el proceso para ver ambos métodos en acción.

if __name__ == "__main__":

    # --- Ejecución con el método nuevo ---
    dataframe_sqlite = cargar_datos_desde_sqlite()
    # ¡Pasamos el nuevo DataFrame a la MISMA función de análisis!
    # La función 'analizar_dataframe' ni se entera del cambio.
    analizar_dataframe(dataframe_sqlite, fuente_de_datos="Base de Datos SQLite")
    motor_db = create_engine(f"sqlite:///{RUTA_DB}")
    ejecutar_consultas_sql(motor_db)
