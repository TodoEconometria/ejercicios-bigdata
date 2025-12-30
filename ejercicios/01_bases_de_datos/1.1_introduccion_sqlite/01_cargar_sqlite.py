import os
import pandas as pd
from sqlalchemy import create_engine

# --- CONFIGURACIÓN DE RUTAS ---
# Es importante ser ordenado con las rutas.
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
RUTA_CSV = os.path.join(BASE_DIR, "ejercicios-bigdata", "datos", "nyc_taxi.csv")
RUTA_DB = os.path.join(BASE_DIR, "ejercicios-bigdata", "taxi.db")

def cargar_csv_a_sqlite():
    """
    Lee un CSV y lo guarda en una base de datos SQLite.
    """
    # 1. Verificación defensiva
    if not os.path.exists(RUTA_CSV):
        print(f"❌ Error: No encuentro el archivo {RUTA_CSV}")
        print("   ¿Ejecutaste primero el script 'datos/descargar_datos.py'?")
        return

    print(f"📖 Leyendo archivo CSV: {RUTA_CSV} ...")
    # Pandas lee el CSV y lo convierte en un DataFrame (una tabla en memoria).
    # En Big Data real, leer todo a memoria puede ser imposible, pero para aprender es perfecto.
    df = pd.read_csv(RUTA_CSV)
    
    print(f"   Filas leídas: {len(df)}")
    print(f"   Columnas: {list(df.columns)}")

    # 2. Conexión a Base de Datos
    # SQLAlchemy es el estándar en Python para hablar con bases de datos.
    # 'sqlite:///' indica que usaremos SQLite (una base de datos en un solo archivo).
    motor = create_engine(f"sqlite:///{RUTA_DB}")

    print(f"💾 Guardando en base de datos SQLite: {RUTA_DB} ...")
    
    # 3. Escribir en la Base de Datos
    # to_sql hace la magia: crea la tabla 'viajes_taxi' e inserta los datos.
    # if_exists="replace": si la tabla ya existe, la borra y la crea de nuevo.
    # index=False: no guardamos el índice numérico de pandas (0, 1, 2...) como columna.
    df.to_sql("viajes_taxi", con=motor, if_exists="replace", index=False)
    
    print("✅ ¡Éxito! Datos guardados en la tabla 'viajes_taxi'.")
    print("   Ahora puedes usar cualquier visor de SQLite para consultar tus datos con SQL.")

if __name__ == "__main__":
    cargar_csv_a_sqlite()
