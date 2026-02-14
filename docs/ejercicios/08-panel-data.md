# Modulo 06: Analisis de Datos de Panel﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌​​‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​​‌‌​​​​‍​​‌‌​​​​‍​​‌‌​‌‌‌‍​​‌‌‌​​‌‍​‌‌​​​‌‌﻿

> **Estado:** Disponible

---

## Descripcion General

Aprenderemos econometria de datos de panel: la combinacion de datos de corte transversal﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌​​‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​​‌‌​​​​‍​​‌‌​​​​‍​​‌‌​‌‌‌‍​​‌‌‌​​‌‍​‌‌​​​‌‌﻿
(paises, individuos) con series temporales (anios). Trabajaremos con modelos de Efectos Fijos,
Efectos Aleatorios y Two-Way Fixed Effects aplicados a problemas reales de ciencias sociales.

**Nivel:** Avanzado
**Tecnologias:** Python, linearmodels, pandas, Altair
**Prerequisitos:** Estadistica basica, regresion lineal

---

## Objetivos de Aprendizaje

- Comprender la estructura de datos de panel (unidad x tiempo)
- Distinguir entre Pooled OLS, Efectos Fijos y Efectos Aleatorios
- Aplicar el Test de Hausman para elegir entre FE y RE
- Implementar Two-Way Fixed Effects (efectos de unidad + tiempo)
- Interpretar Odds Ratios en modelos logisticos
- Calcular efectos marginales en modelos no lineales

---

## Contenido del Modulo

El modulo completo esta en:

```
ejercicios/06_analisis_datos_de_panel/
├── 01_analisis_guns.py              # Panel: leyes de armas y criminalidad
├── 02_analisis_fatality.py          # TWFE: impuesto cerveza vs mortalidad
├── 03_dashboard_educativo.py        # Dashboard interactivo 4 pestanas
├── conceptos_visuales_panel.py      # Visualizaciones conceptuales
├── GUIA_PANEL_DATA.md               # Guia teorica completa
├── grafico_panel_guns.png           # Resultado del analisis
└── requirements.txt                 # linearmodels, altair, etc.
```

---

## Ejercicios Practicos

### 01 - Analisis Guns: Leyes de Armas y Criminalidad

**Pregunta:** Las leyes de portacion de armas reducen la criminalidad violenta?

