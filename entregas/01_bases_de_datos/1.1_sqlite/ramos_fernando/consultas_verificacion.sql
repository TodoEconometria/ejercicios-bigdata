-- ═══════════════════════════════════════════════════════════════════
-- CONSULTAS DE VERIFICACIÓN - Ejercicio 1.1
-- ═══════════════════════════════════════════════════════════════════
--
-- Este archivo contiene consultas SQL de ejemplo para los 3 modelos.
-- Úsalo para verificar que tus bases de datos fueron creadas correctamente.
--
-- Instrucciones:
-- 1. Abre cada base de datos (.db) con DB Browser for SQLite
-- 2. Copia y pega estas consultas en la pestaña "Ejecutar SQL"
-- 3. Verifica que los resultados tienen sentido
--
-- Autor: Profesor
-- Fecha: 2025-12-11
-- ═══════════════════════════════════════════════════════════════════


-- ═══════════════════════════════════════════════════════════════════
-- MODELO A: CATÁLOGO SIMPLE (tienda_modelo_a.db)
-- ═══════════════════════════════════════════════════════════════════

-- Consulta 1: ¿Cuántas CPUs hay en el catálogo?
SELECT COUNT(*) AS total_cpus
FROM cpu;

-- Consulta 2: ¿Cuál es el precio promedio de las placas base?
SELECT
    AVG(price) AS precio_promedio,
    MIN(price) AS precio_minimo,
    MAX(price) AS precio_maximo
FROM motherboard;

-- Consulta 3: Top 5 tarjetas gráficas más caras
SELECT
    name,
    price,
    memory,
    chipset
FROM video_card
ORDER BY price DESC
LIMIT 5;

-- Consulta 4: Memoria RAM ordenada por precio/GB (mejor relación calidad-precio)
SELECT
    name,
    price,
    speed,
    price_per_gb
FROM memory
WHERE price_per_gb IS NOT NULL
ORDER BY price_per_gb ASC
LIMIT 10;

-- Consulta 5: CPUs de AMD con más de 6 cores
SELECT
    name,
    core_count,
    price,
    tdp
FROM cpu
WHERE name LIKE 'AMD%'
  AND core_count > 6
ORDER BY core_count DESC;

-- Consulta 6: Monitores por rango de precio
SELECT
    CASE
        WHEN price < 200 THEN 'Económico'
        WHEN price BETWEEN 200 AND 500 THEN 'Gama Media'
        ELSE 'Premium'
    END AS rango_precio,
    COUNT(*) AS cantidad,
    AVG(price) AS precio_promedio
FROM monitor
GROUP BY rango_precio;

-- Consulta 7: ¿Cuántos productos hay en cada tabla?
SELECT
    'cpu' AS tabla, COUNT(*) AS productos FROM cpu
UNION ALL
SELECT 'motherboard', COUNT(*) FROM motherboard
UNION ALL
SELECT 'memory', COUNT(*) FROM memory
UNION ALL
SELECT 'video_card', COUNT(*) FROM video_card
UNION ALL
SELECT 'monitor', COUNT(*) FROM monitor
ORDER BY productos DESC;


-- ═══════════════════════════════════════════════════════════════════
-- MODELO B: NORMALIZADO (tienda_modelo_b.db)
-- ═══════════════════════════════════════════════════════════════════

-- Consulta 1: ¿Cuántos productos hay por categoría?
SELECT
    c.nombre AS categoria,
    COUNT(p.id) AS num_productos,
    AVG(p.precio) AS precio_promedio
FROM categorias c
LEFT JOIN productos p ON c.id = p.categoria_id
GROUP BY c.nombre
ORDER BY num_productos DESC;

-- Consulta 2: ¿Qué fabricantes tienen más productos?
SELECT
    f.nombre AS fabricante,
    COUNT(p.id) AS num_productos,
    AVG(p.precio) AS precio_promedio,
    MIN(p.precio) AS precio_min,
    MAX(p.precio) AS precio_max
FROM fabricantes f
LEFT JOIN productos p ON f.id = p.fabricante_id
GROUP BY f.nombre
HAVING num_productos > 0
ORDER BY num_productos DESC
LIMIT 10;

-- Consulta 3: Productos con color "Black" del fabricante "Corsair"
SELECT
    p.nombre,
    p.precio,
    f.nombre AS fabricante,
    c.nombre AS categoria,
    col.nombre AS color
FROM productos p
JOIN fabricantes f ON p.fabricante_id = f.id
JOIN categorias c ON p.categoria_id = c.id
JOIN productos_colores pc ON p.id = pc.producto_id
JOIN colores col ON pc.color_id = col.id
WHERE f.nombre = 'Corsair'
  AND col.nombre = 'Black'
