📝 Ejercicio 1.3: Consultas SQL Avanzadas

Solución Completa

📚 PARTE 1: INNER JOIN (tienda_modelo_b.db)
═══════════════════════════════════════════════════════════════
Ejercicio 1.1: Productos con su categoría
═══════════════════════════════════════════════════════════════
Objetivo: JOIN básico entre productos y categorías
Descripción: Muestra el nombre del producto, la categoría y el precio
Resultado esperado: Listado ordenado por categoría y precio ascendente
Nota: Muchos productos no tienen precio asignado (NULL)
═══════════════════════════════════════════════════════════════
SELECT
p.name AS product_name, -- Nombre del producto
c.name AS category_name, -- Nombre de la categoría del producto
p.price AS price -- Precio del producto (puede ser NULL)
FROM product AS p -- Tabla principal de productos
INNER JOIN category AS c -- Relaciona cada producto con su categoría
ON p.category_id = c.id
ORDER BY
c.name ASC, -- Ordena primero por categoría (A-Z)
p.price ASC; -- Dentro de cada categoría, del más barato al más caro

═══════════════════════════════════════════════════════════════
Ejercicio 1.2: Productos con fabricante y categoría
═══════════════════════════════════════════════════════════════
Objetivo: JOIN triple entre productos, fabricantes y categorías
Descripción: Solo productos con precio superior a $200
Resultado esperado: Listado con fabricante, categoría, producto y precio
═══════════════════════════════════════════════════════════════
SELECT
m.name AS manufacturer_name, -- Nombre del fabricante
c.name AS category_name, -- Nombre de la categoría del producto
p.name AS product_name, -- Nombre del producto
p.price -- Precio del producto
FROM product AS p -- Tabla principal de productos
INNER JOIN manufacturer AS m -- Relaciona cada producto con su fabricante
ON p.manufacturer_id = m.id
INNER JOIN category AS c -- Relaciona cada producto con su categoría
ON p.category_id = c.id
WHERE p.price > 200 -- Solo productos de precio superior a 200
ORDER BY
m.name ASC, -- Ordena primero por fabricante (A-Z)
c.name ASC, -- Luego por categoría (A-Z)
p.price DESC; -- Dentro de cada grupo, del más caro al más barato

═══════════════════════════════════════════════════════════════
Ejercicio 1.3: Productos con colores
═══════════════════════════════════════════════════════════════
Objetivo: Agregar productos con sus colores usando GROUP_CONCAT
Descripción: Muestra cada producto junto con la lista de colores asociados
Resultado esperado: Lista de productos con colores concatenados
Nota: En este modelo cada producto tiene como máximo un color (color_id)
═══════════════════════════════════════════════════════════════
SELECT
p.name AS product_name, -- Nombre del producto
GROUP_CONCAT(col.name, ', ') AS colors -- Colores asociados al producto (lista separada por comas)
FROM product AS p -- Tabla principal de productos
LEFT JOIN color AS col -- Relaciona cada producto con su color
ON p.color_id = col.id
GROUP BY
p.id, -- Agrupa por el identificador del producto
p.name -- y por su nombre para obtener una fila por producto
ORDER BY
p.name ASC; -- Ordena los productos alfabéticamente

═══════════════════════════════════════════════════════════════
Ejercicio 1.4: Top productos por fabricante
═══════════════════════════════════════════════════════════════
Objetivo: Usar window function para obtener el producto más caro por fabricante
Descripción: Muestra, para cada fabricante, el producto más caro (price máximo)
Resultado esperado: Un producto por fabricante (el de mayor precio)
Técnica: Window function ROW_NUMBER() con PARTITION BY
═══════════════════════════════════════════════════════════════
WITH products_ranked AS (
SELECT
m.name AS manufacturer_name, -- Nombre del fabricante
p.name AS product_name, -- Nombre del producto
p.price, -- Precio del producto
ROW_NUMBER() OVER (
PARTITION BY m.id -- Re-inicia la numeración por cada fabricante
ORDER BY p.price DESC -- Ordena de más caro a más barato dentro de cada fabricante
) AS rn
FROM product AS p -- Tabla principal de productos
INNER JOIN manufacturer AS m -- Relaciona cada producto con su fabricante
ON p.manufacturer_id = m.id
WHERE p.price IS NOT NULL -- Ignora productos sin precio
)
SELECT
manufacturer_name, -- Nombre del fabricante
product_name, -- Nombre del producto más caro
price -- Precio del producto más caro
FROM products_ranked
WHERE rn = 1 -- Se queda solo con el producto nº1 (más caro) por fabricante
ORDER BY
manufacturer_name ASC; -- Ordena fabricantes alfabéticamente

