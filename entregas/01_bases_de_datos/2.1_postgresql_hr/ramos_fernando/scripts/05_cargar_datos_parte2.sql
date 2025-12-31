-- ============================================
-- Script: 05_cargar_datos_parte2.sql
-- Descripción: Carga de empleados e historial laboral
-- Adaptado de: Modelo_HR-1.sql (Oracle)
-- Autor: Fernando Ramos Treviño
-- Fecha: 2025-12-31
-- ============================================

-- EJECUTAR EN: hr_database
-- NOTA: Ejecutar DESPUÉS de 04_cargar_datos_parte1.sql


-- =====================================================
-- INSERTAR DATOS: EMPLOYEES (107 filas)
-- =====================================================
-- Propósito: Cargar todos los empleados de la empresa
-- IMPORTANTE:
-- - Las fechas se convierten de TO_DATE('DD-MM-YYYY') a 'YYYY-MM-DD'::DATE
-- - Las comisiones decimales se escriben como 0.40, 0.25, etc.
-- - manager_id puede ser NULL (CEO no tiene jefe)
-- - Se insertan en orden para respetar auto-referencia de manager_id
-- =====================================================

-- CEO y VP (nivel más alto, no tienen manager o reportan entre ellos)
INSERT INTO employees VALUES (100, 'Steven', 'King', 'SKING', '515.123.4567', '2003-06-17'::DATE, 'AD_PRES', 24000, NULL, NULL, 90);
INSERT INTO employees VALUES (101, 'Neena', 'Kochhar', 'NKOCHHAR', '515.123.4568', '2005-09-21'::DATE, 'AD_VP', 17000, NULL, 100, 90);
INSERT INTO employees VALUES (102, 'Lex', 'De Haan', 'LDEHAAN', '515.123.4569', '2001-01-13'::DATE, 'AD_VP', 17000, NULL, 100, 90);

-- Departamento IT (reportan a Lex De Haan - 102)
INSERT INTO employees VALUES (103, 'Alexander', 'Hunold', 'AHUNOLD', '590.423.4567', '2006-01-03'::DATE, 'IT_PROG', 9000, NULL, 102, 60);
INSERT INTO employees VALUES (104, 'Bruce', 'Ernst', 'BERNST', '590.423.4568', '2007-05-21'::DATE, 'IT_PROG', 6000, NULL, 103, 60);
INSERT INTO employees VALUES (105, 'David', 'Austin', 'DAUSTIN', '590.423.4569', '2005-06-25'::DATE, 'IT_PROG', 4800, NULL, 103, 60);
INSERT INTO employees VALUES (106, 'Valli', 'Pataballa', 'VPATABAL', '590.423.4560', '2006-02-05'::DATE, 'IT_PROG', 4800, NULL, 103, 60);
INSERT INTO employees VALUES (107, 'Diana', 'Lorentz', 'DLORENTZ', '590.423.5567', '2007-02-07'::DATE, 'IT_PROG', 4200, NULL, 103, 60);

-- Departamento Finance (reportan a Neena Kochhar - 101)
INSERT INTO employees VALUES (108, 'Nancy', 'Greenberg', 'NGREENBE', '515.124.4569', '2002-08-17'::DATE, 'FI_MGR', 12008, NULL, 101, 100);
INSERT INTO employees VALUES (109, 'Daniel', 'Faviet', 'DFAVIET', '515.124.4169', '2002-08-16'::DATE, 'FI_ACCOUNT', 9000, NULL, 108, 100);
INSERT INTO employees VALUES (110, 'John', 'Chen', 'JCHEN', '515.124.4269', '2005-09-28'::DATE, 'FI_ACCOUNT', 8200, NULL, 108, 100);
INSERT INTO employees VALUES (111, 'Ismael', 'Sciarra', 'ISCIARRA', '515.124.4369', '2005-09-30'::DATE, 'FI_ACCOUNT', 7700, NULL, 108, 100);
INSERT INTO employees VALUES (112, 'Jose Manuel', 'Urman', 'JMURMAN', '515.124.4469', '2006-03-07'::DATE, 'FI_ACCOUNT', 7800, NULL, 108, 100);
INSERT INTO employees VALUES (113, 'Luis', 'Popp', 'LPOPP', '515.124.4567', '2007-12-07'::DATE, 'FI_ACCOUNT', 6900, NULL, 108, 100);

