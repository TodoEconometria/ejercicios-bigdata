-- =====================================================
-- EJERCICIO 1.4 - PARTE 2: Normalización tabla VENTAS
-- =====================================================

/*
DIAGNÓSTICO: Cumple 1NF/2NF, VIOLA 3NF (transitivas)
DEPENDENCIAS:
- vendedor_email → vendedor_nombre, vendedor_comision
- cliente_nombre → cliente_direccion
- producto_nombre → producto_categoria, producto_fabricante
ANOMALÍA: Actualizar email vendedor = 1000 filas
*/

-- ===== 4 TABLAS NORMALIZADAS 3NF =====
CREATE TABLE vendedores (
    vendedor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    vendedor_nombre TEXT NOT NULL,
    vendedor_email TEXT UNIQUE NOT NULL,
    vendedor_comision REAL NOT NULL
);

CREATE TABLE clientes (
    cliente_id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_nombre TEXT NOT NULL,
    cliente_direccion TEXT NOT NULL
);

CREATE TABLE productos (
    producto_id INTEGER PRIMARY KEY AUTOINCREMENT,
    producto_nombre TEXT NOT NULL,
    producto_categoria TEXT NOT NULL,
    producto_fabricante TEXT NOT NULL
);

CREATE TABLE ventas (
    venta_id INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha DATE NOT NULL,
    vendedor_id INTEGER REFERENCES vendedores(vendedor_id),
    cliente_id INTEGER REFERENCES clientes(cliente_id),
    producto_id INTEGER REFERENCES productos(producto_id),
    cantidad INTEGER NOT NULL,
    precio_unitario REAL NOT NULL,
    descuento REAL DEFAULT 0
);

-- ===== SCRIPT MIGRACIÓN (ventas_antigua → nuevo) =====
INSERT INTO vendedores (vendedor_nombre, vendedor_email, vendedor_comision)
SELECT DISTINCT vendedor_nombre, vendedor_email, vendedor_comision
FROM ventas_antigua;

INSERT INTO clientes (cliente_nombre, cliente_direccion)
SELECT DISTINCT cliente_nombre, cliente_direccion FROM ventas_antigua;

INSERT INTO productos (producto_nombre, producto_categoria, producto_fabricante)
SELECT DISTINCT producto_nombre, producto_categoria, producto_fabricante
FROM ventas_antigua;

INSERT INTO ventas (venta_id, fecha, vendedor_id, cliente_id, producto_id,
                   cantidad, precio_unitario, descuento)
SELECT v.venta_id, v.fecha, ven.vendedor_id, cli.cliente_id, prod.producto_id,
       v.cantidad, v.precio_unitario, v.descuento
FROM ventas_antigua v
JOIN vendedores ven ON v.vendedor_email = ven.vendedor_email
JOIN clientes cli ON v.cliente_nombre = cli.cliente_nombre
JOIN productos prod ON v.producto_nombre = prod.producto_nombre;

-- ===== RESULTADO PARTE 2: 4 tablas 3NF ✅ =====
-- 0 redundancia, 0 anomalías de actualización
