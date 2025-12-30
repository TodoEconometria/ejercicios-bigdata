-- Consulta 2.5: Top 10 productos más caros
SELECT
    id,
    name,
    price
FROM product
WHERE price > 500
ORDER BY price DESC
LIMIT 10;