-- Departamento Purchasing (reportan a Steven King - 100)
INSERT INTO employees VALUES (114, 'Den', 'Raphaely', 'DRAPHEAL', '515.127.4561', '2002-12-07'::DATE, 'PU_MAN', 11000, NULL, 100, 30);
INSERT INTO employees VALUES (115, 'Alexander', 'Khoo', 'AKHOO', '515.127.4562', '2003-05-18'::DATE, 'PU_CLERK', 3100, NULL, 114, 30);
INSERT INTO employees VALUES (116, 'Shelli', 'Baida', 'SBAIDA', '515.127.4563', '2005-12-24'::DATE, 'PU_CLERK', 2900, NULL, 114, 30);
INSERT INTO employees VALUES (117, 'Sigal', 'Tobias', 'STOBIAS', '515.127.4564', '2005-07-24'::DATE, 'PU_CLERK', 2800, NULL, 114, 30);
INSERT INTO employees VALUES (118, 'Guy', 'Himuro', 'GHIMURO', '515.127.4565', '2006-11-15'::DATE, 'PU_CLERK', 2600, NULL, 114, 30);
INSERT INTO employees VALUES (119, 'Karen', 'Colmenares', 'KCOLMENA', '515.127.4566', '2007-08-10'::DATE, 'PU_CLERK', 2500, NULL, 114, 30);

-- Departamento Shipping (Stock Managers reportan a Steven King - 100)
INSERT INTO employees VALUES (120, 'Matthew', 'Weiss', 'MWEISS', '650.123.1234', '2004-07-18'::DATE, 'ST_MAN', 8000, NULL, 100, 50);
INSERT INTO employees VALUES (121, 'Adam', 'Fripp', 'AFRIPP', '650.123.2234', '2005-04-10'::DATE, 'ST_MAN', 8200, NULL, 100, 50);
INSERT INTO employees VALUES (122, 'Payam', 'Kaufling', 'PKAUFLIN', '650.123.3234', '2003-05-01'::DATE, 'ST_MAN', 7900, NULL, 100, 50);
INSERT INTO employees VALUES (123, 'Shanta', 'Vollman', 'SVOLLMAN', '650.123.4234', '2005-10-10'::DATE, 'ST_MAN', 6500, NULL, 100, 50);
INSERT INTO employees VALUES (124, 'Kevin', 'Mourgos', 'KMOURGOS', '650.123.5234', '2007-11-16'::DATE, 'ST_MAN', 5800, NULL, 100, 50);

-- Stock Clerks (reportan a Matthew Weiss - 120)
INSERT INTO employees VALUES (125, 'Julia', 'Nayer', 'JNAYER', '650.124.1214', '2005-07-16'::DATE, 'ST_CLERK', 3200, NULL, 120, 50);
INSERT INTO employees VALUES (126, 'Irene', 'Mikkilineni', 'IMIKKILI', '650.124.1224', '2006-09-28'::DATE, 'ST_CLERK', 2700, NULL, 120, 50);
INSERT INTO employees VALUES (127, 'James', 'Landry', 'JLANDRY', '650.124.1334', '2007-01-14'::DATE, 'ST_CLERK', 2400, NULL, 120, 50);
INSERT INTO employees VALUES (128, 'Steven', 'Markle', 'SMARKLE', '650.124.1434', '2008-03-08'::DATE, 'ST_CLERK', 2200, NULL, 120, 50);

-- Stock Clerks (reportan a Adam Fripp - 121)
INSERT INTO employees VALUES (129, 'Laura', 'Bissot', 'LBISSOT', '650.124.5234', '2005-08-20'::DATE, 'ST_CLERK', 3300, NULL, 121, 50);
INSERT INTO employees VALUES (130, 'Mozhe', 'Atkinson', 'MATKINSO', '650.124.6234', '2005-10-30'::DATE, 'ST_CLERK', 2800, NULL, 121, 50);
INSERT INTO employees VALUES (131, 'James', 'Marlow', 'JAMRLOW', '650.124.7234', '2005-02-16'::DATE, 'ST_CLERK', 2500, NULL, 121, 50);
INSERT INTO employees VALUES (132, 'TJ', 'Olson', 'TJOLSON', '650.124.8234', '2007-04-10'::DATE, 'ST_CLERK', 2100, NULL, 121, 50);

