"""
================================================================================
|| EJERCICIO DIDÁCTICO: De Archivos CSV a Bases de Datos SQLite               ||
================================================================================
|| PROFESOR: Juan Marcelo Gutierrez Miranda                                   ||
|| CURSO: Big Data - Antigravity                                             ||
================================================================================

Objetivo:
---------
Este script demuestra la transición fundamental de leer datos desde un archivo
plano (CSV) a consultarlos desde una base de datos relacional (SQLite).
Veremos cómo adaptar una aplicación para usar una fuente de datos más robusta
y profesional, y entenderemos por qué este es un paso crucial en cualquier
proyecto de datos.

Contexto:
---------
Imagina que nuestro dashboard de análisis de taxis de NYC lee los datos de un
archivo 'nyc_taxi.csv'. Funciona, pero ¿qué pasa si el archivo crece a 50 GB?
Cargarlo en memoria sería imposible.

La solución es usar una base de datos. El script '01_cargar_sqlite.py' ya ha
hecho el trabajo de migrar los datos del CSV a una base de datos SQLite
llamada 'taxi.db', dentro de una tabla 'viajes_taxi'.

Ahora, vamos a simular cómo nuestro dashboard se adaptaría a este cambio.

Requisitos:
-----------
- Haber ejecutado previamente el script '01_cargar_sqlite.py' para que
  exista la base de datos 'taxi.db'.
- Tener instaladas las librerías: pandas, sqlalchemy
  (pip install pandas sqlalchemy)

"""

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
print("== INICIO DEL SCRIPT: CSV vs. SQLite ==")
print("========================================================")

# --- Definición de Rutas ---
# Para que el script sea robusto, construimos las rutas de forma dinámica.
# BASE_DIR apunta a la raíz del proyecto 'ejercicios_bigdata'.
# __file__ es una variable mágica de Python que contiene la ruta de este script.
# os.path.dirname() nos da el directorio que contiene un archivo.
# Hacemos 'os.path.dirname()' varias veces para "subir" en el árbol de carpetas.
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

# Ruta al archivo CSV original (la forma "antigua")
RUTA_CSV = os.path.join(BASE_DIR, "ejercicios-bigdata", "datos", "nyc_taxi.csv")

# Ruta a la base de datos SQLite (la forma "nueva")
RUTA_DB = os.path.join(BASE_DIR,"ejercicios-bigdata", "taxi.db")

# Nombre de la tabla donde se guardaron los datos
NOMBRE_TABLA = "viajes_taxi"

print(f"\n[CONFIG] Raíz del proyecto detectada en: {BASE_DIR}")
print(f"[CONFIG] Ruta del CSV de origen: {RUTA_CSV}")
print(f"[CONFIG] Ruta de la BD SQLite de destino: {RUTA_DB}")


# ------------------------------------------------------------------------------
# PASO 2: La forma "antigua" - Cargar datos desde un archivo CSV
# ------------------------------------------------------------------------------
# Esta función simula lo que hacía nuestro dashboard originalmente.
# Lee el archivo CSV completo y lo carga en un DataFrame de Pandas.

def cargar_datos_desde_csv():
    """
    Lee los datos de los taxis directamente desde el archivo CSV.

    Ventajas:
    - Simple y directo para archivos pequeños.

    Desventajas:
    - Ineficiente: Carga TODO el archivo en memoria RAM.
    - No escalable: Imposible de usar con archivos de gigabytes.
    - Sin capacidad de consulta: Si solo quieres los viajes de más de 10$,
      tienes que leer todo el archivo primero y luego filtrarlo en Pandas.
    """
    print("\n--------------------------------------------------------")
    print("--- MÉTODO 1: Leyendo desde archivo CSV ---")
    print("--------------------------------------------------------")

    if not os.path.exists(RUTA_CSV):
        print(f"❌ ERROR: No se encontró el archivo CSV en {RUTA_CSV}")
        return None

    print(f"📖 Abriendo y leyendo '{os.path.basename(RUTA_CSV)}'...")
    # pd.read_csv es la función que hace todo el trabajo.
    df = pd.read_csv(RUTA_CSV)
    print(f"✅ ¡Éxito! Se han cargado {len(df)} filas en un DataFrame.")
    return df


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


# ------------------------------------------------------------------------------
# PASO 5: Ejecución principal del script
# ------------------------------------------------------------------------------
# Aquí orquestamos todo el proceso para ver ambos métodos en acción.

if __name__ == "__main__":
    # --- Ejecución con el método antiguo ---
    dataframe_csv = cargar_datos_desde_csv()
    # Pasamos el DataFrame a nuestra función de análisis.
    analizar_dataframe(dataframe_csv, fuente_de_datos="Archivo CSV")

    # --- Ejecución con el método nuevo ---
    dataframe_sqlite = cargar_datos_desde_sqlite()
    # ¡Pasamos el nuevo DataFrame a la MISMA función de análisis!
    # La función 'analizar_dataframe' ni se entera del cambio.
    analizar_dataframe(dataframe_sqlite, fuente_de_datos="Base de Datos SQLite")

    print("\n========================================================")
    print("== CONCLUSIÓN ==")
    print("========================================================")
    print("Ambos métodos produjeron un DataFrame con los mismos datos,")
    print("lo que demuestra que nuestra migración fue un éxito.")
    print("\nLa clave es que hemos separado 'cómo se cargan los datos' de")
    print("'qué se hace con ellos'. Esto hace que nuestra aplicación sea:")
    print("  1. Más robusta y escalable.")
    print("  2. Más fácil de mantener y mejorar en el futuro.")
    print("\n¡Felicidades! Has completado un paso fundamental para convertirte")
    print("en un profesional del desarrollo con datos.")
    print("========================================================")