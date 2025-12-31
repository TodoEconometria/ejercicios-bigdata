SELECT
    name       AS nombre,
    price      AS precio,
    core_count,
    core_clock
FROM cpu
WHERE name LIKE '%AMD%'
  AND price < 200
ORDER BY price ASC;