-- Stock Clerks (reportan a Payam Kaufling - 122)
INSERT INTO employees VALUES (133, 'Jason', 'Mallin', 'JMALLIN', '650.127.1934', '2004-06-14'::DATE, 'ST_CLERK', 3300, NULL, 122, 50);
INSERT INTO employees VALUES (134, 'Michael', 'Rogers', 'MROGERS', '650.127.1834', '2006-08-26'::DATE, 'ST_CLERK', 2900, NULL, 122, 50);
INSERT INTO employees VALUES (135, 'Ki', 'Gee', 'KGEE', '650.127.1734', '2007-12-12'::DATE, 'ST_CLERK', 2400, NULL, 122, 50);
INSERT INTO employees VALUES (136, 'Hazel', 'Philtanker', 'HPHILTAN', '650.127.1634', '2008-02-06'::DATE, 'ST_CLERK', 2200, NULL, 122, 50);

-- Stock Clerks (reportan a Shanta Vollman - 123)
INSERT INTO employees VALUES (137, 'Renske', 'Ladwig', 'RLADWIG', '650.121.1234', '2003-07-14'::DATE, 'ST_CLERK', 3600, NULL, 123, 50);
INSERT INTO employees VALUES (138, 'Stephen', 'Stiles', 'SSTILES', '650.121.2034', '2005-10-26'::DATE, 'ST_CLERK', 3200, NULL, 123, 50);
INSERT INTO employees VALUES (139, 'John', 'Seo', 'JSEO', '650.121.2019', '2006-02-12'::DATE, 'ST_CLERK', 2700, NULL, 123, 50);
INSERT INTO employees VALUES (140, 'Joshua', 'Patel', 'JPATEL', '650.121.1834', '2006-04-06'::DATE, 'ST_CLERK', 2500, NULL, 123, 50);

-- Stock Clerks (reportan a Kevin Mourgos - 124)
INSERT INTO employees VALUES (141, 'Trenna', 'Rajs', 'TRAJS', '650.121.8009', '2003-10-17'::DATE, 'ST_CLERK', 3500, NULL, 124, 50);
INSERT INTO employees VALUES (142, 'Curtis', 'Davies', 'CDAVIES', '650.121.2994', '2005-01-29'::DATE, 'ST_CLERK', 3100, NULL, 124, 50);
INSERT INTO employees VALUES (143, 'Randall', 'Matos', 'RMATOS', '650.121.2874', '2006-03-15'::DATE, 'ST_CLERK', 2600, NULL, 124, 50);
INSERT INTO employees VALUES (144, 'Peter', 'Vargas', 'PVARGAS', '650.121.2004', '2006-07-09'::DATE, 'ST_CLERK', 2500, NULL, 124, 50);

-- Departamento Sales (Sales Managers reportan a Steven King - 100)
INSERT INTO employees VALUES (145, 'John', 'Russell', 'JRUSSEL', '011.44.1344.429268', '2004-10-01'::DATE, 'SA_MAN', 14000, 0.40, 100, 80);
INSERT INTO employees VALUES (146, 'Karen', 'Partners', 'KPARTNER', '011.44.1344.467268', '2005-01-05'::DATE, 'SA_MAN', 13500, 0.30, 100, 80);
INSERT INTO employees VALUES (147, 'Alberto', 'Errazuriz', 'AERRAZUR', '011.44.1344.429278', '2005-03-10'::DATE, 'SA_MAN', 12000, 0.30, 100, 80);
INSERT INTO employees VALUES (148, 'Gerald', 'Cambrault', 'GCAMBRAU', '011.44.1344.619268', '2007-10-15'::DATE, 'SA_MAN', 11000, 0.30, 100, 80);
INSERT INTO employees VALUES (149, 'Eleni', 'Zlotkey', 'EZLOTKEY', '011.44.1344.429018', '2008-01-29'::DATE, 'SA_MAN', 10500, 0.20, 100, 80);

