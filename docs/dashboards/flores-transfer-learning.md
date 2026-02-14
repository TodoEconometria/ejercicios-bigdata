# Dashboard: Clasificación de Flores con Transfer Learning﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​​‌‌‍​‌‌​​‌‌​‍​​‌‌​‌​‌‍​​‌‌​‌​​‍​​‌‌​​​​‍​‌‌​​​​‌‍​​‌‌​​​‌‍​​‌‌​​‌‌﻿

## Descripción

Pipeline de **Computer Vision** que clasifica imágenes de flores usando **Transfer Learning** con MobileNetV2.﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​​‌‌‍​‌‌​​‌‌​‍​​‌‌​‌​‌‍​​‌‌​‌​​‍​​‌‌​​​​‍​‌‌​​​​‌‍​​‌‌​​​‌‍​​‌‌​​‌‌﻿

**¿Qué es Transfer Learning?** En lugar de entrenar una red neuronal desde cero (necesitaríamos millones de imágenes), usamos una red ya entrenada en ImageNet y la adaptamos a nuestro problema.

## Pipeline

```
1. DESCARGA          2. EMBEDDINGS         3. CLASIFICACIÓN      4. VISUALIZACIÓN
   3,670 flores         MobileNetV2           ML tradicional        Dashboard
   5 clases             1280 features         KNN/SVM/RF            Plotly
```

## Resultados

| Modelo | Accuracy |
|--------|----------|
| **SVM** | **89.9%** |
| Random Forest | 86.5% |
| KNN | 86.2% |

## Visualizaciones

El dashboard incluye 4 pestañas interactivas:

1. **t-SNE**: Proyección 2D de los embeddings - flores similares aparecen juntas
2. **Comparativa**: Barras con accuracy de cada modelo
3. **Confusion Matrix**: Aciertos/errores por clase (porcentajes)
4. **Distribución**: Radar chart del dataset

## Ver Dashboard

<div class="dashboard-link">
<a href="dashboard_flores.html" target="_blank" class="md-button md-button--primary">
    Abrir Dashboard Interactivo
</a>
</div>

## Ejecutar el Ejercicio

```bash
cd ejercicios/04_machine_learning/flores_transfer_learning/
pip install -r requirements.txt
python 01_flores_transfer_learning.py
```

**Requisitos:** TensorFlow (GPU recomendado pero funciona en CPU)

﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​​‌‌‍​‌‌​​‌‌​‍​​‌‌​‌​‌‍​​‌‌​‌​​‍​​‌‌​​​​‍​‌‌​​​​‌‍​​‌‌​​​‌‍​​‌‌​​‌‌﻿---
**Curso:** Big Data con Python - De Cero a Producción
**Profesor:** Juan Marcelo Gutierrez Miranda | @TodoEconometria
**Hash ID:** 4e8d9b1a5f6e7c3d2b1a0f9e8d7c6b5a4f3e2d1c0b9a8f7e6d5c4b3a2f1e0d9c

**Referencias académicas:**

- Sandler, M., et al. (2018). MobileNetV2: Inverted Residuals and Linear Bottlenecks. CVPR.
- Yosinski, J., et al. (2014). How transferable are features in deep neural networks? NeurIPS.
- van der Maaten, L. & Hinton, G. (2008). Visualizing Data using t-SNE. JMLR.
