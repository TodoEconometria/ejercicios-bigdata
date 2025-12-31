-- Paso 1: obtener id de la categoría "CPU"
SELECT id
FROM category
WHERE name = 'CPU';
-- Paso 2: productos de la categoría CPU con precio > 100
SELECT
    name,
    price,
    category_id
FROM product
WHERE category_id = 3      -- id de "CPU"
  AND price > 100
ORDER BY price DESC;