-- Sales Representatives (reportan a John Russell - 145)
INSERT INTO employees VALUES (150, 'Peter', 'Tucker', 'PTUCKER', '011.44.1344.129268', '2005-01-30'::DATE, 'SA_REP', 10000, 0.30, 145, 80);
INSERT INTO employees VALUES (151, 'David', 'Bernstein', 'DBERNSTE', '011.44.1344.345268', '2005-03-24'::DATE, 'SA_REP', 9500, 0.25, 145, 80);
INSERT INTO employees VALUES (152, 'Peter', 'Hall', 'PHALL', '011.44.1344.478968', '2005-08-20'::DATE, 'SA_REP', 9000, 0.25, 145, 80);
INSERT INTO employees VALUES (153, 'Christopher', 'Olsen', 'COLSEN', '011.44.1344.498718', '2006-03-30'::DATE, 'SA_REP', 8000, 0.20, 145, 80);
INSERT INTO employees VALUES (154, 'Nanette', 'Cambrault', 'NCAMBRAU', '011.44.1344.987668', '2006-12-09'::DATE, 'SA_REP', 7500, 0.20, 145, 80);
INSERT INTO employees VALUES (155, 'Oliver', 'Tuvault', 'OTUVAULT', '011.44.1344.486508', '2007-11-23'::DATE, 'SA_REP', 7000, 0.15, 145, 80);

-- Sales Representatives (reportan a Karen Partners - 146)
INSERT INTO employees VALUES (156, 'Janette', 'King', 'JKING', '011.44.1345.429268', '2004-01-30'::DATE, 'SA_REP', 10000, 0.35, 146, 80);
INSERT INTO employees VALUES (157, 'Patrick', 'Sully', 'PSULLY', '011.44.1345.929268', '2004-03-04'::DATE, 'SA_REP', 9500, 0.35, 146, 80);
INSERT INTO employees VALUES (158, 'Allan', 'McEwen', 'AMCEWEN', '011.44.1345.829268', '2004-08-01'::DATE, 'SA_REP', 9000, 0.35, 146, 80);
INSERT INTO employees VALUES (159, 'Lindsey', 'Smith', 'LSMITH', '011.44.1345.729268', '2005-03-10'::DATE, 'SA_REP', 8000, 0.30, 146, 80);
INSERT INTO employees VALUES (160, 'Louise', 'Doran', 'LDORAN', '011.44.1345.629268', '2005-12-15'::DATE, 'SA_REP', 7500, 0.30, 146, 80);
INSERT INTO employees VALUES (161, 'Sarath', 'Sewall', 'SSEWALL', '011.44.1345.529268', '2006-11-03'::DATE, 'SA_REP', 7000, 0.25, 146, 80);

-- Sales Representatives (reportan a Alberto Errazuriz - 147)
INSERT INTO employees VALUES (162, 'Clara', 'Vishney', 'CVISHNEY', '011.44.1346.129268', '2005-11-11'::DATE, 'SA_REP', 10500, 0.25, 147, 80);
INSERT INTO employees VALUES (163, 'Danielle', 'Greene', 'DGREENE', '011.44.1346.229268', '2007-03-19'::DATE, 'SA_REP', 9500, 0.15, 147, 80);
INSERT INTO employees VALUES (164, 'Mattea', 'Marvins', 'MMARVINS', '011.44.1346.329268', '2008-01-24'::DATE, 'SA_REP', 7200, 0.10, 147, 80);
INSERT INTO employees VALUES (165, 'David', 'Lee', 'DLEE', '011.44.1346.529268', '2008-02-23'::DATE, 'SA_REP', 6800, 0.10, 147, 80);
INSERT INTO employees VALUES (166, 'Sundar', 'Ande', 'SANDE', '011.44.1346.629268', '2008-03-24'::DATE, 'SA_REP', 6400, 0.10, 147, 80);
INSERT INTO employees VALUES (167, 'Amit', 'Banda', 'ABANDA', '011.44.1346.729268', '2008-04-21'::DATE, 'SA_REP', 6200, 0.10, 147, 80);

