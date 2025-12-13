"""
CONSULTAS SQL - TIENDA (MODELO A)
Lee la base de datos 'tienda_modelo_a.db' (SQLite) y ejecuta consultas interesantes
sobre las tablas generadas (una tabla por CSV).

- Robusto ante nombres de tablas reservadas (ej: "case")
- Detecta columnas disponibles antes de ejecutar consultas
"""

import os
from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine


print("========================================================")
print("== CONSULTAS TIENDA (MODELO A) ==")
print("========================================================")

# Ruta a la base de datos SQLite
RUTA_DB = Path(__file__).parent / "tienda_modelo_a.db"
print(f"[CONFIG] Ruta de la BD SQLite: {RUTA_DB}")


# ─────────────────────────────────────────────────────────────
# Helpers SQL (para evitar errores con palabras reservadas)
# ─────────────────────────────────────────────────────────────

def qident(name: str) -> str:
    """
    Cita un identificador SQL (tabla/columna) con comillas dobles.
    Ej: case -> "case"
    Además, escapa comillas dobles internas por seguridad.
    """
    return f'"{name.replace(chr(34), chr(34) * 2)}"'


def obtener_tablas(motor_db):
    sql = """
    SELECT name
    FROM sqlite_master
    WHERE type='table'
    ORDER BY name;
    """
    df = pd.read_sql(sql, motor_db)
    return df["name"].tolist()


def columnas_tabla(motor_db, tabla: str):
    # PRAGMA table_info("tabla")
    df = pd.read_sql(f"PRAGMA table_info({qident(tabla)});", motor_db)
    return df["name"].tolist()


def ejecutar_y_mostrar(motor_db, titulo: str, sql: str, head: int = 10):
    print(f"\n🧾 {titulo}")
    print("-" * 70)
    try:
        dfq = pd.read_sql(sql, motor_db)
        print(dfq.head(head))
        return dfq
    except Exception as e:
        print(f"❌ Error: {e}")
        return None


# ─────────────────────────────────────────────────────────────
# Consultas interesantes (defensivas)
# ─────────────────────────────────────────────────────────────