ORDER BY p.precio DESC;

-- Consulta 4: ¿Cuántos productos tiene cada color?
SELECT
    col.nombre AS color,
    COUNT(pc.producto_id) AS num_productos
FROM colores col
LEFT JOIN productos_colores pc ON col.id = pc.color_id
GROUP BY col.nombre
ORDER BY num_productos DESC;

-- Consulta 5: Productos más caros por categoría
SELECT
    c.nombre AS categoria,
    p.nombre AS producto,
    f.nombre AS fabricante,
    p.precio
FROM productos p
JOIN categorias c ON p.categoria_id = c.id
LEFT JOIN fabricantes f ON p.fabricante_id = f.id
WHERE p.precio = (
    SELECT MAX(p2.precio)
    FROM productos p2
    WHERE p2.categoria_id = p.categoria_id
)
ORDER BY p.precio DESC;

-- Consulta 6: Productos que tienen múltiples colores
SELECT
    p.nombre,
    p.precio,
    COUNT(pc.color_id) AS num_colores,
    GROUP_CONCAT(col.nombre, ', ') AS colores
FROM productos p
JOIN productos_colores pc ON p.id = pc.producto_id
JOIN colores col ON pc.color_id = col.id
GROUP BY p.id, p.nombre, p.precio
HAVING num_colores > 1
ORDER BY num_colores DESC
LIMIT 10;

-- Consulta 7: Fabricantes con productos en múltiples categorías
SELECT
    f.nombre AS fabricante,
    COUNT(DISTINCT p.categoria_id) AS num_categorias,
    GROUP_CONCAT(DISTINCT c.nombre, ', ') AS categorias
FROM fabricantes f
JOIN productos p ON f.id = p.fabricante_id
JOIN categorias c ON p.categoria_id = c.id
GROUP BY f.nombre
HAVING num_categorias > 1
ORDER BY num_categorias DESC;


-- ═══════════════════════════════════════════════════════════════════
-- MODELO C: E-COMMERCE COMPLETO (tienda_modelo_c.db)
-- ═══════════════════════════════════════════════════════════════════

-- Consulta 1: ¿Cuántos pedidos tiene cada cliente?
SELECT
    c.nombre || ' ' || c.apellido AS cliente,
    c.email,
    COUNT(p.id) AS num_pedidos,
    SUM(p.total) AS total_gastado,
    AVG(p.total) AS gasto_promedio
FROM clientes c
LEFT JOIN pedidos p ON c.id = p.cliente_id
GROUP BY c.id, c.nombre, c.apellido, c.email
ORDER BY total_gastado DESC;

-- Consulta 2: Pedidos por estado
SELECT
    estado,
    COUNT(*) AS num_pedidos,
    SUM(total) AS valor_total,
    AVG(total) AS valor_promedio
FROM pedidos
GROUP BY estado
ORDER BY num_pedidos DESC;

-- Consulta 3: Top 10 productos más vendidos
SELECT
    p.nombre AS producto,
    cat.nombre AS categoria,
    SUM(lp.cantidad) AS unidades_vendidas,
    SUM(lp.subtotal) AS ventas_totales,
    AVG(lp.precio_unitario) AS precio_promedio
FROM productos p
JOIN lineas_pedido lp ON p.id = lp.producto_id
JOIN categorias cat ON p.categoria_id = cat.id
GROUP BY p.id, p.nombre, cat.nombre
ORDER BY unidades_vendidas DESC
LIMIT 10;

-- Consulta 4: Total de ventas por categoría
SELECT
    c.nombre AS categoria,
    COUNT(DISTINCT lp.pedido_id) AS num_pedidos,
    SUM(lp.cantidad) AS unidades_vendidas,
    SUM(lp.subtotal) AS ventas_totales
FROM categorias c
JOIN productos p ON c.id = p.categoria_id
JOIN lineas_pedido lp ON p.id = lp.producto_id
GROUP BY c.nombre
ORDER BY ventas_totales DESC;

-- Consulta 5: Productos con stock bajo (menor al mínimo)
SELECT
    p.nombre,
    cat.nombre AS categoria,
    i.cantidad_stock AS stock_actual,
    i.stock_minimo,
    i.ubicacion,
    (i.stock_minimo - i.cantidad_stock) AS unidades_faltantes
FROM inventario i
JOIN productos p ON i.producto_id = p.id
JOIN categorias cat ON p.categoria_id = cat.id
WHERE i.cantidad_stock < i.stock_minimo
ORDER BY unidades_faltantes DESC;

