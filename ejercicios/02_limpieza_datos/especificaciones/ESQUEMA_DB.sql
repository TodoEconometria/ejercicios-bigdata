-- =====================================================
-- ESQUEMA DE BASE DE DATOS - Quality of Government
-- =====================================================
--
-- Este es el esquema mínimo requerido para el proyecto.
-- Puedes extenderlo según tu análisis.
--
-- IMPORTANTE:
-- - NO cambies los nombres de las tablas principales
-- - Puedes agregar columnas adicionales
-- - Puedes crear tablas auxiliares
-- =====================================================

-- Eliminar si existe (para desarrollo)
DROP SCHEMA IF EXISTS qog CASCADE;
CREATE SCHEMA qog;

SET search_path TO qog;

-- =====================================================
-- TABLA: countries
-- Catálogo de países (dimension table)
-- =====================================================
CREATE TABLE countries (
    country_id SERIAL PRIMARY KEY,
    country_code VARCHAR(3) UNIQUE NOT NULL,      -- Código ISO3 (ej: ESP, USA, KAZ)
    country_name VARCHAR(100) NOT NULL,           -- Nombre completo
    region VARCHAR(50),                           -- Región geográfica
    subregion VARCHAR(50),                        -- Subregión
    income_group VARCHAR(50),                     -- Grupo ingreso (Banco Mundial)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_countries_code ON countries(country_code);
CREATE INDEX idx_countries_region ON countries(region);

COMMENT ON TABLE countries IS 'Catálogo de países con metadatos geográficos';

-- =====================================================
-- TABLA: qog_data
-- Datos QoG (fact table - estructura wide)
-- =====================================================
CREATE TABLE qog_data (
    id SERIAL PRIMARY KEY,
    country_code VARCHAR(3) NOT NULL REFERENCES countries(country_code),
    year INTEGER NOT NULL,

    -- Variables institucionales (tema común)
    vdem_polyarchy NUMERIC(5,4),                  -- Índice poliarquía V-Dem
    fh_pr INTEGER,                                -- Freedom House - Political Rights
    fh_cl INTEGER,                                -- Freedom House - Civil Liberties
    fh_status VARCHAR(20),                        -- Freedom House - Status
    polity2 INTEGER,                              -- Polity IV score

    ti_cpi NUMERIC(5,2),                          -- Transparency Int. - Corruption Index
    wbgi_cce NUMERIC(5,2),                        -- WB Governance - Control Corruption
    wbgi_rle NUMERIC(5,2),                        -- WB Governance - Rule of Law
    icrg_qog NUMERIC(5,2),                        -- ICRG - Quality of Government

    -- Variables económicas (control)
    wdi_gdppc NUMERIC(12,2),                      -- PIB per cápita (USD constantes)
    wdi_gdpgr NUMERIC(6,2),                       -- Crecimiento PIB (%)
    wdi_gini NUMERIC(5,2),                        -- Índice Gini
    undp_hdi NUMERIC(5,3),                        -- Índice Desarrollo Humano

    -- Variables sociodemográficas
    wdi_pop BIGINT,                               -- Población total
    wdi_lifexp NUMERIC(5,2),                      -- Esperanza de vida
    wdi_liter NUMERIC(5,2),                       -- Alfabetización adultos (%)

    -- Variables recursos naturales (tema 2)
    ross_oil_value NUMERIC(10,2),                 -- Valor petróleo per cápita
    ross_gas_value NUMERIC(10,2),                 -- Valor gas per cápita
    wdi_nrrent NUMERIC(6,2),                      -- Rentas recursos naturales (% PIB)
    wdi_ores NUMERIC(6,2),                        -- Exportaciones minerales (%)
    wdi_fuel NUMERIC(6,2),                        -- Exportaciones combustibles (%)

    wdi_agrvad NUMERIC(6,2),                      -- Agricultura (% PIB)
    wdi_agrland NUMERIC(6,2),                     -- Tierra agrícola (%)
    wdi_water NUMERIC(6,2),                       -- Acceso agua potable (%)
    wdi_sanit NUMERIC(6,2),                       -- Acceso saneamiento (%)

    -- Metadata
    data_source VARCHAR(50),                      -- Fuente (ej: qog_std_ts_jan23)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    -- Constraints
    UNIQUE(country_code, year),
    CHECK(year >= 1900 AND year <= 2030)
);

-- Índices para performance
CREATE INDEX idx_qog_country ON qog_data(country_code);
CREATE INDEX idx_qog_year ON qog_data(year);
CREATE INDEX idx_qog_country_year ON qog_data(country_code, year);

COMMENT ON TABLE qog_data IS 'Datos longitudinales QoG - estructura wide (cada fila = país-año)';

-- =====================================================
-- VISTA: panel_balanced
-- Vista con panel balanceado (solo países con datos completos)
-- =====================================================
CREATE VIEW panel_balanced AS
SELECT
    country_code,
    year,
    vdem_polyarchy,
    ti_cpi,
    wdi_gdppc,
    wdi_gini,
    undp_hdi
FROM qog_data
WHERE
    vdem_polyarchy IS NOT NULL
    AND ti_cpi IS NOT NULL
    AND wdi_gdppc IS NOT NULL
    AND year >= 2000  -- Desde 2000 para tener más datos completos
ORDER BY country_code, year;

COMMENT ON VIEW panel_balanced IS 'Panel balanceado para regresiones (sin valores nulos en variables clave)';

-- =====================================================
-- VISTA: tema1_instituciones
-- Vista específica Tema 1: Evolución Institucional
-- =====================================================
CREATE VIEW tema1_instituciones AS
SELECT
    c.country_name,
    c.region,
    d.year,
    d.vdem_polyarchy,
    d.fh_status,
    d.polity2,
    d.ti_cpi,
    d.wbgi_cce,
    d.wdi_gdppc,
    d.undp_hdi,

    -- Variable derivada: clasificación régimen
    CASE
        WHEN d.polity2 >= 6 THEN 'Democracia'
        WHEN d.polity2 >= -5 AND d.polity2 < 6 THEN 'Híbrido'
        WHEN d.polity2 < -5 THEN 'Autocracia'
        ELSE 'Sin datos'
    END AS regime_type,

    -- Deciles de desarrollo
    NTILE(10) OVER (PARTITION BY d.year ORDER BY d.wdi_gdppc) AS gdp_decile

FROM qog_data d
JOIN countries c ON d.country_code = c.country_code
WHERE d.year >= 1990  -- Post-guerra fría
ORDER BY c.country_name, d.year;

COMMENT ON VIEW tema1_instituciones IS 'Datos para análisis Tema 1: Instituciones y democracia';

-- =====================================================
-- VISTA: tema2_recursos
-- Vista específica Tema 2: Recursos Naturales
-- =====================================================
CREATE VIEW tema2_recursos AS
SELECT
    c.country_name,
    c.region,
    d.year,
    d.ross_oil_value,
    d.ross_gas_value,
    d.wdi_nrrent,
    d.wdi_agrvad,
    d.wdi_water,
    d.wdi_sanit,
    d.wdi_gdppc,
    d.wdi_gini,
    d.ti_cpi,

    -- Variable derivada: dependencia recursos
    CASE
        WHEN d.wdi_nrrent > 20 THEN 'Alta'
        WHEN d.wdi_nrrent > 10 THEN 'Media'
        WHEN d.wdi_nrrent > 0 THEN 'Baja'
        ELSE 'Sin datos'
    END AS resource_dependence,

    -- Índice compuesto: acceso servicios básicos
    (COALESCE(d.wdi_water, 0) + COALESCE(d.wdi_sanit, 0)) / 2.0 AS basic_services_index

FROM qog_data d
JOIN countries c ON d.country_code = c.country_code
WHERE d.year >= 1990
ORDER BY c.country_name, d.year;

COMMENT ON VIEW tema2_recursos IS 'Datos para análisis Tema 2: Recursos naturales y desarrollo';

-- =====================================================
-- TABLA: metadata_variables
-- Diccionario de variables (para documentación)
-- =====================================================
CREATE TABLE metadata_variables (
    variable_name VARCHAR(50) PRIMARY KEY,
    description TEXT NOT NULL,
    source VARCHAR(100),                          -- Ej: "World Bank - WDI"
    unit VARCHAR(50),                             -- Ej: "USD constantes 2017"
    min_value NUMERIC,
    max_value NUMERIC,
    interpretation TEXT                           -- Cómo interpretar (mayor = mejor?)
);

-- Insertar algunos ejemplos
INSERT INTO metadata_variables (variable_name, description, source, unit, min_value, max_value, interpretation) VALUES
('vdem_polyarchy', 'Índice de poliarquía V-Dem', 'Varieties of Democracy', '0-1', 0, 1, 'Mayor = más democrático'),
('ti_cpi', 'Índice de percepción de corrupción', 'Transparency International', '0-100', 0, 100, 'Mayor = menos corrupto'),
('wdi_gdppc', 'PIB per cápita', 'World Bank - WDI', 'USD constantes', NULL, NULL, 'Mayor = más rico'),
('polity2', 'Polity IV Score', 'Polity IV Project', '-10 a +10', -10, 10, 'Mayor = más democrático');

COMMENT ON TABLE metadata_variables IS 'Diccionario de variables QoG para documentación';

-- =====================================================
-- FUNCIONES ÚTILES
-- =====================================================

-- Función: Obtener países por región
CREATE OR REPLACE FUNCTION get_countries_by_region(p_region VARCHAR)
RETURNS TABLE(country_code VARCHAR, country_name VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT c.country_code, c.country_name
    FROM countries c
    WHERE c.region = p_region
    ORDER BY c.country_name;
END;
$$ LANGUAGE plpgsql;

-- Función: Contar datos disponibles por país
CREATE OR REPLACE FUNCTION count_data_availability(p_country_code VARCHAR)
RETURNS TABLE(year INTEGER, variables_available INTEGER) AS $$
BEGIN
    RETURN QUERY
    SELECT
        d.year,
        (
            CASE WHEN d.vdem_polyarchy IS NOT NULL THEN 1 ELSE 0 END +
            CASE WHEN d.ti_cpi IS NOT NULL THEN 1 ELSE 0 END +
            CASE WHEN d.wdi_gdppc IS NOT NULL THEN 1 ELSE 0 END +
            CASE WHEN d.wdi_gini IS NOT NULL THEN 1 ELSE 0 END
        )::INTEGER AS vars_available
    FROM qog_data d
    WHERE d.country_code = p_country_code
    ORDER BY d.year;
END;
$$ LANGUAGE plpgsql;

-- =====================================================
-- PERMISOS (ajustar según tu usuario PostgreSQL)
-- =====================================================
-- GRANT ALL PRIVILEGES ON SCHEMA qog TO tu_usuario;
-- GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA qog TO tu_usuario;
-- GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA qog TO tu_usuario;

-- =====================================================
-- NOTAS FINALES
-- =====================================================
/*
Este esquema es un PUNTO DE PARTIDA. Puedes:

1. Agregar más columnas a qog_data según tu análisis
2. Crear nuevas vistas para consultas específicas
3. Agregar tablas auxiliares (ej: regiones custom, clasificaciones)
4. Crear índices adicionales si notas lentitud
5. Agregar constraints de validación (ej: CHECK para rangos)

IMPORTANTE para datos de panel:
- La combinación (country_code, year) es tu unidad de análisis
- Asegúrate de que sea UNIQUE (ya está en el esquema)
- Para regresiones panel necesitas datos balanceados (usa la vista panel_balanced)

FORMATO DE PANEL DATA:
+---------------+------+----------+--------+
| country_code  | year | gdp_pc   | ti_cpi |
+---------------+------+----------+--------+
| ESP           | 2020 | 30000    | 62     |
| ESP           | 2021 | 31000    | 61     |
| USA           | 2020 | 65000    | 67     |
| USA           | 2021 | 66000    | 67     |
+---------------+------+----------+--------+

Esto es PERFECTO para:
- Fixed Effects models
- Random Effects models
- Difference-in-Differences
- Event Study designs
*/