def ejecutar_consultas_tienda(motor_db):
    tablas = obtener_tablas(motor_db)

    print("\n📦 Tablas detectadas:")
    print(tablas)

    if not tablas:
        print("❌ No hay tablas en la BD. ¿Seguro que cargaste los CSVs?")
        return

    # 1) Conteo de filas por tabla (para comprobar carga)
    print("\n" + "=" * 70)
    print("1) INVENTARIO: filas por tabla")
    print("=" * 70)
    for t in tablas:
        ejecutar_y_mostrar(
            motor_db,
            f"Filas en tabla '{t}'",
            f"SELECT COUNT(*) AS filas FROM {qident(t)};"
        )

    # 2) Busca una tabla con 'price' para rankings y stats de precios
    tabla_con_price = None
    for t in tablas:
        cols = columnas_tabla(motor_db, t)
        if "price" in cols:
            tabla_con_price = t
            break

    if tabla_con_price:
        print("\n" + "=" * 70)
        print("2) PRECIOS: ranking y estadísticas")
        print("=" * 70)

        ejecutar_y_mostrar(
            motor_db,
            f"Top 10 más caros (tabla '{tabla_con_price}')",
            f"""
            SELECT *
            FROM {qident(tabla_con_price)}
            WHERE price IS NOT NULL
            ORDER BY CAST(price AS REAL) DESC
            LIMIT 10;
            """
        )

        ejecutar_y_mostrar(
            motor_db,
            f"Stats de precio (tabla '{tabla_con_price}')",
            f"""
            SELECT
                MIN(CAST(price AS REAL)) AS min_price,
                AVG(CAST(price AS REAL)) AS avg_price,
                MAX(CAST(price AS REAL)) AS max_price,
                COUNT(*) AS n
            FROM {qident(tabla_con_price)}
            WHERE price IS NOT NULL;
            """
        )
    else:
        print("\nℹ️ No encontré ninguna tabla con columna 'price'.")

    # 3) Top marcas (si existe 'brand' en alguna tabla)
    tabla_con_brand = None
    for t in tablas:
        cols = columnas_tabla(motor_db, t)
        if "brand" in cols:
            tabla_con_brand = t
            break

    if tabla_con_brand:
        print("\n" + "=" * 70)
        print("3) MARCAS: top marcas más frecuentes")
        print("=" * 70)

        ejecutar_y_mostrar(
            motor_db,
            f"Top 15 marcas (tabla '{tabla_con_brand}')",
            f"""
            SELECT brand, COUNT(*) AS n
            FROM {qident(tabla_con_brand)}
            WHERE brand IS NOT NULL AND TRIM(brand) <> ''
            GROUP BY brand
            ORDER BY n DESC
            LIMIT 15;
            """
        )
    else:
        print("\nℹ️ No encontré ninguna tabla con columna 'brand'.")

    # 4) CPU: top precio y €/core (si existe core_count)
    if "cpu" in tablas:
        cols = columnas_tabla(motor_db, "cpu")
        print("\n" + "=" * 70)
        print("4) CPU: análisis")
        print("=" * 70)

        if "price" in cols and "name" in cols:
            ejecutar_y_mostrar(
                motor_db,
                "CPU: Top 10 más caras",
                """
                SELECT name, price
                FROM "cpu"
                WHERE price IS NOT NULL
                ORDER BY CAST(price AS REAL) DESC
                LIMIT 10;
                """
            )

        if "brand" in cols:
            ejecutar_y_mostrar(
                motor_db,
                "CPU: conteo por marca",
                """
                SELECT brand, COUNT(*) AS n
                FROM "cpu"
                WHERE brand IS NOT NULL AND TRIM(brand) <> ''
                GROUP BY brand
                ORDER BY n DESC;
                """
            )

        if "price" in cols and "core_count" in cols and "name" in cols:
            ejecutar_y_mostrar(
                motor_db,
                "CPU: mejor €/core (menor precio por core)",
                """
                SELECT
                    name,
                    CAST(price AS REAL) AS price,
                    CAST(core_count AS REAL) AS cores,
                    ROUND(CAST(price AS REAL) / NULLIF(CAST(core_count AS REAL), 0), 2) AS eur_por_core
                FROM "cpu"
                WHERE price IS NOT NULL AND core_count IS NOT NULL
                ORDER BY eur_por_core ASC
                LIMIT 15;
                """
            )

    # 5) GPU (video_card): top precio y chipset
    if "video_card" in tablas:
        cols = columnas_tabla(motor_db, "video_card")
        print("\n" + "=" * 70)
        print("5) GPU (video_card): análisis")
        print("=" * 70)

        if "price" in cols and "name" in cols:
            ejecutar_y_mostrar(
                motor_db,
                "GPU: Top 10 más caras",
                """
                SELECT name, price
                FROM "video_card"
                WHERE price IS NOT NULL
                ORDER BY CAST(price AS REAL) DESC
                LIMIT 10;
                """
            )

        if "chipset" in cols:
            ejecutar_y_mostrar(
                motor_db,
                "GPU: conteo por chipset (Top 15)",
                """
                SELECT chipset, COUNT(*) AS n
                FROM "video_card"
                WHERE chipset IS NOT NULL AND TRIM(chipset) <> ''
                GROUP BY chipset
                ORDER BY n DESC
                LIMIT 15;
                """
            )

    # 6) RAM (memory): capacidad y €/GB
    if "memory" in tablas:
        cols = columnas_tabla(motor_db, "memory")
        print("\n" + "=" * 70)
        print("6) RAM (memory): análisis")
        print("=" * 70)

        if "capacity" in cols:
            ejecutar_y_mostrar(
                motor_db,
                "RAM: conteo por capacidad (Top 15)",
                """
                SELECT capacity, COUNT(*) AS n
                FROM "memory"
                WHERE capacity IS NOT NULL AND TRIM(CAST(capacity AS TEXT)) <> ''
                GROUP BY capacity
                ORDER BY n DESC
                LIMIT 15;
                """
            )

        if "price" in cols and "capacity" in cols and "name" in cols:
            ejecutar_y_mostrar(
                motor_db,
                "RAM: €/GB (más barato por GB)",
                """
                SELECT
                    name,
                    CAST(price AS REAL) AS price,
                    CAST(capacity AS REAL) AS capacity_gb,
                    ROUND(CAST(price AS REAL) / NULLIF(CAST(capacity AS REAL), 0), 4) AS eur_por_gb
                FROM "memory"
                WHERE price IS NOT NULL AND capacity IS NOT NULL
                ORDER BY eur_por_gb ASC
                LIMIT 15;
                """
            )

    # 7) Almacenamiento (internal/external): €/GB
    print("\n" + "=" * 70)
    print("7) ALMACENAMIENTO: €/GB")
    print("=" * 70)

    for t in ["internal_hard_drive", "external_hard_drive"]:
        if t in tablas:
            cols = columnas_tabla(motor_db, t)
            if "price" in cols and "capacity" in cols and "name" in cols:
                ejecutar_y_mostrar(
                    motor_db,
                    f"{t}: €/GB (más barato por GB)",
                    f"""
                    SELECT
                        name,
                        CAST(price AS REAL) AS price,
                        CAST(capacity AS REAL) AS capacity_gb,
                        ROUND(CAST(price AS REAL) / NULLIF(CAST(capacity AS REAL), 0), 4) AS eur_por_gb
                    FROM {qident(t)}
                    WHERE price IS NOT NULL AND capacity IS NOT NULL
                    ORDER BY eur_por_gb ASC
                    LIMIT 15;
                    """
                )
            else:
                print(f"ℹ️ Tabla '{t}' no tiene columnas necesarias (name/price/capacity).")

    # 8) Calidad de datos: precios raros (<=0) en cualquier tabla con price
    print("\n" + "=" * 70)
    print("8) CALIDAD DE DATOS: precios sospechosos (<= 0)")
    print("=" * 70)

    for t in tablas:
        cols = columnas_tabla(motor_db, t)
        if "price" in cols:
            ejecutar_y_mostrar(
                motor_db,
                f"Precios sospechosos en '{t}'",
                f"""
                SELECT *
                FROM {qident(t)}
                WHERE price IS NOT NULL AND CAST(price AS REAL) <= 0
                LIMIT 10;
                """
            )

    print("\n✅ Fin de consultas tienda.")


# ─────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    if not os.path.exists(RUTA_DB):
        print(f"❌ ERROR: No se encontró la base de datos en {RUTA_DB}")
        print("   Asegúrate de haber ejecutado el script que crea 'tienda_modelo_a.db'.")
    else:
        motor_db = create_engine(f"sqlite:///{RUTA_DB}")
        ejecutar_consultas_tienda(motor_db)
