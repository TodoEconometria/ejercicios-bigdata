SELECT
    id          AS id,
    customer_id AS cliente_id,
    "order_date" AS fecha,
    status      AS estado,
    total       AS total
FROM "order"
WHERE status IN ('pending', 'processing')
ORDER BY "order_date" DESC;
