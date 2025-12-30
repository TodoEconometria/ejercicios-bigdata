# Ejercicio 2.3: Migración SQLite → PostgreSQL

> **Estado:** En construcción

---

## Descripción General

Aprenderás a **migrar bases de datos** desde SQLite a PostgreSQL, comprendiendo las diferencias entre ambos motores.

**Duración estimada:** 3-4 horas
**Nivel:** Intermedio-Avanzado
**Prerequisitos:** Ejercicio 1.1 (SQLite), Ejercicio 2.1 (PostgreSQL)

---

## Objetivos de Aprendizaje

Al completar este ejercicio serás capaz de:

- ✅ Identificar diferencias entre SQLite y PostgreSQL
- ✅ Adaptar tipos de datos entre motores
- ✅ Migrar esquemas (DDL)
- ✅ Migrar datos (DML)
- ✅ Escribir scripts de migración en Python
- ✅ Validar integridad después de la migración
- ✅ Comparar rendimiento entre motores

---

## Contexto del Ejercicio

Usarás las bases de datos que creaste en el **Ejercicio 1.1** (tienda informática):

- `tienda_modelo_a.db` - 26 tablas independientes
- `tienda_modelo_b.db` - Modelo normalizado
- `tienda_modelo_c.db` - E-commerce completo

**Objetivo:** Migrarlas a PostgreSQL y comparar.

---

## Diferencias Principales

### Tipos de Datos

| SQLite | PostgreSQL |
|--------|------------|
| `INTEGER` | `INTEGER` o `BIGINT` |
| `REAL` | `NUMERIC(p,s)` o `DOUBLE PRECISION` |
| `TEXT` | `VARCHAR(n)` o `TEXT` |
| `BLOB` | `BYTEA` |
| Sin tipo | PostgreSQL es estricto |

### Auto-increment

| SQLite | PostgreSQL |
|--------|------------|
| `AUTOINCREMENT` | `SERIAL` o `IDENTITY` |

### Constraints

PostgreSQL tiene constraints más estrictos y soporta más tipos.

### Performance

PostgreSQL es mucho más rápido con grandes volúmenes y consultas complejas.

---

## Contenido del Ejercicio

El ejercicio completo está en:

```
ejercicios/01_bases_de_datos/2.3_postgresql_tienda/
```

### Archivos

- `migracion_desde_sqlite.py` - Script de migración (plantilla)
- `comparativa_sqlite_vs_postgres.md` - Análisis comparativo

---

## Proceso de Migración

### 1. Análisis del Esquema Origen

```python
# Conectar a SQLite
import sqlite3
conn = sqlite3.connect('tienda_modelo_b.db')

# Obtener lista de tablas
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
```

### 2. Adaptación de Tipos de Datos

Convertir tipos SQLite → PostgreSQL:
- Detectar tipos dinámicamente
- Mapear a tipos PostgreSQL equivalentes
- Ajustar precisión de NUMERIC

### 3. Recreación del Esquema

Generar DDL para PostgreSQL:
- CREATE TABLE con tipos adaptados
- PRIMARY KEY
- FOREIGN KEY
- CONSTRAINTS

### 4. Migración de Datos

```python
# Leer datos de SQLite
df = pd.read_sql("SELECT * FROM productos", sqlite_conn)

# Insertar en PostgreSQL
df.to_sql('productos', postgres_engine, if_exists='append')
```

### 5. Validación

- Verificar conteos: SQLite vs PostgreSQL
- Validar integridad referencial
- Probar consultas complejas

---

## Tareas a Realizar

### Parte 1: Script de Migración

Crear `migracion_desde_sqlite.py` que:

1. Lee esquema de SQLite
2. Genera DDL para PostgreSQL
3. Migra datos tabla por tabla
4. Valida la migración
5. Genera reporte de éxito/errores

### Parte 2: Análisis Comparativo

Crear `comparativa_sqlite_vs_postgres.md` con:

1. **Diferencias de Esquema**
   - Tipos de datos modificados
   - Constraints añadidos
   - Índices creados

2. **Pruebas de Rendimiento**
   - Misma consulta en ambos motores
   - Tiempos de ejecución
   - Uso de memoria

3. **Conclusiones**
   - ¿Cuándo usar SQLite?
   - ¿Cuándo usar PostgreSQL?
   - Recomendaciones

---

## Requisitos Técnicos

### Software

- SQLite (ya instalado)
- PostgreSQL 14+
- Python con:
  ```bash
  pip install pandas psycopg2-binary sqlite3
  ```

### Datos Origen

Tus bases de datos del Ejercicio 1.1:
- `tienda_modelo_a.db`
- `tienda_modelo_b.db`
- `tienda_modelo_c.db`

---

## Entregas

Consulta las [instrucciones de entrega](../../entregas/01_bases_de_datos/) para saber qué archivos debes subir.

**Carpeta de entrega:**
```
entregas/01_bases_de_datos/tu_apellido_nombre/2.3_postgresql_tienda/
├── migracion_desde_sqlite.py
├── comparativa_sqlite_vs_postgres.md
└── capturas/
    ├── sqlite_query.png
    └── postgres_query.png
```

---

## Recursos de Apoyo

### Herramientas de Migración

- [pgloader](https://pgloader.io/) - Migración automática
- [SQLite to PostgreSQL Converter](https://github.com/caiiiycuk/sqlite-to-postgres)

### Documentación

- [PostgreSQL Data Types](https://www.postgresql.org/docs/current/datatype.html)
- [Migración de Bases de Datos](https://www.postgresql.org/docs/current/migration.html)

### Tutoriales

- [Comparativa SQLite vs PostgreSQL](https://www.sqlite.org/whentouse.html)
- [Psycopg2 Tutorial](https://www.psycopg.org/docs/)

---

## Próximos Pasos

Después de completar este ejercicio:

1. **Ejercicio 3.1** - Oracle con BD HR
2. **Ejercicio 4.1** - SQL Server con Tienda

---

**Fecha de publicación:** Por definir
**Última actualización:** 2025-12-17
