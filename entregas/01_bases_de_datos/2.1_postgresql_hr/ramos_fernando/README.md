Ejercicio 2.1: PostgreSQL con Base de Datos HR
Autor: Fernando Ramos Treviño & Claude
Usuario GitHub: fernandoramostrevi-ctrl
Fecha: 31 de diciembre de 2025
Rama: ramos-ejercicio-2.1

Descripción
Este ejercicio consiste en adaptar la base de datos HR (Human Resources) de Oracle a PostgreSQL, realizando las conversiones necesarias de sintaxis y tipos de datos, cargando los datos y ejecutando consultas SQL avanzadas para demostrar el dominio de PostgreSQL y la comprensión de las diferencias con Oracle.

La base de datos HR es un modelo clásico de Oracle que contiene información sobre empleados, departamentos, ubicaciones, puestos de trabajo e historial laboral de una empresa.

Objetivos cumplidos
✅ Instalar y configurar PostgreSQL 16

✅ Adaptar scripts SQL de Oracle a PostgreSQL

✅ Crear la base de datos HR en PostgreSQL

✅ Cargar datos completos (107 empleados, 27 departamentos, 23 ubicaciones)

✅ Realizar consultas SQL avanzadas

✅ Comparar sintaxis SQL: Oracle vs PostgreSQL

Estructura de la base de datos
Modelo Entidad-Relación
text
REGIONS (4 filas)
    ↓
COUNTRIES (25 filas)
    ↓
LOCATIONS (23 filas)
    ↓
DEPARTMENTS (27 filas) ↔ EMPLOYEES (107 filas)
    ↓                        ↓
JOB_HISTORY (10 filas)   JOBS (19 filas)
Tablas principales
Tabla	Filas	Descripción
regions	4	Regiones geográficas (Europa, América, Asia, Medio Oriente/África)
countries	25	Países del mundo
locations	23	Ubicaciones físicas de oficinas
departments	27	Departamentos de la empresa
jobs	19	Puestos de trabajo con rangos salariales
employees	107	Empleados con información completa
job_history	10	Historial de cambios de puesto
Archivos del ejercicio
Scripts SQL
text
scripts/
├── 01_crear_usuario.sql           # Creación de usuario y base de datos
├── 02_crear_schema_parte1.sql     # Tablas básicas (regions, countries, locations)
├── 03_crear_schema_parte2.sql     # Tablas avanzadas (departments, jobs, employees, job_history)
├── 04_cargar_datos_parte1.sql     # Datos básicos (regions → jobs)
├── 05_cargar_datos_parte2.sql     # Datos avanzados (employees, job_history)
└── 06_consultas_avanzadas.sql     # Consultas SQL avanzadas (JOINs, subconsultas, CTEs)
Instalación y ejecución
Requisitos previos
PostgreSQL 16+

pgAdmin 4 o cliente SQL compatible

Git

Pasos para recrear la base de datos
1. Crear usuario y base de datos
bash
# Ejecutar como usuario postgres en pgAdmin
psql -U postgres
sql
-- Ejecutar 01_crear_usuario.sql (en dos partes)
CREATE USER hr WITH PASSWORD 'HRmdyOnce31';

CREATE DATABASE hr_database
    WITH 
    OWNER = hr
    ENCODING = 'UTF8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;
2. Conectarse a hr_database
En pgAdmin:

Click derecho en hr_database → Query Tool

3. Crear tablas
bash
# Ejecutar en orden:
02_crear_schema_parte1.sql     # Tablas básicas
03_crear_schema_parte2.sql     # Tablas avanzadas
4. Cargar datos
bash
# Ejecutar en orden:
04_cargar_datos_parte1.sql     # Datos básicos
05_cargar_datos_parte2.sql     # Empleados e historial
5. Verificar carga
sql
SELECT 'regions' AS tabla, COUNT(*) AS filas FROM regions
UNION ALL
SELECT 'countries', COUNT(*) FROM countries
UNION ALL
SELECT 'locations', COUNT(*) FROM locations
UNION ALL
SELECT 'departments', COUNT(*) FROM departments
UNION ALL
SELECT 'jobs', COUNT(*) FROM jobs
UNION ALL
SELECT 'employees', COUNT(*) FROM employees
UNION ALL
SELECT 'job_history', COUNT(*) FROM job_history;
Resultado esperado:

