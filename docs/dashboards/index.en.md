# Visualization and Dashboard Gallery﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​‌​‌‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​‌​‌‍​‌‌​​​​‌‍​‌‌​​‌‌​‍​​‌‌​‌​​‍​​‌‌​​​​﻿

Results from the Machine Learning and NLP algorithms of the course.﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​‌​‌‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​‌​‌‍​‌‌​​​​‌‍​‌‌​​‌‌​‍​​‌‌​‌​​‍​​‌‌​​​​﻿
Each page includes analysis, charts, and source code.

---

## Machine Learning

### Full Analyses

- [PCA + K-Means Clustering: Iris Dataset](02_pca_iris_clustering.md) -- Dimensionality reduction and clustering on Fisher's classic dataset
- [Manual PCA FactoMineR Style](02_PCA_FactoMineR_style.md) -- Replicating the gold standard of multivariate analysis in Python

### Time Series

- [ARIMA/SARIMA - Box-Jenkins Methodology](04_series_temporales_arima.md) -- Identification, estimation, diagnostics, and forecasting
- [ARIMA Dashboard (interactive)](04_series_temporales_arima.html){target="_blank"} -- 6 tabs: series, decomposition, ACF/PACF, diagnostics, forecast, radar
- [ARIMA PRO Dashboard](arima-sarima-pro.md) -- Bloomberg-style financial theme, KPIs, 7 tabs, model comparison
- [ARIMA PRO Dashboard (interactive)](dashboard_arima_pro.html){target="_blank"} -- Design inspired by OECD Explorer and Portfolio Optimizer

### Computer Vision (Transfer Learning)

- [Flower Classification with Transfer Learning](flores-transfer-learning.md) -- MobileNetV2 + traditional ML on embeddings
- [Flowers Dashboard (interactive)](dashboard_flores.html){target="_blank"} -- t-SNE, model comparison, confusion matrix, radar

### Interactive Dashboards (HTML)

- [PCA Iris Dashboard (interactive)](02_pca_iris_dashboard.html){target="_blank"} -- Full-screen visualization
- [FactoMineR Dashboard (interactive)](02_PCA_FactoMineR_style.html){target="_blank"} -- Correlation circles and biplots

---

## NLP and Text Mining

### Guided Exercises

- [Exercise 01: Text Anatomy and Word Counting](EJERCICIO_01_CONTEO.md) -- Frequency, tokenization, and visualization
- [Exercise 02: Stopword Filtering](EJERCICIO_02_LIMPIEZA.md) -- Semantic noise cleaning

### Full Analyses

- [Jaccard Similarity](04_similitud_jaccard.md) -- Document comparison and recommendation system
- [Document Vectorization and Clustering](05_vectorizacion_y_clustering.md) -- TF-IDF, K-Means, and topic analysis

---

## Panel Data Analysis (Big Data)

### Full Pipeline: Spark + PostgreSQL + ML

- [Module 06: QoG - 4 Research Lines + ML](06_analisis_panel_qog.md) -- Central Asia, Water Security, Terrorism, Maghreb, PCA + K-Means
- [QoG Dashboard (interactive)](06_analisis_panel_qog.html){target="_blank"} -- 5 tabs with interactive Plotly charts

---

## Streaming and Cloud (Real-Time)

### Live Dashboards

- [Global Seismic Observatory](dashboard_sismos_global.md) -- Real-time earthquakes from USGS API
- [Earthquake Dashboard (interactive)](dashboard_sismos_global.html){target="_blank"} -- Leaflet map with live data, category filters
- [ISS Tracker](dashboard_iss_tracker.md) -- International Space Station tracking
- [ISS Dashboard (interactive)](dashboard_iss_tracker.html){target="_blank"} -- Real-time position, pass predictor, orbital trajectory

### Technologies

- **Live APIs:** USGS Earthquakes, Where The ISS At, Open Notify
- **Visualization:** Leaflet.js, CARTO dark tiles, Lucide icons
- **Refresh rate:** Auto-refresh every 5-30 seconds

﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​‌​‌‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​‌​‌‍​‌‌​​​​‌‍​‌‌​​‌‌​‍​​‌‌​‌​​‍​​‌‌​​​​﻿---

## Source Code

The scripts that generate these visualizations are located in:

- `ejercicios/04_machine_learning/` -- PCA, K-Means, Silhouette
- `ejercicios/05_nlp_text_mining/` -- Counting, cleaning, sentiment, Jaccard
- `ejercicios/06_análisis_datos_de_panel/` -- QoG Pipeline with Apache Spark
- `ejercicios/07_infraestructura_bigdata/` -- Docker Compose, Spark Cluster
- `ejercicios/08_streaming_kafka/` -- Kafka, Spark Structured Streaming
- `ejercicios/09_cloud_localstack/` -- LocalStack, Terraform, AWS
