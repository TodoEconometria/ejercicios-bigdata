-- ============================================
-- Script: 02_crear_schema_parte1.sql
-- Descripción: Creación de tablas básicas (regions, countries, locations)
-- Adaptado de: Modelo_HR-1.sql (Oracle)
-- Autor: Fernando Ramos Treviño
-- Fecha: 2025-12-31
-- ============================================

-- EJECUTAR EN: hr_database
-- CONECTADO COMO: hr o postgres

-- =====================================================
-- TABLA: REGIONS (Regiones geográficas)
-- =====================================================
-- Propósito: Almacena las grandes regiones del mundo (Europa, Asia, etc.)
-- Esta tabla no tiene dependencias, por eso se crea primero
-- =====================================================

CREATE TABLE regions (
    -- ID único de la región (1, 2, 3, 4...)
    -- INTEGER porque son números enteros pequeños
    -- NOT NULL asegura que siempre tenga valor
    region_id   INTEGER NOT NULL,

    -- Nombre de la región (ej: "Europe", "Americas")
    -- VARCHAR(25) permite texto variable hasta 25 caracteres
    region_name VARCHAR(25),

    -- PRIMARY KEY: Identifica de forma única cada fila
    -- PostgreSQL crea automáticamente un índice para optimizar búsquedas
    CONSTRAINT reg_id_pk PRIMARY KEY (region_id)
);

-- COMMENT ON: Documenta el propósito de la tabla y columnas
-- Útil para que otros desarrolladores entiendan el modelo
COMMENT ON TABLE regions IS
'Regions table that contains region numbers and names. Contains 4 rows; references with the Countries table.';

COMMENT ON COLUMN regions.region_id IS 'Primary key of regions table.';
COMMENT ON COLUMN regions.region_name IS 'Names of regions. Locations are in the countries of these regions.';


-- =====================================================
-- TABLA: COUNTRIES (Países)
-- =====================================================
-- Propósito: Almacena países del mundo
-- Depende de REGIONS porque cada país pertenece a una región
-- =====================================================

CREATE TABLE countries (
    -- ID del país: código ISO de 2 letras (ej: "US", "FR", "ES")
    -- CHAR(2) porque SIEMPRE son exactamente 2 caracteres
    -- NOT NULL porque es obligatorio
    country_id   CHAR(2) NOT NULL,

    -- Nombre completo del país (ej: "United States of America")
    -- VARCHAR(40) permite hasta 40 caracteres
    country_name VARCHAR(40),

    -- ID de la región a la que pertenece este país
    -- INTEGER para coincidir con regions.region_id
    -- Puede ser NULL si no se conoce la región
    region_id    INTEGER,

    -- PRIMARY KEY: country_id identifica de forma única cada país
    CONSTRAINT country_c_id_pk PRIMARY KEY (country_id),

    -- FOREIGN KEY: Establece relación con tabla regions
    -- Garantiza que region_id exista en la tabla regions
    -- Si intentas poner region_id=99 y no existe, dará error
    CONSTRAINT countr_reg_fk FOREIGN KEY (region_id)
        REFERENCES regions(region_id)
);

COMMENT ON TABLE countries IS
'Country table. Contains 25 rows. References with locations table.';

COMMENT ON COLUMN countries.country_id IS 'Primary key of countries table.';
COMMENT ON COLUMN countries.country_name IS 'Country name';
COMMENT ON COLUMN countries.region_id IS 'Region ID for the country. Foreign key to region_id column in the regions table.';


-- =====================================================
-- TABLA: LOCATIONS (Ubicaciones físicas)
-- =====================================================
-- Propósito: Almacena direcciones de oficinas de la empresa
-- Depende de COUNTRIES porque cada ubicación está en un país
-- =====================================================

CREATE TABLE locations (
    -- ID único de la ubicación
    -- INTEGER para números enteros
    location_id    INTEGER NOT NULL,

    -- Dirección de la calle (ej: "2004 Charade Rd")
    street_address VARCHAR(40),

    -- Código postal (ej: "98199", "28820")
    postal_code    VARCHAR(12),

    -- Ciudad (ej: "Seattle", "Madrid")
    -- NOT NULL porque la ciudad es obligatoria
    city           VARCHAR(30) NOT NULL,

    -- Estado o provincia (ej: "Washington", "Comunidad de Madrid")
    -- Puede ser NULL en países sin estados
    state_province VARCHAR(25),

    -- Código del país donde está esta ubicación
    -- CHAR(2) para coincidir con countries.country_id
    country_id     CHAR(2),

    -- PRIMARY KEY: location_id identifica cada ubicación
    CONSTRAINT loc_id_pk PRIMARY KEY (location_id),

    -- FOREIGN KEY: Relación con tabla countries
    -- Asegura que country_id exista en la tabla countries
    CONSTRAINT loc_c_id_fk FOREIGN KEY (country_id)
        REFERENCES countries(country_id)
);

