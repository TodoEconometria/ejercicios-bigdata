# Dashboard PRO: Series Temporales ARIMA/SARIMA﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​​‌​‍​‌‌​​‌​‌‍​​‌‌​‌​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​​‌‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​﻿

Dashboard interactivo con diseño profesional inspirado en terminales financieras tipo Bloomberg,﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​​‌​‍​‌‌​​‌​‌‍​​‌‌​‌​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​​‌‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​﻿
para el analisis completo de series temporales siguiendo la metodologia Box-Jenkins.

[Abrir Dashboard PRO](dashboard_arima_pro.html){target="_blank" .md-button .md-button--primary}

---

## Caracteristicas del Dashboard

| Elemento | Descripcion |
|----------|-------------|
| **Tema** | Oscuro tipo terminal financiera (inspirado Bloomberg/OECD Explorer) |
| **KPIs** | Cards con metricas en tiempo real: RMSE, MAE, MAPE, R2, AIC |
| **Pestanas** | 7 secciones interactivas con transiciones suaves |
| **Responsivo** | Adaptable a diferentes tamanos de pantalla |

---

## Contenido por Pestana

| # | Pestana | Descripcion |
|---|---------|-------------|
| 1 | **Serie Original** | Pasajeros aereos 1949-1960 con media movil 12M |
| 2 | **Descomposicion** | Tendencia + Estacionalidad + Residuo (multiplicativa) |
| 3 | **ACF / PACF** | Autocorrelacion de la serie diferenciada (d=1, D=1, s=12) |
| 4 | **Diagnostico** | Residuos, histograma, ACF residual, Q-Q plot |
| 5 | **Pronostico** | Serie + ajuste SARIMA + forecast 24 meses + IC 95% |
| 6 | **Metricas Radar** | Visualizacion polar de las metricas normalizadas |
| 7 | **Comparativa** | Comparacion de diferentes ordenes SARIMA |

---

## Inspiracion de Diseno

Este dashboard fue creado siguiendo las mejores practicas de visualizacion financiera:

- [OECD Pension Explorer](https://oecd-pension-explorer.plotly.app/) - Plotly App oficial de la OECD
- [Portfolio Optimizer](https://panel.holoviz.org/gallery/portfolio_optimizer.html) - Panel/HoloViz Gallery
- [Dash Bootstrap Templates](https://pypi.org/project/dash-bootstrap-templates/) - Temas profesionales para Dash

---

## Metodologia Box-Jenkins

1. **Identificacion:** Analisis ACF/PACF para determinar ordenes (p, d, q)(P, D, Q)[s]
2. **Estimacion:** Ajuste por maxima verosimilitud con SARIMAX
3. **Diagnostico:** Tests de Ljung-Box, Jarque-Bera, Q-Q plot
4. **Pronostico:** Forecast con intervalos de confianza al 95%

---

## Codigo Fuente

- Script de ejercicio: `ejercicios/04_machine_learning/07_series_temporales_arima/`
- Exportador dashboard: `.profesor/soluciones/TRABAJO_FINAL/export_arima_pro.py`
- Guia teorica: [Series Temporales ARIMA](../ejercicios/07-series-temporales-arima.md)

﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​​‌​‍​‌‌​​‌​‌‍​​‌‌​‌​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​​‌‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​﻿---

**Curso:** Big Data con Python - De Cero a Produccion
**Profesor:** Juan Marcelo Gutierrez Miranda | @TodoEconometria
**Hash ID:** 4e8d9b1a5f6e7c3d2b1a0f9e8d7c6b5a4f3e2d1c0b9a8f7e6d5c4b3a2f1e0d9c

**Referencias academicas:**

- Box, G.E.P. & Jenkins, G.M. (1976). *Time Series Analysis: Forecasting and Control*. Holden-Day.
- Hyndman, R.J. & Athanasopoulos, G. (2021). *Forecasting: Principles and Practice* (3rd ed.). OTexts.
- Hamilton, J.D. (1994). *Time Series Analysis*. Princeton University Press.
