# Exercise 02: Professional ETL Pipeline - Quality of Government﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​​​‌‍​​‌‌‌​​‌‍​​‌‌‌​​‌‍​‌‌​​​‌‌‍​​‌‌​‌‌​‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​​‌‌​​​‌﻿

> **Level:** Advanced | **Duration:** 15-20 hours | **Mode:** Group or Individual﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​​​‌‍​​‌‌‌​​‌‍​​‌‌‌​​‌‍​‌‌​​​‌‌‍​​‌‌​‌‌​‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​​‌‌​​​‌﻿

---

## General Description

You will build a **professional ETL pipeline** working with the Quality of Government dataset, a longitudinal database with over 1000 variables on institutional quality, democracy, and economic development.

**Objective:** Apply software engineering and data science techniques to clean, transform, and analyze real academic research data.

![Data Flow and Life Cycle in Distributed Databases](../assets/slides/m2_flujo_p01.jpg)

---

## The Data Life Cycle

![Management from Creation to Deletion](../assets/slides/m2_flujo_p02.jpg)

---

## Dataset: Quality of Government (QoG)

**What is it?**

A database maintained by the University of Gothenburg that aggregates variables from multiple international sources.

**Characteristics:**
- **1289 variables** on institutional quality, economy, society
- **194+ countries** with data since 1946
- **Sources:** World Bank, V-Dem, Transparency International, Freedom House, UNDP

**Source:** https://www.qog.pol.gu.se/

---

## Learning Objectives

- ✅ Design a modular ETL architecture
- ✅ Work with PostgreSQL for longitudinal analysis
- ✅ Clean complex datasets (>1000 variables)
- ✅ Prepare panel data for econometrics
- ✅ Apply software engineering best practices
- ✅ Write production-ready code

---

## Analysis Topics

Choose **ONE:**

### Topic 1: Post-Authoritarian Institutional Evolution

**Question:** How does institutional quality evolve during democratic transitions?

**Key variables:**
- Democracy indices (V-Dem, Polity)
- Institutional quality (Transparency International)
- Economic development (GDP, HDI)

**Cases:** Eastern Europe, Latin America, Central Asia

---

### Topic 2: Natural Resources and Development

**Question:** Does dependence on natural resources affect development?

**Key variables:**
- Oil/gas production (Ross dataset)
- Natural resource rents (World Bank)
- Access to basic services (water, sanitation)
- Institutional quality

**Cases:** Oil-producing countries, resource curse, water security

---

## Project Architecture

### Expected Structure

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

