-- ============================================
-- Script: 01_crear_usuario.sql
-- Descripción: Creación del usuario HR en PostgreSQL
-- Adaptado de: Usuario_HR-1.sql (Oracle)
-- Autor: Fernando Ramos Treviño
-- Fecha: 2025-12-31
-- ============================================

-- NOTA: Ejecutar comandos por separado en pgAdmin
-- Conectado a base de datos 'postgres'

-- 1. Crear el usuario HR
CREATE USER hr WITH PASSWORD 'HRmdyOnce31';

-- 2. Crear la base de datos HR
CREATE DATABASE hr_database
    WITH
    OWNER = hr
    ENCODING = 'UTF8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

-- 3. Conectarse a hr_database y ejecutar:
-- (Click derecho en hr_database → Query Tool)

GRANT ALL PRIVILEGES ON DATABASE hr_database TO hr;
GRANT ALL PRIVILEGES ON SCHEMA public TO hr;
ALTER SCHEMA public OWNER TO hr;

-- =====================================================
-- DIFERENCIAS ORACLE vs POSTGRESQL
-- =====================================================
-- Oracle: CREATE USER hr IDENTIFIED BY 'password'
-- PostgreSQL: CREATE USER hr WITH PASSWORD 'password'
--
-- Oracle: ALTER USER ... TABLESPACE
-- PostgreSQL: Configurado en CREATE DATABASE
--
-- Oracle: GRANT CREATE SESSION (requerido)
-- PostgreSQL: Implícito al crear usuario
--
-- Oracle: No hay concepto de DATABASE separado
-- PostgreSQL: DATABASE es obligatoria como contenedor
-- =====================================================
