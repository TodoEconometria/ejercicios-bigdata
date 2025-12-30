"""
Ejercicio 1.1 - Solución Modelo C: E-Commerce Completo

Este script extiende el Modelo B agregando:
- Tabla clientes
- Tabla pedidos
- Tabla lineas_pedido
- Tabla carritos
- Tabla items_carrito
- Tabla inventario

Además genera datos de ejemplo para simular un sistema de tienda online.

Autor: Profesor
Fecha: 2025-12-11
Base de Datos Generada: tienda_modelo_c.db
"""

import os
import glob
import pandas as pd
import sqlite3
from pathlib import Path
import random
from datetime import datetime, timedelta


# ═══════════════════════════════════════════════════════════════════
# CONFIGURACIÓN DE RUTAS
# ═══════════════════════════════════════════════════════════════════

BASE_DIR = Path(__file__).parent.parent.parent.parent
RUTA_CSVs = BASE_DIR / ".profesor" / ".datos" / "csv_tienda_informatica"
RUTA_DB = Path(__file__).parent / "tienda_modelo_c.db"

# Importar funciones del Modelo B
# (En producción sería mejor tener un módulo común)
import sys
sys.path.append(str(Path(__file__).parent))

# Copiar funciones necesarias del modelo_b
def extraer_categoria_de_csv(nombre_archivo):
    """Extrae categoría del nombre del archivo CSV"""
    nombre = Path(nombre_archivo).stem
    categoria = nombre.replace('-', ' ').title()
    return categoria

def extraer_fabricante(nombre_producto):
    """Extrae fabricante del nombre del producto"""
    if not isinstance(nombre_producto, str) or not nombre_producto.strip():
        return "Unknown"
    if nombre_producto.startswith("G.Skill"):
        return "G.Skill"
    return nombre_producto.split()[0]


# ═══════════════════════════════════════════════════════════════════
# FUNCIONES DE CREACIÓN DE ESQUEMA
# ═══════════════════════════════════════════════════════════════════

def crear_esquema_base(conexion):
    """Crea las tablas del Modelo B (categorías, fabricantes, productos, colores)"""
    cursor = conexion.cursor()

    # Tablas del Modelo B
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS categorias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL UNIQUE,
            descripcion TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS fabricantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL UNIQUE,
            pais TEXT,
            sitio_web TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS colores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL UNIQUE,
            codigo_hex TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            categoria_id INTEGER NOT NULL,
            fabricante_id INTEGER,
            precio REAL CHECK(precio > 0),
            especificaciones TEXT,
            FOREIGN KEY (categoria_id) REFERENCES categorias(id),
            FOREIGN KEY (fabricante_id) REFERENCES fabricantes(id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos_colores (
            producto_id INTEGER NOT NULL,
            color_id INTEGER NOT NULL,
            PRIMARY KEY (producto_id, color_id),
            FOREIGN KEY (producto_id) REFERENCES productos(id),
            FOREIGN KEY (color_id) REFERENCES colores(id)
        )
    """)

    conexion.commit()


def crear_esquema_ecommerce(conexion):
    """Crea las tablas adicionales del e-commerce (Modelo C)"""
    cursor = conexion.cursor()

    # Tabla clientes
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL UNIQUE,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            direccion TEXT,
            telefono TEXT,
            fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Tabla pedidos
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pedidos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_id INTEGER NOT NULL,
            fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
            estado TEXT CHECK(estado IN ('pendiente', 'procesando', 'enviado', 'entregado', 'cancelado')),
            total REAL,
            metodo_pago TEXT,
            direccion_envio TEXT,
            FOREIGN KEY (cliente_id) REFERENCES clientes(id)
        )
    """)

    # Tabla líneas de pedido
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS lineas_pedido (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pedido_id INTEGER NOT NULL,
            producto_id INTEGER NOT NULL,
            cantidad INTEGER NOT NULL CHECK(cantidad > 0),
            precio_unitario REAL NOT NULL,
            subtotal REAL NOT NULL,
            FOREIGN KEY (pedido_id) REFERENCES pedidos(id),
            FOREIGN KEY (producto_id) REFERENCES productos(id)
        )
    """)

    # Tabla carritos
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS carritos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_id INTEGER NOT NULL UNIQUE,
            fecha_creacion DATETIME DEFAULT CURRENT_TIMESTAMP,
            ultima_modificacion DATETIME DEFAULT CURRENT_TIMESTAMP,
            activo BOOLEAN DEFAULT 1,
            FOREIGN KEY (cliente_id) REFERENCES clientes(id)
        )
    """)

    # Tabla items en carrito
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS items_carrito (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            carrito_id INTEGER NOT NULL,
            producto_id INTEGER NOT NULL,
            cantidad INTEGER NOT NULL CHECK(cantidad > 0),
            FOREIGN KEY (carrito_id) REFERENCES carritos(id),
            FOREIGN KEY (producto_id) REFERENCES productos(id),
            UNIQUE(carrito_id, producto_id)
        )
    """)

    # Tabla inventario
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS inventario (
            producto_id INTEGER PRIMARY KEY,
            cantidad_stock INTEGER NOT NULL DEFAULT 0 CHECK(cantidad_stock >= 0),
            ubicacion TEXT,
            stock_minimo INTEGER DEFAULT 10,
            ultima_actualizacion DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (producto_id) REFERENCES productos(id)
        )
    """)

    # Índices para mejorar performance
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_pedidos_cliente ON pedidos(cliente_id)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_pedidos_fecha ON pedidos(fecha)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_lineas_pedido ON lineas_pedido(pedido_id)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_items_carrito ON items_carrito(carrito_id)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_inventario_stock ON inventario(cantidad_stock)")

    conexion.commit()
    print("✅ Esquema e-commerce creado (6 tablas adicionales + índices)\n")