-- Sales Representatives (reportan a Gerald Cambrault - 148)
INSERT INTO employees VALUES (168, 'Lisa', 'Ozer', 'LOZER', '011.44.1343.929268', '2005-03-11'::DATE, 'SA_REP', 11500, 0.25, 148, 80);
INSERT INTO employees VALUES (169, 'Harrison', 'Bloom', 'HBLOOM', '011.44.1343.829268', '2006-03-23'::DATE, 'SA_REP', 10000, 0.20, 148, 80);
INSERT INTO employees VALUES (170, 'Tayler', 'Fox', 'TFOX', '011.44.1343.729268', '2006-01-24'::DATE, 'SA_REP', 9600, 0.20, 148, 80);
INSERT INTO employees VALUES (171, 'William', 'Smith', 'WSMITH', '011.44.1343.629268', '2007-02-23'::DATE, 'SA_REP', 7400, 0.15, 148, 80);
INSERT INTO employees VALUES (172, 'Elizabeth', 'Bates', 'EBATES', '011.44.1343.529268', '2007-03-24'::DATE, 'SA_REP', 7300, 0.15, 148, 80);
INSERT INTO employees VALUES (173, 'Sundita', 'Kumar', 'SKUMAR', '011.44.1343.329268', '2008-04-21'::DATE, 'SA_REP', 6100, 0.10, 148, 80);

-- Sales Representatives (reportan a Eleni Zlotkey - 149)
INSERT INTO employees VALUES (174, 'Ellen', 'Abel', 'EABEL', '011.44.1644.429267', '2004-05-11'::DATE, 'SA_REP', 11000, 0.30, 149, 80);
INSERT INTO employees VALUES (175, 'Alyssa', 'Hutton', 'AHUTTON', '011.44.1644.429266', '2005-03-19'::DATE, 'SA_REP', 8800, 0.25, 149, 80);
INSERT INTO employees VALUES (176, 'Jonathon', 'Taylor', 'JTAYLOR', '011.44.1644.429265', '2006-03-24'::DATE, 'SA_REP', 8600, 0.20, 149, 80);
INSERT INTO employees VALUES (177, 'Jack', 'Livingston', 'JLIVINGS', '011.44.1644.429264', '2006-04-23'::DATE, 'SA_REP', 8400, 0.20, 149, 80);
INSERT INTO employees VALUES (178, 'Kimberely', 'Grant', 'KGRANT', '011.44.1644.429263', '2007-05-24'::DATE, 'SA_REP', 7000, 0.15, 149, NULL);
INSERT INTO employees VALUES (179, 'Charles', 'Johnson', 'CJOHNSON', '011.44.1644.429262', '2008-01-04'::DATE, 'SA_REP', 6200, 0.10, 149, 80);

-- Shipping Clerks (reportan a Matthew Weiss - 120)
INSERT INTO employees VALUES (180, 'Winston', 'Taylor', 'WTAYLOR', '650.507.9876', '2006-01-24'::DATE, 'SH_CLERK', 3200, NULL, 120, 50);
INSERT INTO employees VALUES (181, 'Jean', 'Fleaur', 'JFLEAUR', '650.507.9877', '2006-02-23'::DATE, 'SH_CLERK', 3100, NULL, 120, 50);
INSERT INTO employees VALUES (182, 'Martha', 'Sullivan', 'MSULLIVA', '650.507.9878', '2007-06-21'::DATE, 'SH_CLERK', 2500, NULL, 120, 50);
INSERT INTO employees VALUES (183, 'Girard', 'Geoni', 'GGEONI', '650.507.9879', '2008-02-03'::DATE, 'SH_CLERK', 2800, NULL, 120, 50);

