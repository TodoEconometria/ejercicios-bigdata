-- Consulta 1.6: Monitores grandes
SELECT
    name,
    screen_size,
    refresh_rate,
    price
FROM monitor
WHERE screen_size >= 27
  AND refresh_rate >= 144
  AND price IS NOT NULL
ORDER BY screen_size DESC;
