-- ============================================
-- Script: 03_crear_schema_parte2.sql
-- Descripción: Creación de tablas avanzadas (jobs, departments, employees, job_history)
-- Adaptado de: Modelo_HR-1.sql (Oracle)
-- Autor: Fernando Ramos Treviño
-- Fecha: 2025-12-31
-- ============================================

-- EJECUTAR EN: hr_database
-- CONECTADO COMO: hr o postgres

-- =====================================================
-- TABLA: JOBS (Puestos de trabajo)
-- =====================================================
-- Propósito: Define los puestos disponibles en la empresa con rangos salariales
-- No tiene dependencias, se puede crear independientemente
-- =====================================================

CREATE TABLE jobs (
    -- ID del puesto (ej: "IT_PROG", "SA_MAN", "AD_PRES")
    -- VARCHAR(10) porque son códigos alfanuméricos cortos
    job_id     VARCHAR(10) NOT NULL,

    -- Título del puesto (ej: "Programmer", "Sales Manager")
    -- NOT NULL porque todo puesto debe tener un nombre
    job_title  VARCHAR(35) NOT NULL,

    -- Salario mínimo para este puesto
    -- NUMERIC(6) permite números hasta 999999 sin decimales
    min_salary NUMERIC(6),

    -- Salario máximo para este puesto
    -- NUMERIC(6) permite números hasta 999999 sin decimales
    max_salary NUMERIC(6),

    -- PRIMARY KEY: job_id identifica cada puesto de forma única
    CONSTRAINT job_id_pk PRIMARY KEY (job_id)
);

COMMENT ON TABLE jobs IS
'Jobs table with job titles and salary ranges. Contains 19 rows. References with employees and job_history table.';

COMMENT ON COLUMN jobs.job_id IS 'Primary key of jobs table.';
COMMENT ON COLUMN jobs.job_title IS 'A not null column that shows job title, e.g. AD_VP, FI_ACCOUNTANT';
COMMENT ON COLUMN jobs.min_salary IS 'Minimum salary for a job title.';
COMMENT ON COLUMN jobs.max_salary IS 'Maximum salary for a job title';


-- =====================================================
-- TABLA: DEPARTMENTS (Departamentos)
-- =====================================================
-- Propósito: Define los departamentos de la empresa
-- Tiene referencia circular con EMPLOYEES (se resuelve después)
-- =====================================================

CREATE TABLE departments (
    -- ID único del departamento
    -- INTEGER para números enteros
    department_id   INTEGER NOT NULL,

    -- Nombre del departamento (ej: "IT", "Sales", "Finance")
    -- NOT NULL porque todo departamento debe tener nombre
    department_name VARCHAR(30) NOT NULL,

    -- ID del empleado que es manager del departamento
    -- INTEGER para coincidir con employees.employee_id
    -- Puede ser NULL si el departamento no tiene manager asignado aún
    -- NOTA: Esta FK se añadirá DESPUÉS de crear la tabla employees
    manager_id      INTEGER,

    -- ID de la ubicación física del departamento
    -- INTEGER para coincidir con locations.location_id
    location_id     INTEGER,

    -- PRIMARY KEY: department_id identifica cada departamento
    CONSTRAINT dept_id_pk PRIMARY KEY (department_id),

    -- FOREIGN KEY: Relaciona con la ubicación del departamento
    CONSTRAINT dept_loc_fk FOREIGN KEY (location_id)
        REFERENCES locations(location_id)
);

-- Secuencia para generar nuevos department_id automáticamente
CREATE SEQUENCE departments_seq
    START WITH 280         -- Comienza en 280 (los datos existentes van hasta ahí)
    INCREMENT BY 10        -- Cada nuevo ID suma 10 (280, 290, 300...)
    MAXVALUE 9990          -- No puede superar 9990
    CACHE 1                -- Cache mínimo
    NO CYCLE;              -- Cuando llegue al máximo, da error

