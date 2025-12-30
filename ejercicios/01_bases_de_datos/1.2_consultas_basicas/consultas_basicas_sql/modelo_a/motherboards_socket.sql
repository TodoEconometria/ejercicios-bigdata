-- Consulta 1.3: Motherboards por socket
SELECT
    name        AS nombre,
    socket,
    price       AS precio,
    form_factor
FROM motherboard
WHERE socket IN ('AM5', 'LGA1700')
ORDER BY socket ASC,
         price ASC;
