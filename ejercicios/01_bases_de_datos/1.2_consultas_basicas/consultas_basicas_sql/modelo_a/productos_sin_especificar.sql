-- Consulta 1.8: CPUs sin GPU integrada
SELECT
    name,
    price,
    core_count
FROM cpu
WHERE graphics IS NULL
ORDER BY price DESC;
