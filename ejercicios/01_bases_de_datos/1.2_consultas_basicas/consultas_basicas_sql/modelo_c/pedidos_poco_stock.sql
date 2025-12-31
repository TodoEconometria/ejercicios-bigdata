SELECT
    product_id      AS producto_id,
    stock AS cantidad_stock,
    min_stock   AS stock_minimo,
    location        AS ubicacion
FROM inventory
WHERE stock < min_stock
ORDER BY stock ASC;
