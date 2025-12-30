SELECT
    id           AS id,
    customer_id  AS cliente_id,
    created_at   AS fecha_creacion,
    last_modified_at  AS ultima_modificacion
FROM cart
WHERE active = 1
ORDER BY last_modified_at DESC;
