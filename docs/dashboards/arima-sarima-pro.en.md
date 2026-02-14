# PRO Dashboard: ARIMA/SARIMA Time Series﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌‌​​​‍​‌‌​​​‌‌‍​​‌‌​​‌​‍​​‌‌​‌​‌‍​​‌‌‌​​‌‍​‌‌​​​‌‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​﻿

Interactive dashboard with a professional design inspired by Bloomberg-style financial terminals,﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌‌​​​‍​‌‌​​​‌‌‍​​‌‌​​‌​‍​​‌‌​‌​‌‍​​‌‌‌​​‌‍​‌‌​​​‌‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​﻿
for complete time series analysis following the Box-Jenkins methodology.

[Open PRO Dashboard](dashboard_arima_pro.html){target="_blank" .md-button .md-button--primary}

---

## Dashboard Features

| Element | Description |
|---------|-------------|
| **Theme** | Dark financial terminal style (inspired by Bloomberg/OECD Explorer) |
| **KPIs** | Cards with real-time metrics: RMSE, MAE, MAPE, R2, AIC |
| **Tabs** | 7 interactive sections with smooth transitions |
| **Responsive** | Adaptable to different screen sizes |

---

## Content by Tab

| # | Tab | Description |
|---|-----|-------------|
| 1 | **Original Series** | Airline passengers 1949-1960 with 12M moving average |
| 2 | **Decomposition** | Trend + Seasonality + Residual (multiplicative) |
| 3 | **ACF / PACF** | Autocorrelation of the differenced series (d=1, D=1, s=12) |
| 4 | **Diagnostics** | Residuals, histogram, residual ACF, Q-Q plot |
| 5 | **Forecast** | Series + SARIMA fit + 24-month forecast + 95% CI |
| 6 | **Radar Metrics** | Polar visualization of normalized metrics |
| 7 | **Comparison** | Comparison of different SARIMA orders |

---

## Design Inspiration

This dashboard was created following best practices in financial visualization:

- [OECD Pension Explorer](https://oecd-pension-explorer.plotly.app/) - Official OECD Plotly App
- [Portfolio Optimizer](https://panel.holoviz.org/gallery/portfolio_optimizer.html) - Panel/HoloViz Gallery
- [Dash Bootstrap Templates](https://pypi.org/project/dash-bootstrap-templates/) - Professional themes for Dash

---

## Box-Jenkins Methodology

1. **Identification:** ACF/PACF analysis to determine orders (p, d, q)(P, D, Q)[s]
2. **Estimation:** Maximum likelihood fitting with SARIMAX
3. **Diagnostics:** Ljung-Box, Jarque-Bera tests, Q-Q plot
4. **Forecasting:** Forecast with 95% confidence intervals

---

## Source Code

- Exercise script: `ejercicios/04_machine_learning/07_series_temporales_arima/`
- Dashboard exporter: `.profesor/soluciones/TRABAJO_FINAL/export_arima_pro.py`
- Theoretical guide: [ARIMA Time Series](../ejercicios/07-series-temporales-arima.md)

﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌‌​​​‍​‌‌​​​‌‌‍​​‌‌​​‌​‍​​‌‌​‌​‌‍​​‌‌‌​​‌‍​‌‌​​​‌‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​﻿---

**Course:** Big Data with Python - From Zero to Production
**Professor:** Juan Marcelo Gutierrez Miranda | @TodoEconometria
**Hash ID:** 4e8d9b1a5f6e7c3d2b1a0f9e8d7c6b5a4f3e2d1c0b9a8f7e6d5c4b3a2f1e0d9c

**Academic references:**

- Box, G.E.P. & Jenkins, G.M. (1976). *Time Series Analysis: Forecasting and Control*. Holden-Day.
- Hyndman, R.J. & Athanasopoulos, G. (2021). *Forecasting: Principles and Practice* (3rd ed.). OTexts.
- Hamilton, J.D. (1994). *Time Series Analysis*. Princeton University Press.