COMMENT ON TABLE departments IS
'Departments table that shows details of departments where employees work. Contains 27 rows; references with locations, employees, and job_history tables.';

COMMENT ON COLUMN departments.department_id IS 'Primary key column of departments table.';
COMMENT ON COLUMN departments.department_name IS 'A not null column that shows name of a department. Administration, Marketing, Purchasing, Human Resources, Shipping, IT, Executive, Public Relations, Sales, Finance, and Accounting.';
COMMENT ON COLUMN departments.manager_id IS 'Manager_id of a department. Foreign key to employee_id column of employees table. The manager_id column of the employee table references this column.';
COMMENT ON COLUMN departments.location_id IS 'Location id where a department is located. Foreign key to location_id column of locations table.';


-- =====================================================
-- TABLA: EMPLOYEES (Empleados)
-- =====================================================
-- Propósito: Almacena información de todos los empleados
-- Tabla central del modelo, con múltiples relaciones
-- Tiene auto-referencia (manager_id apunta a otro empleado)
-- =====================================================

CREATE TABLE employees (
    -- ID único del empleado
    -- INTEGER para números enteros
    employee_id    INTEGER NOT NULL,

    -- Nombre del empleado
    -- VARCHAR(20) permite hasta 20 caracteres
    first_name     VARCHAR(20),

    -- Apellido del empleado
    -- NOT NULL porque es obligatorio
    last_name      VARCHAR(25) NOT NULL,

    -- Email corporativo del empleado
    -- NOT NULL porque todos necesitan email
    email          VARCHAR(25) NOT NULL,

    -- Número de teléfono (incluye código de país y área)
    -- Ejemplo: "515.123.4567", "011.44.1344.429268"
    phone_number   VARCHAR(20),

    -- Fecha de contratación
    -- DATE almacena fecha sin hora
    -- NOT NULL porque todos tienen fecha de inicio
    hire_date      DATE NOT NULL,

    -- ID del puesto actual del empleado
    -- VARCHAR(10) para coincidir con jobs.job_id
    -- NOT NULL porque todo empleado debe tener un puesto
    job_id         VARCHAR(10) NOT NULL,

    -- Salario mensual del empleado
    -- NUMERIC(8,2) permite hasta 999999.99 (8 dígitos, 2 decimales)
    -- Ejemplo: 24000.00, 17000.50
    salary         NUMERIC(8,2),

    -- Porcentaje de comisión (solo para ventas)
    -- NUMERIC(2,2) permite valores como 0.25 (25%), 0.30 (30%)
    -- CAMBIO: Oracle usa NUMBER(2,2) pero PostgreSQL necesita (3,2) para 0.xx
    commission_pct NUMERIC(3,2),

    -- ID del manager de este empleado
    -- INTEGER que apunta a otro employee_id
    -- AUTO-REFERENCIA: Un empleado tiene como manager a otro empleado
    -- Puede ser NULL si es el CEO (no tiene manager)
    manager_id     INTEGER,

    -- ID del departamento donde trabaja
    -- INTEGER para coincidir con departments.department_id
    department_id  INTEGER,

    -- PRIMARY KEY: employee_id identifica cada empleado
    CONSTRAINT emp_emp_id_pk PRIMARY KEY (employee_id),

    -- UNIQUE: El email debe ser único (no pueden dos empleados tener el mismo)
    CONSTRAINT emp_email_uk UNIQUE (email),

    -- CHECK: El salario debe ser mayor que 0
    CONSTRAINT emp_salary_min CHECK (salary > 0),

    -- FOREIGN KEY: Relaciona con la tabla jobs
    CONSTRAINT emp_job_fk FOREIGN KEY (job_id)
        REFERENCES jobs(job_id),

    -- FOREIGN KEY: Relaciona con departments
    -- NOTA: La FK de departments.manager_id se añadirá después de insertar datos
    CONSTRAINT emp_dept_fk FOREIGN KEY (department_id)
        REFERENCES departments(department_id),

    -- FOREIGN KEY: Auto-referencia a la misma tabla employees
    -- manager_id apunta a otro employee_id
    CONSTRAINT emp_manager_fk FOREIGN KEY (manager_id)
        REFERENCES employees(employee_id)
);

