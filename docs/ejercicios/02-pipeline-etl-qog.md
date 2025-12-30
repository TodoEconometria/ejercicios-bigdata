# Ejercicio 02: Pipeline ETL Profesional - Quality of Government

> **Nivel:** Avanzado | **Duración:** 15-20 horas | **Modalidad:** Grupal o Individual

---

## Descripción General

Construirás un **pipeline ETL profesional** trabajando con el dataset Quality of Government, una base de datos longitudinal con más de 1000 variables sobre calidad institucional, democracia y desarrollo económico.

**Objetivo:** Aplicar técnicas de ingeniería de software y ciencia de datos para limpiar, transformar y analizar datos reales de investigación académica.

---

## Dataset: Quality of Government (QoG)

**¿Qué es?**

Base de datos mantenida por la Universidad de Gotemburgo que agrega variables de múltiples fuentes internacionales.

**Características:**
- **1289 variables** de calidad institucional, economía, sociedad
- **194+ países** con datos desde 1946
- **Fuentes:** World Bank, V-Dem, Transparency International, Freedom House, UNDP

**Fuente:** https://www.qog.pol.gu.se/

---

## Objetivos de Aprendizaje

- ✅ Diseñar arquitectura ETL modular
- ✅ Trabajar con PostgreSQL para análisis longitudinal
- ✅ Limpiar datasets complejos (>1000 variables)
- ✅ Preparar datos de panel para econometría
- ✅ Aplicar buenas prácticas de software engineering
- ✅ Escribir código production-ready

---

## Temas de Análisis

Elige **UNO:**

### Tema 1: Evolución Institucional Post-Autoritaria

**Pregunta:** ¿Cómo evoluciona la calidad institucional en transiciones democráticas?

**Variables clave:**
- Índices de democracia (V-Dem, Polity)
- Calidad institucional (Transparency International)
- Desarrollo económico (PIB, HDI)

**Casos:** Europa del Este, América Latina, Asia Central

---

### Tema 2: Recursos Naturales y Desarrollo

**Pregunta:** ¿La dependencia de recursos naturales afecta el desarrollo?

**Variables clave:**
- Producción petróleo/gas (Ross dataset)
- Rentas recursos naturales (World Bank)
- Acceso servicios básicos (agua, saneamiento)
- Calidad institucional

**Casos:** Países petroleros, resource curse, seguridad hídrica

---

## Arquitectura del Proyecto

### Estructura Esperada

```
tu_apellido_nombre/
├── src/
│   ├── database/          # Conexión PostgreSQL
│   ├── etl/               # Extract, Transform, Load
│   ├── analysis/          # Análisis de datos
│   └── utils/             # Logging, helpers
├── scripts/               # CLI ejecutables
├── sql/                   # Queries complejas
├── tests/                 # Tests (opcional)
└── docs/                  # Documentación
```

