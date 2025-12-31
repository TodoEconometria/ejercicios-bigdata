-- ============================================
-- Script: 04_cargar_datos_parte1.sql
-- Descripción: Carga de datos básicos (regions, countries, locations, departments, jobs)
-- Adaptado de: Modelo_HR-1.sql (Oracle)
-- Autor: Fernando Ramos Treviño
-- Fecha: 2025-12-31
-- ============================================

-- EJECUTAR EN: hr_database
-- NOTA: Debe ejecutarse DESPUÉS de crear todas las tablas


-- =====================================================
-- INSERTAR DATOS: REGIONS (4 filas)
-- =====================================================
-- Propósito: Cargar las 4 regiones principales del mundo
-- =====================================================

INSERT INTO regions VALUES (1, 'Europe');
INSERT INTO regions VALUES (2, 'Americas');
INSERT INTO regions VALUES (3, 'Asia');
INSERT INTO regions VALUES (4, 'Middle East and Africa');

-- Verificar inserción
-- SELECT * FROM regions;


-- =====================================================
-- INSERTAR DATOS: COUNTRIES (25 filas)
-- =====================================================
-- Propósito: Cargar países distribuidos por regiones
-- Cada país tiene su código ISO de 2 letras
-- =====================================================

INSERT INTO countries VALUES ('IT', 'Italy', 1);
INSERT INTO countries VALUES ('JP', 'Japan', 3);
INSERT INTO countries VALUES ('US', 'United States of America', 2);
INSERT INTO countries VALUES ('CA', 'Canada', 2);
INSERT INTO countries VALUES ('CN', 'China', 3);
INSERT INTO countries VALUES ('IN', 'India', 3);
INSERT INTO countries VALUES ('AU', 'Australia', 3);
INSERT INTO countries VALUES ('ZW', 'Zimbabwe', 4);
INSERT INTO countries VALUES ('SG', 'Singapore', 3);
INSERT INTO countries VALUES ('UK', 'United Kingdom', 1);
INSERT INTO countries VALUES ('FR', 'France', 1);
INSERT INTO countries VALUES ('DE', 'Germany', 1);
INSERT INTO countries VALUES ('ZM', 'Zambia', 4);
INSERT INTO countries VALUES ('EG', 'Egypt', 4);
INSERT INTO countries VALUES ('BR', 'Brazil', 2);
INSERT INTO countries VALUES ('CH', 'Switzerland', 1);
INSERT INTO countries VALUES ('NL', 'Netherlands', 1);
INSERT INTO countries VALUES ('MX', 'Mexico', 2);
INSERT INTO countries VALUES ('KW', 'Kuwait', 4);
INSERT INTO countries VALUES ('IL', 'Israel', 4);
INSERT INTO countries VALUES ('DK', 'Denmark', 1);
INSERT INTO countries VALUES ('ML', 'Malaysia', 3);
INSERT INTO countries VALUES ('NG', 'Nigeria', 4);
INSERT INTO countries VALUES ('AR', 'Argentina', 2);
INSERT INTO countries VALUES ('BE', 'Belgium', 1);

-- Verificar inserción
-- SELECT COUNT(*) FROM countries;  -- Debe devolver 25


-- =====================================================
-- INSERTAR DATOS: LOCATIONS (23 filas)
-- =====================================================
-- Propósito: Cargar ubicaciones físicas de oficinas
-- =====================================================

