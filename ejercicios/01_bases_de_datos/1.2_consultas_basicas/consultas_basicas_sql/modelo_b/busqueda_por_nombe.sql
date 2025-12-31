-- Consulta 2.6: Productos con RGB
SELECT
    name,
    price
FROM product
WHERE name LIKE '%RGB%'
ORDER BY price ASC;
