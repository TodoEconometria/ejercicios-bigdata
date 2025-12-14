"""
Script para realizar consultas de ejemplo en las bases de datos
generadas por el Modelo A (desnormalizado) y el Modelo B (normalizado).

Este script utiliza pandas para mostrar los resultados en un formato
de tabla claro y legible.
"""

import sqlite3
from pathlib import Path
import pandas as pd

# --- CONFIGURACIÓN DE RUTAS ---
RUTA_BASE = Path(__file__).parent
DB_MODELO_A = RUTA_BASE / "tienda_modelo_a.db"
DB_MODELO_B = RUTA_BASE / "tienda_modelo_b.db"


def ejecutar_consulta(db_path, query, title):
    """
    Se conecta a una base de datos, ejecuta una consulta y muestra los
    resultados en formato de tabla usando pandas.
    """
    print("=" * 80)
    print(f"📄 CONSULTA: {title}")
    print(f"💾 BASE DE DATOS: {db_path.name}")
    print("-" * 80)
    print(f"SQL: {query.strip()}")
    print("-" * 80)

    if not db_path.exists():
        print(f"❌ ERROR: No se encontró la base de datos en '{db_path}'")
        print("=" * 80 + "\n")
        return

    try:
        with sqlite3.connect(db_path) as conexion:
            # Usar pandas para leer la consulta SQL directamente en un DataFrame
            df = pd.read_sql_query(query, conexion)

            if df.empty:
                print("La consulta no devolvió resultados.")
            else:
                # Mostrar el DataFrame
                print(df.to_string())

    except (sqlite3.Error, pd.io.sql.DatabaseError) as e:
        print(f"❌ ERROR de SQL: {e}")

    print("=" * 80 + "\n")


def main():
    """Función principal que ejecuta todas las consultas."""

    # --- Consultas para el Modelo A (Desnormalizado) ---

    ejecutar_consulta(
        db_path=DB_MODELO_A,
        title="Ver los primeros 10 registros de la tabla 'cpu'",
        query="SELECT * FROM cpu LIMIT 10;"
    )

    ejecutar_consulta(
        db_path=DB_MODELO_A,
        title="Contar cuántos registros hay en la tabla 'gpu'",
        query="SELECT COUNT(*) AS total_gpus FROM cpu;"
    )

    ejecutar_consulta(
        db_path=DB_MODELO_A,
        title="Seleccionar nombre y precio de 5 registros en 'memory'",
        query="SELECT name, price FROM memory LIMIT 5;"
    )

    ejecutar_consulta(
        db_path=DB_MODELO_A,
        title="Filtrar CPUs con precio mayor a 300",
        query="SELECT name, price FROM cpu WHERE price > 2000;"
    )

    # --- Consulta JOIN para el Modelo B (Normalizado) ---
    # CORREGIDO: Esta consulta ahora usa la estructura correcta del Modelo B.
    # Une 'productos' con 'fabricantes' y 'categorias'.

    query_join_modelo_b = """
    SELECT
        p.nombre,
        p.precio,
        f.nombre AS fabricante
    FROM
        productos AS p
    INNER JOIN
        fabricantes AS f ON p.fabricante_id = f.id
    INNER JOIN
        categorias AS c ON p.categoria_id = c.id
    WHERE
        p.precio > 2000 AND c.nombre = 'Cpu';
    """

    ejecutar_consulta(
        db_path=DB_MODELO_B,
        title="COMPARACIÓN: Filtrar CPUs con precio > 2000 (usando JOIN)",
        query=query_join_modelo_b
    )


if __name__ == "__main__":
    # Asegurarse de que pandas esté instalado
    try:
        import pandas
    except ImportError:
        print("="*80)
        print("⚠️ ADVERTENCIA: La librería 'pandas' no está instalada.")
        print("   Para ver los resultados como tablas, por favor, instálala ejecutando:")
        print("   pip install pandas")
        print("="*80)
    else:
        main()
