SELECT
    first_name    AS nombre,
    last_name     AS apellido,
    email,
    registered_at AS fecha_registro
FROM customer
ORDER BY registered_at DESC;
