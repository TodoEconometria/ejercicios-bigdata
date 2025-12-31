SELECT id, name
FROM color
WHERE name = 'Black';
-- Consulta 2.3: Productos en color Black
SELECT
    p.id,
    p.name,
    p.price
FROM product pc
JOIN product p
      ON product_id = p.id
WHERE pc.color_id = 1        -- sustituye 1 por el id real de "Black"
LIMIT 20;
