
-- ============================================
-- Script: 06_consultas_avanzadas.sql
-- Descripción: Consultas SQL avanzadas sobre la base de datos HR
-- Objetivo: Demostrar JOINs, subconsultas, agregaciones, funciones de ventana
-- Autor: Fernando Ramos Treviño
-- Fecha: 2025-12-31
-- ============================================

-- EJECUTAR EN: hr_database


-- =====================================================
-- CONSULTA 1: Empleados con su departamento y ubicación
-- =====================================================
-- Objetivo: JOIN múltiple (4 tablas)
-- Muestra: empleado, departamento, ciudad, país
-- =====================================================

SELECT
    e.employee_id,
    e.first_name || ' ' || e.last_name AS nombre_completo,
    d.department_name,
    l.city,
    c.country_name
FROM employees e
INNER JOIN departments d ON e.department_id = d.department_id
INNER JOIN locations l ON d.location_id = l.location_id
INNER JOIN countries c ON l.country_id = c.country_id
ORDER BY e.employee_id
LIMIT 10;

-- Diferencia Oracle vs PostgreSQL:
-- Oracle: || para concatenar (igual)
-- Oracle: ROWNUM <= 10 (en lugar de LIMIT 10)
-- PostgreSQL: LIMIT es más simple y claro


-- =====================================================
-- CONSULTA 2: Salario promedio por departamento
-- =====================================================
-- Objetivo: Agregación con GROUP BY y HAVING
-- Muestra: Solo departamentos con salario promedio > 8000
-- =====================================================

SELECT
    d.department_name,
    COUNT(e.employee_id) AS num_empleados,
    ROUND(AVG(e.salary), 2) AS salario_promedio,
    MIN(e.salary) AS salario_minimo,
    MAX(e.salary) AS salario_maximo
FROM departments d
LEFT JOIN employees e ON d.department_id = e.department_id
GROUP BY d.department_id, d.department_name
HAVING AVG(e.salary) > 8000
ORDER BY salario_promedio DESC;

-- Diferencia Oracle vs PostgreSQL:
-- ROUND(): Sintaxis idéntica
-- Ambos requieren incluir todas las columnas no agregadas en GROUP BY


-- =====================================================
-- CONSULTA 3: Top 5 empleados mejor pagados por departamento
-- =====================================================
-- Objetivo: Función de ventana RANK()
-- Muestra: Los 5 salarios más altos en cada departamento
-- =====================================================

WITH ranked_employees AS (
    SELECT
        e.employee_id,
        e.first_name || ' ' || e.last_name AS nombre,
        e.salary,
        d.department_name,
        RANK() OVER (PARTITION BY e.department_id ORDER BY e.salary DESC) AS ranking
    FROM employees e
    INNER JOIN departments d ON e.department_id = d.department_id
)
SELECT
    department_name,
    nombre,
    salary,
    ranking
FROM ranked_employees
WHERE ranking <= 5
ORDER BY department_name, ranking;

-- Diferencia Oracle vs PostgreSQL:
-- Funciones de ventana: Sintaxis idéntica
-- CTE (WITH): Sintaxis idéntica
-- Ambos soportan RANK(), DENSE_RANK(), ROW_NUMBER()


-- =====================================================
-- CONSULTA 4: Empleados que ganan más que el promedio de su departamento
-- =====================================================
-- Objetivo: Subconsulta correlacionada
-- Muestra: Empleados "privilegiados" en cada departamento
-- =====================================================

SELECT
    e.employee_id,
    e.first_name || ' ' || e.last_name AS nombre,
    e.salary,
    d.department_name,
    (SELECT ROUND(AVG(e2.salary), 2)
     FROM employees e2
     WHERE e2.department_id = e.department_id) AS salario_promedio_dept,
    ROUND(e.salary - (SELECT AVG(e2.salary)
                      FROM employees e2
                      WHERE e2.department_id = e.department_id), 2) AS diferencia
FROM employees e
INNER JOIN departments d ON e.department_id = d.department_id
WHERE e.salary > (SELECT AVG(e2.salary)
                  FROM employees e2
                  WHERE e2.department_id = e.department_id)
ORDER BY diferencia DESC
LIMIT 10;

-- Diferencia Oracle vs PostgreSQL:
-- Subconsultas correlacionadas: Sintaxis idéntica
-- PostgreSQL puede ser más eficiente con CTEs en casos complejos