INSERT INTO locations VALUES (1000, '1297 Via Cola di Rie', '00989', 'Roma', NULL, 'IT');
INSERT INTO locations VALUES (1100, '93091 Calle della Testa', '10934', 'Venice', NULL, 'IT');
INSERT INTO locations VALUES (1200, '2017 Shinjuku-ku', '1689', 'Tokyo', 'Tokyo Prefecture', 'JP');
INSERT INTO locations VALUES (1300, '9450 Kamiya-cho', '6823', 'Hiroshima', NULL, 'JP');
INSERT INTO locations VALUES (1400, '2014 Jabberwocky Rd', '26192', 'Southlake', 'Texas', 'US');
INSERT INTO locations VALUES (1500, '2011 Interiors Blvd', '99236', 'South San Francisco', 'California', 'US');
INSERT INTO locations VALUES (1600, '2007 Zagora St', '50090', 'South Brunswick', 'New Jersey', 'US');
INSERT INTO locations VALUES (1700, '2004 Charade Rd', '98199', 'Seattle', 'Washington', 'US');
INSERT INTO locations VALUES (1800, '147 Spadina Ave', 'M5V 2L7', 'Toronto', 'Ontario', 'CA');
INSERT INTO locations VALUES (1900, '6092 Boxwood St', 'YSW 9T2', 'Whitehorse', 'Yukon', 'CA');
INSERT INTO locations VALUES (2000, '40-5-12 Laogianggen', '190518', 'Beijing', NULL, 'CN');
INSERT INTO locations VALUES (2100, '1298 Vileparle E', '490231', 'Bombay', 'Maharashtra', 'IN');
INSERT INTO locations VALUES (2200, '12-98 Victoria Street', '2901', 'Sydney', 'New South Wales', 'AU');
INSERT INTO locations VALUES (2300, '198 Clementi North', '540198', 'Singapore', NULL, 'SG');
INSERT INTO locations VALUES (2400, '8204 Arthur St', NULL, 'London', NULL, 'UK');
INSERT INTO locations VALUES (2500, 'Magdalen Centre, The Oxford Science Park', 'OX9 9ZB', 'Oxford', 'Oxford', 'UK');
INSERT INTO locations VALUES (2600, '9702 Chester Road', '09629850293', 'Stretford', 'Manchester', 'UK');
INSERT INTO locations VALUES (2700, 'Schwanthalerstr. 7031', '80925', 'Munich', 'Bavaria', 'DE');
INSERT INTO locations VALUES (2800, 'Rua Frei Caneca 1360', '01307-002', 'Sao Paulo', 'Sao Paulo', 'BR');
INSERT INTO locations VALUES (2900, '20 Rue des Corps-Saints', '1730', 'Geneva', 'Geneve', 'CH');
INSERT INTO locations VALUES (3000, 'Murtenstrasse 921', '3095', 'Bern', 'BE', 'CH');
INSERT INTO locations VALUES (3100, 'Pieter Breughelstraat 837', '3029SK', 'Utrecht', 'Utrecht', 'NL');
INSERT INTO locations VALUES (3200, 'Mariano Escobedo 9991', '11932', 'Mexico City', 'Distrito Federal,', 'MX');

-- Verificar inserción
-- SELECT COUNT(*) FROM locations;  -- Debe devolver 23


-- =====================================================
-- INSERTAR DATOS: DEPARTMENTS (27 filas)
-- =====================================================
-- Propósito: Cargar departamentos de la empresa
-- IMPORTANTE: manager_id se deja NULL por ahora (referencia circular)
-- Se actualizará DESPUÉS de insertar empleados
-- =====================================================

-- Primero DESHABILITAMOS temporalmente la FK dept_mgr_fk (que no existe aún, OK)
-- Solo insertamos sin manager_id

INSERT INTO departments VALUES (10, 'Administration', NULL, 1700);
INSERT INTO departments VALUES (20, 'Marketing', NULL, 1800);
INSERT INTO departments VALUES (30, 'Purchasing', NULL, 1700);
INSERT INTO departments VALUES (40, 'Human Resources', NULL, 2400);
INSERT INTO departments VALUES (50, 'Shipping', NULL, 1500);
INSERT INTO departments VALUES (60, 'IT', NULL, 1400);
INSERT INTO departments VALUES (70, 'Public Relations', NULL, 2700);
INSERT INTO departments VALUES (80, 'Sales', NULL, 2500);
INSERT INTO departments VALUES (90, 'Executive', NULL, 1700);
INSERT INTO departments VALUES (100, 'Finance', NULL, 1700);
INSERT INTO departments VALUES (110, 'Accounting', NULL, 1700);
INSERT INTO departments VALUES (120, 'Treasury', NULL, 1700);
INSERT INTO departments VALUES (130, 'Corporate Tax', NULL, 1700);
INSERT INTO departments VALUES (140, 'Control And Credit', NULL, 1700);
INSERT INTO departments VALUES (150, 'Shareholder Services', NULL, 1700);
INSERT INTO departments VALUES (160, 'Benefits', NULL, 1700);
INSERT INTO departments VALUES (170, 'Manufacturing', NULL, 1700);
INSERT INTO departments VALUES (180, 'Construction', NULL, 1700);
INSERT INTO departments VALUES (190, 'Contracting', NULL, 1700);
INSERT INTO departments VALUES (200, 'Operations', NULL, 1700);
INSERT INTO departments VALUES (210, 'IT Support', NULL, 1700);
INSERT INTO departments VALUES (220, 'NOC', NULL, 1700);
INSERT INTO departments VALUES (230, 'IT Helpdesk', NULL, 1700);
INSERT INTO departments VALUES (240, 'Government Sales', NULL, 1700);
INSERT INTO departments VALUES (250, 'Retail Sales', NULL, 1700);
INSERT INTO departments VALUES (260, 'Recruiting', NULL, 1700);
INSERT INTO departments VALUES (270, 'Payroll', NULL, 1700);