- **Dataset:** [Guns](https://vincentarelbundock.github.io/Rdatasets/csv/AER/Guns.csv) (Stock & Watson) - 50 estados de EE.UU., 1977-1999
- **Variable dependiente:** `log(violent)` - tasa de criminalidad violenta (logaritmo)
- **Variable clave:** `law` - si el estado tiene ley "shall-carry" (portacion obligatoria)
- **Controles:** ingreso, poblacion, densidad
- **Modelos:** Pooled OLS vs Fixed Effects vs Random Effects
- **Metodologia:** Comparacion de los 3 modelos + Test de Hausman

```bash
python ejercicios/06_analisis_datos_de_panel/01_analisis_guns.py
```

### 02 - Analisis Fatality: Impuesto a la Cerveza y Mortalidad

**Pregunta:** Subir el impuesto a la cerveza reduce las muertes por accidentes de trafico?

- **Dataset:** [Fatalities](https://vincentarelbundock.github.io/Rdatasets/csv/AER/Fatalities.csv) (AER) - 48 estados, 1982-1988
- **Variable dependiente:** `fatality_rate` - muertes por 10,000 habitantes
- **Variable clave:** `beertax` - impuesto a la cerveza
- **Controles:** edad minima para beber (`drinkage`), desempleo, ingreso
- **Modelos:** Entity FE vs **Two-Way Fixed Effects** (estado + anio)
- **Innovacion:** TWFE controla tendencias temporales (coches mas seguros cada anio)

```bash
python ejercicios/06_analisis_datos_de_panel/02_analisis_fatality.py
```

### 03 - Dashboard Educativo Interactivo (Panel + Altair)

Dashboard local con 4 pestanas interactivas para explorar los conceptos visualmente:

1. **Pooled OLS:** Slider de heterogeneidad que muestra la Paradoja de Simpson en accion
2. **FE vs RE:** Explicacion y tabla de decision del Test de Hausman
3. **Odds Ratios:** Sliders para explorar probabilidad vs odds vs odds ratio en tiempo real
4. **Efectos Marginales:** Comparacion Lin-Lin, Log-Lin, Log-Log con graficos dinamicos

```bash
panel serve ejercicios/06_analisis_datos_de_panel/03_dashboard_educativo.py
# Abrir http://localhost:5006 en el navegador
```

### Archivos adicionales

- **`conceptos_visuales_panel.py`** - Genera graficos estaticos explicando los conceptos de panel
- **`dashboard_educativo_panel.py`** - Version alternativa del dashboard educativo
- **`GUIA_PANEL_DATA.md`** - Guia teorica completa: Pooled OLS, FE, RE, Hausman, TWFE

---

## Teoria: Conceptos Clave

### Que son los datos de panel?

Datos que combinan **corte transversal** (N unidades) con **serie temporal** (T periodos):

![Estructura de los Datos de Panel](../assets/slides/m6_panel_p02.jpg)

```
| pais | anio | democracia | pib_pc |
|------|------|------------|--------|
| ESP  | 2000 | 0.85       | 24000  |
| ESP  | 2001 | 0.86       | 24500  |
| FRA  | 2000 | 0.88       | 28000  |
| FRA  | 2001 | 0.89       | 28500  |
```

### Ingenieria de Datos: Formato Wide vs Long

![Ingenieria de Datos en Python: Wide vs Long](../assets/slides/m6_panel_p04.jpg)

### Pooled OLS vs Fixed Effects vs Random Effects

| Modelo | Supuesto | Cuando usarlo |
|--------|----------|---------------|
| **Pooled OLS** | No hay heterogeneidad individual | Rara vez apropiado |
| **Fixed Effects** | Heterogeneidad correlacionada con X | Ciencias sociales (regla general) |
| **Random Effects** | Heterogeneidad NO correlacionada con X | Encuestas aleatorias |

### El Modelo Ingenuo: Pooled OLS

![El Modelo Ingenuo: Pooled OLS](../assets/slides/m6_panel_p05.jpg)

### Heterogeneidad no Observada

![El Enemigo Invisible: Heterogeneidad no Observada](../assets/slides/m6_panel_p03.jpg)

### Test de Hausman

Decide entre FE y RE:

- **H0:** RE es consistente y eficiente (preferir RE)
- **H1:** Solo FE es consistente (preferir FE)
- Si p-valor < 0.05: usar **Fixed Effects**

---

## Dashboards

### Dashboard Educativo (local)

El dashboard principal de este modulo se ejecuta localmente con Panel (HoloViz):

```bash
panel serve ejercicios/06_analisis_datos_de_panel/03_dashboard_educativo.py
```

Incluye 4 pestanas interactivas: Pooled OLS, FE vs RE, Odds Ratios, Efectos Marginales.

### Dashboard QoG - Analisis Avanzado (GitHub Pages)

Como complemento, puedes explorar un dashboard con analisis de panel aplicado al dataset QoG
(4 lineas de investigacion con Spark + PostgreSQL + ML):

[Ver Dashboard QoG - Panel Data Aplicado](../dashboards/06_analisis_panel_qog.md){ .md-button }

---

## Recursos

### Documentacion
- [linearmodels Documentation](https://bashtage.github.io/linearmodels/)
- [Altair Documentation](https://altair-viz.github.io/)

### Referencias Teoricas
- Wooldridge, J. M. (2010). Econometric Analysis of Cross Section and Panel Data (2nd ed.). MIT Press.
- Stock, J. H., & Watson, M. W. (2019). Introduction to Econometrics (4th ed.). Pearson.

﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌​​‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​​‌‌​​​​‍​​‌‌​​​​‍​​‌‌​‌‌‌‍​​‌‌‌​​‌‍​‌‌​​​‌‌﻿---

**Curso:** Big Data con Python - De Cero a Produccion
**Profesor:** Juan Marcelo Gutierrez Miranda | @TodoEconometria
**Hash ID:** 4e8d9b1a5f6e7c3d2b1a0f9e8d7c6b5a4f3e2d1c0b9a8f7e6d5c4b3a2f1e0d9c
**Metodologia:** Ejercicios progresivos con datos reales y herramientas profesionales

**Referencias academicas:**

- Wooldridge, J. M. (2010). Econometric Analysis of Cross Section and Panel Data (2nd ed.). MIT Press.
- Stock, J. H., & Watson, M. W. (2019). Introduction to Econometrics (4th ed.). Pearson.
- Baltagi, B. H. (2021). Econometric Analysis of Panel Data (6th ed.). Springer.
