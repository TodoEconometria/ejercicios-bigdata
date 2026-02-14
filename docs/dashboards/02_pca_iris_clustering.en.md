# PCA + K-Means Clustering: Iris Dataset﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​​‌‌‍​​‌‌​‌​​‍​‌‌​​‌​​‍​​‌‌​‌‌‌‍​‌‌​​‌​‌‍​‌‌​​‌​​‍​​‌‌​​‌​‍​‌‌​​‌​​﻿

**Author:** @TodoEconometria | **Professor:** Juan Marcelo Gutierrez Miranda

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [The Iris Dataset: A Machine Learning Classic](#2-the-iris-dataset-a-machine-learning-classic)﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​​‌‌‍​​‌‌​‌​​‍​‌‌​​‌​​‍​​‌‌​‌‌‌‍​‌‌​​‌​‌‍​‌‌​​‌​​‍​​‌‌​​‌​‍​‌‌​​‌​​﻿
3. [Why Combine PCA + Clustering](#3-why-combine-pca--clustering)
4. [Principal Component Analysis (PCA)](#4-principal-component-analysis-pca)
5. [K-Means Clustering](#5-k-means-clustering)
6. [Interpretation of Results](#6-interpretation-of-results)
7. [Conclusions and Recommendations](#7-conclusions-and-recommendations)

---

## 1. Introduction

This document presents a **complete analysis** of the famous **Iris dataset** combining two fundamental unsupervised Machine Learning techniques:

- **PCA (Principal Component Analysis)**: Dimensionality reduction
- **K-Means Clustering**: Observation grouping

### Analysis Objectives

1. **Reduce** the 4 original dimensions to 2 principal dimensions
2. **Identify** natural groups in the data (flower species)
3. **Visualize** patterns and relationships in a 2D space
4. **Validate** whether unsupervised clustering can discover the 3 known species

---

## 2. The Iris Dataset: A Machine Learning Classic

### History and Context

The Iris dataset was introduced by **Ronald Fisher** in 1936 in his seminal paper:

> Fisher, R. A. (1936). *The use of multiple measurements in taxonomic problems*. Annals of Eugenics, 7(2), 179-188.

It is one of the most widely used datasets in:

- Machine Learning education
- Classification algorithm validation
- Data visualization examples

### Dataset Description

| Feature | Description |
|---------|-------------|
| **Observations** | 150 flowers |
| **Species** | 3 (Setosa, Versicolor, Virginica) |
| **Variables** | 4 measurements in centimeters |
| **Distribution** | 50 flowers per species (balanced) |

### Measured Variables

1. **Sepal Length**
2. **Sepal Width**
3. **Petal Length**
4. **Petal Width**

> **BOTANICAL NOTE:** The **sepal** is the green part that protects the flower before it opens. The **petal** is the colorful part of the flower.

### Exploratory Data Analysis (EDA)

![Iris Dataset EDA](02_pca_iris_eda.png)

### Why Is This Dataset Important?

1. **Manageable Size**: 150 observations are sufficient for learning without being overwhelming
2. **Well Balanced**: 50 flowers of each species (no class imbalance)
3. **Separability**: One species (Setosa) is linearly separable, the other two slightly overlap
4. **Multivariate**: 4 variables allow practicing dimensionality reduction techniques

---

## 3. Why Combine PCA + Clustering

### The Dimensionality Problem

When we have **more than 3 dimensions**, it is impossible to visualize the data directly:

- **1D**: Line (easy)
- **2D**: Plane (easy)
- **3D**: 3D space (possible but difficult)
- **4D+**: **Impossible to visualize**

### The Solution: PCA + Clustering

```
Original Data (4D)
        ↓
    PCA (Reduction)
        ↓
Reduced Data (2D) ← Now we can VISUALIZE
        ↓
    K-Means (Grouping)
        ↓
  Identified Clusters
```

### Advantages of This Combination

| Advantage | Explanation |
|-----------|-------------|
| **Visualization** | PCA reduces to 2D for plotting |
| **Noise Reduction** | PCA removes non-informative variance |
| **Better Clustering** | K-Means works better in lower-dimensional spaces |
| **Interpretability** | We can see and understand clusters in 2D |

---

## 4. Principal Component Analysis (PCA)

### What is PCA?

**PCA** is a technique that:

1. **Finds** the directions of maximum variance in the data
2. **Projects** the data onto those directions (principal components)
3. **Reduces** dimensionality while retaining the most information possible

### PCA Results on Iris

#### Explained Variance

| Dimension | Eigenvalue | Variance (%) | Cumulative Variance (%) |
|-----------|-----------|--------------|------------------------|
| **Dim.1** | ~2.92 | ~73% | ~73% |
| **Dim.2** | ~0.91 | ~23% | ~96% |
| Dim.3 | ~0.15 | ~4% | ~99% |
| Dim.4 | ~0.02 | ~1% | ~100% |

> **INTERPRETATION:** The first 2 dimensions capture **~96%** of the total variance. This means we can reduce from 4D to 2D losing only ~4% of information.

#### Kaiser Rule

The **Kaiser Rule** states: *Retain components with eigenvalue > 1*

- **Dim.1**: Eigenvalue = 2.92 (Retain)
- **Dim.2**: Eigenvalue = 0.91 (Close to 1, retain for visualization)
- **Dim.3**: Eigenvalue = 0.15 (Discard)
- **Dim.4**: Eigenvalue = 0.02 (Discard)

### Interpretation of the Dimensions

#### Dimension 1 (~73% of variance)

**Most contributing variables:**

- **Petal Length** (~42%)
- **Petal Width** (~42%)

**Interpretation:**
> Dim.1 represents **"petal size"**. Flowers with high Dim.1 values have large petals; low values have small petals.

#### Dimension 2 (~23% of variance)

**Most contributing variables:**

- **Sepal Width** (~72%)

**Interpretation:**
> Dim.2 represents **"sepal width"**. Flowers with high Dim.2 values have wide sepals; low values have narrow sepals.

### Correlation Circle

The **correlation circle** shows how original variables relate to the principal dimensions:

```
           Dim.2 (Sepal Width)
                 ↑
                 |
    Sepal Width  |
         ↑       |
         |       |
─────────┼───────┼─────────→ Dim.1 (Petal Size)
         |       |
         |   Petal Length →
         |   Petal Width →
         |
```

**Observations:**

- **Petal Length** and **Petal Width** are highly correlated (arrows in the same direction)
- **Sepal Width** is nearly perpendicular to petal measurements (low correlation)
- **Sepal Length** is between both dimensions

---

## 5. K-Means Clustering

### What is K-Means?

**K-Means** is a clustering algorithm that:

1. **Divides** the data into K groups (clusters)
2. **Minimizes** the distance of each point to its centroid
3. **Iterates** until convergence

### Determining the Optimal Number of Clusters

#### Elbow Method

We plot **inertia** (sum of squared distances) vs K:

```
Inertia
  │
  │ ●
  │   ●
  │     ●  ← "Elbow" at K=3
  │       ●
  │         ●
  │           ●
  └─────────────────→ K
    2  3  4  5  6  7
```

**Interpretation:** The "elbow" is at **K=3**, suggesting 3 clusters.

#### Silhouette Score

The **Silhouette Score** measures how well separated the clusters are:

- **Value**: Between -1 and 1
- **Interpretation**:
  - Close to **1**: Well separated clusters
  - Close to **0**: Overlapping clusters
  - Negative: Misassigned points

**Result for Iris:** Silhouette Score ~ **0.55** (good separation)

### Clustering Results

#### Confusion Matrix: Clusters vs Real Species

|           | Cluster 0 | Cluster 1 | Cluster 2 |
|-----------|-----------|-----------|-----------|
| **Setosa**     | 50 | 0 | 0 |
| **Versicolor** | 0 | 48 | 2 |
| **Virginica**  | 0 | 14 | 36 |

**Observations:**

- **Setosa**: Perfectly separated (100% in Cluster 0)
- **Versicolor**: Mostly in Cluster 1 (96%)
- **Virginica**: Mostly in Cluster 2 (72%), but with overlap with Versicolor

#### Cluster Purity

**Purity** measures the percentage of correctly grouped observations:

```
Purity = (50 + 48 + 36) / 150 = 89.3%
```

> **INTERPRETATION:** The K-Means algorithm correctly identified the species in **89.3%** of cases, **without knowing the real labels**. This is excellent for an unsupervised method.

### Cluster Visualization

In the PCA 2D space, the clusters look like this:

```
     Dim.2
       ↑
       │     ● Cluster 2 (Virginica)
       │    ●●●
       │   ●●●●
       │  ●●●●
       │ ●●●●  ■■■ Cluster 1 (Versicolor)
       │●●●   ■■■■
───────┼■■■■■■■■■──────→ Dim.1
       │
       │  ▲▲▲
       │ ▲▲▲▲▲
       │▲▲▲▲▲▲  Cluster 0 (Setosa)
       │
```

**Centroids** (marked with X):

- **Cluster 0**: (-2.7, 0.3) → Setosa
- **Cluster 1**: (0.3, -0.5) → Versicolor
- **Cluster 2**: (1.7, 0.2) → Virginica

---

## 6. Interpretation of Results

### Full Panel: PCA + K-Means Clustering

![PCA + K-Means Clustering: Iris Dataset](02_pca_iris_clustering.png)

### Analysis by Species

#### Setosa (Cluster 0)

**Characteristics:**

- **Petal Length**: Very small (~1.5 cm)
- **Petal Width**: Very small (~0.2 cm)
- **Sepal Width**: Relatively large

**PCA Position:**

- **Dim.1**: Very negative values (small petals)
- **Dim.2**: Positive values (wide sepals)

**Separability:** **Perfect** (100% correctly grouped)

#### Versicolor (Cluster 1)

**Characteristics:**

- **Petal Length**: Medium (~4.3 cm)
- **Petal Width**: Medium (~1.3 cm)
- **Sepal Width**: Medium

**PCA Position:**

- **Dim.1**: Values close to 0 (medium petals)
- **Dim.2**: Slightly negative values

**Separability:** **Good** (96% correctly grouped, 4% confused with Virginica)

#### Virginica (Cluster 2)

**Characteristics:**

- **Petal Length**: Large (~5.5 cm)
- **Petal Width**: Large (~2.0 cm)
- **Sepal Width**: Medium

**PCA Position:**

- **Dim.1**: Very positive values (large petals)
- **Dim.2**: Values close to 0

**Separability:** **Moderate** (72% correctly grouped, 28% confused with Versicolor)

### Evaluation Metrics

| Metric | Value | Interpretation |
|--------|-------|----------------|
| **Silhouette Score** | 0.55 | Good separation between clusters |
| **Davies-Bouldin Index** | 0.66 | Compact and separated clusters (lower is better) |
| **Calinski-Harabasz Index** | 561.63 | High separation between clusters (higher is better) |
| **Purity** | 89.3% | High agreement with real species |

### Why Do Versicolor and Virginica Overlap?

**Biological Reason:**

- Versicolor and Virginica are **evolutionarily closer** species
- They share similar morphological characteristics
- Setosa is more distinct (probably from a different lineage)

**Statistical Reason:**

- The petal measurements of Versicolor and Virginica have **overlapping ranges**
- There is no clear boundary in the 4-dimensional space

---

## 7. Conclusions and Recommendations

### Main Conclusions

1. **PCA is Effective**:
   - Reduces from 4D to 2D while retaining **96%** of the information
   - The first 2 dimensions are sufficient for visualization and clustering

2. **Petal Measurements are Key**:
   - **Petal Length** and **Petal Width** are the most discriminating variables
   - Dim.1 (which represents petal size) explains **73%** of the variance

3. **K-Means Works Well**:
   - Correctly identifies the 3 species in **89.3%** of cases
   - Setosa is perfectly separable
   - Versicolor and Virginica have some natural overlap

4. **Validation of the Unsupervised Method**:
   - Without knowing the labels, K-Means discovers the 3 natural groups
   - This validates that the species have real morphological differences

### Lessons for Students

#### Lesson 1: The Importance of Dimensionality Reduction

> **BEFORE PCA:** 4 variables → Hard to visualize → Hard to interpret
>
> **AFTER PCA:** 2 dimensions → Easy to visualize → Clear patterns

**Takeaway:** You don't always need all the variables. Sometimes, less is more.

#### Lesson 2: Unsupervised Clustering Can Discover Real Structure

> **WITHOUT LABELS:** K-Means finds 3 groups
>
> **WITH LABELS:** There are 3 real species
>
> **MATCH:** 89.3%

**Takeaway:** Data has natural structure. Algorithms can find it.

#### Lesson 3: Not All Groups Are Perfectly Separable

> **Setosa:** 100% separable
>
> **Versicolor/Virginica:** Natural overlap

**Takeaway:** In real data, overlap is normal. Don't expect perfect clusters.

#### Lesson 4: Validate, Validate, Validate

> **Elbow Method:** Suggests K=3
>
> **Silhouette Score:** Confirms K=3
>
> **Purity:** Validates that K=3 is correct

**Takeaway:** Use multiple metrics to validate your decisions.

### Practical Recommendations

#### For Iris Species Classification

1. **Focus on petal measurements** (they are the most discriminating)
2. **Use PCA for visualization** (reduces complexity without losing information)
3. **K=3 is optimal** (validated by multiple metrics)

#### For Similar Data Analyses

1. **Always do EDA first** (understand distributions and correlations)
2. **Standardize before PCA** (variables on different scales bias results)
3. **Validate the number of clusters** (don't assume K, use Elbow + Silhouette)
4. **Compare with ground truth** (if available, as in this case)

### Possible Extensions

1. **Other Clustering Algorithms**:
   - DBSCAN (for arbitrarily shaped clusters)
   - Hierarchical Clustering (for dendrograms)
   - Gaussian Mixture Models (for probabilistic clusters)

2. **Supervised Classification**:
   - Use the known species to train a classifier
   - Compare with unsupervised clustering

3. **Supplementary Variable Analysis**:
   - Add geographic location information
   - Add collection season information

---

## References

### Original Papers

- **Fisher, R. A. (1936).** *The use of multiple measurements in taxonomic problems*. Annals of Eugenics, 7(2), 179-188.
  - The original paper that introduced the Iris dataset

- **Anderson, E. (1935).** *The irises of the Gaspe Peninsula*. Bulletin of the American Iris Society, 59, 2-5.
  - The botanist who collected the original data

### Reference Books

- **Husson, F., Le, S., & Pages, J. (2017).** *Exploratory Multivariate Analysis by Example Using R*. CRC Press.
  - Main reference for FactoMineR-style PCA

- **James, G., Witten, D., Hastie, T., & Tibshirani, R. (2013).** *An Introduction to Statistical Learning*. Springer.
  - Chapters on PCA and Clustering

### Technical Articles

- **Pedregosa, F., et al. (2011).** *Scikit-learn: Machine Learning in Python*. JMLR 12, pp. 2825-2830.
  - Documentation for the libraries used

- **Rousseeuw, P. J. (1987).** *Silhouettes: A graphical aid to the interpretation and validation of cluster analysis*. Journal of Computational and Applied Mathematics, 20, 53-65.
  - Silhouette Score method

---

## Additional Resources

### Online Tutorials

- [Scikit-learn: PCA Tutorial](https://scikit-learn.org/stable/modules/decomposition.html#pca)
- [Scikit-learn: K-Means Tutorial](https://scikit-learn.org/stable/modules/clustering.html#k-means)
- [FactoMineR Tutorial](http://factominer.free.fr/course/FactoTuto.html)

### Similar Datasets

- **Wine Dataset**: 178 wines, 13 chemical variables, 3 classes
- **Breast Cancer Dataset**: 569 tumors, 30 variables, 2 classes (malignant/benign)
- **Digits Dataset**: 1797 digit images, 64 pixels, 10 classes

---

**Author:** @TodoEconometria
**Professor:** Juan Marcelo Gutierrez Miranda
**Date:** January 2026
**License:** Educational use with attribution

---

## Frequently Asked Questions (FAQ)

### Why standardize before PCA?

**Answer:** Because PCA is sensitive to the scale of variables. If one variable has much larger values than another (e.g., income in thousands vs age in tens), it will dominate the variance and bias the results.

### How many components should I retain?

**Answer:** It depends on the objective:

- **Visualization**: 2-3 components
- **Kaiser Rule**: Components with eigenvalue > 1
- **Cumulative Variance**: Retain until reaching 80-95% of variance

### Does K-Means always find the correct clusters?

**Answer:** No. K-Means has limitations:

- Assumes spherical clusters
- Sensitive to initialization (use high `n_init`)
- Requires specifying K in advance

### What if I have more than 3 species?

**Answer:** The process is the same:

1. Use Elbow + Silhouette to determine the optimal K
2. Validate with metrics (purity, confusion matrix)
3. Visualize in 2D with PCA (even with more than 3 clusters)

﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​​‌‌‍​​‌‌​‌​​‍​‌‌​​‌​​‍​​‌‌​‌‌‌‍​‌‌​​‌​‌‍​‌‌​​‌​​‍​​‌‌​​‌​‍​‌‌​​‌​​﻿---

**END OF DOCUMENT**
