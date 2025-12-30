-- Consulta 2.1: Productos por fabricante (id = 1)
SELECT
    name,
    price,
    category_id
FROM product
WHERE manufacturer_id = 1
ORDER BY price DESC
LIMIT 15;
