# Series Temporales: ARIMA/SARIMA (Box-Jenkins)﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​‌​‌‍​​‌‌​​‌‌‍​​‌‌​​​‌‍​‌‌​​​‌​‍​‌‌​​‌​​‍​‌‌​​‌​​‍​​‌‌​​​‌‍​‌‌​​‌​‌﻿

Analisis completo de series temporales siguiendo la metodologia Box-Jenkins,﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​‌​‌‍​​‌‌​​‌‌‍​​‌‌​​​‌‍​‌‌​​​‌​‍​‌‌​​‌​​‍​‌‌​​‌​​‍​​‌‌​​​‌‍​‌‌​​‌​‌﻿
desde la identificacion del modelo hasta el pronostico con intervalos de confianza.

[Abrir Dashboard Interactivo](04_series_temporales_arima.html){target="_blank" .md-button .md-button--primary}

---

## Contenido

El dashboard presenta **6 pestanas interactivas**:

| Pestana | Contenido |
|---------|-----------|
| **Serie Original** | Pasajeros aereos mensuales 1949-1960 (144 observaciones) |
| **Descomposicion** | Tendencia + Estacionalidad + Residuo (multiplicativa) |
| **ACF / PACF** | Autocorrelacion y autocorrelacion parcial de la serie diferenciada |
| **Diagnostico** | Residuos, histograma, ACF residual, Q-Q plot |
| **Pronostico Final** | Serie original + ajuste SARIMA + forecast 12 meses + IC 95% |
| **Metricas Radar** | RMSE, MAE, MAPE, R2 del modelo |

---

## Metodologia Box-Jenkins

1. **Identificacion:** ACF/PACF para determinar ordenes (p, d, q)(P, D, Q)[s]
2. **Estimacion:** Ajuste por maxima verosimilitud
3. **Diagnostico:** Tests de Ljung-Box, Jarque-Bera sobre residuos
4. **Pronostico:** Forecast con intervalos de confianza al 95%

**Modelo seleccionado:** SARIMA(1,1,0)(0,1,0)[12] — AIC = -445.41

﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​‌​‌‍​​‌‌​​‌‌‍​​‌‌​​​‌‍​‌‌​​​‌​‍​‌‌​​‌​​‍​‌‌​​‌​​‍​​‌‌​​​‌‍​‌‌​​‌​‌﻿---

## Codigo fuente

- Script completo: `ejercicios/04_machine_learning/07_series_temporales_arima/`
- Guia teorica: `07_series_temporales_arima/README.md`