═══════════════════════════════════════════════════════════════
Ejercicio 1.5: Productos sin color asignado
═══════════════════════════════════════════════════════════════
Objetivo: Contar productos sin color usando filtro NULL
Descripción: Cuenta cuántos productos NO tienen color asociado
Resultado esperado: Número total de productos sin color_id
═══════════════════════════════════════════════════════════════
SELECT
COUNT(*) AS products_without_color -- Número total de productos sin color
FROM product AS p -- Tabla principal de productos
WHERE p.color_id IS NULL; -- Filtra solo productos sin color asignado

📊 PARTE 2: AGREGACIONES (tienda_modelo_b.db)
═══════════════════════════════════════════════════════════════
Ejercicio 2.1: Contar productos por categoría
═══════════════════════════════════════════════════════════════
Objetivo: Usar COUNT y GROUP BY con LEFT JOIN
Descripción: Cuenta cuántos productos hay en cada categoría
Resultado esperado: Todas las categorías (incluso sin productos)
Técnica: LEFT JOIN para incluir categorías vacías
═══════════════════════════════════════════════════════════════
SELECT
c.name AS category_name, -- Nombre de la categoría
COUNT(p.id) AS product_count -- Número de productos en esa categoría
FROM category AS c -- Lista de todas las categorías
LEFT JOIN product AS p -- Relación opcional con productos
ON p.category_id = c.id
GROUP BY
c.id, -- Agrupa por id de categoría
c.name -- y por su nombre
ORDER BY
product_count DESC, -- Categorías con más productos primero
category_name ASC; -- Desempata alfabéticamente por nombre

═══════════════════════════════════════════════════════════════
Ejercicio 2.2: Estadísticas de precios por fabricante
═══════════════════════════════════════════════════════════════
Objetivo: Calcular funciones de agregación (COUNT, AVG, MIN, MAX)
Descripción: Estadísticas de precios agrupadas por fabricante
Resultado esperado: Fabricantes con más de 10 productos
Técnica: HAVING para filtrar después de agrupar
═══════════════════════════════════════════════════════════════
SELECT
m.name AS manufacturer_name, -- Nombre del fabricante
COUNT(p.id) AS product_count, -- Número de productos con precio
ROUND(AVG(p.price), 2) AS avg_price, -- Precio medio (redondeado a 2 decimales)
MIN(p.price) AS min_price, -- Precio mínimo
MAX(p.price) AS max_price -- Precio máximo
FROM manufacturer AS m -- Tabla de fabricantes
INNER JOIN product AS p -- Productos asociados a cada fabricante
ON p.manufacturer_id = m.id
WHERE p.price IS NOT NULL -- Ignora productos sin precio
GROUP BY
m.id,
m.name
HAVING
COUNT(p.id) > 10 -- Solo fabricantes con más de 10 productos
ORDER BY
product_count DESC, -- Los fabricantes más "grandes" primero
manufacturer_name ASC; -- Desempata por nombre de fabricante

═══════════════════════════════════════════════════════════════
Ejercicio 2.3: Productos por rango de precio
═══════════════════════════════════════════════════════════════
Objetivo: Usar CASE para crear categorías dinámicas
Descripción: Clasifica productos en rangos Económico, Medio y Premium
Resultado esperado: Cuenta y precio medio por rango
Técnica: CASE dentro de SELECT y GROUP BY
═══════════════════════════════════════════════════════════════
SELECT
CASE
WHEN p.price < 100 THEN 'Economico' -- Productos baratos
WHEN p.price < 300 THEN 'Medio' -- Rango intermedio
ELSE 'Premium' -- Productos de gama alta
END AS price_range, -- Nombre del rango de precio
COUNT(*) AS product_count, -- Número de productos en el rango
ROUND(AVG(p.price), 2) AS avg_price -- Precio medio dentro del rango
FROM product AS p -- Tabla principal de productos
WHERE p.price IS NOT NULL -- Solo productos con precio conocido
GROUP BY
price_range -- Agrupa por el rango calculado con CASE
ORDER BY
CASE price_range -- Orden lógico de los rangos
WHEN 'Economico' THEN 1
WHEN 'Medio' THEN 2
WHEN 'Premium' THEN 3
END;