# ═══════════════════════════════════════════════════════════════════
# FUNCIONES DE CARGA DE DATOS (Reutilizadas del Modelo B)
# ═══════════════════════════════════════════════════════════════════

def cargar_datos_base(archivos_csv, conexion):
    """Carga categorías, fabricantes, colores y productos (Modelo B)"""
    cursor = conexion.cursor()

    # 1. Cargar categorías
    print("📋 Cargando categorías...")
    for archivo in sorted(archivos_csv):
        categoria = extraer_categoria_de_csv(archivo)
        try:
            cursor.execute("INSERT INTO categorias (nombre) VALUES (?)", (categoria,))
        except sqlite3.IntegrityError:
            pass
    conexion.commit()

    # 2. Cargar fabricantes y colores
    print("📋 Extrayendo fabricantes y colores...")
    fabricantes = set()
    colores = set()

    for archivo in archivos_csv:
        try:
            df = pd.read_csv(archivo)
            if 'name' in df.columns:
                for nombre in df['name'].dropna():
                    fabricantes.add(extraer_fabricante(nombre))
            if 'color' in df.columns:
                for color in df['color'].dropna():
                    if '/' in str(color):
                        for c in str(color).split('/'):
                            colores.add(c.strip())
                    else:
                        colores.add(str(color).strip())
        except Exception as e:
            pass

    for fab in sorted(fabricantes):
        try:
            cursor.execute("INSERT INTO fabricantes (nombre) VALUES (?)", (fab,))
        except sqlite3.IntegrityError:
            pass

    for color in sorted(colores):
        if color and color != "nan":
            try:
                cursor.execute("INSERT INTO colores (nombre) VALUES (?)", (color,))
            except sqlite3.IntegrityError:
                pass

    conexion.commit()

    # 3. Cargar productos
    print("📋 Cargando productos...")
    productos_insertados = 0

    for archivo in sorted(archivos_csv):
        try:
            df = pd.read_csv(archivo)
            categoria_nombre = extraer_categoria_de_csv(archivo)

            cursor.execute("SELECT id FROM categorias WHERE nombre = ?", (categoria_nombre,))
            categoria_id = cursor.fetchone()[0]

            for _, row in df.iterrows():
                nombre = row.get('name', '')
                precio = row.get('price', None)

                if not nombre or pd.isna(nombre):
                    continue

                fabricante_nombre = extraer_fabricante(nombre)
                cursor.execute("SELECT id FROM fabricantes WHERE nombre = ?", (fabricante_nombre,))
                resultado = cursor.fetchone()
                fabricante_id = resultado[0] if resultado else None

                especificaciones = row.drop(['name', 'price'], errors='ignore')
                if 'color' in especificaciones:
                    especificaciones = especificaciones.drop('color')
                espec_str = especificaciones.to_json()

                cursor.execute("""
                    INSERT INTO productos (nombre, categoria_id, fabricante_id, precio, especificaciones)
                    VALUES (?, ?, ?, ?, ?)
                """, (nombre, categoria_id, fabricante_id, precio, espec_str))

                producto_id = cursor.lastrowid
                productos_insertados += 1

                # Relacionar colores
                if 'color' in row and not pd.isna(row['color']):
                    colores_lista = [c.strip() for c in str(row['color']).split('/')]
                    for color_nombre in colores_lista:
                        cursor.execute("SELECT id FROM colores WHERE nombre = ?", (color_nombre,))
                        resultado_color = cursor.fetchone()
                        if resultado_color:
                            try:
                                cursor.execute("""
                                    INSERT INTO productos_colores (producto_id, color_id)
                                    VALUES (?, ?)
                                """, (producto_id, resultado_color[0]))
                            except sqlite3.IntegrityError:
                                pass

        except Exception as e:
            pass

    conexion.commit()
    print(f"✅ {productos_insertados:,} productos cargados\n")