-- Shipping Clerks (reportan a Adam Fripp - 121)
INSERT INTO employees VALUES (184, 'Nandita', 'Sarchand', 'NSARCHAN', '650.509.1876', '2004-01-27'::DATE, 'SH_CLERK', 4200, NULL, 121, 50);
INSERT INTO employees VALUES (185, 'Alexis', 'Bull', 'ABULL', '650.509.2876', '2005-02-20'::DATE, 'SH_CLERK', 4100, NULL, 121, 50);
INSERT INTO employees VALUES (186, 'Julia', 'Dellinger', 'JDELLING', '650.509.3876', '2006-06-24'::DATE, 'SH_CLERK', 3400, NULL, 121, 50);
INSERT INTO employees VALUES (187, 'Anthony', 'Cabrio', 'ACABRIO', '650.509.4876', '2007-02-07'::DATE, 'SH_CLERK', 3000, NULL, 121, 50);

-- Shipping Clerks (reportan a Payam Kaufling - 122)
INSERT INTO employees VALUES (188, 'Kelly', 'Chung', 'KCHUNG', '650.505.1876', '2005-06-14'::DATE, 'SH_CLERK', 3800, NULL, 122, 50);
INSERT INTO employees VALUES (189, 'Jennifer', 'Dilly', 'JDILLY', '650.505.2876', '2005-08-13'::DATE, 'SH_CLERK', 3600, NULL, 122, 50);
INSERT INTO employees VALUES (190, 'Timothy', 'Gates', 'TGATES', '650.505.3876', '2006-07-11'::DATE, 'SH_CLERK', 2900, NULL, 122, 50);
INSERT INTO employees VALUES (191, 'Randall', 'Perkins', 'RPERKINS', '650.505.4876', '2007-12-19'::DATE, 'SH_CLERK', 2500, NULL, 122, 50);

-- Shipping Clerks (reportan a Shanta Vollman - 123)
INSERT INTO employees VALUES (192, 'Sarah', 'Bell', 'SBELL', '650.501.1876', '2004-02-04'::DATE, 'SH_CLERK', 4000, NULL, 123, 50);
INSERT INTO employees VALUES (193, 'Britney', 'Everett', 'BEVERETT', '650.501.2876', '2005-03-03'::DATE, 'SH_CLERK', 3900, NULL, 123, 50);
INSERT INTO employees VALUES (194, 'Samuel', 'McCain', 'SMCCAIN', '650.501.3876', '2006-07-01'::DATE, 'SH_CLERK', 3200, NULL, 123, 50);
INSERT INTO employees VALUES (195, 'Vance', 'Jones', 'VJONES', '650.501.4876', '2007-03-17'::DATE, 'SH_CLERK', 2800, NULL, 123, 50);

-- Shipping Clerks (reportan a Kevin Mourgos - 124)
INSERT INTO employees VALUES (196, 'Alana', 'Walsh', 'AWALSH', '650.507.9811', '2006-04-24'::DATE, 'SH_CLERK', 3100, NULL, 124, 50);
INSERT INTO employees VALUES (197, 'Kevin', 'Feeney', 'KFEENEY', '650.507.9822', '2006-05-23'::DATE, 'SH_CLERK', 3000, NULL, 124, 50);
INSERT INTO employees VALUES (198, 'Donald', 'OConnell', 'DOCONNEL', '650.507.9833', '2007-06-21'::DATE, 'SH_CLERK', 2600, NULL, 124, 50);
INSERT INTO employees VALUES (199, 'Douglas', 'Grant', 'DGRANT', '650.507.9844', '2008-01-13'::DATE, 'SH_CLERK', 2600, NULL, 124, 50);

-- Otros departamentos
INSERT INTO employees VALUES (200, 'Jennifer', 'Whalen', 'JWHALEN', '515.123.4444', '2003-09-17'::DATE, 'AD_ASST', 4400, NULL, 101, 10);
INSERT INTO employees VALUES (201, 'Michael', 'Hartstein', 'MHARTSTE', '515.123.5555', '2004-02-17'::DATE, 'MK_MAN', 13000, NULL, 100, 20);
INSERT INTO employees VALUES (202, 'Pat', 'Fay', 'PFAY', '603.123.6666', '2005-08-17'::DATE, 'MK_REP', 6000, NULL, 201, 20);
INSERT INTO employees VALUES (203, 'Susan', 'Mavris', 'SMAVRIS', '515.123.7777', '2002-06-07'::DATE, 'HR_REP', 6500, NULL, 101, 40);
INSERT INTO employees VALUES (204, 'Hermann', 'Baer', 'HBAER', '515.123.8888', '2002-06-07'::DATE, 'PR_REP', 10000, NULL, 101, 70);
INSERT INTO employees VALUES (205, 'Shelley', 'Higgins', 'SHIGGINS', '515.123.8080', '2002-06-07'::DATE, 'AC_MGR', 12008, NULL, 101, 110);
INSERT INTO employees VALUES (206, 'William', 'Gietz', 'WGIETZ', '515.123.8181', '2002-06-07'::DATE, 'AC_ACCOUNT', 8300, NULL, 205, 110);


