"""
Ejercicio 1.1 - Solución Modelo A: Catálogo Simple (Desnormalizado)

Este script carga todos los CSV de la tienda de componentes directamente
a una base de datos SQLite, creando una tabla por cada archivo CSV.

Autor: Profesor
Fecha: 2025-12-11
Base de Datos Generada: tienda_modelo_a.db
"""

import os
import glob
import pandas as pd
import sqlite3
from pathlib import Path


# ═══════════════════════════════════════════════════════════════════
# CONFIGURACIÓN DE RUTAS
# ═══════════════════════════════════════════════════════════════════

# Ruta a la carpeta con los CSVs (ajusta según tu estructura)
BASE_DIR = Path(__file__).parent.parent.parent.parent
RUTA_CSVs = BASE_DIR / ".profesor" / ".datos" / "csv_tienda_informatica"
RUTA_DB = Path(__file__).parent / "tienda_modelo_a.db"

print(f"📂 Buscando CSVs en: {RUTA_CSVs}")
print(f"💾 Base de datos se guardará en: {RUTA_DB}")
print("=" * 70)


# ═══════════════════════════════════════════════════════════════════
# FUNCIONES AUXILIARES
# ═══════════════════════════════════════════════════════════════════

def extraer_nombre_tabla(ruta_csv):
    """
    Extrae el nombre de la tabla desde el nombre del archivo CSV.

    Ejemplo:
        'cpu.csv' → 'cpu'
        'case-fan.csv' → 'case_fan'
    """
    nombre = Path(ruta_csv).stem  # Obtiene nombre sin extensión
    nombre = nombre.replace('-', '_')  # Reemplaza guiones por guiones bajos
    return nombre


def cargar_csv_a_tabla(ruta_csv, conexion):
    """
    Lee un archivo CSV y lo carga como tabla en SQLite.

    Parámetros:
        ruta_csv (str): Ruta completa al archivo CSV
        conexion: Objeto de conexión a SQLite

    Retorna:
        tuple: (nombre_tabla, cantidad_filas)
    """
    # Obtener nombre de tabla
    nombre_tabla = extraer_nombre_tabla(ruta_csv)

    # Leer CSV con pandas
    try:
        df = pd.read_csv(ruta_csv)

        # Información del CSV
        num_filas = len(df)
        num_columnas = len(df.columns)

        print(f"📄 {Path(ruta_csv).name}")
        print(f"   └─ Tabla: {nombre_tabla}")
        print(f"   └─ Filas: {num_filas:,} | Columnas: {num_columnas}")

        # Cargar a SQLite
        # if_exists='replace': Si la tabla ya existe, la reemplaza
        # index=False: No guardamos el índice de pandas como columna
        df.to_sql(nombre_tabla, conexion, if_exists='replace', index=False)

        print(f"   └─ ✅ Cargado exitosamente\n")

        return (nombre_tabla, num_filas)

    except Exception as e:
        print(f"   └─ ❌ Error: {e}\n")
        return (nombre_tabla, 0)


# ═══════════════════════════════════════════════════════════════════
# SCRIPT PRINCIPAL
# ═══════════════════════════════════════════════════════════════════

def main():
    """Función principal que coordina la carga de todos los CSVs"""

    # 1. Verificar que la carpeta de CSVs existe
    if not RUTA_CSVs.exists():
        print(f"❌ Error: No se encontró la carpeta {RUTA_CSVs}")
        print("   Asegúrate de tener los CSVs en la ruta correcta.")
        return

    # 2. Buscar todos los archivos CSV
    patron_csv = str(RUTA_CSVs / "*.csv")
    archivos_csv = glob.glob(patron_csv)

    if not archivos_csv:
        print(f"❌ No se encontraron archivos CSV en {RUTA_CSVs}")
        return

    print(f"✅ Se encontraron {len(archivos_csv)} archivos CSV\n")

    # 3. Conectar a la base de datos SQLite
    # Si el archivo no existe, se crea automáticamente
    try:
        conexion = sqlite3.connect(RUTA_DB)
        print(f"💾 Conectado a la base de datos: {RUTA_DB}\n")
    except Exception as e:
        print(f"❌ Error al conectar a la BD: {e}")
        return

    # 4. Cargar cada CSV como una tabla
    resultados = []

    for ruta_csv in sorted(archivos_csv):  # Ordenados alfabéticamente
        nombre_tabla, num_filas = cargar_csv_a_tabla(ruta_csv, conexion)
        resultados.append((nombre_tabla, num_filas))

    # 5. Cerrar conexión
    conexion.close()

    # 6. Resumen final
    print("=" * 70)
    print("📊 RESUMEN DE LA CARGA")
    print("=" * 70)

    total_tablas = len(resultados)
    total_filas = sum(num_filas for _, num_filas in resultados)

    print(f"\n✅ Total de tablas creadas: {total_tablas}")
    print(f"✅ Total de registros cargados: {total_filas:,}")
    print(f"\n💾 Base de datos guardada en: {RUTA_DB}")
    print(f"   Tamaño: {RUTA_DB.stat().st_size / 1024 / 1024:.2f} MB")

    # Tabla de resumen
    print("\n📋 DETALLE POR TABLA:")
    print("-" * 70)
    print(f"{'Tabla':<30} {'Registros':>15}")
    print("-" * 70)
    for nombre_tabla, num_filas in resultados:
        if num_filas > 0:
            print(f"{nombre_tabla:<30} {num_filas:>15,}")
    print("-" * 70)

    # 7. Verificación opcional con consultas SQL
    print("\n🔍 VERIFICACIÓN (muestra de datos):")
    print("-" * 70)

    conexion = sqlite3.connect(RUTA_DB)
    cursor = conexion.cursor()

    # Listar todas las tablas
    cursor.execute("""
        SELECT name FROM sqlite_master
        WHERE type='table'
        ORDER BY name
    """)
    tablas = cursor.fetchall()

    # Mostrar primeras filas de la tabla 'cpu' como ejemplo
    if ('cpu',) in tablas:
        print("\n📄 Ejemplo: Primeras 3 filas de tabla 'cpu':")
        cursor.execute("SELECT * FROM cpu LIMIT 3")
        filas = cursor.fetchall()

        # Obtener nombres de columnas
        columnas = [desc[0] for desc in cursor.description]
        print(f"\nColumnas: {', '.join(columnas)}")
        print()

        for fila in filas:
            print(f"  {fila[0][:40]:<40} | ${fila[1]:>7.2f}")

    conexion.close()

    print("\n" + "=" * 70)
    print("✅ PROCESO COMPLETADO CON ÉXITO")
    print("=" * 70)
    print("\n💡 Próximos pasos:")
    print("   1. Abre 'tienda_modelo_a.db' con DB Browser for SQLite")
    print("   2. Explora las tablas y datos")
    print("   3. Prueba hacer consultas SQL básicas")
    print("   4. Compara este modelo con el Modelo B (normalizado)")


# ═══════════════════════════════════════════════════════════════════
# PUNTO DE ENTRADA
# ═══════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("\n" + "=" * 70)
    print(" MODELO A: CATÁLOGO SIMPLE (DESNORMALIZADO)")
    print("=" * 70 + "\n")

    main()