═══════════════════════════════════════════════════════════════
Ejercicio 2.4: Colores más populares
═══════════════════════════════════════════════════════════════
Objetivo: Contar productos por color y ordenar por popularidad
Descripción: Muestra los 10 colores con más productos asociados
Resultado esperado: Top 10 colores ordenados descendentemente
Técnica: LEFT JOIN para incluir colores sin productos
═══════════════════════════════════════════════════════════════
SELECT
col.name AS color_name, -- Nombre del color
COUNT(p.id) AS product_count -- Número de productos con ese color
FROM color AS col -- Tabla de colores
LEFT JOIN product AS p -- Relación opcional con productos
ON p.color_id = col.id
GROUP BY
col.id,
col.name
ORDER BY
product_count DESC, -- Colores con más productos primero
color_name ASC -- Desempata por nombre
LIMIT 10; -- Solo el top 10 de colores

═══════════════════════════════════════════════════════════════
Ejercicio 2.5: Fabricantes con productos en múltiples categorías
═══════════════════════════════════════════════════════════════
Objetivo: Contar categorías distintas por fabricante
Descripción: Identifica fabricantes diversificados (2+ categorías)
Resultado esperado: Fabricantes con productos en varias categorías
Técnica: COUNT(DISTINCT) con HAVING
═══════════════════════════════════════════════════════════════
SELECT
m.name AS manufacturer_name, -- Nombre del fabricante
COUNT(DISTINCT p.category_id) AS category_count -- Número de categorías distintas
FROM manufacturer AS m -- Tabla de fabricantes
INNER JOIN product AS p -- Productos asociados a cada fabricante
ON p.manufacturer_id = m.id
WHERE p.category_id IS NOT NULL -- Ignora productos sin categoría asignada
GROUP BY
m.id,
m.name
HAVING
COUNT(DISTINCT p.category_id) >= 2 -- Solo fabricantes con 2+ categorías
ORDER BY
category_count DESC, -- Más categorías primero
manufacturer_name ASC; -- Desempata por nombre

🛒 PARTE 3: E-COMMERCE ANALYTICS (tienda_modelo_c.db)
═══════════════════════════════════════════════════════════════
Ejercicio 3.1: Ventas por cliente
═══════════════════════════════════════════════════════════════
Objetivo: Analizar comportamiento de compra por cliente
Descripción: Calcula total gastado, número de pedidos y ticket promedio
Resultado esperado: Clientes ordenados por gasto total descendente
Técnica: JOIN múltiple con agregaciones
═══════════════════════════════════════════════════════════════
SELECT
c.id AS customer_id, -- Identificador del cliente
c.first_name || ' ' || c.last_name AS customer_name, -- Nombre completo del cliente
COUNT(DISTINCT o.id) AS order_count, -- Número de pedidos realizados
ROUND(SUM(o.total), 2) AS total_spent, -- Total gastado (suma de total de pedidos)
ROUND(AVG(o.total), 2) AS avg_ticket -- Importe medio por pedido (ticket promedio)
FROM customer AS c -- Tabla de clientes
LEFT JOIN "order" AS o -- Relaciona cada cliente con sus pedidos
ON o.customer_id = c.id
GROUP BY
c.id,
c.first_name,
c.last_name
HAVING
COUNT(DISTINCT o.id) > 0 -- Solo clientes que han hecho al menos un pedido
ORDER BY
total_spent DESC, -- Clientes que más han gastado primero
customer_name ASC; -- Desempata por nombre

═══════════════════════════════════════════════════════════════
Ejercicio 3.2: Productos más vendidos
═══════════════════════════════════════════════════════════════
Objetivo: Identificar productos estrella por volumen de ventas
Descripción: Calcula unidades vendidas e ingresos por producto
Resultado esperado: Top 20 productos más vendidos
Técnica: JOIN con order_item y agregación de ventas
═══════════════════════════════════════════════════════════════
SELECT
p.id AS product_id, -- Identificador del producto
p.name AS product_name, -- Nombre del producto
m.name AS manufacturer_name, -- Nombre del fabricante
c.name AS category_name, -- Nombre de la categoría
SUM(oi.quantity) AS total_quantity_sold, -- Unidades totales vendidas
ROUND(SUM(oi.quantity * oi.unit_price), 2) AS total_revenue -- Ingresos totales por producto
FROM order_item AS oi -- Líneas de pedido (detalle de ventas)
INNER JOIN product AS p -- Relaciona cada línea con su producto
ON oi.product_id = p.id
LEFT JOIN manufacturer AS m -- Fabricante del producto (opcional si falta)
ON p.manufacturer_id = m.id
LEFT JOIN category AS c -- Categoría del producto (opcional si falta)
ON p.category_id = c.id
GROUP BY
p.id,
p.name,
m.name,
c.name
HAVING
SUM(oi.quantity) > 0 -- Solo productos que se han vendido al menos una unidad
ORDER BY
total_quantity_sold DESC, -- Ordena por unidades vendidas (más vendidos primero)
total_revenue DESC -- Desempata por ingresos totales
LIMIT 20; -- Top 20 productos