text
tabla         | filas
--------------+-------
regions       |     4
countries     |    25
locations     |    23
departments   |    27
jobs          |    19
employees     |   107
job_history   |    10
Principales adaptaciones Oracle → PostgreSQL
1. Tipos de datos
Oracle	PostgreSQL	Ejemplo
NUMBER	INTEGER	IDs, contadores
NUMBER(8,2)	NUMERIC(8,2)	Salarios con decimales
NUMBER(2,2)	NUMERIC(3,2)	Comisiones (0.00-0.99)
VARCHAR2(25)	VARCHAR(25)	Texto variable
CHAR(2)	CHAR(2)	Códigos fijos
2. Fechas
Oracle:

sql
TO_DATE('17-06-2003', 'dd-MM-yyyy')
PostgreSQL:

sql
'2003-06-17'::DATE
3. Secuencias
Oracle:

sql
CREATE SEQUENCE employees_seq
 START WITH 207
 INCREMENT BY 1
 NOCACHE
 NOCYCLE;
PostgreSQL:

sql
CREATE SEQUENCE employees_seq
    START WITH 207
    INCREMENT BY 1
    CACHE 1          -- NO CACHE → CACHE 1
    NO CYCLE;
4. Constraints y Primary Keys
Oracle (dos pasos):

sql
CREATE UNIQUE INDEX reg_id_pk ON regions (region_id);
ALTER TABLE regions ADD CONSTRAINT reg_id_pk PRIMARY KEY (region_id);
PostgreSQL (un paso):

sql
CREATE TABLE regions (
    region_id INTEGER NOT NULL,
    CONSTRAINT reg_id_pk PRIMARY KEY (region_id)
);
5. Jerarquías (consultas recursivas)
Oracle:

sql
SELECT employee_id, last_name, manager_id, LEVEL
FROM employees
START WITH manager_id IS NULL
CONNECT BY PRIOR employee_id = manager_id;
PostgreSQL:

sql
WITH RECURSIVE employee_hierarchy AS (
    SELECT employee_id, first_name, manager_id, 1 AS nivel
    FROM employees
    WHERE manager_id IS NULL

    UNION ALL

    SELECT e.employee_id, e.first_name, e.manager_id, eh.nivel + 1
    FROM employees e
    INNER JOIN employee_hierarchy eh ON e.manager_id = eh.employee_id
)
SELECT * FROM employee_hierarchy;
6. Funciones de fecha
Concepto	Oracle	PostgreSQL
Fecha actual	SYSDATE	CURRENT_DATE o NOW()
Diferencia de fechas	MONTHS_BETWEEN()	AGE(), DATE_PART()
Formato de fecha	TO_DATE()	TO_DATE() o ::DATE
Consultas SQL avanzadas incluidas
El script 06_consultas_avanzadas.sql incluye 10 consultas que demuestran:

JOINs múltiples (4 tablas): Empleados con departamento, ciudad y país

Agregaciones: Salario promedio por departamento con GROUP BY y HAVING

Funciones de ventana: Top 5 empleados mejor pagados por departamento (RANK)

Subconsultas correlacionadas: Empleados que ganan más que el promedio de su departamento

Consultas recursivas: Jerarquía organizacional con WITH RECURSIVE

JOIN con historial: Empleados que han cambiado de puesto

Cálculos: Análisis de comisiones en ventas

Funciones de fecha: Antigüedad de empleados con AGE()

Estadísticas: Distribución salarial por región geográfica

Validación de datos: Empleados sin departamento asignado

