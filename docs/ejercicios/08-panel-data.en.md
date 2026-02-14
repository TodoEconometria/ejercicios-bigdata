# Module 06: Panel Data Analysis﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​​‌​‍​​‌‌​​‌​‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌‌​​‌‍​​‌‌‌​​​‍​​‌‌​‌​‌‍​‌‌​​‌‌​﻿

> **Status:** Available

---

## General Description

We will learn panel data econometrics: the combination of cross-sectional data﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​​‌​‍​​‌‌​​‌​‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌‌​​‌‍​​‌‌‌​​​‍​​‌‌​‌​‌‍​‌‌​​‌‌​﻿
(countries, individuals) with time series (years). We will work with Fixed Effects,
Random Effects, and Two-Way Fixed Effects models applied to real social science problems.

**Level:** Advanced
**Technologies:** Python, linearmodels, pandas, Altair
**Prerequisites:** Basic statistics, linear regression

---

## Learning Objectives

- Understand the structure of panel data (unit x time)
- Distinguish between Pooled OLS, Fixed Effects, and Random Effects
- Apply the Hausman Test to choose between FE and RE
- Implement Two-Way Fixed Effects (unit + time effects)
- Interpret Odds Ratios in logistic models
- Calculate marginal effects in nonlinear models

---

## Module Content

The complete module is located at:

```
ejercicios/06_analisis_datos_de_panel/
├── 01_analisis_guns.py              # Panel: gun laws and crime
├── 02_analisis_fatality.py          # TWFE: beer tax vs mortality
├── 03_dashboard_educativo.py        # Interactive dashboard with 4 tabs
├── conceptos_visuales_panel.py      # Conceptual visualizations
├── GUIA_PANEL_DATA.md               # Complete theoretical guide
├── grafico_panel_guns.png           # Analysis result
└── requirements.txt                 # linearmodels, altair, etc.
```

---

## Practical Exercises

### 01 - Guns Analysis: Gun Laws and Crime

**Question:** Do gun-carry laws reduce violent crime?