-- =====================================================
-- CONSULTA 5: Jerarquía de managers (árbol organizacional)
-- =====================================================
-- Objetivo: Recursive CTE (consulta recursiva)
-- Muestra: Cadena de mando desde el CEO hasta empleados
-- =====================================================

WITH RECURSIVE employee_hierarchy AS (
    -- Caso base: CEO (sin manager)
    SELECT
        employee_id,
        first_name || ' ' || last_name AS nombre,
        job_id,
        manager_id,
        1 AS nivel,
        first_name || ' ' || last_name AS ruta_jerarquia
    FROM employees
    WHERE manager_id IS NULL

    UNION ALL

    -- Caso recursivo: empleados que reportan a los anteriores
    SELECT
        e.employee_id,
        e.first_name || ' ' || e.last_name AS nombre,
        e.job_id,
        e.manager_id,
        eh.nivel + 1,
        eh.ruta_jerarquia || ' → ' || e.first_name || ' ' || e.last_name
    FROM employees e
    INNER JOIN employee_hierarchy eh ON e.manager_id = eh.employee_id
)
SELECT
    nivel,
    REPEAT('  ', nivel - 1) || nombre AS empleado_indentado,
    job_id,
    ruta_jerarquia
FROM employee_hierarchy
ORDER BY ruta_jerarquia
LIMIT 20;

-- Diferencia Oracle vs PostgreSQL:
-- Oracle: CONNECT BY PRIOR (sintaxis específica de Oracle)
--   SELECT employee_id, last_name, manager_id, LEVEL
--   FROM employees
--   START WITH manager_id IS NULL
--   CONNECT BY PRIOR employee_id = manager_id;
--
-- PostgreSQL: WITH RECURSIVE (estándar SQL)
-- PostgreSQL es más flexible y potente para jerarquías complejas


-- =====================================================
-- CONSULTA 6: Empleados que han cambiado de puesto
-- =====================================================
-- Objetivo: JOIN con historial laboral
-- Muestra: Empleados con cambios de trabajo y sus fechas
-- =====================================================

SELECT
    e.employee_id,
    e.first_name || ' ' || e.last_name AS nombre,
    j_actual.job_title AS puesto_actual,
    j_anterior.job_title AS puesto_anterior,
    jh.start_date AS fecha_inicio_anterior,
    jh.end_date AS fecha_fin_anterior,
    jh.end_date - jh.start_date AS dias_en_puesto_anterior
FROM employees e
INNER JOIN job_history jh ON e.employee_id = jh.employee_id
INNER JOIN jobs j_actual ON e.job_id = j_actual.job_id
INNER JOIN jobs j_anterior ON jh.job_id = j_anterior.job_id
ORDER BY e.employee_id, jh.start_date;

-- Diferencia Oracle vs PostgreSQL:
-- Operaciones con fechas:
-- Oracle: end_date - start_date devuelve días directamente
-- PostgreSQL: También devuelve intervalo, pero puede ser necesario ::INTEGER


-- =====================================================
-- CONSULTA 7: Análisis de comisiones en ventas
-- =====================================================
-- Objetivo: Filtrado y cálculo de comisiones
-- Muestra: Solo empleados de ventas con comisión
-- =====================================================

SELECT
    e.employee_id,
    e.first_name || ' ' || e.last_name AS nombre,
    e.salary,
    e.commission_pct,
    ROUND(e.salary * e.commission_pct, 2) AS comision_mensual,
    ROUND(e.salary * e.commission_pct * 12, 2) AS comision_anual,
    d.department_name
FROM employees e
INNER JOIN departments d ON e.department_id = d.department_id
WHERE e.commission_pct IS NOT NULL
ORDER BY comision_anual DESC;

-- Diferencia Oracle vs PostgreSQL:
-- Manejo de NULL: Idéntico en ambos
-- ROUND(): Sintaxis idéntica


-- =====================================================
-- CONSULTA 8: Antigüedad de empleados
-- =====================================================
-- Objetivo: Funciones de fecha
-- Muestra: Años de servicio de cada empleado
-- =====================================================

SELECT
    e.employee_id,
    e.first_name || ' ' || e.last_name AS nombre,
    e.hire_date AS fecha_contratacion,
    CURRENT_DATE AS fecha_actual,
    DATE_PART('year', AGE(CURRENT_DATE, e.hire_date)) AS años_servicio,
    DATE_PART('month', AGE(CURRENT_DATE, e.hire_date)) AS meses_adicionales,
    d.department_name