-- Secuencia para generar nuevos employee_id automáticamente
CREATE SEQUENCE employees_seq
    START WITH 207         -- Comienza en 207 (los datos existentes van hasta 206)
    INCREMENT BY 1         -- Cada nuevo ID suma 1 (207, 208, 209...)
    CACHE 1                -- Cache mínimo
    NO CYCLE;              -- Cuando llegue al máximo, da error

COMMENT ON TABLE employees IS
'Employees table. Contains 107 rows. References with departments, jobs, job_history tables. Contains a self reference.';

COMMENT ON COLUMN employees.employee_id IS 'Primary key of employees table.';
COMMENT ON COLUMN employees.first_name IS 'First name of the employee. A not null column.';
COMMENT ON COLUMN employees.last_name IS 'Last name of the employee. A not null column.';
COMMENT ON COLUMN employees.email IS 'Email id of the employee';
COMMENT ON COLUMN employees.phone_number IS 'Phone number of the employee; includes country code and area code';
COMMENT ON COLUMN employees.hire_date IS 'Date when the employee started on this job. A not null column.';
COMMENT ON COLUMN employees.job_id IS 'Current job of the employee; foreign key to job_id column of the jobs table. A not null column.';
COMMENT ON COLUMN employees.salary IS 'Monthly salary of the employee. Must be greater than zero (enforced by constraint emp_salary_min)';
COMMENT ON COLUMN employees.commission_pct IS 'Commission percentage of the employee; Only employees in sales department elgible for commission percentage';
COMMENT ON COLUMN employees.manager_id IS 'Manager id of the employee; has same domain as manager_id in departments table. Foreign key to employee_id column of employees table. (useful for reflexive joins and CONNECT BY query)';
COMMENT ON COLUMN employees.department_id IS 'Department id where employee works; foreign key to department_id column of the departments table';


-- =====================================================
-- TABLA: JOB_HISTORY (Historial laboral)
-- =====================================================
-- Propósito: Registra cambios de puesto/departamento de empleados
-- Tiene CLAVE PRIMARIA COMPUESTA (employee_id + start_date)
-- =====================================================

CREATE TABLE job_history (
    -- ID del empleado
    -- INTEGER para coincidir con employees.employee_id
    -- NOT NULL porque es parte de la clave primaria
    employee_id   INTEGER NOT NULL,

    -- Fecha de inicio en este puesto/departamento
    -- DATE para almacenar la fecha
    -- NOT NULL porque es parte de la clave primaria
    start_date    DATE NOT NULL,

    -- Fecha de finalización en este puesto/departamento
    -- NOT NULL porque siempre debe tener fecha de fin
    end_date      DATE NOT NULL,

    -- ID del puesto que tuvo el empleado en este período
    -- VARCHAR(10) para coincidir con jobs.job_id
    -- NOT NULL porque debe registrar qué puesto tuvo
    job_id        VARCHAR(10) NOT NULL,

    -- ID del departamento donde trabajó en este período
    -- INTEGER para coincidir con departments.department_id
    department_id INTEGER,

    -- PRIMARY KEY COMPUESTA: La combinación de employee_id + start_date
    -- identifica de forma única cada registro histórico
    -- Un empleado puede tener múltiples registros, pero no dos con la misma fecha de inicio
    CONSTRAINT jhist_emp_id_st_date_pk PRIMARY KEY (employee_id, start_date),

    -- CHECK: La fecha de fin debe ser mayor que la fecha de inicio
    -- Evita registros inválidos donde end_date < start_date
    CONSTRAINT jhist_date_interval CHECK (end_date > start_date),

    -- FOREIGN KEY: Relaciona con employees
    CONSTRAINT jhist_emp_fk FOREIGN KEY (employee_id)
        REFERENCES employees(employee_id),

    -- FOREIGN KEY: Relaciona con jobs
    CONSTRAINT jhist_job_fk FOREIGN KEY (job_id)
        REFERENCES jobs(job_id),

    -- FOREIGN KEY: Relaciona con departments
    CONSTRAINT jhist_dept_fk FOREIGN KEY (department_id)
        REFERENCES departments(department_id)
);