# ═══════════════════════════════════════════════════════════════════
# FUNCIONES DE GENERACIÓN DE DATOS FICTICIOS
# ═══════════════════════════════════════════════════════════════════

def generar_clientes(conexion):
    """Genera clientes de ejemplo"""
    cursor = conexion.cursor()

    clientes_ficticios = [
        ("juan.perez@email.com", "Juan", "Pérez", "Calle Mayor 123, Madrid", "666-111-222"),
        ("maria.lopez@email.com", "María", "López", "Av. Libertad 45, Barcelona", "677-333-444"),
        ("carlos.garcia@email.com", "Carlos", "García", "Plaza España 7, Valencia", "688-555-666"),
        ("ana.martinez@email.com", "Ana", "Martínez", "Calle Real 89, Sevilla", "699-777-888"),
        ("luis.rodriguez@email.com", "Luis", "Rodríguez", "Paseo Gracia 34, Bilbao", "611-222-333"),
    ]

    for email, nombre, apellido, direccion, telefono in clientes_ficticios:
        cursor.execute("""
            INSERT INTO clientes (email, nombre, apellido, direccion, telefono)
            VALUES (?, ?, ?, ?, ?)
        """, (email, nombre, apellido, direccion, telefono))

    conexion.commit()
    print(f"✅ {len(clientes_ficticios)} clientes generados")


def generar_inventario(conexion):
    """Genera inventario inicial para todos los productos"""
    cursor = conexion.cursor()

    cursor.execute("SELECT id FROM productos")
    productos = cursor.fetchall()

    for (producto_id,) in productos:
        # Stock aleatorio entre 50 y 200 unidades
        stock = random.randint(50, 200)
        # Stock mínimo aleatorio entre 5 y 20
        stock_minimo = random.randint(5, 20)
        # Ubicaciones ficticias
        ubicaciones = ["Almacén A", "Almacén B", "Almacén C", "Tienda Central"]
        ubicacion = random.choice(ubicaciones)

        cursor.execute("""
            INSERT INTO inventario (producto_id, cantidad_stock, ubicacion, stock_minimo)
            VALUES (?, ?, ?, ?)
        """, (producto_id, stock, ubicacion, stock_minimo))

    conexion.commit()
    print(f"✅ Inventario generado para {len(productos)} productos")