═══════════════════════════════════════════════════════════════
Ejercicio 3.3: Análisis de inventario
═══════════════════════════════════════════════════════════════
Objetivo: Detectar productos con stock crítico
Descripción: Identifica productos por debajo del stock mínimo
Resultado esperado: Productos con stock_actual < stock_minimo
Técnica: JOIN con cálculo de valor de reposición necesaria
═══════════════════════════════════════════════════════════════
SELECT
    p.id AS product_id,                        -- Identificador del producto
    p.name AS product_name,                    -- Nombre del producto
    c.name AS category_name,                   -- Categoría del producto
    m.name AS manufacturer_name,               -- Fabricante del producto
    i.stock AS current_stock,                  -- Stock actual en inventario
    i.min_stock AS minimum_stock,              -- Stock mínimo requerido
    (i.min_stock - i.stock) AS units_needed,   -- Unidades faltantes
    ROUND(p.price * (i.min_stock - i.stock), 2) AS restock_value  -- Valor de reposición necesario
FROM inventory AS i                            -- Tabla de inventario
INNER JOIN product AS p                        -- Relaciona inventario con productos
    ON i.product_id = p.id
LEFT JOIN category AS c                        -- Categoría del producto
    ON p.category_id = c.id
LEFT JOIN manufacturer AS m                    -- Fabricante del producto
    ON p.manufacturer_id = m.id
WHERE i.stock < i.min_stock                    -- Filtro: productos con stock crítico
    AND p.price IS NOT NULL                    -- Solo productos con precio conocido
ORDER BY
    (i.min_stock - i.stock) DESC,              -- Productos con mayor déficit primero
    restock_value DESC;

═══════════════════════════════════════════════════════════════
Ejercicio 3.4: Pedidos del último mes
═══════════════════════════════════════════════════════════════
Objetivo: Analizar evolución de ventas diarias del último mes
Descripción: Agrupa pedidos por día mostrando métricas clave
Resultado esperado: Estadísticas diarias de los últimos 30 días
Técnica: Filtro de fecha con DATE() y agregación temporal
═══════════════════════════════════════════════════════════════
SELECT
DATE(o.order_date) AS order_day, -- Fecha del pedido (solo día, sin hora)
COUNT(DISTINCT o.id) AS num_orders, -- Número de pedidos realizados ese día
ROUND(SUM(o.total), 2) AS total_sales, -- Ventas totales del día
ROUND(AVG(o.total), 2) AS avg_ticket, -- Ticket promedio del día
COUNT(DISTINCT o.customer_id) AS unique_customers -- Clientes únicos que compraron
FROM "order" AS o -- Tabla de pedidos
WHERE o.order_date >= DATE('now', '-30 day') -- Filtro: solo últimos 30 días
GROUP BY
DATE(o.order_date) -- Agrupa por día
ORDER BY
order_day DESC; -- Ordena de más reciente a más antiguo

═══════════════════════════════════════════════════════════════
Ejercicio 3.5: Análisis de carritos abandonados
═══════════════════════════════════════════════════════════════
Objetivo: Identificar clientes con carritos activos sin compras recientes
Descripción: Calcula valor estimado de carritos abandonados
Resultado esperado: Clientes con carrito activo pero sin pedidos en 30 días
Técnica: NOT EXISTS para detectar ausencia de pedidos recientes
═══════════════════════════════════════════════════════════════
SELECT
c.id AS customer_id, -- Identificador del cliente
c.first_name || ' ' || c.last_name AS customer_name, -- Nombre completo del cliente
ROUND(SUM(ci.quantity * p.price), 2) AS cart_value -- Valor estimado del carrito
FROM cart AS ca -- Tabla de carritos
INNER JOIN customer AS c -- Relaciona carrito con cliente
ON ca.customer_id = c.id
INNER JOIN cart_item AS ci -- Líneas del carrito
ON ci.cart_id = ca.id
INNER JOIN product AS p -- Productos en el carrito
ON ci.product_id = p.id
WHERE
ca.active = 1 -- Carrito activo
AND NOT EXISTS ( -- No tiene pedidos recientes
SELECT 1
FROM "order" AS o
WHERE o.customer_id = c.id
AND o.order_date >= DATE('now', '-30 day')
)
AND p.price IS NOT NULL -- Solo productos con precio conocido
GROUP BY
c.id,
c.first_name,
c.last_name
ORDER BY
cart_value DESC; -- Carritos de mayor valor primero