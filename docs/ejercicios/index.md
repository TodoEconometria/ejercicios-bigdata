# Ejercicios

Lista completa de todos los ejercicios disponibles en el curso.

---

## Roadmap de Ejercicios

### Módulo 1: Bases de Datos

| # | Ejercicio | Tecnología | Nivel | Tiempo | Estado |
|---|-----------|------------|-------|--------|--------|
| 1.1 | Introducción SQLite | SQLite + Pandas | 🟢 Básico | 8-10h | ✅ Disponible |
| 2.1 | PostgreSQL HR | PostgreSQL | 🟡 Intermedio | 4-6h | 🚧 Próximo |
| 2.2 | PostgreSQL Jardinería | PostgreSQL | 🟡 Intermedio | 4-6h | 🚧 Próximo |
| 2.3 | Migración SQLite → PostgreSQL | PostgreSQL + Python | 🟡 Intermedio | 3-4h | 🚧 Próximo |
| 3.1 | Oracle HR | Oracle Database | 🔴 Avanzado | 5-7h | 🚧 Próximo |
| 3.2 | Oracle Jardinería | Oracle Database | 🔴 Avanzado | 4-5h | 🚧 Próximo |
| 4.1 | SQL Server Tienda | SQL Server | 🔴 Avanzado | 4-5h | 🚧 Próximo |
| 5.1 | Análisis Excel/Python | Pandas + Excel | 🟢 Básico | 3-4h | 🚧 Próximo |

### Módulo 2: Big Data (Próximamente)

| # | Ejercicio | Tecnología | Nivel | Tiempo | Estado |
|---|-----------|------------|-------|--------|--------|
| 02 | Limpieza de Datos | Pandas | 🟢 Básico | 3-4h | 📅 Planificado |
| 03 | Parquet y Dask | Dask + Parquet | 🟡 Intermedio | 4-5h | 📅 Planificado |
| 04 | PySpark Queries | PySpark | 🔴 Avanzado | 5-6h | 📅 Planificado |
| 05 | Dashboard Interactivo | Flask + Chart.js | 🔴 Avanzado | 8-10h | 📅 Planificado |
| 06 | Pipeline ETL | Dask + PySpark | 🔴 Avanzado | 10-12h | 📅 Planificado |

---

## MÓDULO 1: Bases de Datos

### [Ejercicio 1.1: Introducción a SQLite](01-introduccion-sqlite.md)

!!! info "Detalles"
    - **Nivel:** 🟢 Basico
    - **Tiempo:** 2-3 horas
    - **Dataset:** NYC Taxi (muestra 10MB)
    - **Tecnologias:** SQLite, Pandas

**Que aprenderas:**

- Cargar datos CSV a base de datos SQLite
- Queries SQL basicas (SELECT, WHERE, GROUP BY)
- Optimizacion con indices
- Exportar resultados a CSV

**Objetivos:**

- [x] Cargar CSV en chunks
- [x] Crear base de datos SQLite
- [x] Ejecutar queries SQL
- [x] Crear indices para optimizacion
- [x] Exportar resultados

[Ver Ejercicio Completo →](01-introduccion-sqlite.md){ .md-button .md-button--primary }

---

### [Ejercicio 2.1: PostgreSQL con BD HR](02-postgresql-hr.md)

!!! info "Detalles"
    - **Nivel:** 🟡 Intermedio
    - **Tiempo:** 4-6 horas
    - **Base de Datos:** HR (Human Resources) de Oracle
    - **Tecnologías:** PostgreSQL, SQL

**Qué aprenderás:**

- Instalar y configurar PostgreSQL
- Cargar bases de datos desde scripts SQL
- Consultas complejas con múltiples JOINs
- Funciones específicas de PostgreSQL
- Comparar Oracle vs PostgreSQL

[Ver Ejercicio Completo →](02-postgresql-hr.md){ .md-button }

---

### [Ejercicio 2.2: PostgreSQL Jardinería](03-postgresql-jardineria.md)

!!! info "Detalles"
    - **Nivel:** 🟡 Intermedio
    - **Tiempo:** 4-6 horas
    - **Base de Datos:** Sistema de ventas de jardinería
    - **Tecnologías:** PostgreSQL, Window Functions

**Qué aprenderás:**

- Análisis de ventas con SQL
- Agregaciones complejas (GROUP BY, HAVING)
- Window Functions para rankings
- Optimización con índices
- Vistas materializadas

[Ver Ejercicio Completo →](03-postgresql-jardineria.md){ .md-button }