**See details:** [Full architecture](https://github.com/TodoEconometria/ejercicios-bigdata/tree/main/ejercicios/02_limpieza_datos/especificaciones/ARQUITECTURA.md)

---

## Technologies

### Required

- **Python 3.11+**
- **PostgreSQL 14+**
- **pandas** - Data manipulation
- **psycopg2** - PostgreSQL connection

### Recommended

- SQLAlchemy - ORM
- pytest - Testing
- Black - Code formatting

---

## Ingestion Architecture

![Transfer Models: Batch, Streaming, and Delta Load](../assets/slides/m2_flujo_p04.jpg)

![Advanced Data Acquisition Methods](../assets/slides/m2_flujo_p05.jpg)

---

## Data Cleaning: A Practical Approach

![Data Cleaning and Analysis for Big Data](../assets/slides/m2_limpieza_p01.jpg)

![Case Study: Linelist Dataset](../assets/slides/m2_limpieza_p03.jpg)

![Technical Inspection: Dataframe X-Ray](../assets/slides/m2_limpieza_p05.jpg)

---

## Project Phases

### 1. Extract (E)
- Download QoG dataset
- Filter by topic and period
- Validate integrity

### 2. Transform (T)
- Rename columns
- Create derived variables
- Handle missing values

### 3. Load (L)
- Load into PostgreSQL
- Validate referential integrity
- Optimize with indexes

### 4. Analysis
- Descriptive statistics
- Prepare balanced panel
- Export for econometrics (.dta, .csv)

---

## Panel Data

This exercise prepares you for **econometric analysis**.

**Panel data = Cross-section x Time-series**

```
| country | year | democracy | gdp_pc |
|---------|------|-----------|--------|
| ESP     | 2000 | 0.85      | 24000  |
| ESP     | 2001 | 0.86      | 24500  |
```

**Allows for:**
- Fixed Effects (control for heterogeneity)
- Random Effects
- Difference-in-Differences
- Dynamic models

---

## Technical Specifications

All detailed technical documentation is in:

```
ejercicios/02_limpieza_datos/especificaciones/
├── ARQUITECTURA.md           # Estructura de proyecto
├── ESQUEMA_DB.sql            # Schema PostgreSQL completo
├── FUNCIONES_REQUERIDAS.md   # Firmas de funciones
├── VARIABLES_TEMA1.md        # Variables + prompts AI
├── VARIABLES_TEMA2.md        # Variables + prompts AI
└── VALIDACIONES.md           # Checks obligatorios
```

**Especially useful:** VARIABLES_TEMA*.md includes **prompts for Claude/ChatGPT** to research additional variables.

---

## Evaluation Criteria

| Criterion | Weight | What We Evaluate |
|-----------|--------|-------------------|
| **Functionality** | 40% | Pipeline runs without errors, correct data |
| **Architecture** | 25% | Modular code, separation of concerns |
| **Code Quality** | 20% | PEP 8, type hints, docstrings |
| **Documentation** | 10% | README, methodology, comments |
| **Innovation** | 5% | Tests, visualizations, additional analysis |

---

## Deliverables

**Location:** `entregas/02_limpieza_datos/tu_apellido_nombre/`

**Minimum required:**
- Modular source code (src/)
- Executable scripts (scripts/)
- SQL queries (sql/)
- Complete README
- METODOLOGIA.md (design decisions)
- requirements.txt

**DO NOT include:** Data, logs, venv/, .env

---

## Support Resources

### Dataset
- [QoG Website](https://www.qog.pol.gu.se/)
- [Codebook PDF](https://www.qogdata.pol.gu.se/data/codebook_std_jan23.pdf)
- [Download CSV](https://www.qogdata.pol.gu.se/data/qog_std_ts_jan23.csv)

### Project Guides
- [Setup PostgreSQL](https://github.com/TodoEconometria/ejercicios-bigdata/tree/main/ejercicios/02_limpieza_datos/docs/POSTGRESQL_SETUP.md)
- [Submission Instructions](https://github.com/TodoEconometria/ejercicios-bigdata/tree/main/ejercicios/02_limpieza_datos/INSTRUCCIONES_ENTREGA.md)

### Technical Documentation
- [PostgreSQL Docs](https://www.postgresql.org/docs/)
- [pandas Docs](https://pandas.pydata.org/docs/)
- [psycopg2 Docs](https://www.psycopg.org/docs/)

---

## Docker Preparation

This project is designed to be **dockerized** in future exercises.

Your modular architecture will facilitate:
- PostgreSQL container
- Python application container
- docker-compose orchestration

**For now:** Local PostgreSQL installation.

---

## How to Get Started

1. **Read all the documentation** in `ejercicios/02_limpieza_datos/`
2. **Install PostgreSQL** (see POSTGRESQL_SETUP.md)
3. **Choose a topic** (1 or 2)
4. **Research variables** using prompts in VARIABLES_TEMA*.md
5. **Implement step by step:** Extract → Transform → Load → Analysis
6. **Test frequently**
7. **Document as you code**

---

## Tips

- Start with a basic pipeline, optimize later
- Logging everywhere (your best friend for debugging)
- Frequent Git commits
- Test with a small subset first (not 1M rows at once)
- Read the QoG codebook - it is your bible
- Ask early if something is unclear

---

## FAQ

**Q: Individual or group?**
A: Your choice. Groups of 2-5 people.

**Q: Do I have to use ALL the suggested variables?**
A: No, they are suggestions. Research and choose the relevant ones.

**Q: Can I use Docker?**
A: Not for this exercise. Local PostgreSQL. Docker will come later.

**Q: What if I cannot find a variable?**
A: Use the AI prompts in VARIABLES_TEMA*.md to search for alternatives.

﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​​​‌‍​​‌‌‌​​‌‍​​‌‌‌​​‌‍​‌‌​​​‌‌‍​​‌‌​‌‌​‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​​‌‌​​​‌﻿---

**Publication date:** To be defined
**Last updated:** 2025-12-17
