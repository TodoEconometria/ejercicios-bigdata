import sqlite3
import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Configuración
SQLITE_DBS = [
    r"C:\Users\Tucanae Ramos\PycharmProjects\ejercicios-bigdata\ejercicios\01_bases_de_datos\1.1_introduccion_sqlite\modelos_tienda_fer\tienda_modelo_a.db",
    r"C:\Users\Tucanae Ramos\PycharmProjects\ejercicios-bigdata\ejercicios\01_bases_de_datos\1.1_introduccion_sqlite\modelos_tienda_fer\tienda_modelo_b.db",
    r"C:\Users\Tucanae Ramos\PycharmProjects\ejercicios-bigdata\ejercicios\01_bases_de_datos\1.1_introduccion_sqlite\modelos_tienda_fer\tienda_modelo_c.db"
]

POSTGRES_DBS = [
    "tienda_modelo_a_postgres",
    "tienda_modelo_b_postgres",
    "tienda_modelo_c_postgres"
]

PG_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "user": "postgres",
    "password": "PostGre1234"
}

# Mapeo de tipos SQLite → PostgreSQL
TYPE_MAPPING = {
    "INTEGER": "INTEGER",
    "TEXT": "VARCHAR(255)",
    "REAL": "NUMERIC(10,2)",
    "BLOB": "BYTEA",
    "DECIMAL": "NUMERIC(10,2)",
    "VARCHAR": "VARCHAR"
}


def crear_base_datos_postgres(db_name):
    """Crea una base de datos en PostgreSQL"""
    conn = psycopg2.connect(
        host=PG_CONFIG["host"],
        port=PG_CONFIG["port"],
        user=PG_CONFIG["user"],
        password=PG_CONFIG["password"],
        database="postgres"
    )
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()

    cursor.execute(f"DROP DATABASE IF EXISTS {db_name}")
    cursor.execute(f"CREATE DATABASE {db_name}")
    print(f"✅ Base de datos '{db_name}' creada en PostgreSQL")

    cursor.close()
    conn.close()


def obtener_esquema_sqlite(sqlite_path):
    """Extrae el esquema de una base SQLite"""
    conn = sqlite3.connect(sqlite_path)
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")
    tablas = cursor.fetchall()

    esquema = {}
    for (tabla,) in tablas:
        # Escapar nombre de tabla con comillas dobles
        cursor.execute(f'PRAGMA table_info("{tabla}")')
        columnas = cursor.fetchall()
        esquema[tabla] = columnas

    conn.close()
    return esquema

def convertir_tipo(tipo_sqlite):
    """Convierte tipos de SQLite a PostgreSQL"""
    tipo_upper = tipo_sqlite.upper()
    for sqlite_type, pg_type in TYPE_MAPPING.items():
        if sqlite_type in tipo_upper:
            return pg_type
    return "TEXT"


def migrar_esquema(sqlite_path, pg_db_name):
    """Migra el esquema de SQLite a PostgreSQL"""
    esquema = obtener_esquema_sqlite(sqlite_path)

    conn = psycopg2.connect(
        host=PG_CONFIG["host"],
        port=PG_CONFIG["port"],
        user=PG_CONFIG["user"],
        password=PG_CONFIG["password"],
        database=pg_db_name
    )
    cursor = conn.cursor()

    for tabla, columnas in esquema.items():
        cols_def = []
        for col in columnas:
            col_id, col_name, col_type, not_null, default_val, pk = col
            tipo_pg = convertir_tipo(col_type)
            # Escapar nombre de columna
            definicion = f'"{col_name}" {tipo_pg}'

            if pk:
                definicion += " PRIMARY KEY"
            elif not_null:
                definicion += " NOT NULL"

            cols_def.append(definicion)

        # Escapar nombre de tabla
        create_sql = f'CREATE TABLE "{tabla}" ({", ".join(cols_def)})'
        cursor.execute(create_sql)
        print(f"  📋 Tabla '{tabla}' creada")

    conn.commit()
    cursor.close()
    conn.close()


def migrar_datos(sqlite_path, pg_db_name):
    """Migra los datos de SQLite a PostgreSQL"""
    sqlite_conn = sqlite3.connect(sqlite_path)
    sqlite_cursor = sqlite_conn.cursor()

    pg_conn = psycopg2.connect(
        host=PG_CONFIG["host"],
        port=PG_CONFIG["port"],
        user=PG_CONFIG["user"],
        password=PG_CONFIG["password"],
        database=pg_db_name
    )
    pg_cursor = pg_conn.cursor()

    sqlite_cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")
    tablas = sqlite_cursor.fetchall()

    total_registros = 0
    for (tabla,) in tablas:
        # Escapar nombre de tabla
        sqlite_cursor.execute(f'SELECT * FROM "{tabla}"')
        datos = sqlite_cursor.fetchall()

        if datos:
            # Escapar nombre de tabla
            columnas_query = f'PRAGMA table_info("{tabla}")'
            sqlite_cursor.execute(columnas_query)
            columnas_info = sqlite_cursor.fetchall()
            columnas = [f'"{col[1]}"' for col in columnas_info]  # Escapar columnas

            placeholders = ', '.join(['%s'] * len(columnas))
            # Escapar nombre de tabla y columnas
            insert_sql = f'INSERT INTO "{tabla}" ({", ".join(columnas)}) VALUES ({placeholders})'

            pg_cursor.executemany(insert_sql, datos)
            total_registros += len(datos)
            print(f"  📊 {len(datos)} registros migrados en '{tabla}'")

    pg_conn.commit()

    sqlite_cursor.close()
    sqlite_conn.close()
    pg_cursor.close()
    pg_conn.close()

    return total_registros


def migrar_base_datos(sqlite_path, pg_db_name, nombre_modelo):
    """Migración completa de una base de datos"""
    print(f"\n{'=' * 60}")
    print(f"🔄 Migrando {nombre_modelo}")
    print(f"{'=' * 60}")

    crear_base_datos_postgres(pg_db_name)
    migrar_esquema(sqlite_path, pg_db_name)
    total = migrar_datos(sqlite_path, pg_db_name)

    print(f"✅ Migración completada: {total} registros totales")


def main():
    print("=" * 60)
    print("🚀 MIGRACIÓN SQLite → PostgreSQL")
    print("=" * 60)

    for i, (sqlite_db, postgres_db) in enumerate(zip(SQLITE_DBS, POSTGRES_DBS)):
        nombre_modelo = f"Modelo {'ABC'[i]}"
        migrar_base_datos(sqlite_db, postgres_db, nombre_modelo)

    print("\n" + "=" * 60)
    print("🎉 MIGRACIÓN COMPLETA")
    print("=" * 60)
    print("\n📌 Bases de datos creadas en PostgreSQL:")
    for db in POSTGRES_DBS:
        print(f"   - {db}")


if __name__ == "__main__":
    main()
