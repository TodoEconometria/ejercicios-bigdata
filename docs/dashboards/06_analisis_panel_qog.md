# Modulo 06: Analisis de Datos de Panel (QoG)﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​‌​‌‍​‌‌​​​​‌‍​​‌‌​​​​‍​​‌‌​‌‌‌‍​​‌‌​‌​‌‍​‌‌​​​‌​‍​‌‌​​‌​​‍​​‌‌​‌​‌﻿

Dashboard interactivo con los resultados del pipeline Big Data sobre el﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​‌​‌‍​‌‌​​​​‌‍​​‌‌​​​​‍​​‌‌​‌‌‌‍​​‌‌​‌​‌‍​‌‌​​​‌​‍​‌‌​​‌​​‍​​‌‌​‌​‌﻿
**Quality of Government Standard Dataset** (University of Gothenburg, Enero 2024).

[Abrir Dashboard Interactivo](06_analisis_panel_qog.html){target="_blank" .md-button .md-button--primary}

---

## Contenido

El dashboard presenta **5 pestanas interactivas**:

| Pestana | Linea de investigacion | Paises |
|---------|----------------------|---------|
| **Asia Central** | Evolucion institucional post-sovietica | KAZ, UZB, TKM, KGZ, TJK |
| **Seguridad Hidrica** | Crisis del Mar de Aral | KAZ, UZB, TKM, AFG, IRN |
| **Terrorismo** | Estabilidad politica y fragilidad estatal | 13 paises (Europa + Asia Central + Oriente Medio) |
| **Maghreb** | Autoritarismo vs democracia, Primaveras Arabes | DZA, MAR, TUN, LBY, EGY, MRT |
| **ML: Clusters PCA** | Clasificacion de 28 paises (K-Means + PCA) | 28 paises de todas las lineas |

---

## Infraestructura

- **Procesamiento:** Apache Spark 3.5.4 (cluster Docker: 1 master + 2 workers)
- **Almacenamiento:** PostgreSQL 15 + Parquet
- **Clustering:** scikit-learn (K-Means k=5 + PCA 2 componentes)
- **Visualizacion:** Plotly (graficos interactivos)
- **Dataset:** 924 observaciones (28 paises x 33 anios), 40 variables

---

## Variables principales

| Variable | Fuente | Que mide |
|----------|--------|----------|
| `vdem_polyarchy` | V-Dem | Indice de democracia electoral |
| `ti_cpi` | Transparency International | Percepcion de corrupcion |
| `wbgi_cce` | World Bank | Control de corrupcion |
| `wbgi_rle` | World Bank | Estado de derecho |
| `wbgi_pse` | World Bank | Estabilidad politica |
| `wdi_gdppc` | World Bank | PIB per capita (USD 2015) |
| `undp_hdi` | UNDP | Indice de Desarrollo Humano |
| `ffp_fsi` | Fund for Peace | Indice de fragilidad estatal |

﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​‌​‌‍​‌‌​​​​‌‍​​‌‌​​​​‍​​‌‌​‌‌‌‍​​‌‌​‌​‌‍​‌‌​​​‌​‍​‌‌​​‌​​‍​​‌‌​‌​‌﻿---

## Codigo fuente

- Pipeline ETL + ML: `ejercicios/06_análisis_datos_de_panel/`
- Material teorico: `ejercicios/07_infraestructura_bigdata/`