**Ver detalles:** [Arquitectura completa](https://github.com/TodoEconometria/ejercicios-bigdata/tree/main/ejercicios/02_limpieza_datos/especificaciones/ARQUITECTURA.md)

---

## Tecnologías

### Obligatorias

- **Python 3.11+**
- **PostgreSQL 14+**
- **pandas** - Manipulación de datos
- **psycopg2** - Conexión PostgreSQL

### Recomendadas

- SQLAlchemy - ORM
- pytest - Testing
- Black - Code formatting

---

## Fases del Proyecto

### 1. Extract (E)
- Descargar dataset QoG
- Filtrar por tema y período
- Validar integridad

### 2. Transform (T)
- Renombrar columnas
- Crear variables derivadas
- Manejar valores faltantes

### 3. Load (L)
- Cargar a PostgreSQL
- Validar integridad referencial
- Optimizar con índices

### 4. Analysis
- Estadísticas descriptivas
- Preparar panel balanceado
- Exportar para econometría (.dta, .csv)

---

## Datos de Panel

Este ejercicio te prepara para **análisis econométrico**.

**Panel data = Cross-section × Time-series**

```
| country | year | democracy | gdp_pc |
|---------|------|-----------|--------|
| ESP     | 2000 | 0.85      | 24000  |
| ESP     | 2001 | 0.86      | 24500  |
```

**Permite:**
- Fixed Effects (controlar heterogeneidad)
- Random Effects
- Difference-in-Differences
- Modelos dinámicos

---

## Especificaciones Técnicas

Toda la documentación técnica detallada está en:

```
ejercicios/02_limpieza_datos/especificaciones/
├── ARQUITECTURA.md           # Estructura de proyecto
├── ESQUEMA_DB.sql            # Schema PostgreSQL completo
├── FUNCIONES_REQUERIDAS.md   # Firmas de funciones
├── VARIABLES_TEMA1.md        # Variables + prompts AI
├── VARIABLES_TEMA2.md        # Variables + prompts AI
└── VALIDACIONES.md           # Checks obligatorios
```

**Especialmente útil:** VARIABLES_TEMA*.md incluyen **prompts para Claude/ChatGPT** para investigar variables adicionales.

---

## Criterios de Evaluación

| Criterio | Peso | Qué evaluamos |
|----------|------|---------------|
| **Funcionalidad** | 40% | Pipeline ejecuta sin errores, datos correctos |
| **Arquitectura** | 25% | Código modular, separación responsabilidades |
| **Calidad Código** | 20% | PEP 8, type hints, docstrings |
| **Documentación** | 10% | README, metodología, comentarios |
| **Innovación** | 5% | Tests, visualizaciones, análisis extra |

---

## Entregables

**Ubicación:** `entregas/02_limpieza_datos/tu_apellido_nombre/`

**Mínimo requerido:**
- Código fuente modular (src/)
- Scripts ejecutables (scripts/)
- Queries SQL (sql/)
- README completo
- METODOLOGIA.md (decisiones de diseño)
- requirements.txt

**NO incluir:** Datos, logs, venv/, .env

---

## Recursos de Apoyo

### Dataset
- [QoG Website](https://www.qog.pol.gu.se/)
- [Codebook PDF](https://www.qogdata.pol.gu.se/data/codebook_std_jan23.pdf)
- [Download CSV](https://www.qogdata.pol.gu.se/data/qog_std_ts_jan23.csv)

### Guías del Proyecto
- [Setup PostgreSQL](https://github.com/TodoEconometria/ejercicios-bigdata/tree/main/ejercicios/02_limpieza_datos/docs/POSTGRESQL_SETUP.md)
- [Instrucciones de Entrega](https://github.com/TodoEconometria/ejercicios-bigdata/tree/main/ejercicios/02_limpieza_datos/INSTRUCCIONES_ENTREGA.md)

### Documentación Técnica
- [PostgreSQL Docs](https://www.postgresql.org/docs/)
- [pandas Docs](https://pandas.pydata.org/docs/)
- [psycopg2 Docs](https://www.psycopg.org/docs/)

---

## Preparación para Docker

Este proyecto está diseñado para ser **dockerizado** en ejercicios futuros.

Tu arquitectura modular facilitará:
- Contenedor PostgreSQL
- Contenedor aplicación Python
- docker-compose orchestration

**Por ahora:** PostgreSQL instalación local.

---

## Cómo Empezar

1. **Lee toda la documentación** en `ejercicios/02_limpieza_datos/`
2. **Instala PostgreSQL** (ver POSTGRESQL_SETUP.md)
3. **Elige un tema** (1 o 2)
4. **Investiga variables** usando prompts en VARIABLES_TEMA*.md
5. **Implementa paso a paso:** Extract → Transform → Load → Analysis
6. **Testea frecuentemente**
7. **Documenta mientras codeas**

---

## Consejos

- Empieza con pipeline básico, optimiza después
- Logging en todo (tu mejor amigo para debugging)
- Git commits frecuentes
- Testea con subset pequeño primero (no 1M filas de golpe)
- Lee el codebook QoG - es tu biblia
- Pregunta temprano si algo no está claro

---

## FAQ

**P: ¿Individual o grupal?**
R: Eliges. Grupos 2-5 personas.

**P: ¿Tengo que usar TODAS las variables sugeridas?**
R: No, son sugerencias. Investiga y elige las relevantes.

**P: ¿Puedo usar Docker?**
R: No para este ejercicio. PostgreSQL local. Docker será futuro.

**P: ¿Qué hago si no encuentro una variable?**
R: Usa los prompts AI en VARIABLES_TEMA*.md para buscar alternativas.

---

**Fecha de publicación:** Por definir
**Última actualización:** 2025-12-17