-- =====================================================
-- SECUENCIA para generar IDs automáticos de locations
-- =====================================================
-- Propósito: Genera números consecutivos para location_id
-- Útil cuando insertas nuevas ubicaciones sin especificar ID manual
-- =====================================================

CREATE SEQUENCE locations_seq
    START WITH 3300        -- Comienza en 3300 (los datos existentes van hasta ahí)
    INCREMENT BY 100       -- Cada nuevo ID suma 100 (3300, 3400, 3500...)
    MAXVALUE 9900          -- No puede superar 9900
    CACHE 1                -- Cache mínimo (equivalente a NO CACHE en Oracle)
    NO CYCLE;              -- Cuando llegue a 9900, da error (no vuelve a 3300)

-- Ejemplo de uso de la secuencia:
-- INSERT INTO locations (location_id, city, country_id)
-- VALUES (nextval('locations_seq'), 'Madrid', 'ES');

COMMENT ON TABLE locations IS
'Locations table that contains specific address of a specific office, warehouse, and/or production site of a company.';

COMMENT ON COLUMN locations.location_id IS 'Primary key of locations table';
COMMENT ON COLUMN locations.street_address IS 'Street address of an office, warehouse, or production site of a company.';
COMMENT ON COLUMN locations.postal_code IS 'Postal code of the location of an office, warehouse, or production site of a company.';
COMMENT ON COLUMN locations.city IS 'City where an office, warehouse, or production site of a company is located.';
COMMENT ON COLUMN locations.state_province IS 'State or Province where an office, warehouse, or production site of a company is located.';
COMMENT ON COLUMN locations.country_id IS 'Country where an office, warehouse, or production site of a company is located.';


-- =====================================================
-- ÍNDICES para optimizar consultas
-- =====================================================
-- Propósito: Acelerar búsquedas por columnas específicas
-- PostgreSQL ya crea índices automáticos para PRIMARY KEY
-- Estos son adicionales para columnas que se buscan frecuentemente
-- =====================================================

-- Índice para buscar ubicaciones por ciudad
-- Útil para consultas como: SELECT * FROM locations WHERE city = 'Seattle';
CREATE INDEX loc_city_ix ON locations (city);

-- Índice para buscar por estado/provincia
CREATE INDEX loc_state_province_ix ON locations (state_province);

-- Índice para buscar ubicaciones por país
-- Útil para JOINs: SELECT * FROM locations l JOIN countries c ON l.country_id = c.country_id;
CREATE INDEX loc_country_ix ON locations (country_id);

-- =====================================================
-- DIFERENCIAS CLAVE: ORACLE vs POSTGRESQL
-- =====================================================
--
-- 1. TIPOS DE DATOS:
--    Oracle: NUMBER          → PostgreSQL: INTEGER (para enteros)
--    Oracle: NUMBER(4)       → PostgreSQL: INTEGER (maneja rangos automáticamente)
--    Oracle: VARCHAR2(25)    → PostgreSQL: VARCHAR(25)
--
-- 2. PRIMARY KEY:
--    Oracle: Requiere CREATE UNIQUE INDEX + ALTER TABLE ADD CONSTRAINT
--    PostgreSQL: CONSTRAINT ... PRIMARY KEY crea el índice automáticamente
--
-- 3. ORGANIZATION INDEX:
--    Oracle: ORGANIZATION INDEX (tabla organizada por índice)
--    PostgreSQL: No existe este concepto (eliminado)
--
-- 4. SECUENCIAS:
--    Oracle: NOCACHE (sin espacio)
--    PostgreSQL: NO CACHE (con espacio)
--
-- 5. COMENTARIOS:
--    Ambos usan COMMENT ON TABLE/COLUMN (igual sintaxis)
--
-- =====================================================
