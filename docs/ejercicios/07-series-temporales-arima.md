# Series Temporales: ARIMA/SARIMA con Metodologia Box-Jenkins﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌​‌‌‌‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​​‌‌​​‌‌‍​​‌‌‌​​​‍​​‌‌​‌​‌‍​​‌‌​​‌‌‍​​‌‌​‌​‌﻿

> **Estado:** Disponible

---

## Descripcion General

Aprenderemos a modelar series temporales utilizando la **Metodologia Box-Jenkins** completa:﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌​‌‌‌‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​​‌‌​​‌‌‍​​‌‌‌​​​‍​​‌‌​‌​‌‍​​‌‌​​‌‌‍​​‌‌​‌​‌﻿
identificacion, estimacion, diagnostico y pronostico. Trabajaremos con modelos ARIMA y SARIMA
para capturar tanto tendencias como estacionalidad.

**Nivel:** Avanzado
**Dataset:** AirPassengers (144 observaciones mensuales, 1949-1960)
**Tecnologias:** Python, statsmodels, matplotlib

---

## Objetivos de Aprendizaje

- Comprender la Metodologia Box-Jenkins (4 fases)
- Identificar componentes de una serie: tendencia, estacionalidad, ruido
- Usar ACF y PACF para determinar ordenes p, d, q
- Estimar modelos ARIMA y SARIMA
- Diagnosticar residuos (Ljung-Box, normalidad)
- Generar pronosticos con intervalos de confianza

---

## Contenido del Ejercicio

El ejercicio completo esta en:

```
ejercicios/04_machine_learning/07_series_temporales_arima/
├── README.md                    # Teoria Box-Jenkins completa (829 lineas)
├── serie_temporal_completa.py   # Script 10 partes (1,286 lineas)
├── output/                      # Directorio para graficos generados
└── .gitignore                   # Excluye output/*.png y *.csv
```

### El script `serie_temporal_completa.py` cubre:

1. **Carga y visualizacion** de la serie original
2. **Descomposicion** (tendencia + estacionalidad + residuo)
3. **Tests de estacionariedad** (ADF, KPSS)
4. **Diferenciacion** regular y estacional
5. **ACF/PACF** para identificacion de ordenes
6. **Estimacion ARIMA** con seleccion por AIC
7. **Estimacion SARIMA** con componente estacional
8. **Diagnostico de residuos** (Ljung-Box, QQ-plot, ACF residuos)
9. **Pronostico** con intervalos de confianza
10. **Comparacion** de modelos y metricas (MAPE, RMSE)

---

## Teoria: Metodologia Box-Jenkins

### Anatomia de la Senal: El Proceso Generador de Datos

![Anatomia de la Senal: El Proceso Generador de Datos](../assets/slides/m4_arima_bj_p02.jpg)

### Estacionariedad y Ruido Blanco

![El Objetivo Matematico: Estacionariedad y Ruido Blanco](../assets/slides/m4_arima_bj_p03.jpg)

### Descomposicion de la Serie

![Anatomia de una Senal: Descomponiendo la Serie](../assets/slides/m4_arima_ts_p02.jpg)

### Transformacion y Diferenciacion

![Preparando el Terreno: Transformacion y Diferenciacion](../assets/slides/m4_arima_ts_p04.jpg)

### El Decodificador Clasico: ARIMA

![La Metodologia Box-Jenkins (ARIMA)](../assets/slides/m4_arima_bj_p04.jpg)

### Desestacionalizacion y SARIMA

![Capturando el Ritmo: Desestacionalizacion y SARIMA](../assets/slides/m4_arima_bj_p05.jpg)

### El Flujo de Trabajo Box-Jenkins

![La Metodologia Box-Jenkins: El Flujo de Trabajo](../assets/slides/m4_arima_ts_p05.jpg)

### Fase 1: Identificacion

- Visualizar la serie y detectar tendencia/estacionalidad
- Aplicar diferenciacion para lograr estacionariedad
- Analizar ACF y PACF para determinar ordenes (p, d, q)

### Fase 2: Estimacion

- Ajustar modelo ARIMA(p,d,q) o SARIMA(p,d,q)(P,D,Q)[s]
- Comparar modelos candidatos usando AIC/BIC

### Fase 3: Diagnostico

- Verificar que los residuos sean ruido blanco
- Test de Ljung-Box (autocorrelacion)
- Test de normalidad
- Grafico QQ

### Fase 4: Pronostico

- Generar predicciones con intervalos de confianza
- Evaluar precision con metricas (MAPE, RMSE)

---

## Resultado del Ejercicio

**Modelo seleccionado:** SARIMA(1,1,0)(0,1,0)[12]

- AIC: -445.41
- MAPE: 7.41%
- Captura correctamente tendencia y estacionalidad mensual

---

## Dashboard Interactivo

Puedes explorar los resultados en el dashboard interactivo:

[Ver Dashboard ARIMA/SARIMA](../dashboards/04_series_temporales_arima.md){ .md-button .md-button--primary }

El dashboard incluye 6 pestanas con graficos Plotly interactivos:
serie original, descomposicion, estacionariedad, ACF/PACF, diagnostico y pronostico.

---

## Recursos

- [statsmodels ARIMA Documentation](https://www.statsmodels.org/stable/generated/statsmodels.tsa.arima.model.ARIMA.html)
- [statsmodels SARIMAX](https://www.statsmodels.org/stable/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.html)

﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌​‌‌‌‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​​‌‌​​‌‌‍​​‌‌‌​​​‍​​‌‌​‌​‌‍​​‌‌​​‌‌‍​​‌‌​‌​‌﻿---

**Curso:** Big Data con Python - De Cero a Produccion
**Profesor:** Juan Marcelo Gutierrez Miranda | @TodoEconometria
**Hash ID:** 4e8d9b1a5f6e7c3d2b1a0f9e8d7c6b5a4f3e2d1c0b9a8f7e6d5c4b3a2f1e0d9c
**Metodologia:** Ejercicios progresivos con datos reales y herramientas profesionales

**Referencias academicas:**

- Box, G. E. P., Jenkins, G. M., Reinsel, G. C., & Ljung, G. M. (2015). Time Series Analysis: Forecasting and Control (5th ed.). Wiley.
- Hyndman, R. J., & Athanasopoulos, G. (2021). Forecasting: Principles and Practice (3rd ed.). OTexts.
- Hamilton, J. D. (1994). Time Series Analysis. Princeton University Press.
