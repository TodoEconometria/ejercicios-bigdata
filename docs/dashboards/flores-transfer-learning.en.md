# Dashboard: Flower Classification with Transfer Learning﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌​‌‌​‍​​‌‌​‌‌​‍​​‌‌‌​​​‍​‌‌​​​​‌‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​​‌​‍​​‌‌​‌​​﻿

## Description

**Computer Vision** pipeline that classifies flower images using **Transfer Learning** with MobileNetV2.

**What is Transfer Learning?** Instead of training a neural network from scratch (which would require millions of images), we use a network already trained on ImageNet and adapt it to our problem.

## Pipeline

```
1. DOWNLOAD           2. EMBEDDINGS         3. CLASSIFICATION      4. VISUALIZATION﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌​‌‌​‍​​‌‌​‌‌​‍​​‌‌‌​​​‍​‌‌​​​​‌‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​​‌​‍​​‌‌​‌​​﻿
   3,670 flowers         MobileNetV2           Traditional ML         Dashboard
   5 classes             1280 features         KNN/SVM/RF             Plotly
```

## Results

| Model | Accuracy |
|-------|----------|
| **SVM** | **89.9%** |
| Random Forest | 86.5% |
| KNN | 86.2% |

## Visualizations

The dashboard includes 4 interactive tabs:

1. **t-SNE**: 2D projection of embeddings - similar flowers appear together
2. **Comparison**: Bars with accuracy for each model
3. **Confusion Matrix**: Hits/errors by class (percentages)
4. **Distribution**: Radar chart of the dataset

## View Dashboard

<div class="dashboard-link">
<a href="dashboard_flores.html" target="_blank" class="md-button md-button--primary">
    Open Interactive Dashboard
</a>
</div>

## Run the Exercise

```bash
cd ejercicios/04_machine_learning/flores_transfer_learning/
pip install -r requirements.txt
python 01_flores_transfer_learning.py
```

**Requirements:** TensorFlow (GPU recommended but works on CPU)

﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌​‌‌​‍​​‌‌​‌‌​‍​​‌‌‌​​​‍​‌‌​​​​‌‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​​‌​‍​​‌‌​‌​​﻿---
**Course:** Big Data with Python - From Zero to Production
**Professor:** Juan Marcelo Gutierrez Miranda | @TodoEconometria
**Hash ID:** 4e8d9b1a5f6e7c3d2b1a0f9e8d7c6b5a4f3e2d1c0b9a8f7e6d5c4b3a2f1e0d9c

**Academic references:**

- Sandler, M., et al. (2018). MobileNetV2: Inverted Residuals and Linear Bottlenecks. CVPR.
- Yosinski, J., et al. (2014). How transferable are features in deep neural networks? NeurIPS.
- van der Maaten, L. & Hinton, G. (2008). Visualizing Data using t-SNE. JMLR.
