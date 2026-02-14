# Exercise 3.1: Oracle with HR Database﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌​‌‌‌‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​‌​​‍​​‌‌​‌‌‌‍​​‌‌​​​‌‍​​‌‌​​‌​‍​‌‌​​​​‌﻿

> **Status:** Available

---

## General Description

You will work with **Oracle Database** using the HR database in its original native environment.﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌​‌‌‌‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​‌​​‍​​‌‌​‌‌‌‍​​‌‌​​​‌‍​​‌‌​​‌​‍​‌‌​​​​‌﻿

**Estimated duration:** 5-7 hours
**Level:** Advanced
**Prerequisites:** Exercise 2.1 (PostgreSQL HR)

---

## Learning Objectives

Upon completing this exercise you will be able to:

- ✅ Install and configure Oracle Database Express Edition (XE)
- ✅ Use SQL Developer or SQL*Plus
- ✅ Work with Oracle-specific syntax
- ✅ Create sequences and triggers
- ✅ Write stored procedures in PL/SQL
- ✅ Compare Oracle with PostgreSQL
- ✅ Understand Oracle enterprise features

---

## Oracle Database

Oracle is the leading relational database engine in the enterprise market.

**Features:**
- PL/SQL (procedural language)
- Advanced partitioning
- Replication and high availability
- Enterprise security
- Very powerful query optimizer

---

## Differences: Oracle vs PostgreSQL

### Syntax

| Aspect | Oracle | PostgreSQL |
|---------|--------|------------|
| Auto-increment | SEQUENCE | SERIAL |
| String concat | `\|\|` or `CONCAT()` | `\|\|` |
| VARCHAR types | `VARCHAR2` | `VARCHAR` |
| LIMIT | `ROWNUM` or `FETCH FIRST` | `LIMIT` |
| Outer Join | `(+)` (legacy) | `LEFT/RIGHT JOIN` |

### Functionality

- **PL/SQL vs PL/pgSQL**: Oracle has a more mature PL/SQL
- **Packages**: Oracle supports packages (grouping of procedures)
- **Triggers**: Different syntax
- **Performance**: Oracle optimized for enterprise workloads

---

## Exercise Content

The complete exercise is located at:

```
ejercicios/01_bases_de_datos/3.1_oracle_hr/
```

### Data

Original Oracle SQL scripts are in: `datos/oracle_hr/`

---

## Topics Covered

### 1. Installation and Configuration
- Install Oracle XE 21c
- Configure listener
- Create users and permissions
- Connect with SQL Developer

### 2. Oracle Syntax
- Specific data types
- Oracle built-in functions
- ROWNUM and pagination
- Optimizer hints

### 3. Basic PL/SQL
- Anonymous blocks
- Variables and types
- Control structures
- Exception handling

### 4. Database Objects
- Sequences
- Triggers
- Views
- Synonyms

### 5. Procedures and Functions
- Create stored procedures
- IN/OUT/IN OUT parameters
- Functions that return values

---

## Technical Requirements

### Required Software

1. **Oracle Database 21c Express Edition (XE)** - Free
   - [Download Oracle XE](https://www.oracle.com/database/technologies/xe-downloads.html)
   - Requires an Oracle account (free)
   - XE limitations: 12GB RAM, 2 CPUs, 12GB user data

2. **SQL Developer** - Official Oracle graphical client
   - [Download SQL Developer](https://www.oracle.com/database/sqldeveloper/technologies/download/)
   - Alternative: DBeaver with Oracle driver

3. **Oracle Instant Client** (optional for remote connections)

### Operating System

- **Windows:** Direct installation
- **Mac/Linux:** Use Docker
  ```bash
  docker pull container-registry.oracle.com/database/express:21.3.0-xe
  ```

---

## Submissions

Check the [submission instructions](../../entregas/01_bases_de_datos/) to find out which files you need to upload.

**Submission folder:**
```
entregas/01_bases_de_datos/tu_apellido_nombre/3.1_oracle_hr/
```

---

## Support Resources

### Official Documentation
- [Oracle Database Documentation](https://docs.oracle.com/en/database/)
- [PL/SQL Language Reference](https://docs.oracle.com/en/database/oracle/oracle-database/21/lnpls/)

### Tutorials
- [Oracle Live SQL](https://livesql.oracle.com/) - Free online practice
- [PL/SQL Tutorial](https://www.oracletutorial.com/plsql-tutorial/)

### Comparisons
- [Oracle vs PostgreSQL](https://www.postgresql.org/about/featurematrix/)
- [Oracle to PostgreSQL Migration](https://wiki.postgresql.org/wiki/Oracle_to_Postgres_Conversion)

---

## Next Steps

After completing this exercise:

1. **Exercise 3.2** - Oracle Gardening (more practice with Oracle)
2. **Exercise 4.1** - SQL Server (another enterprise engine)

﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌​‌‌‌‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​‌​​‍​​‌‌​‌‌‌‍​​‌‌​​​‌‍​​‌‌​​‌​‍​‌‌​​​​‌﻿---

**Publication date:** To be defined
**Last updated:** 2025-12-17
