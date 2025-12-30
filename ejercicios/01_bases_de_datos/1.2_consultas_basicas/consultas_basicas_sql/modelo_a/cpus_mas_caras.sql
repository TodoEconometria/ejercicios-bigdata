SELECT
    name       AS nombre,
    price      AS precio,
    core_count,
    core_clock
FROM cpu
ORDER BY price DESC
LIMIT 10;