FROM employees e
INNER JOIN departments d ON e.department_id = d.department_id
ORDER BY años_servicio DESC, meses_adicionales DESC
LIMIT 10;

-- Diferencia Oracle vs PostgreSQL:
-- Oracle: SYSDATE, MONTHS_BETWEEN()
--   TRUNC(MONTHS_BETWEEN(SYSDATE, hire_date) / 12) AS años
-- PostgreSQL: CURRENT_DATE, AGE(), DATE_PART()
-- PostgreSQL es más legible y preciso con AGE()


-- =====================================================
-- CONSULTA 9: Distribución salarial por región
-- =====================================================
-- Objetivo: JOIN completo + agregación geográfica
-- Muestra: Estadísticas salariales por región del mundo
-- =====================================================

SELECT
    r.region_name,
    COUNT(DISTINCT e.employee_id) AS total_empleados,
    COUNT(DISTINCT d.department_id) AS total_departamentos,
    ROUND(AVG(e.salary), 2) AS salario_promedio,
    ROUND(MIN(e.salary), 2) AS salario_minimo,
    ROUND(MAX(e.salary), 2) AS salario_maximo,
    ROUND(STDDEV(e.salary), 2) AS desviacion_estandar
FROM regions r
INNER JOIN countries c ON r.region_id = c.region_id
INNER JOIN locations l ON c.country_id = l.country_id
INNER JOIN departments d ON l.location_id = d.location_id
INNER JOIN employees e ON d.department_id = e.department_id
GROUP BY r.region_id, r.region_name
ORDER BY total_empleados DESC;

-- Diferencia Oracle vs PostgreSQL:
-- STDDEV(): Sintaxis idéntica
-- Ambos soportan funciones estadísticas avanzadas


-- =====================================================
-- CONSULTA 10: Empleados sin departamento asignado
-- =====================================================
-- Objetivo: LEFT JOIN + filtrado de NULL
-- Muestra: Detección de datos inconsistentes
-- =====================================================

SELECT
    e.employee_id,
    e.first_name || ' ' || e.last_name AS nombre,
    e.email,
    e.job_id,
    e.salary,
    e.department_id,
    d.department_name
FROM employees e
LEFT JOIN departments d ON e.department_id = d.department_id
WHERE e.department_id IS NULL OR d.department_name IS NULL;

-- Si devuelve filas: Hay empleados sin departamento (inconsistencia)
-- Si no devuelve filas: Todos los empleados tienen departamento válido

-- Diferencia Oracle vs PostgreSQL:
-- LEFT JOIN: Sintaxis idéntica
-- Manejo de NULL: Idéntico


-- =====================================================
-- RESUMEN DE DIFERENCIAS ORACLE vs POSTGRESQL
-- =====================================================

/*
CATEGORÍA              | ORACLE                    | POSTGRESQL
-----------------------|---------------------------|---------------------------
Límite de filas        | ROWNUM <= N               | LIMIT N
Concatenación          | || (igual)               | || o CONCAT()
Jerarquías             | CONNECT BY PRIOR          | WITH RECURSIVE
Fecha actual           | SYSDATE                   | CURRENT_DATE, NOW()
Diferencia de fechas   | MONTHS_BETWEEN()          | AGE(), DATE_PART()
Auto-incremento        | SEQUENCE + trigger        | SERIAL o SEQUENCE
Tipos numéricos        | NUMBER                    | INTEGER, NUMERIC
Strings                | VARCHAR2                  | VARCHAR, TEXT
Funciones de ventana   | Sintaxis idéntica         | Sintaxis idéntica
CTEs                   | Sintaxis idéntica         | Sintaxis idéntica
Subconsultas           | Sintaxis idéntica         | Sintaxis idéntica

VENTAJAS POSTGRESQL:
- Sintaxis más estándar SQL
- LIMIT más intuitivo que ROWNUM
- WITH RECURSIVE más potente que CONNECT BY
- Open source y multiplataforma
- Mejor manejo de tipos de datos complejos

VENTAJAS ORACLE:
- CONNECT BY más simple para jerarquías básicas
- Optimizador más maduro en casos complejos
- Más funciones analíticas específicas
*/