---

### [Ejercicio 2.3: Migración SQLite → PostgreSQL](04-migracion-sqlite-postgresql.md)

!!! info "Detalles"
    - **Nivel:** 🟡 Intermedio
    - **Tiempo:** 3-4 horas
    - **Tecnologías:** SQLite, PostgreSQL, Python

**Qué aprenderás:**

- Diferencias entre motores de BD
- Migrar esquemas y datos
- Adaptar tipos de datos
- Validar integridad
- Comparar rendimiento

[Ver Ejercicio Completo →](04-migracion-sqlite-postgresql.md){ .md-button }

---

### [Ejercicio 3.1: Oracle con BD HR](05-oracle-hr.md)

!!! warning "Avanzado"
    - **Nivel:** 🔴 Avanzado
    - **Tiempo:** 5-7 horas
    - **Base de Datos:** HR en Oracle nativo
    - **Tecnologías:** Oracle Database, PL/SQL

**Qué aprenderás:**

- Instalar Oracle Database XE
- Sintaxis específica de Oracle
- PL/SQL (procedimientos, funciones)
- Secuencias y triggers
- Comparar con PostgreSQL

[Ver Ejercicio Completo →](05-oracle-hr.md){ .md-button }

---

### [Ejercicio 5.1: Análisis Excel/Python](06-analisis-excel-python.md)

!!! info "Detalles"
    - **Nivel:** 🟢 Básico-Intermedio
    - **Tiempo:** 3-4 horas
    - **Tecnologías:** Python, Pandas, Excel

**Qué aprenderás:**

- Leer archivos Excel con Python
- Análisis exploratorio de datos (EDA)
- Visualizaciones con matplotlib/seaborn
- Automatizar análisis
- Comparar manual vs programático

[Ver Ejercicio Completo →](06-analisis-excel-python.md){ .md-button }

---

## MÓDULO 2: Big Data

### Ejercicio 02: Limpieza y Transformacion

!!! warning "Proximamente"
    Este ejercicio estara disponible pronto.

**Preview de contenido:**

- Detectar y manejar valores nulos
- Identificar y tratar outliers
- Transformaciones de datos
- Validacion de tipos de datos
- Normalizacion y estandarizacion

---

### Ejercicio 03: Procesamiento con Parquet y Dask

!!! warning "Proximamente"
    Este ejercicio estara disponible pronto.

**Preview de contenido:**

- Por que Parquet es mejor que CSV
- Procesamiento paralelo con Dask
- Lazy evaluation
- Optimizacion de memoria
- Comparativa de rendimiento

---

### Ejercicio 04: Queries Complejas con PySpark

!!! warning "Proximamente"
    Este ejercicio estara disponible pronto.

**Preview de contenido:**

- Introduccion a Apache Spark
- DataFrames distribuidos
- SQL en Spark
- Joins de multiples fuentes
- Particionamiento de datos

---

### Ejercicio 05: Dashboard Interactivo

!!! warning "Proximamente"
    Este ejercicio estara disponible pronto.

**Preview de contenido:**

- Flask para backend
- Chart.js para visualizaciones
- Conectar frontend con analisis
- Deploy local con Docker
- Optimizacion de rendimiento

---

### Ejercicio 06: Pipeline ETL Completo

!!! warning "Proximamente"
    Este ejercicio estara disponible pronto.

**Preview de contenido:**

- Diseno de arquitectura ETL
- Extract con multiples fuentes
- Transform con Dask/PySpark
- Load a Parquet optimizado
- Monitoreo y logging
- Deploy a produccion

---

## Datasets Utilizados

### NYC Taxi & Limousine Commission (TLC)

- **Fuente:** [NYC Open Data](https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page)
- **Periodo:** 2021
- **Tamano:** 121 MB (muestra), varios GB (completo)
- **Registros:** 10M+ viajes

**Campos principales:**

- `tpep_pickup_datetime`: Fecha/hora de inicio
- `tpep_dropoff_datetime`: Fecha/hora de fin
- `passenger_count`: Numero de pasajeros
- `trip_distance`: Distancia en millas
- `total_amount`: Tarifa total
- `payment_type`: Metodo de pago

### Weather Data (NOAA)

!!! info "Uso en Ejercicio 04"
    Combinado con datos de taxi para analisis avanzados

- **Fuente:** NOAA Weather Database
- **Variables:** Temperatura, precipitacion, viento
- **Uso:** Join con datos de taxi para analisis de impacto del clima

---

## Como Trabajar los Ejercicios

