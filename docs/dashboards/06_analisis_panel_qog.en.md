# Module 06: Panel Data Analysis (QoG)﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​​‌‌​‌​​‍​​‌‌​‌​​‍​‌‌​​​‌​‍​​‌‌​​‌​‍​​‌‌​‌‌​﻿

Interactive dashboard with results from the Big Data pipeline on the﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​​‌‌​‌​​‍​​‌‌​‌​​‍​‌‌​​​‌​‍​​‌‌​​‌​‍​​‌‌​‌‌​﻿
**Quality of Government Standard Dataset** (University of Gothenburg, January 2024).

[Open Interactive Dashboard](06_analisis_panel_qog.html){target="_blank" .md-button .md-button--primary}

---

## Contents

The dashboard presents **5 interactive tabs**:

| Tab | Research Line | Countries |
|-----|--------------|---------|
| **Central Asia** | Post-Soviet institutional evolution | KAZ, UZB, TKM, KGZ, TJK |
| **Water Security** | Aral Sea crisis | KAZ, UZB, TKM, AFG, IRN |
| **Terrorism** | Political stability and state fragility | 13 countries (Europe + Central Asia + Middle East) |
| **Maghreb** | Authoritarianism vs democracy, Arab Springs | DZA, MAR, TUN, LBY, EGY, MRT |
| **ML: PCA Clusters** | Classification of 28 countries (K-Means + PCA) | 28 countries from all research lines |

---

## Infrastructure

- **Processing:** Apache Spark 3.5.4 (Docker cluster: 1 master + 2 workers)
- **Storage:** PostgreSQL 15 + Parquet
- **Clustering:** scikit-learn (K-Means k=5 + PCA 2 components)
- **Visualization:** Plotly (interactive charts)
- **Dataset:** 924 observations (28 countries x 33 years), 40 variables

---

## Main Variables

| Variable | Source | What it measures |
|----------|--------|-----------------|
| `vdem_polyarchy` | V-Dem | Electoral democracy index |
| `ti_cpi` | Transparency International | Corruption perception |
| `wbgi_cce` | World Bank | Control of corruption |
| `wbgi_rle` | World Bank | Rule of law |
| `wbgi_pse` | World Bank | Political stability |
| `wdi_gdppc` | World Bank | GDP per capita (USD 2015) |
| `undp_hdi` | UNDP | Human Development Index |
| `ffp_fsi` | Fund for Peace | State fragility index |

﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​​‌‌​‌​​‍​​‌‌​‌​​‍​‌‌​​​‌​‍​​‌‌​​‌​‍​​‌‌​‌‌​﻿---

## Source Code

- ETL + ML Pipeline: `ejercicios/06_análisis_datos_de_panel/`
- Theoretical material: `ejercicios/07_infraestructura_bigdata/`
