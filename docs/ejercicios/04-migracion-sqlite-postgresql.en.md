# Exercise 2.3: SQLite to PostgreSQL Migration﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​‌‌​‍​​‌‌​‌‌‌‍​‌‌​​​‌​‍​​‌‌​​‌​‍​‌‌​​​‌​‍​​‌‌​‌​​‍​​‌‌​​‌‌‍​​‌‌​​​‌﻿

> **Status:** Available

---

## General Description

You will learn to **migrate databases** from SQLite to PostgreSQL, understanding the differences between both engines.﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​‌‌​‍​​‌‌​‌‌‌‍​‌‌​​​‌​‍​​‌‌​​‌​‍​‌‌​​​‌​‍​​‌‌​‌​​‍​​‌‌​​‌‌‍​​‌‌​​​‌﻿

**Estimated duration:** 3-4 hours
**Level:** Intermediate-Advanced
**Prerequisites:** Exercise 1.1 (SQLite), Exercise 2.1 (PostgreSQL)

---

## Learning Objectives

Upon completing this exercise you will be able to:

- ✅ Identify differences between SQLite and PostgreSQL
- ✅ Adapt data types between engines
- ✅ Migrate schemas (DDL)
- ✅ Migrate data (DML)
- ✅ Write migration scripts in Python
- ✅ Validate integrity after migration
- ✅ Compare performance between engines

---

## Exercise Context

You will use the databases you created in **Exercise 1.1** (computer store):

- `tienda_modelo_a.db` - 26 independent tables
- `tienda_modelo_b.db` - Normalized model
- `tienda_modelo_c.db` - Complete e-commerce

**Goal:** Migrate them to PostgreSQL and compare.

---

## Key Differences

### Data Types

| SQLite | PostgreSQL |
|--------|------------|
| `INTEGER` | `INTEGER` or `BIGINT` |
| `REAL` | `NUMERIC(p,s)` or `DOUBLE PRECISION` |
| `TEXT` | `VARCHAR(n)` or `TEXT` |
| `BLOB` | `BYTEA` |
| No type | PostgreSQL is strict |

### Auto-increment

| SQLite | PostgreSQL |
|--------|------------|
| `AUTOINCREMENT` | `SERIAL` or `IDENTITY` |

### Constraints

PostgreSQL has stricter constraints and supports more types.

### Performance

PostgreSQL is much faster with large volumes and complex queries.

---

## Exercise Content

The complete exercise is located at:

```
ejercicios/01_bases_de_datos/2.3_postgresql_tienda/
```

### Files

- `migracion_desde_sqlite.py` - Migration script (template)
- `comparativa_sqlite_vs_postgres.md` - Comparative analysis

---

## Migration Process

### 1. Source Schema Analysis

```python
# Conectar a SQLite
import sqlite3
conn = sqlite3.connect('tienda_modelo_b.db')

# Obtener lista de tablas
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
```

### 2. Data Type Adaptation

Convert SQLite types to PostgreSQL:
- Dynamically detect types
- Map to equivalent PostgreSQL types
- Adjust NUMERIC precision

### 3. Schema Recreation

Generate DDL for PostgreSQL:
- CREATE TABLE with adapted types
- PRIMARY KEY
- FOREIGN KEY
- CONSTRAINTS

### 4. Data Migration

```python
# Leer datos de SQLite
df = pd.read_sql("SELECT * FROM productos", sqlite_conn)

# Insertar en PostgreSQL
df.to_sql('productos', postgres_engine, if_exists='append')
```

### 5. Validation

- Verify row counts: SQLite vs PostgreSQL
- Validate referential integrity
- Test complex queries

---

## Tasks to Complete

### Part 1: Migration Script

Create `migracion_desde_sqlite.py` that:

1. Reads the SQLite schema
2. Generates DDL for PostgreSQL
3. Migrates data table by table
4. Validates the migration
5. Generates a success/error report

### Part 2: Comparative Analysis

Create `comparativa_sqlite_vs_postgres.md` with:

1. **Schema Differences**
   - Modified data types
   - Added constraints
   - Created indexes

2. **Performance Tests**
   - Same query on both engines
   - Execution times
   - Memory usage

3. **Conclusions**
   - When to use SQLite?
   - When to use PostgreSQL?
   - Recommendations

---

## Technical Requirements

### Software

- SQLite (already installed)
- PostgreSQL 14+
- Python with:
  ```bash
  pip install pandas psycopg2-binary sqlite3
  ```

### Source Data

Your databases from Exercise 1.1:
- `tienda_modelo_a.db`
- `tienda_modelo_b.db`
- `tienda_modelo_c.db`

---

## Submissions

Check the [submission instructions](../../entregas/01_bases_de_datos/) to find out which files you need to upload.

**Submission folder:**
```
entregas/01_bases_de_datos/tu_apellido_nombre/2.3_postgresql_tienda/
├── migracion_desde_sqlite.py
├── comparativa_sqlite_vs_postgres.md
└── capturas/
    ├── sqlite_query.png
    └── postgres_query.png
```

---

## Support Resources

### Migration Tools

- [pgloader](https://pgloader.io/) - Automatic migration
- [SQLite to PostgreSQL Converter](https://github.com/caiiiycuk/sqlite-to-postgres)

### Documentation

- [PostgreSQL Data Types](https://www.postgresql.org/docs/current/datatype.html)
- [Database Migration](https://www.postgresql.org/docs/current/migration.html)

### Tutorials

- [SQLite vs PostgreSQL Comparison](https://www.sqlite.org/whentouse.html)
- [Psycopg2 Tutorial](https://www.psycopg.org/docs/)

---

## Next Steps

After completing this exercise:

1. **Exercise 3.1** - Oracle with HR Database
2. **Exercise 4.1** - SQL Server with Store

﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​‌‌​‍​​‌‌​‌‌‌‍​‌‌​​​‌​‍​​‌‌​​‌​‍​‌‌​​​‌​‍​​‌‌​‌​​‍​​‌‌​​‌‌‍​​‌‌​​​‌﻿---

**Publication date:** To be defined
**Last updated:** 2025-12-17