COMMENT ON TABLE job_history IS
'Table that stores job history of the employees. If an employee changes departments within the job or changes jobs within the department, new rows get inserted into this table with old job information of the employee. Contains a complex primary key employee_id+start_date. Contains 25 rows. References with jobs, employees, and departments tables.';

COMMENT ON COLUMN job_history.employee_id IS 'A not null column in the complex primary key employee_id+start_date. Foreign key to employee_id column of the employee table';
COMMENT ON COLUMN job_history.start_date IS 'A not null column in the complex primary key employee_id+start_date. Must be less than the end_date of the job_history table. (enforced by constraint jhist_date_interval)';
COMMENT ON COLUMN job_history.end_date IS 'Last day of the employee in this job role. A not null column. Must be greater than the start_date of the job_history table. (enforced by constraint jhist_date_interval)';
COMMENT ON COLUMN job_history.job_id IS 'Job role in which the employee worked in the past; foreign key to job_id column in the jobs table. A not null column.';
COMMENT ON COLUMN job_history.department_id IS 'Department id in which the employee worked in the past; foreign key to deparment_id column in the departments table';


-- =====================================================
-- ÍNDICES para optimizar consultas
-- =====================================================
-- Propósito: Acelerar búsquedas frecuentes y JOINs
-- =====================================================

-- Índices en EMPLOYEES
CREATE INDEX emp_department_ix ON employees(department_id);
CREATE INDEX emp_job_ix ON employees(job_id);
CREATE INDEX emp_manager_ix ON employees(manager_id);
CREATE INDEX emp_name_ix ON employees(last_name, first_name);

-- Índices en DEPARTMENTS
CREATE INDEX dept_location_ix ON departments(location_id);

-- Índices en JOB_HISTORY
CREATE INDEX jhist_job_ix ON job_history(job_id);
CREATE INDEX jhist_employee_ix ON job_history(employee_id);
CREATE INDEX jhist_department_ix ON job_history(department_id);


-- =====================================================
-- DIFERENCIAS CLAVE: ORACLE vs POSTGRESQL
-- =====================================================
--
-- 1. TIPOS NUMÉRICOS:
--    Oracle: NUMBER(6)       → PostgreSQL: NUMERIC(6) o INTEGER
--    Oracle: NUMBER(8,2)     → PostgreSQL: NUMERIC(8,2)
--    Oracle: NUMBER(2,2)     → PostgreSQL: NUMERIC(3,2) ⚠️ IMPORTANTE
--                               (Oracle permite 0.99, PostgreSQL necesita 3 dígitos)
--
-- 2. SECUENCIAS:
--    Sintaxis muy similar, cambio principal: NOCACHE → CACHE 1
--
-- 3. REFERENCIAS CIRCULARES:
--    Mismo problema en ambos: departments ↔ employees
--    Solución: Crear FK dept_mgr_fk DESPUÉS de insertar datos
--
-- 4. AUTO-REFERENCIA:
--    Ambos soportan FOREIGN KEY a la misma tabla (manager_id → employee_id)
--
-- 5. CLAVE PRIMARIA COMPUESTA:
--    Sintaxis idéntica: PRIMARY KEY (employee_id, start_date)
--
-- 6. CONSTRAINTS CHECK:
--    Sintaxis idéntica en ambos
--
-- =====================================================
