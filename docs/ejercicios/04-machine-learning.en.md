# Module 04: Machine Learning﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​​‌​‍​​‌‌​‌‌​‍​‌‌​​‌‌​‍​‌‌​​​‌‌‍​‌‌​​​‌​‍​‌‌​​‌​‌‍​‌‌​​‌​​‍​​‌‌​‌‌​﻿

Machine learning techniques applied to Big Data: from traditional clustering to Computer Vision with Deep Learning.﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​​‌​‍​​‌‌​‌‌​‍​‌‌​​‌‌​‍​‌‌​​​‌‌‍​‌‌​​​‌​‍​‌‌​​‌​‌‍​‌‌​​‌​​‍​​‌‌​‌‌​﻿

---

## Exercise 4.1: PCA and Clustering

We apply unsupervised learning techniques to detect patterns in complex data.

### Scope
- **Dimensionality Reduction:** Principal Component Analysis (PCA)
- **Clustering:** K-Means and Hierarchical Clustering (HCA)

### Tasks
1. **PCA:** Reduce variables to 2 principal components for visualization
2. **Clustering:** Implement K-Means and determine optimal K (elbow method, Silhouette)
3. **Interpretation:** Generate a profile for each cluster

### Resources
- [Dashboard PCA + K-Means Iris](../dashboards/02_pca_iris_clustering.md)
- [Dashboard PCA FactoMineR style](../dashboards/02_PCA_FactoMineR_style.md)

---

## Exercise 4.2: Transfer Learning - Flower Classification

**Computer Vision** pipeline that classifies flower images using Transfer Learning with MobileNetV2.

### What is Transfer Learning?

Instead of training a neural network from scratch (which would require millions of images), we use a network already trained on ImageNet and adapt it:

```
ImageNet (14M imgs) → MobileNetV2 → Embeddings (1280D) → ML Classifier
```

The first layers of the CNN have already learned universal patterns (edges, textures, shapes) that are useful for any image.

### Pipeline

```
1. DOWNLOAD           2. EMBEDDINGS         3. CLASSIFICATION     4. VISUALIZATION
   3,670 flowers         MobileNetV2           Traditional ML        Dashboard
   5 classes             1280 features         KNN/SVM/RF            Plotly
```

### Results

| Model | Accuracy |
|--------|----------|
| **SVM** | **89.9%** |
| Random Forest | 86.5% |
| KNN | 86.2% |

### Run

```bash
cd ejercicios/04_machine_learning/flores_transfer_learning/
pip install -r requirements.txt
python 01_flores_transfer_learning.py
```

**Requirements:** TensorFlow (GPU recommended but works on CPU)

### Resources
- [Transfer Learning Flowers Dashboard](../dashboards/flores-transfer-learning.md) - Gallery, t-SNE, Comparison, Confusion Matrix
- [Interactive Dashboard](../dashboards/dashboard_flores.html){target="_blank"}

---

## Exercise 4.3: Time Series (ARIMA/SARIMA)

Box-Jenkins methodology for time series analysis and forecasting.

### Resources
- [ARIMA/SARIMA - Box-Jenkins Methodology](07-series-temporales-arima.md)
- [Interactive ARIMA Dashboard](../dashboards/04_series_temporales_arima.html){target="_blank"}

﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​​‌​‍​​‌‌​‌‌​‍​‌‌​​‌‌​‍​‌‌​​​‌‌‍​‌‌​​​‌​‍​‌‌​​‌​‌‍​‌‌​​‌​​‍​​‌‌​‌‌​﻿---

**Course:** Big Data with Python - From Zero to Production
**Instructor:** Juan Marcelo Gutierrez Miranda | @TodoEconometria
**Hash ID:** 4e8d9b1a5f6e7c3d2b1a0f9e8d7c6b5a4f3e2d1c0b9a8f7e6d5c4b3a2f1e0d9c

**Academic references:**

- Pedregosa, F., et al. (2011). Scikit-learn: Machine Learning in Python. JMLR 12.
- Sandler, M., et al. (2018). MobileNetV2: Inverted Residuals and Linear Bottlenecks. CVPR.
- van der Maaten, L. & Hinton, G. (2008). Visualizing Data using t-SNE. JMLR.