def generar_pedidos(conexion):
    """Genera pedidos de ejemplo con sus líneas"""
    cursor = conexion.cursor()

    # Obtener IDs de clientes
    cursor.execute("SELECT id FROM clientes")
    clientes_ids = [row[0] for row in cursor.fetchall()]

    # Obtener productos con precio
    cursor.execute("SELECT id, precio FROM productos WHERE precio IS NOT NULL LIMIT 100")
    productos = cursor.fetchall()

    estados = ['entregado', 'enviado', 'procesando', 'pendiente']
    metodos_pago = ['tarjeta_credito', 'paypal', 'transferencia', 'contrareembolso']

    pedidos_generados = 0

    # Generar 2-3 pedidos por cliente
    for cliente_id in clientes_ids:
        num_pedidos = random.randint(2, 3)

        for _ in range(num_pedidos):
            # Fecha aleatoria en los últimos 60 días
            dias_atras = random.randint(1, 60)
            fecha = datetime.now() - timedelta(days=dias_atras)

            estado = random.choice(estados)
            metodo = random.choice(metodos_pago)

            # Crear pedido
            cursor.execute("""
                INSERT INTO pedidos (cliente_id, fecha, estado, metodo_pago, total)
                VALUES (?, ?, ?, ?, ?)
            """, (cliente_id, fecha, estado, metodo, 0.0))  # total se calculará

            pedido_id = cursor.lastrowid
            pedidos_generados += 1

            # Agregar 1-4 productos al pedido
            num_productos = random.randint(1, 4)
            productos_pedido = random.sample(productos, min(num_productos, len(productos)))

            total_pedido = 0.0

            for producto_id, precio in productos_pedido:
                cantidad = random.randint(1, 3)
                subtotal = precio * cantidad
                total_pedido += subtotal

                cursor.execute("""
                    INSERT INTO lineas_pedido (pedido_id, producto_id, cantidad, precio_unitario, subtotal)
                    VALUES (?, ?, ?, ?, ?)
                """, (pedido_id, producto_id, cantidad, precio, subtotal))

                # Actualizar inventario (reducir stock)
                cursor.execute("""
                    UPDATE inventario
                    SET cantidad_stock = cantidad_stock - ?,
                        ultima_actualizacion = CURRENT_TIMESTAMP
                    WHERE producto_id = ?
                """, (cantidad, producto_id))

            # Actualizar total del pedido
            cursor.execute("UPDATE pedidos SET total = ? WHERE id = ?", (total_pedido, pedido_id))

    conexion.commit()
    print(f"✅ {pedidos_generados} pedidos generados")


def generar_carritos(conexion):
    """Genera carritos activos para algunos clientes"""
    cursor = conexion.cursor()

    cursor.execute("SELECT id FROM clientes LIMIT 3")  # Solo 3 clientes con carrito activo
    clientes_ids = [row[0] for row in cursor.fetchall()]

    cursor.execute("SELECT id, precio FROM productos WHERE precio IS NOT NULL LIMIT 50")
    productos = cursor.fetchall()

    for cliente_id in clientes_ids:
        # Crear carrito
        cursor.execute("""
            INSERT INTO carritos (cliente_id, activo)
            VALUES (?, 1)
        """, (cliente_id,))

        carrito_id = cursor.lastrowid

        # Agregar 1-3 productos al carrito
        num_items = random.randint(1, 3)
        productos_carrito = random.sample(productos, num_items)

        for producto_id, precio in productos_carrito:
            cantidad = random.randint(1, 2)

            cursor.execute("""
                INSERT INTO items_carrito (carrito_id, producto_id, cantidad)
                VALUES (?, ?, ?)
            """, (carrito_id, producto_id, cantidad))

    conexion.commit()
    print(f"✅ {len(clientes_ids)} carritos activos generados")


