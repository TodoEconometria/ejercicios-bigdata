# Base de Datos HR (Oracle)

Esta carpeta contiene los scripts SQL de la **base de datos HR de Oracle**.

---

## Descripción

La base de datos **HR (Human Resources)** es una base de datos de ejemplo oficial de Oracle que se utiliza para demostraciones y aprendizaje.

**Contiene:**
- Tabla `employees` - Empleados
- Tabla `departments` - Departamentos
- Tabla `jobs` - Puestos de trabajo
- Tabla `locations` - Ubicaciones
- Tabla `countries` - Países
- Tabla `regions` - Regiones
- Tabla `job_history` - Historial laboral

---

## Archivos

Los scripts SQL se añadirán aquí:

- `hr_schema.sql` - Estructura de tablas (DDL)
- `hr_data.sql` - Datos de ejemplo (DML)
- `hr_constraints.sql` - Constraints y foreign keys
- `hr_views.sql` - Vistas de ejemplo (opcional)

---

## Uso

### Para PostgreSQL (Ejercicio 2.1)

Los scripts necesitan adaptarse ligeramente:
- Cambiar `NUMBER` por `NUMERIC` o `INTEGER`
- Cambiar `VARCHAR2` por `VARCHAR`
- Ajustar secuencias y auto-increment

### Para Oracle (Ejercicio 3.1)

Se usan directamente sin modificaciones.

---

## Descarga de Scripts Originales

Si necesitas los scripts originales de Oracle:

1. **Opción 1:** Instalación de Oracle
   - Los scripts vienen incluidos en Oracle Database XE
   - Ubicación: `$ORACLE_HOME/demo/schema/human_resources/`

2. **Opción 2:** Repositorios públicos
   - [Oracle Sample Schemas en GitHub](https://github.com/oracle/db-sample-schemas)

---

## Diagrama ER

```mermaid
erDiagram
    REGIONS {
        int region_id PK
        string region_name
    }

    COUNTRIES {
        string country_id PK
        string country_name
        int region_id FK
    }

    LOCATIONS {
        int location_id PK
        string street_address
        string city
        string state_province
        string country_id FK
    }

    DEPARTMENTS {
        int department_id PK
        string department_name
        int manager_id FK
        int location_id FK
    }

    JOBS {
        string job_id PK
        string job_title
        int min_salary
        int max_salary
    }

    EMPLOYEES {
        int employee_id PK
        string first_name
        string last_name
        string email
        string phone_number
        date hire_date
        string job_id FK
        decimal salary
        decimal commission_pct
        int manager_id FK
        int department_id FK
    }

    JOB_HISTORY {
        int employee_id PK_FK
        date start_date PK
        date end_date
        string job_id FK
        int department_id FK
    }

    REGIONS ||--o{ COUNTRIES : contains
    COUNTRIES ||--o{ LOCATIONS : has
    LOCATIONS ||--o{ DEPARTMENTS : located_in
    DEPARTMENTS ||--o{ EMPLOYEES : employs
    EMPLOYEES ||--o| EMPLOYEES : manages
    JOBS ||--o{ EMPLOYEES : has_role
    EMPLOYEES ||--o{ JOB_HISTORY : worked_as
    JOBS ||--o{ JOB_HISTORY : job_was
    DEPARTMENTS ||--o{ JOB_HISTORY : department_was
```

---

## Recursos

- [Oracle Sample Schemas Documentation](https://docs.oracle.com/en/database/oracle/oracle-database/21/comsc/)
- [HR Schema Guide](https://docs.oracle.com/en/database/oracle/oracle-database/21/comsc/sample-schema-HR.html)

---

**Última actualización:** 2025-12-17