Problemas encontrados y soluciones
1. Comando \c no funciona en pgAdmin
Problema:
El comando \c hr_database es específico de psql (terminal) y no funciona en pgAdmin.

Solución:
Dividir el script en dos partes:

Parte 1: Crear usuario y BD (ejecutar en BD postgres)

Parte 2: Otorgar permisos (ejecutar en BD hr_database)

2. CREATE DATABASE dentro de transacción
Problema:

text
ERROR: CREATE DATABASE no puede ser ejecutado dentro de un bloque de transacción
Solución:
Ejecutar CREATE DATABASE sin BEGIN...COMMIT o ejecutar comandos por separado.

3. .gitignore bloqueando carpeta scripts/
Problema:
El repositorio tenía scripts/ en .gitignore, impidiendo subir los archivos.

Solución:
Eliminar la línea scripts/ del .gitignore y usar git add -f si es necesario.

4. Referencia circular entre departments y employees
Problema:

departments.manager_id → employees.employee_id

employees.department_id → departments.department_id

Solución:

Crear departments sin manager_id inicialmente

Insertar employees

UPDATE departments SET manager_id

ALTER TABLE para añadir la FK dept_mgr_fk

5. NUMERIC(2,2) insuficiente para comisiones
Problema:
Oracle permite NUMBER(2,2) para valores como 0.40, pero PostgreSQL necesita 3 dígitos totales.

Solución:
Cambiar a NUMERIC(3,2) para permitir 0.00 a 0.99.

Diferencias clave Oracle vs PostgreSQL
Ventajas de PostgreSQL
✅ Open source y gratuito

✅ Multiplataforma (Windows, Linux, macOS)

✅ Sintaxis más estándar SQL

✅ LIMIT más intuitivo que ROWNUM

✅ WITH RECURSIVE más potente que CONNECT BY

✅ Mejor manejo de tipos de datos complejos (JSON, arrays)

✅ Extensiones potentes (PostGIS, pgcrypto)

Ventajas de Oracle
✅ CONNECT BY más simple para jerarquías básicas

✅ Optimizador más maduro para consultas complejas

✅ Soporte empresarial oficial

✅ Herramientas de administración más avanzadas (Enterprise Manager)

Comandos útiles PostgreSQL
Ver estructura de una tabla
sql
\d nombre_tabla
O en pgAdmin:

sql
SELECT column_name, data_type, character_maximum_length
FROM information_schema.columns
WHERE table_name = 'employees';
Ver todas las tablas
sql
SELECT table_name 
FROM information_schema.tables 
WHERE table_schema = 'public';
Ver constraints de una tabla
sql
SELECT constraint_name, constraint_type
FROM information_schema.table_constraints
WHERE table_name = 'employees';
Backup de la base de datos
bash
pg_dump -U postgres hr_database > hr_database_backup.sql
Restaurar desde backup
bash
psql -U postgres -d hr_database < hr_database_backup.sql
Recursos utilizados
Documentación oficial de PostgreSQL

PostgreSQL Tutorial

Oracle HR Schema Documentation

Oracle DB Sample Schemas (GitHub)

Guía general de entregas del curso

Conclusiones
Este ejercicio ha permitido:

Comprender las diferencias fundamentales entre Oracle y PostgreSQL

Adaptar scripts SQL de un SGBD propietario a uno open source

Dominar conceptos avanzados de SQL: JOINs complejos, subconsultas, CTEs, funciones de ventana

Trabajar con un modelo de datos real (HR de Oracle)

Aprender buenas prácticas de documentación y versionado con Git

PostgreSQL demuestra ser una alternativa robusta, eficiente y estándar a Oracle, especialmente para proyectos donde el código abierto y la portabilidad son importantes.

Autor & Claude
Fernando Ramos Treviño
GitHub: @fernandoramostrevi-ctrl
Ejercicio: 2.1 - PostgreSQL con Base de Datos HR
Curso: Big Data
Fecha: 31 de diciembre de 202