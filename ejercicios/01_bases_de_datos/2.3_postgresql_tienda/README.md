# Ejercicio 2.3: Migración SQLite → PostgreSQL

> **Estado:** En construcción

---

## Descripción

Este ejercicio consiste en **migrar** la base de datos de tienda informática desde SQLite a PostgreSQL.

Usarás las bases de datos que creaste en el Ejercicio 1.1 (Modelos A, B y C) y las migrarás a PostgreSQL.

---

## Objetivos

- Comprender diferencias entre SQLite y PostgreSQL
- Migrar esquemas y datos entre motores
- Adaptar tipos de datos y constraints
- Comparar rendimiento entre ambos motores

---

## Contenido del Ejercicio

### Scripts

- `migracion_desde_sqlite.py` - Script de migración automática
- `comparativa_sqlite_vs_postgres.md` - Análisis comparativo

### Datos Origen

Tus bases de datos del Ejercicio 1.1:
- `tienda_modelo_a.db`
- `tienda_modelo_b.db`
- `tienda_modelo_c.db`

---

## Requisitos

- Haber completado Ejercicio 1.1
- PostgreSQL 14+ instalado
- Python con `psycopg2` y `sqlite3`

---

## Entregas

Consulta las [instrucciones de entrega](../../../entregas/2.3_postgresql_tienda/README.md)

---

## Recursos

- [Migración SQLite → PostgreSQL](https://pgloader.io/)
- [Comparativa de tipos de datos](https://www.postgresql.org/docs/current/datatype.html)

---

**Creado:** 2025-12-17
**Estado:** En construcción - Se completará en clase
