-- Consulta 1.5: Tarjetas gráficas NVIDIA
SELECT
    name,
    memory,
    price
FROM "video-card"
WHERE (name LIKE '%NVIDIA%' OR name LIKE '%GeForce%')
  AND memory >= 8
ORDER BY memory DESC,
         price ASC;
