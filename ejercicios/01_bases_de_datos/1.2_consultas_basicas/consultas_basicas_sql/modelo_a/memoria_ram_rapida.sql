SELECT
    name,
    speed,
    price,
    price_per_gb
FROM memory
WHERE speed >= 6000
  AND price BETWEEN 80 AND 150
ORDER BY price_per_gb ASC;
