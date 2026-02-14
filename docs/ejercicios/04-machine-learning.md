# Módulo 04: Machine Learning﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​‌‌​‍​​‌‌​‌‌‌‍​‌‌​​‌​‌‍​​‌‌​​​‌‍​‌‌​​‌​‌‍​‌‌​​​‌‌‍​​‌‌​​‌​‍​‌‌​​‌​​﻿

Técnicas de aprendizaje automático aplicadas a Big Data: desde clustering tradicional hasta Computer Vision con Deep Learning.﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​‌‌​‍​​‌‌​‌‌‌‍​‌‌​​‌​‌‍​​‌‌​​​‌‍​‌‌​​‌​‌‍​‌‌​​​‌‌‍​​‌‌​​‌​‍​‌‌​​‌​​﻿

---

## Ejercicio 4.1: PCA y Clustering

Aplicamos técnicas de aprendizaje no supervisado para detectar patrones en datos complejos.

### Alcance
- **Reducción de Dimensionalidad:** Principal Component Analysis (PCA)
- **Clustering:** K-Means y Hierarchical Clustering (HCA)

### Tareas
1. **PCA:** Reducir variables a 2 componentes principales para visualización
2. **Clustering:** Implementar K-Means y determinar K óptimo (método del codo, Silhouette)
3. **Interpretación:** Generar perfil de cada cluster

### Recursos
- [Dashboard PCA + K-Means Iris](../dashboards/02_pca_iris_clustering.md)
- [Dashboard PCA estilo FactoMineR](../dashboards/02_PCA_FactoMineR_style.md)

---

## Ejercicio 4.2: Transfer Learning - Clasificación de Flores

Pipeline de **Computer Vision** que clasifica imágenes de flores usando Transfer Learning con MobileNetV2.

### ¿Qué es Transfer Learning?

En lugar de entrenar una red neuronal desde cero (necesitaríamos millones de imágenes), usamos una red ya entrenada en ImageNet y la adaptamos:

```
ImageNet (14M imgs) → MobileNetV2 → Embeddings (1280D) → Clasificador ML
```

Las primeras capas de la CNN ya aprendieron patrones universales (bordes, texturas, formas) que sirven para cualquier imagen.

### Pipeline

```
1. DESCARGA          2. EMBEDDINGS         3. CLASIFICACIÓN      4. VISUALIZACIÓN
   3,670 flores         MobileNetV2           ML tradicional        Dashboard
   5 clases             1280 features         KNN/SVM/RF            Plotly
```

### Resultados

| Modelo | Accuracy |
|--------|----------|
| **SVM** | **89.9%** |
| Random Forest | 86.5% |
| KNN | 86.2% |

### Ejecutar

```bash
cd ejercicios/04_machine_learning/flores_transfer_learning/
pip install -r requirements.txt
python 01_flores_transfer_learning.py
```

**Requisitos:** TensorFlow (GPU recomendado pero funciona en CPU)

### Recursos
- [Dashboard Transfer Learning Flores](../dashboards/flores-transfer-learning.md) - Galería, t-SNE, Comparativa, Confusion Matrix
- [Dashboard Interactivo](../dashboards/dashboard_flores.html){target="_blank"}

---

## Ejercicio 4.3: Series Temporales (ARIMA/SARIMA)

Metodología Box-Jenkins para análisis y pronóstico de series temporales.

### Recursos
- [ARIMA/SARIMA - Metodología Box-Jenkins](07-series-temporales-arima.md)
- [Dashboard ARIMA Interactivo](../dashboards/04_series_temporales_arima.html){target="_blank"}

﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​‌‌​‍​​‌‌​‌‌‌‍​‌‌​​‌​‌‍​​‌‌​​​‌‍​‌‌​​‌​‌‍​‌‌​​​‌‌‍​​‌‌​​‌​‍​‌‌​​‌​​﻿---

**Curso:** Big Data con Python - De Cero a Producción
**Profesor:** Juan Marcelo Gutierrez Miranda | @TodoEconometria
**Hash ID:** 4e8d9b1a5f6e7c3d2b1a0f9e8d7c6b5a4f3e2d1c0b9a8f7e6d5c4b3a2f1e0d9c

**Referencias académicas:**

- Pedregosa, F., et al. (2011). Scikit-learn: Machine Learning in Python. JMLR 12.
- Sandler, M., et al. (2018). MobileNetV2: Inverted Residuals and Linear Bottlenecks. CVPR.
- van der Maaten, L. & Hinton, G. (2008). Visualizing Data using t-SNE. JMLR.