-- Consulta 6: Análisis de carritos activos
SELECT
    c.nombre || ' ' || c.apellido AS cliente,
    COUNT(ic.id) AS items_en_carrito,
    SUM(ic.cantidad) AS total_productos,
    SUM(p.precio * ic.cantidad) AS valor_estimado
FROM clientes c
JOIN carritos car ON c.id = car.cliente_id
JOIN items_carrito ic ON car.id = ic.carrito_id
JOIN productos p ON ic.producto_id = p.id
WHERE car.activo = 1
GROUP BY c.id, c.nombre, c.apellido
ORDER BY valor_estimado DESC;

-- Consulta 7: Pedidos del último mes con detalle
SELECT
    p.id AS pedido_id,
    c.nombre || ' ' || c.apellido AS cliente,
    p.fecha,
    p.estado,
    p.total,
    COUNT(lp.id) AS num_items,
    p.metodo_pago
FROM pedidos p
JOIN clientes c ON p.cliente_id = c.id
JOIN lineas_pedido lp ON p.id = lp.pedido_id
WHERE p.fecha >= DATE('now', '-30 days')
GROUP BY p.id, c.nombre, c.apellido, p.fecha, p.estado, p.total, p.metodo_pago
ORDER BY p.fecha DESC;

-- Consulta 8: Clientes sin pedidos (potencial abandono)
SELECT
    c.nombre || ' ' || c.apellido AS cliente,
    c.email,
    c.fecha_registro,
    JULIANDAY('now') - JULIANDAY(c.fecha_registro) AS dias_registrado
FROM clientes c
LEFT JOIN pedidos p ON c.id = p.cliente_id
WHERE p.id IS NULL
ORDER BY c.fecha_registro;

-- Consulta 9: Producto más popular en carritos actuales
SELECT
    p.nombre,
    cat.nombre AS categoria,
    COUNT(DISTINCT ic.carrito_id) AS num_carritos,
    SUM(ic.cantidad) AS total_unidades,
    p.precio
FROM productos p
JOIN items_carrito ic ON p.id = ic.producto_id
JOIN carritos car ON ic.carrito_id = car.id
JOIN categorias cat ON p.categoria_id = cat.id
WHERE car.activo = 1
GROUP BY p.id, p.nombre, cat.nombre, p.precio
ORDER BY num_carritos DESC, total_unidades DESC
LIMIT 10;

-- Consulta 10: Rendimiento de ventas por mes
SELECT
    STRFTIME('%Y-%m', fecha) AS mes,
    COUNT(*) AS num_pedidos,
    SUM(total) AS ventas_totales,
    AVG(total) AS ticket_promedio
FROM pedidos
WHERE estado != 'cancelado'
GROUP BY mes
ORDER BY mes DESC;


-- ═══════════════════════════════════════════════════════════════════
-- CONSULTAS COMPARATIVAS (Ejecutar en cada modelo)
-- ═══════════════════════════════════════════════════════════════════

-- Estas consultas muestran las diferencias de complejidad entre modelos

-- EJERCICIO: Buscar todos los productos AMD en cada modelo

-- Modelo A:
-- SELECT * FROM cpu WHERE name LIKE 'AMD%';
-- SELECT * FROM video_card WHERE name LIKE 'AMD%';
-- ... (repetir para cada tabla)

-- Modelo B:
-- SELECT p.*, c.nombre AS categoria
-- FROM productos p
-- JOIN fabricantes f ON p.fabricante_id = f.id
-- JOIN categorias c ON p.categoria_id = c.id
-- WHERE f.nombre = 'AMD';

-- Modelo C: (igual que Modelo B, pero con más tablas disponibles)


-- ═══════════════════════════════════════════════════════════════════
-- NOTAS PEDAGÓGICAS
-- ═══════════════════════════════════════════════════════════════════
--
-- 1. MODELO A (Desnormalizado):
--    - Consultas simples, directas
--    - No requieren JOINs
--    - Pero... para buscar algo en todas las categorías = múltiples queries
--
-- 2. MODELO B (Normalizado):
--    - Consultas más complejas (requieren JOINs)
--    - Pero... una sola query busca en todas las categorías
--    - Facilita análisis agregados (productos por fabricante, etc.)
--
-- 3. MODELO C (E-Commerce):
--    - Consultas muy complejas (múltiples JOINs)
--    - Pero... permite análisis de negocio avanzado
--    - Refleja queries reales de producción
--
-- REFLEXIÓN: ¿Cuál modelo prefieres? Depende del caso de uso.
--
-- ═══════════════════════════════════════════════════════════════════
