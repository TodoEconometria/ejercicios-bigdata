# Time Series: ARIMA/SARIMA (Box-Jenkins)﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌‌​​​‍​‌‌​​​‌‌‍​​‌‌​‌​​‍​‌‌​​​‌​‍​‌‌​​‌​​‍​​‌‌​​​‌‍​​‌‌​​‌​‍​​‌‌​‌‌‌﻿

Complete time series analysis following the Box-Jenkins methodology,﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌‌​​​‍​‌‌​​​‌‌‍​​‌‌​‌​​‍​‌‌​​​‌​‍​‌‌​​‌​​‍​​‌‌​​​‌‍​​‌‌​​‌​‍​​‌‌​‌‌‌﻿
from model identification to forecasting with confidence intervals.

[Open Interactive Dashboard](04_series_temporales_arima.html){target="_blank" .md-button .md-button--primary}

---

## Contents

The dashboard presents **6 interactive tabs**:

| Tab | Content |
|-----|---------|
| **Original Series** | Monthly airline passengers 1949-1960 (144 observations) |
| **Decomposition** | Trend + Seasonality + Residual (multiplicative) |
| **ACF / PACF** | Autocorrelation and partial autocorrelation of the differenced series |
| **Diagnostics** | Residuals, histogram, residual ACF, Q-Q plot |
| **Final Forecast** | Original series + SARIMA fit + 12-month forecast + 95% CI |
| **Radar Metrics** | RMSE, MAE, MAPE, R2 of the model |

---

## Box-Jenkins Methodology

1. **Identification:** ACF/PACF to determine orders (p, d, q)(P, D, Q)[s]
2. **Estimation:** Maximum likelihood fitting
3. **Diagnostics:** Ljung-Box and Jarque-Bera tests on residuals
4. **Forecasting:** Forecast with 95% confidence intervals

**Selected model:** SARIMA(1,1,0)(0,1,0)[12] -- AIC = -445.41

﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌‌​​​‍​‌‌​​​‌‌‍​​‌‌​‌​​‍​‌‌​​​‌​‍​‌‌​​‌​​‍​​‌‌​​​‌‍​​‌‌​​‌​‍​​‌‌​‌‌‌﻿---

## Source Code

- Full script: `ejercicios/04_machine_learning/07_series_temporales_arima/`
- Theoretical guide: `07_series_temporales_arima/README.md`
