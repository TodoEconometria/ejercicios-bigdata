# Galeria de Visualizaciones y Dashboards﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​‌​​‍​​‌‌​‌‌​‍​​‌‌‌​​​‍​​‌‌​​​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​​​‌‍​​‌‌‌​​​﻿

Resultados de los algoritmos de Machine Learning y NLP del curso.﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​‌​​‍​​‌‌​‌‌​‍​​‌‌‌​​​‍​​‌‌​​​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​​​‌‍​​‌‌‌​​​﻿
Cada pagina incluye analisis, graficos y codigo fuente.

---

## Machine Learning

### Analisis completos

- [PCA + Clustering K-Means: Dataset Iris](02_pca_iris_clustering.md) -- Reduccion dimensional y agrupamiento sobre el dataset clasico de Fisher
- [Manual PCA estilo FactoMineR](02_PCA_FactoMineR_style.md) -- Replicando el estandar de oro del analisis multivariante en Python

### Series Temporales

- [ARIMA/SARIMA - Metodologia Box-Jenkins](04_series_temporales_arima.md) -- Identificacion, estimacion, diagnostico y pronostico
- [Dashboard ARIMA (interactivo)](04_series_temporales_arima.html){target="_blank"} -- 6 pestanas: serie, descomposicion, ACF/PACF, diagnostico, forecast, radar
- [Dashboard ARIMA PRO](arima-sarima-pro.md) -- Tema financiero tipo Bloomberg, KPIs, 7 pestanas, comparativa de modelos
- [Dashboard ARIMA PRO (interactivo)](dashboard_arima_pro.html){target="_blank"} -- Diseno inspirado en OECD Explorer y Portfolio Optimizer

### Computer Vision (Transfer Learning)

- [Clasificacion de Flores con Transfer Learning](flores-transfer-learning.md) -- MobileNetV2 + ML tradicional sobre embeddings
- [Dashboard Flores (interactivo)](dashboard_flores.html){target="_blank"} -- t-SNE, comparativa modelos, confusion matrix, radar

### Dashboards interactivos (HTML)

- [Dashboard PCA Iris (interactivo)](02_pca_iris_dashboard.html){target="_blank"} -- Visualizacion completa en pantalla
- [Dashboard FactoMineR (interactivo)](02_PCA_FactoMineR_style.html){target="_blank"} -- Circulos de correlacion y biplots

---

## NLP y Text Mining

### Ejercicios guiados

- [Ejercicio 01: Anatomia del Texto y Conteo de Palabras](EJERCICIO_01_CONTEO.md) -- Frecuencia, tokenizacion y visualizacion
- [Ejercicio 02: Filtro de Stopwords](EJERCICIO_02_LIMPIEZA.md) -- Limpieza de ruido semantico

### Analisis completos

- [Similitud de Jaccard](04_similitud_jaccard.md) -- Comparacion de documentos y sistema de recomendacion
- [Vectorizacion y Clustering de Documentos](05_vectorizacion_y_clustering.md) -- TF-IDF, K-Means y analisis de topicos

---

## Analisis de Datos de Panel (Big Data)

### Pipeline completo: Spark + PostgreSQL + ML

- [Modulo 06: QoG - 4 Lineas de Investigacion + ML](06_analisis_panel_qog.md) -- Asia Central, Seguridad Hidrica, Terrorismo, Maghreb, PCA + K-Means
- [Dashboard QoG (interactivo)](06_analisis_panel_qog.html){target="_blank"} -- 5 pestanas con graficos Plotly interactivos

---

## Streaming y Cloud (Tiempo Real)

### Dashboards en vivo

- [Observatorio Sismico Global](dashboard_sismos_global.md) -- Sismos en tiempo real desde USGS API
- [Dashboard Sismos (interactivo)](dashboard_sismos_global.html){target="_blank"} -- Mapa Leaflet con datos en vivo, filtros por categoria
- [ISS Tracker](dashboard_iss_tracker.md) -- Seguimiento de la Estacion Espacial Internacional
- [Dashboard ISS (interactivo)](dashboard_iss_tracker.html){target="_blank"} -- Posicion en tiempo real, predictor de pases, trayectoria orbital

### Tecnologias

- **APIs en vivo:** USGS Earthquakes, Where The ISS At, Open Notify
- **Visualizacion:** Leaflet.js, CARTO dark tiles, Lucide icons
- **Actualizacion:** Auto-refresh cada 5-30 segundos

﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​‌​​‍​​‌‌​‌‌​‍​​‌‌‌​​​‍​​‌‌​​​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​​​‌‍​​‌‌‌​​​﻿---

## Codigo fuente

Los scripts que generan estas visualizaciones estan en:

- `ejercicios/04_machine_learning/` -- PCA, K-Means, Silhouette
- `ejercicios/05_nlp_text_mining/` -- Conteo, limpieza, sentimiento, Jaccard
- `ejercicios/06_análisis_datos_de_panel/` -- Pipeline QoG con Apache Spark
- `ejercicios/07_infraestructura_bigdata/` -- Docker Compose, Cluster Spark
- `ejercicios/08_streaming_kafka/` -- Kafka, Spark Structured Streaming
- `ejercicios/09_cloud_localstack/` -- LocalStack, Terraform, AWS
