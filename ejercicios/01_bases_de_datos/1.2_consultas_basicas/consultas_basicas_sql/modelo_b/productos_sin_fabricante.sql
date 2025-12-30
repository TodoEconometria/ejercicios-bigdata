-- Consulta 2.7: Número de productos sin fabricante
SELECT
    COUNT(*) AS productos_sin_fabricante
FROM product
WHERE manufacturer_id IS NULL;