-- =====================================================
-- ACTUALIZAR: DEPARTMENTS.MANAGER_ID
-- =====================================================
-- Propósito: Ahora que existen los empleados, asignar managers a departamentos
-- Esto resuelve la referencia circular departments ↔ employees
-- =====================================================

UPDATE departments SET manager_id = 200 WHERE department_id = 10;
UPDATE departments SET manager_id = 201 WHERE department_id = 20;
UPDATE departments SET manager_id = 114 WHERE department_id = 30;
UPDATE departments SET manager_id = 203 WHERE department_id = 40;
UPDATE departments SET manager_id = 121 WHERE department_id = 50;
UPDATE departments SET manager_id = 103 WHERE department_id = 60;
UPDATE departments SET manager_id = 204 WHERE department_id = 70;
UPDATE departments SET manager_id = 145 WHERE department_id = 80;
UPDATE departments SET manager_id = 100 WHERE department_id = 90;
UPDATE departments SET manager_id = 108 WHERE department_id = 100;
UPDATE departments SET manager_id = 205 WHERE department_id = 110;


-- =====================================================
-- AGREGAR FOREIGN KEY: DEPARTMENTS.MANAGER_ID
-- =====================================================
-- Propósito: Ahora que los datos están correctos, activar la constraint
-- =====================================================

ALTER TABLE departments
ADD CONSTRAINT dept_mgr_fk
FOREIGN KEY (manager_id) REFERENCES employees(employee_id);


-- =====================================================
-- INSERTAR DATOS: JOB_HISTORY (10 filas)
-- =====================================================
-- Propósito: Registrar cambios históricos de puestos/departamentos
-- =====================================================

INSERT INTO job_history VALUES (102, '2001-01-13'::DATE, '2006-07-24'::DATE, 'IT_PROG', 60);
INSERT INTO job_history VALUES (101, '1997-09-21'::DATE, '2001-10-27'::DATE, 'AC_ACCOUNT', 110);
INSERT INTO job_history VALUES (101, '2001-10-28'::DATE, '2005-03-15'::DATE, 'AC_MGR', 110);
INSERT INTO job_history VALUES (201, '2004-02-17'::DATE, '2007-12-19'::DATE, 'MK_REP', 20);
INSERT INTO job_history VALUES (114, '2006-03-24'::DATE, '2007-12-31'::DATE, 'ST_CLERK', 50);
INSERT INTO job_history VALUES (122, '2007-01-01'::DATE, '2007-12-31'::DATE, 'ST_CLERK', 50);
INSERT INTO job_history VALUES (200, '1995-09-17'::DATE, '2001-06-17'::DATE, 'AD_ASST', 90);
INSERT INTO job_history VALUES (176, '2006-03-24'::DATE, '2006-12-31'::DATE, 'SA_REP', 80);
INSERT INTO job_history VALUES (176, '2007-01-01'::DATE, '2007-12-31'::DATE, 'SA_MAN', 80);
INSERT INTO job_history VALUES (200, '2002-07-01'::DATE, '2006-12-31'::DATE, 'AC_ACCOUNT', 90);


-- =====================================================
-- VERIFICACIÓN FINAL COMPLETA
-- =====================================================

-- Resumen de TODOS los datos
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

-- Resultado esperado:
-- regions: 4
-- countries: 25
-- locations: 23
-- departments: 27
-- jobs: 19
-- employees: 107  ← ESTO ES LO IMPORTANTE
-- job_history: 10

COMMIT;