### Flujo Recomendado

1. **Leer el enunciado completo** - No empieces a codear sin leer todo
2. **Entender los objetivos** - Que se espera que logres?
3. **Crear rama de trabajo** - `git checkout -b tu-apellido-ejercicio-XX`
4. **Trabajar en pasos pequenos** - No intentes hacerlo todo de una vez
5. **Probar frecuentemente** - Ejecuta tu codigo cada vez que completes una parte
6. **Hacer commits regulares** - Guarda tu progreso frecuentemente
7. **Crear Pull Request** - Cuando completes el ejercicio

### Mejores Practicas

!!! tip "Consejos para el Exito"

    - **No copiar y pegar sin entender** - Escribe el codigo tu mismo
    - **Leer los errores** - Los mensajes de error te dicen que esta mal
    - **Usar print() para debug** - Imprime variables para ver su contenido
    - **Comentar tu codigo** - Explica que hace cada parte
    - **Pedir ayuda si te atoras** - Pero intenta resolverlo primero

---

## Evaluacion

### Criterios de Evaluacion

Los ejercicios se evaluan basandose en:

1. **Funcionalidad** (40%)
    - El codigo ejecuta sin errores?
    - Cumple con todos los objetivos?
    - Los resultados son correctos?

2. **Codigo Limpio** (30%)
    - Es legible?
    - Esta bien documentado?
    - Sigue buenas practicas?

3. **Rendimiento** (20%)
    - Esta optimizado?
    - Usa memoria eficientemente?
    - Tiempo de ejecucion razonable?

4. **Creatividad** (10%)
    - Agrega analisis adicionales?
    - Propone mejoras?
    - Resuelve de forma innovadora?

### Rubrica

| Criterio | Excelente (100%) | Bueno (80%) | Suficiente (60%) | Insuficiente (<60%) |
|----------|------------------|-------------|------------------|---------------------|
| **Funcionalidad** | Cumple todos los objetivos sin errores | Cumple objetivos con errores menores | Cumple parcialmente | No funciona |
| **Codigo** | Muy legible, bien documentado | Legible, documentacion basica | Poco legible | Ilegible |
| **Rendimiento** | Optimizado | Funcional | Lento pero funciona | Muy lento |
| **Creatividad** | Analisis adicionales innovadores | Algunas mejoras | Basico | Solo lo minimo |

---

## FAQ de Ejercicios

??? question "Puedo usar librerias adicionales?"

    Si, pero:

    - Justifica por que las necesitas
    - Agregalas a `requirements.txt`
    - Documenta como instalarlas

??? question "Cuanto tiempo debo dedicar a cada ejercicio?"

    Los tiempos son estimados:

    - **Principiantes:** Pueden tomar el doble
    - **Intermedios:** El tiempo estimado
    - **Avanzados:** La mitad del tiempo

    No hay prisa. Aprende bien cada concepto.

??? question "Que hago si me atorο?"

    1. Lee el error cuidadosamente
    2. Busca en Google el mensaje de error
    3. Revisa la documentacion de la libreria
    4. Pregunta en el PR con `@TodoEconometria`
    5. Alumnos presenciales: Consulta en clase

??? question "Puedo hacer los ejercicios en desorden?"

    **No recomendado.** Los ejercicios estan disenados para:

    - Construir sobre conocimientos previos
    - Aumentar dificultad gradualmente
    - Introducir conceptos en orden logico

    Si ya tienes experiencia, puedes saltar niveles, pero no ejercicios dentro del mismo nivel.

---

## Recursos Adicionales

### Documentacion

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [SQLite Tutorial](https://www.sqlitetutorial.net/)
- [Dask Documentation](https://docs.dask.org/)
- [PySpark Documentation](https://spark.apache.org/docs/latest/api/python/)

### Tutoriales

- [Python for Data Analysis](https://wesmckinney.com/book/)
- [SQL for Data Science](https://mode.com/sql-tutorial/)
- [Dask Tutorial](https://tutorial.dask.org/)

---

## Proximos Pasos

Empieza con el primer ejercicio:

[Ejercicio 01: Introduccion SQLite →](01-introduccion-sqlite.md){ .md-button .md-button--primary }

O revisa:

- [Roadmap del Curso](../guia-inicio/roadmap.md) - Plan completo de estudio
- [Tu Primer Ejercicio](../guia-inicio/primer-ejercicio.md) - Flujo de trabajo
- [Crear Pull Requests](../git-github/pull-requests.md) - Como entregar ejercicios
