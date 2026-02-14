# Educational Guide: Document Vectorization and Clustering﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​​‌​‍​​‌‌​‌‌‌‍​​‌‌​‌‌‌‍​​‌‌​​​​‍​‌‌​​‌​​‍​‌‌​​‌​​‍​‌‌​​​‌‌‍​​‌‌​‌‌‌﻿

## Topic Analysis with Artificial Intelligence (NLP & Machine Learning)

---

> ### Certification and Reference Information
>
> **Original author/Reference:** @TodoEconometria
> **Professor:** Juan Marcelo Gutierrez Miranda
> **Methodology:** Advanced Courses in Big Data, Data Science, AI Application Development & Applied Econometrics.﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​​‌​‍​​‌‌​‌‌‌‍​​‌‌​‌‌‌‍​​‌‌​​​​‍​‌‌​​‌​​‍​‌‌​​‌​​‍​‌‌​​​‌‌‍​​‌‌​‌‌‌﻿
> **Certification Hash ID:** `4e8d9b1a5f6e7c3d2b1a0f9e8d7c6b5a4f3e2d1c0b9a8f7e6d5c4b3a2f1e0d9c`
> **Repository:** [https://github.com/TodoEconometria/certificaciones](https://github.com/TodoEconometria/certificaciones)
>
> **ACADEMIC REFERENCE:**
>
> - McKinney, W. (2012). Python for Data Analysis: Data Wrangling with Pandas, NumPy, and IPython. O'Reilly Media.
> - Harris, C. R., et al. (2020). Array programming with NumPy. Nature, 585(7825), 357-362.
> - Pedregosa, F., et al. (2011). Scikit-learn: Machine Learning in Python. JMLR 12, pp. 2825-2830.

---

## 1. Laboratory Introduction

In the world of **Big Data**, most information is **unstructured** (texts, emails, news). The fundamental challenge is: *How can a computer understand that two documents discuss the same topic without reading them?*

This exercise implements a complete Data Science pipeline to automatically group **1,200 documents** in Spanish, using a combination of advanced mathematical techniques to transform human language into structures that machines can process.

---

## 2. Theoretical Foundations (What Do We Use and Why?)

### A. Vectorization: The Bridge Between Text and Mathematics

Computers don't understand words, only numbers. We use **TF-IDF (Term Frequency - Inverse Document Frequency)** for its ability to discern relevance.

- **What is it?**: A statistical value that seeks to measure how important a word is to a document within a collection (corpus).
- **How does it work?**:
    $$TF(t, d) = \frac{\text{Count of word } t \text{ in document } d}{\text{Total words in } d}$$
    $$IDF(t) = \log\left(\frac{\text{Total documents}}{\text{Documents containing word } t}\right)$$
- **Why do we use it?**: Unlike simple counting (Bag-of-Words), TF-IDF penalizes words that appear everywhere (like "the", "that", "is") and rewards thematic words ("processor", "investment", "vaccine").

### B. K-Means: The Clustering Brain

For **Unsupervised Learning**, the **K-Means** algorithm is the gold standard for finding patterns without prior labels.

- **The Process**:
    1. Define $k$ random points (centroids).
    2. Assign each document to the nearest centroid (using Euclidean distance in vector space).
    3. Recalculate the group center and repeat until the groups stabilize.
- **Why we use it**: It is extremely efficient for large data volumes and allows us to segment markets, news, or legal documents automatically.

### C. PCA: Visualizing Hyperspace

Our TF-IDF matrix has hundreds of dimensions (one per unique word). Humans can only see in 2D or 3D.

- **What does it mean?**: **Principal Component Analysis** "compresses" the information. It finds the directions (components) where the data varies the most and projects everything onto them.
- **Didactic utility**: Without PCA, the clustering would be a list of abstract numbers. With PCA, we can "see" the concept separation in a chart.

---

## 3. Interpreting What We Are Seeing

When running the code, the visualization `05_visualizacion_clustering.png` is generated.

![Document Clustering](05_visualizacion_clustering.png)

### How to Read This Chart?

1. **Proximity is Similarity**: Two points that are close together represent documents that share keywords and, therefore, topics.
2. **Cluster Dispersion**:
    - If the groups are well separated, the algorithm has been fully successful identifying unique topics.
    - If there is overlap, it indicates that some documents share vocabulary from several topics (e.g., an article about "Technology in Healthcare").
3. **The Axes (PCA)**: The X-axis (Component 1) usually captures the biggest difference between topics (e.g., medical terms vs financial terms).

### Dominant Words per Cluster

Each cluster has a "semantic profile" defined by the words that contribute most to its identity:

![Clustering with Dominant Words](05_clustering_palabras_dominantes.png)

### Optimal k Selection (Elbow and Silhouette)

How do we know how many clusters to create? Two complementary methods:

- **Elbow Method:** We look for the point where inertia stops decreasing significantly.
- **Silhouette Coefficient:** A value close to 1 indicates well-separated clusters.

![Elbow and Silhouette](05_elbow_silhouette.png)

### Silhouette Analysis by Cluster

Granular analysis shows the internal cohesion of each cluster. Uniform width indicates well-defined clusters:

![Detailed Silhouette](05_silhouette_detallado.png)

### Validation: Real Topics vs Clusters

Venn diagrams show the overlap between the corpus's real topics and the automatically detected clusters. 100% overlap confirms that K-Means has correctly identified the topics:

![Venn: Real Topics vs Clusters](05_venn_clusters.png)

---

## 4. Practical Case: Titanic Clustering

To demonstrate that K-Means works beyond text, we apply the same algorithm to the Titanic dataset with demographic features (age, fare, class):

### k Selection for Titanic

![Elbow and Silhouette - Titanic](05_titanic_elbow_silhouette.png)

### Passenger Clustering (PCA)

![Titanic Clustering](05_titanic_clustering.png)

### Cluster Profiling

Each cluster reveals a different passenger profile (average age, fare, survival rate):

![Characteristics by Cluster](05_titanic_clustering_caracteristicas.png)

---

## 5. Didactic Guide: Step by Step

### Step 1: Corpus Generation

We create 1,200 synthetic documents. In a real training scenario, this simulates data ingestion from an API or SQL database.

### Step 2: Cleaning and Tokenization

Although the script is straightforward, in real NLP we would remove punctuation, convert to lowercase, and remove *Stop Words* so that the model is not distracted by noise.

### Step 3: Model Training

The command `kmeans.fit(tfidf_matrix)` is where the "magic" happens. The model "learns" the latent structure of the data without human assistance.

---

## References and Academic Citations

For further study of the methodology, the following fundamental sources are recommended:

- **McKinney, W. (2012).** *Python for Data Analysis*. O'Reilly Media. (Reference for matrix manipulation).
- **Pedregosa, F., et al. (2011).** *Scikit-learn: Machine Learning in Python*. JMLR. (Official documentation of the framework used).
- **Manning, C. D., et al. (2008).** *Introduction to Information Retrieval*. Cambridge University Press. (Foundational theory for TF-IDF).

﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​​‌​‍​​‌‌​‌‌‌‍​​‌‌​‌‌‌‍​​‌‌​​​​‍​‌‌​​‌​​‍​‌‌​​‌​​‍​‌‌​​​‌‌‍​​‌‌​‌‌‌﻿---

## Institutional Information

**Author/Reference:** @TodoEconometria
**Professor:** Juan Marcelo Gutierrez Miranda
**Area:** Big Data, Data Science & Applied Econometrics.

**Certification Hash ID:**
`4e8d9b1a5f6e7c3d2b1a0f9e8d7c6b5a4f3e2d1c0b9a8f7e6d5c4b3a2f1e0d9c`
