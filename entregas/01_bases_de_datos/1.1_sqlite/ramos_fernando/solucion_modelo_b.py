"""
Ejercicio 1.1 - Solución Modelo B: Normalizado (3NF)

Este script carga los CSV y crea un esquema normalizado con:
- Tabla categorias (26 categorías, una por tipo de componente)
- Tabla fabricantes (extraídos de los nombres de productos)
- Tabla productos (con FKs a categorias y fabricantes)
- Tabla colores (colores únicos extraídos)
- Tabla productos_colores (relación N:M)

Autor: Profesor
Fecha: 2025-12-11
Base de Datos Generada: tienda_modelo_b.db
"""

import os
import glob
import pandas as pd
import sqlite3
from pathlib import Path
import re


# ═══════════════════════════════════════════════════════════════════
# CONFIGURACIÓN DE RUTAS
# ═══════════════════════════════════════════════════════════════════

BASE_DIR = Path(__file__).parent.parent.parent.parent
RUTA_CSVs = BASE_DIR / ".profesor" / ".datos" / "csv_tienda_informatica"
RUTA_DB = Path(__file__).parent / "tienda_modelo_b.db"

print(f"📂 Buscando CSVs en: {RUTA_CSVs}")
print(f"💾 Base de datos se guardará en: {RUTA_DB}")
print("=" * 70)


# ═══════════════════════════════════════════════════════════════════
# FUNCIONES AUXILIARES
# ═══════════════════════════════════════════════════════════════════

def extraer_categoria_de_csv(nombre_archivo):
    """
    Extrae el nombre de categoría desde el nombre del CSV.

    Ejemplos:
        'cpu.csv' → 'CPU'
        'case-fan.csv' → 'Case Fan'
        'video-card.csv' → 'Video Card'
    """
    nombre = Path(nombre_archivo).stem  # Sin extensión
    # Reemplazar guiones por espacios y capitalizar
    categoria = nombre.replace('-', ' ').title()
    return categoria


def extraer_fabricante(nombre_producto):
    """
    Extrae el fabricante del nombre del producto.

    Por convención, el fabricante es la primera palabra.

    Ejemplos:
        'AMD Ryzen 7 7800X3D' → 'AMD'
        'Corsair Vengeance LPX 16 GB' → 'Corsair'
        'G.Skill Trident Z5 RGB' → 'G.Skill'
    """
    # Manejar casos como "G.Skill" (fabricantes con punto)
    if not isinstance(nombre_producto, str) or not nombre_producto.strip():
        return "Unknown"

    # Caso especial: G.Skill
    if nombre_producto.startswith("G.Skill"):
        return "G.Skill"

    # Caso general: primera palabra
    fabricante = nombre_producto.split()[0]
    return fabricante