- **Dataset:** [Guns](https://vincentarelbundock.github.io/Rdatasets/csv/AER/Guns.csv) (Stock & Watson) - 50 U.S. states, 1977-1999
- **Dependent variable:** `log(violent)` - violent crime rate (logarithm)
- **Key variable:** `law` - whether the state has a "shall-carry" law (mandatory carry)
- **Controls:** income, population, density
- **Models:** Pooled OLS vs Fixed Effects vs Random Effects
- **Methodology:** Comparison of the 3 models + Hausman Test

```bash
python ejercicios/06_analisis_datos_de_panel/01_analisis_guns.py
```

### 02 - Fatality Analysis: Beer Tax and Mortality

**Question:** Does raising the beer tax reduce traffic accident deaths?

- **Dataset:** [Fatalities](https://vincentarelbundock.github.io/Rdatasets/csv/AER/Fatalities.csv) (AER) - 48 states, 1982-1988
- **Dependent variable:** `fatality_rate` - deaths per 10,000 inhabitants
- **Key variable:** `beertax` - beer tax
- **Controls:** minimum drinking age (`drinkage`), unemployment, income
- **Models:** Entity FE vs **Two-Way Fixed Effects** (state + year)
- **Innovation:** TWFE controls for temporal trends (safer cars each year)

```bash
python ejercicios/06_analisis_datos_de_panel/02_analisis_fatality.py
```

### 03 - Interactive Educational Dashboard (Panel + Altair)

Local dashboard with 4 interactive tabs to visually explore the concepts:

1. **Pooled OLS:** Heterogeneity slider that shows Simpson's Paradox in action
2. **FE vs RE:** Explanation and decision table for the Hausman Test
3. **Odds Ratios:** Sliders to explore probability vs odds vs odds ratio in real time
4. **Marginal Effects:** Lin-Lin, Log-Lin, Log-Log comparison with dynamic charts

```bash
panel serve ejercicios/06_analisis_datos_de_panel/03_dashboard_educativo.py
# Open http://localhost:5006 in your browser
```

### Additional Files

- **`conceptos_visuales_panel.py`** - Generates static charts explaining panel concepts
- **`dashboard_educativo_panel.py`** - Alternative version of the educational dashboard
- **`GUIA_PANEL_DATA.md`** - Complete theoretical guide: Pooled OLS, FE, RE, Hausman, TWFE

---

## Theory: Key Concepts

### What is panel data?

Data that combines **cross-sectional** (N units) with **time series** (T periods):

![Panel Data Structure](../assets/slides/m6_panel_p02.jpg)

```
| country | year | democracy | gdp_pc |
|---------|------|-----------|--------|
| ESP     | 2000 | 0.85      | 24000  |
| ESP     | 2001 | 0.86      | 24500  |
| FRA     | 2000 | 0.88      | 28000  |
| FRA     | 2001 | 0.89      | 28500  |
```

### Data Engineering: Wide vs Long Format

![Data Engineering in Python: Wide vs Long](../assets/slides/m6_panel_p04.jpg)

### Pooled OLS vs Fixed Effects vs Random Effects

| Model | Assumption | When to use |
|-------|-----------|-------------|
| **Pooled OLS** | No individual heterogeneity | Rarely appropriate |
| **Fixed Effects** | Heterogeneity correlated with X | Social sciences (general rule) |
| **Random Effects** | Heterogeneity NOT correlated with X | Random surveys |

### The Naive Model: Pooled OLS

![The Naive Model: Pooled OLS](../assets/slides/m6_panel_p05.jpg)

### Unobserved Heterogeneity

![The Invisible Enemy: Unobserved Heterogeneity](../assets/slides/m6_panel_p03.jpg)

### Hausman Test

Decides between FE and RE:

- **H0:** RE is consistent and efficient (prefer RE)
- **H1:** Only FE is consistent (prefer FE)
- If p-value < 0.05: use **Fixed Effects**

---

## Dashboards

### Educational Dashboard (local)

The main dashboard for this module runs locally with Panel (HoloViz):

```bash
panel serve ejercicios/06_analisis_datos_de_panel/03_dashboard_educativo.py
```

Includes 4 interactive tabs: Pooled OLS, FE vs RE, Odds Ratios, Marginal Effects.

### QoG Dashboard - Advanced Analysis (GitHub Pages)

As a complement, you can explore a dashboard with panel analysis applied to the QoG dataset
(4 research lines with Spark + PostgreSQL + ML):

[View QoG Dashboard - Applied Panel Data](../dashboards/06_analisis_panel_qog.md){ .md-button }

---

## Resources

### Documentation
- [linearmodels Documentation](https://bashtage.github.io/linearmodels/)
- [Altair Documentation](https://altair-viz.github.io/)

### Theoretical References
- Wooldridge, J. M. (2010). Econometric Analysis of Cross Section and Panel Data (2nd ed.). MIT Press.
- Stock, J. H., & Watson, M. W. (2019). Introduction to Econometrics (4th ed.). Pearson.

﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​​‌​‍​​‌‌​​‌​‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌‌​​‌‍​​‌‌‌​​​‍​​‌‌​‌​‌‍​‌‌​​‌‌​﻿---

**Course:** Big Data with Python - From Zero to Production
**Instructor:** Juan Marcelo Gutierrez Miranda | @TodoEconometria
**Hash ID:** 4e8d9b1a5f6e7c3d2b1a0f9e8d7c6b5a4f3e2d1c0b9a8f7e6d5c4b3a2f1e0d9c
**Methodology:** Progressive exercises with real data and professional tools

**Academic references:**

- Wooldridge, J. M. (2010). Econometric Analysis of Cross Section and Panel Data (2nd ed.). MIT Press.
- Stock, J. H., & Watson, M. W. (2019). Introduction to Econometrics (4th ed.). Pearson.
- Baltagi, B. H. (2021). Econometric Analysis of Panel Data (6th ed.). Springer.
