-- Consulta 1.7: Rangos de precio (teclados)
SELECT
    name,
    price,
    style,
    switches
FROM keyboard
WHERE price BETWEEN 50 AND 150
ORDER BY price ASC;
