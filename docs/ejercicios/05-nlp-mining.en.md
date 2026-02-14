# Module 05: NLP and Text Mining﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌​‌​‌‍​‌‌​​​​‌‍​​‌‌​​​​‍​​‌‌​‌​‌‍​‌‌​​‌​‌‍​​‌‌​​​​‍​​‌‌​​‌​‍​‌‌​​​‌‌﻿

> **Status:** Available

---

## General Description

Introduction to unstructured data processing using Natural Language Processing techniques. From basic tokenization to sentiment analysis and document similarity.﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌​‌​‌‍​‌‌​​​​‌‍​​‌‌​​​​‍​​‌‌​‌​‌‍​‌‌​​‌​‌‍​​‌‌​​​​‍​​‌‌​​‌​‍​‌‌​​​‌‌﻿

**Level:** Intermediate-Advanced
**Technologies:** Python, NLTK, TF-IDF, Scikit-learn
**Prerequisites:** Intermediate Python, basic statistics

![Advanced NLP: Tokenization, Attention Architectures, Parsing](../assets/slides/m5_nlp_p01.jpg)

---

## Learning Objectives

- Understand text tokenization and normalization
- Remove stopwords and apply noise filters
- Calculate document similarity with Jaccard Distance
- Vectorize text with TF-IDF
- Apply clustering on vectorized documents
- Perform basic sentiment analysis

---

## Course Visual Material

### Beyond Bag-of-Words

![Capturing Nuances and Structure](../assets/slides/m5_nlp_p02.jpg)

### The Challenge of Multilingual Tokenization

![Multilingual Tokenization: BPE, WordPiece, Unigram](../assets/slides/m5_nlp_p03.jpg)

### Dependency Parsing: The Hierarchy of Thought

![Dependency Parsing](../assets/slides/m5_nlp_p04.jpg)

### Parsing Algorithms

![Transition-Based vs Graph-Based](../assets/slides/m5_nlp_p05.jpg)

---

## Key Concepts

| Concept | Description |
|----------|-------------|
| **Tokenization** | Splitting text into processable units (tokens) |
| **Stopwords** | Noise removal (articles, prepositions) |
| **Jaccard Similarity** | Mathematical measurement of how similar two documents are |
| **TF-IDF** | Vectorization that weights term importance in a corpus |
| **Sentiment Analysis** | Polar classification (Positive/Negative) based on lexicons |
| **Clustering** | Grouping documents by semantic similarity |

---

## Module Content

The complete module is located at:

```
ejercicios/05_nlp_text_mining/
├── 01_conteo_palabras.py          # Tokenization and counting
├── 02_limpieza_texto.py           # Stopwords and filtering
├── 03_sentimiento.py              # Sentiment analysis
├── 04_similitud_jaccard.py        # Document similarity
├── 05_vectorizacion_clustering.py # TF-IDF + K-Means
└── requirements.txt               # nltk, scikit-learn
```

---

## Practical Exercises

### 01 - Word Count
Basic tokenization, normalization, and term frequency.

### 02 - Stopword Filtering
Noise removal to reveal words with real weight.

### 03 - Sentiment Analysis
Polar classification using predefined lexicons.

### 04 - Jaccard Similarity
Compare documents using Jaccard Distance.

**Main Challenge:** Implement a system that compares public policy descriptions from different countries and detects which ones are semantically similar.

### 05 - Vectorization and Clustering
TF-IDF for numerical representation + K-Means for grouping.

---

## Dashboards

Explore the results visually:

- [Word Count](../dashboards/EJERCICIO_01_CONTEO.md)
- [Stopword Filtering](../dashboards/EJERCICIO_02_LIMPIEZA.md)
- [Jaccard Similarity](../dashboards/04_similitud_jaccard.md)
- [Vectorization and Clustering](../dashboards/05_vectorizacion_y_clustering.md)

﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌​‌​‌‍​‌‌​​​​‌‍​​‌‌​​​​‍​​‌‌​‌​‌‍​‌‌​​‌​‌‍​​‌‌​​​​‍​​‌‌​​‌​‍​‌‌​​​‌‌﻿---

**Course:** Big Data with Python - From Zero to Production
**Instructor:** Juan Marcelo Gutierrez Miranda | @TodoEconometria
**Hash ID:** 4e8d9b1a5f6e7c3d2b1a0f9e8d7c6b5a4f3e2d1c0b9a8f7e6d5c4b3a2f1e0d9c
**Methodology:** Progressive exercises with real data and professional tools

**Academic references:**

- Jurafsky, D., & Martin, J. H. (2024). Speech and Language Processing (3rd ed.). Prentice Hall.
- Manning, C. D., Raghavan, P., & Schutze, H. (2008). Introduction to Information Retrieval. Cambridge University Press.
- Bird, S., Klein, E., & Loper, E. (2009). Natural Language Processing with Python. O'Reilly Media.