-- Verificar inserción
-- SELECT COUNT(*) FROM departments;  -- Debe devolver 27


-- =====================================================
-- INSERTAR DATOS: JOBS (19 filas)
-- =====================================================
-- Propósito: Cargar puestos de trabajo con rangos salariales
-- =====================================================

INSERT INTO jobs VALUES ('AD_PRES', 'President', 20080, 40000);
INSERT INTO jobs VALUES ('AD_VP', 'Administration Vice President', 15000, 30000);
INSERT INTO jobs VALUES ('AD_ASST', 'Administration Assistant', 3000, 6000);
INSERT INTO jobs VALUES ('FI_MGR', 'Finance Manager', 8200, 16000);
INSERT INTO jobs VALUES ('FI_ACCOUNT', 'Accountant', 4200, 9000);
INSERT INTO jobs VALUES ('AC_MGR', 'Accounting Manager', 8200, 16000);
INSERT INTO jobs VALUES ('AC_ACCOUNT', 'Public Accountant', 4200, 9000);
INSERT INTO jobs VALUES ('SA_MAN', 'Sales Manager', 10000, 20080);
INSERT INTO jobs VALUES ('SA_REP', 'Sales Representative', 6000, 12008);
INSERT INTO jobs VALUES ('PU_MAN', 'Purchasing Manager', 8000, 15000);
INSERT INTO jobs VALUES ('PU_CLERK', 'Purchasing Clerk', 2500, 5500);
INSERT INTO jobs VALUES ('ST_MAN', 'Stock Manager', 5500, 8500);
INSERT INTO jobs VALUES ('ST_CLERK', 'Stock Clerk', 2008, 5000);
INSERT INTO jobs VALUES ('SH_CLERK', 'Shipping Clerk', 2500, 5500);
INSERT INTO jobs VALUES ('IT_PROG', 'Programmer', 4000, 10000);
INSERT INTO jobs VALUES ('MK_MAN', 'Marketing Manager', 9000, 15000);
INSERT INTO jobs VALUES ('MK_REP', 'Marketing Representative', 4000, 9000);
INSERT INTO jobs VALUES ('HR_REP', 'Human Resources Representative', 4000, 9000);
INSERT INTO jobs VALUES ('PR_REP', 'Public Relations Representative', 4500, 10500);

-- Verificar inserción
-- SELECT COUNT(*) FROM jobs;  -- Debe devolver 19


-- =====================================================
-- VERIFICACIÓN FINAL
-- =====================================================

-- Resumen de datos insertados
SELECT 'regions' AS tabla, COUNT(*) AS filas FROM regions
UNION ALL
SELECT 'countries', COUNT(*) FROM countries
UNION ALL
SELECT 'locations', COUNT(*) FROM locations
UNION ALL
SELECT 'departments', COUNT(*) FROM departments
UNION ALL
SELECT 'jobs', COUNT(*) FROM jobs;

-- Resultado esperado:
-- regions: 4
-- countries: 25
-- locations: 23
-- departments: 27
-- jobs: 19


-- =====================================================
-- DIFERENCIAS ORACLE vs POSTGRESQL EN DATOS
-- =====================================================
--
-- 1. FECHAS:
--    No aplica aún (las fechas están en employees)
--
-- 2. COMILLAS:
--    Ambos usan comillas simples para strings
--
-- 3. NULL:
--    Sintaxis idéntica en ambos
--
-- 4. ORDEN DE INSERCIÓN:
--    Igual en ambos: respetar dependencias de FKs
--
-- =====================================================

COMMIT;
