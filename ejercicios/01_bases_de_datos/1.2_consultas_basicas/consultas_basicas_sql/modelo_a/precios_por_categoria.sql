SELECT id, name
FROM category
WHERE name = 'Memory';
-- Consulta 2.8: RAM de gama media
SELECT
    name,
    price,
    category_id
FROM product
WHERE category_id = 5          -- id de la categoría "Memory"
  AND price BETWEEN 40 AND 120
ORDER BY price ASC
LIMIT 20;