def crear_esquema(conexion):
    """
    Crea las tablas del modelo normalizado.
    """
    cursor = conexion.cursor()

    # Tabla categorias
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS categorias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL UNIQUE,
            descripcion TEXT
        )
    """)

    # Tabla fabricantes
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS fabricantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL UNIQUE,
            pais TEXT,
            sitio_web TEXT
        )
    """)

    # Tabla colores
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS colores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL UNIQUE,
            codigo_hex TEXT
        )
    """)

    # Tabla productos
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            categoria_id INTEGER NOT NULL,
            fabricante_id INTEGER,
            precio REAL,
            especificaciones TEXT,
            FOREIGN KEY (categoria_id) REFERENCES categorias(id),
            FOREIGN KEY (fabricante_id) REFERENCES fabricantes(id)
        )
    """)

    # Tabla productos_colores (relación N:M)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos_colores (
            producto_id INTEGER NOT NULL,
            color_id INTEGER NOT NULL,
            PRIMARY KEY (producto_id, color_id),
            FOREIGN KEY (producto_id) REFERENCES productos(id),
            FOREIGN KEY (color_id) REFERENCES colores(id)
        )
    """)

    # Índices para mejorar performance en JOINs
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_productos_categoria ON productos(categoria_id)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_productos_fabricante ON productos(fabricante_id)")

    conexion.commit()
    print("✅ Esquema de base de datos creado (5 tablas + índices)\n")


def cargar_categorias(archivos_csv, conexion):
    """
    Carga las categorías basadas en los nombres de archivos CSV.
    """
    cursor = conexion.cursor()
    categorias_insertadas = 0

    for archivo in sorted(archivos_csv):
        categoria = extraer_categoria_de_csv(archivo)

        try:
            cursor.execute("""
                INSERT INTO categorias (nombre)
                VALUES (?)
            """, (categoria,))
            categorias_insertadas += 1
        except sqlite3.IntegrityError:
            # Ya existe (UNIQUE constraint)
            pass

    conexion.commit()
    print(f"✅ {categorias_insertadas} categorías cargadas")
    return categorias_insertadas


def cargar_fabricantes_y_colores(archivos_csv, conexion):
    """
    Lee todos los CSVs y extrae fabricantes y colores únicos.
    """
    cursor = conexion.cursor()

    fabricantes = set()
    colores = set()

    # Recorrer todos los CSVs
    for archivo in archivos_csv:
        try:
            df = pd.read_csv(archivo)

            # Extraer fabricantes del campo 'name'
            if 'name' in df.columns:
                for nombre in df['name'].dropna():
                    fab = extraer_fabricante(nombre)
                    fabricantes.add(fab)

            # Extraer colores del campo 'color' (si existe)
            if 'color' in df.columns:
                for color in df['color'].dropna():
                    # Manejar "Black / Yellow" → ["Black", "Yellow"]
                    if '/' in str(color):
                        for c in str(color).split('/'):
                            colores.add(c.strip())
                    else:
                        colores.add(str(color).strip())

        except Exception as e:
            print(f"   ⚠️  Error leyendo {Path(archivo).name}: {e}")

    # Insertar fabricantes
    for fab in sorted(fabricantes):
        try:
            cursor.execute("INSERT INTO fabricantes (nombre) VALUES (?)", (fab,))
        except sqlite3.IntegrityError:
            pass

    # Insertar colores
    for color in sorted(colores):
        if color and color != "nan":  # Evitar vacíos
            try:
                cursor.execute("INSERT INTO colores (nombre) VALUES (?)", (color,))
            except sqlite3.IntegrityError:
                pass

    conexion.commit()

    print(f"✅ {len(fabricantes)} fabricantes cargados")
    print(f"✅ {len(colores)} colores cargados\n")


def cargar_productos(archivos_csv, conexion):
    """
    Carga todos los productos con sus relaciones a categorías y fabricantes.
    """
    cursor = conexion.cursor()
    productos_insertados = 0

    for archivo in sorted(archivos_csv):
        try:
            df = pd.read_csv(archivo)
            categoria_nombre = extraer_categoria_de_csv(archivo)

            # Obtener ID de categoría
            cursor.execute("SELECT id FROM categorias WHERE nombre = ?", (categoria_nombre,))
            categoria_id = cursor.fetchone()[0]

            print(f"📄 {Path(archivo).name} → Categoría: {categoria_nombre}")

            # Insertar cada producto
            for _, row in df.iterrows():
                nombre = row.get('name', '')
                precio = row.get('price', None)

                if not nombre or pd.isna(nombre):
                    continue

                # Extraer fabricante
                fabricante_nombre = extraer_fabricante(nombre)

                # Obtener ID de fabricante
                cursor.execute("SELECT id FROM fabricantes WHERE nombre = ?", (fabricante_nombre,))
                resultado = cursor.fetchone()
                fabricante_id = resultado[0] if resultado else None

                # Guardar especificaciones como JSON (simplificado)
                # Todas las columnas excepto name, price, color
                especificaciones = row.drop(['name', 'price'], errors='ignore')
                if 'color' in especificaciones:
                    especificaciones = especificaciones.drop('color')

                # Convertir a string (en producción usarías JSON)
                espec_str = especificaciones.to_json()

                # Insertar producto
                cursor.execute("""
                    INSERT INTO productos (nombre, categoria_id, fabricante_id, precio, especificaciones)
                    VALUES (?, ?, ?, ?, ?)
                """, (nombre, categoria_id, fabricante_id, precio, espec_str))

                producto_id = cursor.lastrowid
                productos_insertados += 1

                # Relacionar con colores (si tiene)
                if 'color' in row and not pd.isna(row['color']):
                    color_str = str(row['color'])

                    # Manejar colores múltiples separados por "/"
                    colores_lista = [c.strip() for c in color_str.split('/')]

                    for color_nombre in colores_lista:
                        cursor.execute("SELECT id FROM colores WHERE nombre = ?", (color_nombre,))
                        resultado_color = cursor.fetchone()

                        if resultado_color:
                            color_id = resultado_color[0]
                            try:
                                cursor.execute("""
                                    INSERT INTO productos_colores (producto_id, color_id)
                                    VALUES (?, ?)
                                """, (producto_id, color_id))
                            except sqlite3.IntegrityError:
                                pass  # Ya existe

            print(f"   └─ ✅ {len(df)} productos cargados\n")

        except Exception as e:
            print(f"   └─ ❌ Error: {e}\n")

    conexion.commit()
    print(f"✅ Total de productos cargados: {productos_insertados:,}\n")


# ═══════════════════════════════════════════════════════════════════
# SCRIPT PRINCIPAL
# ═══════════════════════════════════════════════════════════════════

def main():
    """Función principal"""

    # 1. Verificar carpeta de CSVs
    if not RUTA_CSVs.exists():
        print(f"❌ Error: No se encontró la carpeta {RUTA_CSVs}")
        return

    # 2. Buscar archivos CSV
    archivos_csv = glob.glob(str(RUTA_CSVs / "*.csv"))

    if not archivos_csv:
        print(f"❌ No se encontraron archivos CSV")
        return

    print(f"✅ Se encontraron {len(archivos_csv)} archivos CSV\n")

    # 3. Conectar a BD (se crea si no existe)
    conexion = sqlite3.connect(RUTA_DB)
    print(f"💾 Conectado a: {RUTA_DB}\n")

    # 4. Crear esquema
    crear_esquema(conexion)

    # 5. Cargar datos
    print("📋 Paso 1: Cargando categorías...")
    cargar_categorias(archivos_csv, conexion)

    print("\n📋 Paso 2: Extrayendo fabricantes y colores...")
    cargar_fabricantes_y_colores(archivos_csv, conexion)

    print("📋 Paso 3: Cargando productos con relaciones...")
    cargar_productos(archivos_csv, conexion)

    # 6. Estadísticas finales
    cursor = conexion.cursor()

    cursor.execute("SELECT COUNT(*) FROM categorias")
    num_categorias = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM fabricantes")
    num_fabricantes = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM productos")
    num_productos = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM colores")
    num_colores = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM productos_colores")
    num_relaciones = cursor.fetchone()[0]

    conexion.close()

    # 7. Resumen
    print("=" * 70)
    print("📊 RESUMEN DEL MODELO NORMALIZADO")
    print("=" * 70)
    print(f"\n✅ Categorías: {num_categorias}")
    print(f"✅ Fabricantes: {num_fabricantes}")
    print(f"✅ Productos: {num_productos:,}")
    print(f"✅ Colores: {num_colores}")
    print(f"✅ Relaciones productos-colores: {num_relaciones}")

    print(f"\n💾 Base de datos: {RUTA_DB}")
    print(f"   Tamaño: {RUTA_DB.stat().st_size / 1024 / 1024:.2f} MB")

    print("\n" + "=" * 70)
    print("✅ MODELO NORMALIZADO CREADO CON ÉXITO")
    print("=" * 70)

    print("\n💡 Próximos pasos:")
    print("   1. Abre la BD con DB Browser for SQLite")
    print("   2. Explora las relaciones entre tablas")
    print("   3. Prueba consultas con JOINs")
    print("   4. Compara con Modelo A (desnormalizado)")


# ═══════════════════════════════════════════════════════════════════
# PUNTO DE ENTRADA
# ═══════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("\n" + "=" * 70)
    print(" MODELO B: NORMALIZADO (3NF)")
    print("=" * 70 + "\n")

    main()