# ═══════════════════════════════════════════════════════════════════
# SCRIPT PRINCIPAL
# ═══════════════════════════════════════════════════════════════════

def main():
    """Función principal"""

    print(f"📂 Buscando CSVs en: {RUTA_CSVs}")
    print(f"💾 Base de datos: {RUTA_DB}")
    print("=" * 70)

    # 1. Verificar carpeta
    if not RUTA_CSVs.exists():
        print(f"❌ Error: No se encontró {RUTA_CSVs}")
        return

    # 2. Buscar CSVs
    archivos_csv = glob.glob(str(RUTA_CSVs / "*.csv"))
    if not archivos_csv:
        print("❌ No se encontraron CSVs")
        return

    print(f"✅ {len(archivos_csv)} archivos CSV encontrados\n")

    # 3. Conectar a BD
    conexion = sqlite3.connect(RUTA_DB)

    # 4. Crear esquemas
    print("📋 Creando esquema base (Modelo B)...")
    crear_esquema_base(conexion)
    print("✅ Esquema base creado\n")

    print("📋 Creando esquema e-commerce (Modelo C)...")
    crear_esquema_ecommerce(conexion)

    # 5. Cargar datos base
    cargar_datos_base(archivos_csv, conexion)

    # 6. Generar datos ficticios
    print("📋 Generando datos de ejemplo para e-commerce...\n")
    generar_clientes(conexion)
    generar_inventario(conexion)
    generar_pedidos(conexion)
    generar_carritos(conexion)

    # 7. Estadísticas
    cursor = conexion.cursor()

    tablas_info = [
        ("categorias", "Categorías"),
        ("fabricantes", "Fabricantes"),
        ("productos", "Productos"),
        ("colores", "Colores"),
        ("clientes", "Clientes"),
        ("pedidos", "Pedidos"),
        ("lineas_pedido", "Líneas de pedido"),
        ("carritos", "Carritos"),
        ("items_carrito", "Items en carritos"),
        ("inventario", "Registros de inventario"),
    ]

    print("\n" + "=" * 70)
    print("📊 ESTADÍSTICAS DEL MODELO E-COMMERCE")
    print("=" * 70)

    for tabla, nombre_display in tablas_info:
        cursor.execute(f"SELECT COUNT(*) FROM {tabla}")
        count = cursor.fetchone()[0]
        print(f"✅ {nombre_display}: {count:,}")

    # Estadísticas adicionales
    cursor.execute("SELECT SUM(total) FROM pedidos")
    total_ventas = cursor.fetchone()[0] or 0

    cursor.execute("SELECT COUNT(*) FROM inventario WHERE cantidad_stock < stock_minimo")
    productos_bajo_stock = cursor.fetchone()[0]

    print(f"\n💰 Total ventas: ${total_ventas:,.2f}")
    print(f"⚠️  Productos bajo stock mínimo: {productos_bajo_stock}")

    conexion.close()

    print(f"\n💾 Base de datos: {RUTA_DB}")
    print(f"   Tamaño: {RUTA_DB.stat().st_size / 1024 / 1024:.2f} MB")

    print("\n" + "=" * 70)
    print("✅ MODELO E-COMMERCE COMPLETO CREADO")
    print("=" * 70)

    print("\n💡 Próximos pasos:")
    print("   1. Abre la BD con DB Browser for SQLite")
    print("   2. Explora las relaciones complejas")
    print("   3. Analiza los pedidos y clientes")
    print("   4. Revisa el inventario")
    print("   5. Compara los 3 modelos (A, B, C)")


# ═══════════════════════════════════════════════════════════════════
# PUNTO DE ENTRADA
# ═══════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("\n" + "=" * 70)
    print(" MODELO C: E-COMMERCE COMPLETO")
    print("=" * 70 + "\n")

    main()
