# PCA + Clustering K-Means: Dataset Iris﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​​‌​‍​​‌‌​​‌​‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌​‌‌‌‍​‌‌​​‌​‌‍​‌‌​​‌​‌‍​​‌‌​​​​﻿

**Autor:** @TodoEconometria | **Profesor:** Juan Marcelo Gutierrez Miranda

---

## 📚 Tabla de Contenidos

1. [Introducción](#1-introducción)
2. [El Dataset Iris: Un Clásico del Machine Learning](#2-el-dataset-iris-un-clásico-del-machine-learning)﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​​‌​‍​​‌‌​​‌​‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌​‌‌‌‍​‌‌​​‌​‌‍​‌‌​​‌​‌‍​​‌‌​​​​﻿
3. [Por Qué Combinar PCA + Clustering](#3-por-qué-combinar-pca--clustering)
4. [Análisis de Componentes Principales (PCA)](#4-análisis-de-componentes-principales-pca)
5. [Clustering K-Means](#5-clustering-k-means)
6. [Interpretación de Resultados](#6-interpretación-de-resultados)
7. [Conclusiones y Recomendaciones](#7-conclusiones-y-recomendaciones)

---

## 1. Introducción

Este documento presenta un **análisis completo** del famoso **dataset Iris** combinando dos técnicas fundamentales del Machine Learning no supervisado:

- **PCA (Principal Component Analysis)**: Reducción de dimensionalidad
- **K-Means Clustering**: Agrupación de observaciones

### 🎯 Objetivos del Análisis

1. **Reducir** las 4 dimensiones originales a 2 dimensiones principales
2. **Identificar** grupos naturales en los datos (especies de flores)
3. **Visualizar** patrones y relaciones en un espacio 2D
4. **Validar** si el clustering no supervisado puede descubrir las 3 especies conocidas

---

## 2. El Dataset Iris: Un Clásico del Machine Learning

### 📖 Historia y Contexto

El dataset Iris fue introducido por **Ronald Fisher** en 1936 en su paper seminal:

> Fisher, R. A. (1936). *The use of multiple measurements in taxonomic problems*. Annals of Eugenics, 7(2), 179-188.

Es uno de los datasets más utilizados en:

- Enseñanza de Machine Learning
- Validación de algoritmos de clasificación
- Ejemplos de visualización de datos

### 🌸 Descripción del Dataset

| Característica | Descripción |
|----------------|-------------|
| **Observaciones** | 150 flores |
| **Especies** | 3 (Setosa, Versicolor, Virginica) |
| **Variables** | 4 medidas en centímetros |
| **Distribución** | 50 flores por especie (balanceado) |

### 📏 Variables Medidas

1. **Sepal Length** (Largo del sépalo)
2. **Sepal Width** (Ancho del sépalo)
3. **Petal Length** (Largo del pétalo)
4. **Petal Width** (Ancho del pétalo)

> **NOTA BOTÁNICA:** El **sépalo** es la parte verde que protege la flor antes de abrirse. El **pétalo** es la parte colorida de la flor.

### 📊 Análisis Exploratorio de Datos (EDA)

![EDA del Dataset Iris](02_pca_iris_eda.png)

### 🔍 ¿Por Qué es Importante Este Dataset?

1. **Tamaño Manejable**: 150 observaciones son suficientes para aprender sin ser abrumadoras
2. **Bien Balanceado**: 50 flores de cada especie (no hay desbalance de clases)
3. **Separabilidad**: Una especie (Setosa) es linealmente separable, las otras dos se superponen ligeramente
4. **Multivariate**: 4 variables permiten practicar técnicas de reducción de dimensionalidad

---

## 3. Por Qué Combinar PCA + Clustering

### 🤔 El Problema de la Dimensionalidad

Cuando tenemos **más de 3 dimensiones**, es imposible visualizar los datos directamente:

- **1D**: Línea (fácil)
- **2D**: Plano (fácil)
- **3D**: Espacio 3D (posible pero difícil)
- **4D+**: ❌ **Imposible de visualizar**

### 💡 La Solución: PCA + Clustering

```
Datos Originales (4D)
        ↓
    PCA (Reducción)
        ↓
Datos Reducidos (2D) ← Ahora podemos VISUALIZAR
        ↓
    K-Means (Agrupación)
        ↓
  Clusters Identificados
```

### ✅ Ventajas de Esta Combinación

| Ventaja | Explicación |
|---------|-------------|
| **Visualización** | PCA reduce a 2D para graficar |
| **Reducción de Ruido** | PCA elimina varianza no informativa |
| **Mejor Clustering** | K-Means funciona mejor en espacios de menor dimensión |
| **Interpretabilidad** | Podemos ver y entender los clusters en 2D |

---

## 4. Análisis de Componentes Principales (PCA)

### 🎯 ¿Qué es PCA?

**PCA** es una técnica que:

1. **Encuentra** las direcciones de máxima varianza en los datos
2. **Proyecta** los datos en esas direcciones (componentes principales)
3. **Reduce** la dimensionalidad manteniendo la mayor información posible

### 📊 Resultados del PCA en Iris

#### Varianza Explicada

| Dimensión | Autovalor | Varianza (%) | Varianza Acumulada (%) |
|-----------|-----------|--------------|------------------------|
| **Dim.1** | ~2.92 | ~73% | ~73% |
| **Dim.2** | ~0.91 | ~23% | ~96% |
| Dim.3 | ~0.15 | ~4% | ~99% |
| Dim.4 | ~0.02 | ~1% | ~100% |

> **INTERPRETACIÓN:** Las primeras 2 dimensiones capturan **~96%** de la varianza total. Esto significa que podemos reducir de 4D a 2D perdiendo solo ~4% de información.

#### Regla de Kaiser

La **Regla de Kaiser** dice: *Retener componentes con autovalor > 1*

- **Dim.1**: Autovalor = 2.92 ✅ (Retener)
- **Dim.2**: Autovalor = 0.91 ⚠️ (Casi 1, retener para visualización)
- **Dim.3**: Autovalor = 0.15 ❌ (Descartar)
- **Dim.4**: Autovalor = 0.02 ❌ (Descartar)

### 🔍 Interpretación de las Dimensiones

#### Dimensión 1 (~73% de varianza)

**Variables que más contribuyen:**

- **Petal Length** (~42%)
- **Petal Width** (~42%)

**Interpretación:**
> Dim.1 representa el **"tamaño del pétalo"**. Flores con valores altos en Dim.1 tienen pétalos grandes; valores bajos tienen pétalos pequeños.

#### Dimensión 2 (~23% de varianza)

**Variables que más contribuyen:**

- **Sepal Width** (~72%)

**Interpretación:**
> Dim.2 representa el **"ancho del sépalo"**. Flores con valores altos en Dim.2 tienen sépalos anchos; valores bajos tienen sépalos estrechos.

### 📈 Círculo de Correlación

El **círculo de correlación** muestra cómo las variables originales se relacionan con las dimensiones principales:

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

**Observaciones:**

- **Petal Length** y **Petal Width** están muy correlacionadas (flechas en la misma dirección)
- **Sepal Width** es casi perpendicular a las medidas de pétalo (baja correlación)
- **Sepal Length** está entre ambas dimensiones

---

## 5. Clustering K-Means

### 🎯 ¿Qué es K-Means?

**K-Means** es un algoritmo de clustering que:

1. **Divide** los datos en K grupos (clusters)
2. **Minimiza** la distancia de cada punto a su centroide
3. **Itera** hasta convergencia

### 🔢 Determinación del Número Óptimo de Clusters

#### Método del Codo (Elbow Method)

Graficamos la **inercia** (suma de distancias al cuadrado) vs K:

```
Inercia
  │
  │ ●
  │   ●
  │     ●  ← "Codo" en K=3
  │       ●
  │         ●
  │           ●
  └─────────────────→ K
    2  3  4  5  6  7
```

**Interpretación:** El "codo" está en **K=3**, sugiriendo 3 clusters.

#### Silhouette Score

El **Silhouette Score** mide qué tan bien separados están los clusters:

- **Valor**: Entre -1 y 1
- **Interpretación**:
  - Cercano a **1**: Clusters bien separados ✅
  - Cercano a **0**: Clusters superpuestos ⚠️
  - Negativo: Puntos mal asignados ❌

**Resultado para Iris:** Silhouette Score ≈ **0.55** (buena separación)

### 📊 Resultados del Clustering

#### Confusion Matrix: Clusters vs Especies Reales

|           | Cluster 0 | Cluster 1 | Cluster 2 |
|-----------|-----------|-----------|-----------|
| **Setosa**     | 50 | 0 | 0 |
| **Versicolor** | 0 | 48 | 2 |
| **Virginica**  | 0 | 14 | 36 |

**Observaciones:**

- **Setosa**: Perfectamente separada (100% en Cluster 0)
- **Versicolor**: Mayormente en Cluster 1 (96%)
- **Virginica**: Mayormente en Cluster 2 (72%), pero con superposición con Versicolor

#### Pureza de Clusters

La **pureza** mide el porcentaje de observaciones correctamente agrupadas:

```
Pureza = (50 + 48 + 36) / 150 = 89.3%
```

> **INTERPRETACIÓN:** El algoritmo K-Means logró identificar correctamente las especies en **89.3%** de los casos, **sin conocer las etiquetas reales**. Esto es excelente para un método no supervisado.

### 🎨 Visualización de Clusters

En el espacio 2D del PCA, los clusters se ven así:

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

**Centroides** (marcados con X):

- **Cluster 0**: (-2.7, 0.3) → Setosa
- **Cluster 1**: (0.3, -0.5) → Versicolor
- **Cluster 2**: (1.7, 0.2) → Virginica

---

## 6. Interpretación de Resultados

### Panel Completo: PCA + Clustering K-Means

![PCA + Clustering K-Means: Iris Dataset](02_pca_iris_clustering.png)

### 🔬 Análisis por Especie

#### Setosa (Cluster 0)

**Características:**

- **Petal Length**: Muy pequeño (~1.5 cm)
- **Petal Width**: Muy pequeño (~0.2 cm)
- **Sepal Width**: Relativamente grande

**Posición en PCA:**

- **Dim.1**: Valores muy negativos (pétalos pequeños)
- **Dim.2**: Valores positivos (sépalos anchos)

**Separabilidad:** ✅ **Perfecta** (100% correctamente agrupada)

#### Versicolor (Cluster 1)

**Características:**

- **Petal Length**: Mediano (~4.3 cm)
- **Petal Width**: Mediano (~1.3 cm)
- **Sepal Width**: Mediano

**Posición en PCA:**

- **Dim.1**: Valores cercanos a 0 (pétalos medianos)
- **Dim.2**: Valores ligeramente negativos

**Separabilidad:** ⚠️ **Buena** (96% correctamente agrupada, 4% confundida con Virginica)

#### Virginica (Cluster 2)

**Características:**

- **Petal Length**: Grande (~5.5 cm)
- **Petal Width**: Grande (~2.0 cm)
- **Sepal Width**: Mediano

**Posición en PCA:**

- **Dim.1**: Valores muy positivos (pétalos grandes)
- **Dim.2**: Valores cercanos a 0

**Separabilidad:** ⚠️ **Moderada** (72% correctamente agrupada, 28% confundida con Versicolor)

### 📊 Métricas de Evaluación

| Métrica | Valor | Interpretación |
|---------|-------|----------------|
| **Silhouette Score** | 0.55 | Buena separación entre clusters |
| **Davies-Bouldin Index** | 0.66 | Clusters compactos y separados (menor es mejor) |
| **Calinski-Harabasz Index** | 561.63 | Alta separación entre clusters (mayor es mejor) |
| **Pureza** | 89.3% | Alta concordancia con especies reales |

### 🎯 ¿Por Qué Versicolor y Virginica se Superponen?

**Razón Biológica:**

- Versicolor y Virginica son especies **evolutivamente más cercanas**
- Comparten características morfológicas similares
- Setosa es más distinta (probablemente de un linaje diferente)

**Razón Estadística:**

- Las medidas de pétalo de Versicolor y Virginica tienen **rangos superpuestos**
- No existe una frontera clara en el espacio de 4 dimensiones

---

## 7. Conclusiones y Recomendaciones

### ✅ Conclusiones Principales

1. **PCA es Efectivo**:
   - Reduce de 4D a 2D manteniendo **96%** de la información
   - Las 2 primeras dimensiones son suficientes para visualización y clustering

2. **Las Medidas de Pétalo son Clave**:
   - **Petal Length** y **Petal Width** son las variables más discriminantes
   - Dim.1 (que representa el tamaño del pétalo) explica **73%** de la varianza

3. **K-Means Funciona Bien**:
   - Identifica correctamente las 3 especies en **89.3%** de los casos
   - Setosa es perfectamente separable
   - Versicolor y Virginica tienen cierta superposición natural

4. **Validación del Método No Supervisado**:
   - Sin conocer las etiquetas, K-Means descubre los 3 grupos naturales
   - Esto valida que las especies tienen diferencias morfológicas reales

### 🎓 Lecciones para Estudiantes

#### Lección 1: La Importancia de la Reducción de Dimensionalidad

> **ANTES DE PCA:** 4 variables → Difícil de visualizar → Difícil de interpretar
>
> **DESPUÉS DE PCA:** 2 dimensiones → Fácil de visualizar → Patrones claros

**Moraleja:** No siempre necesitas todas las variables. A veces, menos es más.

#### Lección 2: El Clustering No Supervisado Puede Descubrir Estructura Real

> **SIN ETIQUETAS:** K-Means encuentra 3 grupos
>
> **CON ETIQUETAS:** Hay 3 especies reales
>
> **COINCIDENCIA:** 89.3%

**Moraleja:** Los datos tienen estructura natural. Los algoritmos pueden encontrarla.

#### Lección 3: No Todos los Grupos son Perfectamente Separables

> **Setosa:** 100% separable
>
> **Versicolor/Virginica:** Superposición natural

**Moraleja:** En datos reales, la superposición es normal. No esperes clusters perfectos.

#### Lección 4: Validar, Validar, Validar

> **Método del Codo:** Sugiere K=3
>
> **Silhouette Score:** Confirma K=3
>
> **Pureza:** Valida que K=3 es correcto

**Moraleja:** Usa múltiples métricas para validar tus decisiones.

### 🔧 Recomendaciones Prácticas

#### Para Clasificación de Especies de Iris

1. **Enfocarse en medidas de pétalo** (son las más discriminantes)
2. **Usar PCA para visualización** (reduce complejidad sin perder información)
3. **K=3 es óptimo** (validado por múltiples métricas)

#### Para Análisis de Datos Similares

1. **Siempre hacer EDA primero** (entender distribuciones y correlaciones)
2. **Estandarizar antes de PCA** (variables en diferentes escalas sesgan resultados)
3. **Validar número de clusters** (no asumir K, usar Elbow + Silhouette)
4. **Comparar con ground truth** (si está disponible, como en este caso)

### 🚀 Extensiones Posibles

1. **Otros Algoritmos de Clustering**:
   - DBSCAN (para clusters de forma arbitraria)
   - Hierarchical Clustering (para dendrogramas)
   - Gaussian Mixture Models (para clusters probabilísticos)

2. **Clasificación Supervisada**:
   - Usar las especies conocidas para entrenar un clasificador
   - Comparar con clustering no supervisado

3. **Análisis de Variables Suplementarias**:
   - Agregar información de ubicación geográfica
   - Agregar información de temporada de recolección

---

## 📚 Referencias

### Papers Originales

- **Fisher, R. A. (1936).** *The use of multiple measurements in taxonomic problems*. Annals of Eugenics, 7(2), 179-188.
  - El paper original que introdujo el dataset Iris

- **Anderson, E. (1935).** *The irises of the Gaspe Peninsula*. Bulletin of the American Iris Society, 59, 2-5.
  - El botánico que recolectó los datos originales

### Libros de Referencia

- **Husson, F., Lê, S., & Pagès, J. (2017).** *Exploratory Multivariate Analysis by Example Using R*. CRC Press.
  - Referencia principal para PCA estilo FactoMineR

- **James, G., Witten, D., Hastie, T., & Tibshirani, R. (2013).** *An Introduction to Statistical Learning*. Springer.
  - Capítulos sobre PCA y Clustering

### Artículos Técnicos

- **Pedregosa, F., et al. (2011).** *Scikit-learn: Machine Learning in Python*. JMLR 12, pp. 2825-2830.
  - Documentación de las librerías utilizadas

- **Rousseeuw, P. J. (1987).** *Silhouettes: A graphical aid to the interpretation and validation of cluster analysis*. Journal of Computational and Applied Mathematics, 20, 53-65.
  - Método del Silhouette Score

---

## 🔗 Recursos Adicionales

### Tutoriales Online

- [Scikit-learn: PCA Tutorial](https://scikit-learn.org/stable/modules/decomposition.html#pca)
- [Scikit-learn: K-Means Tutorial](https://scikit-learn.org/stable/modules/clustering.html#k-means)
- [FactoMineR Tutorial](http://factominer.free.fr/course/FactoTuto.html)

### Datasets Similares

- **Wine Dataset**: 178 vinos, 13 variables químicas, 3 clases
- **Breast Cancer Dataset**: 569 tumores, 30 variables, 2 clases (maligno/benigno)
- **Digits Dataset**: 1797 imágenes de dígitos, 64 píxeles, 10 clases

---

**Autor:** @TodoEconometria  
**Profesor:** Juan Marcelo Gutierrez Miranda  
**Fecha:** Enero 2026  
**Licencia:** Uso educativo con atribución

---

## 💬 Preguntas Frecuentes (FAQ)

### ¿Por qué estandarizar antes de PCA?

**Respuesta:** Porque PCA es sensible a la escala de las variables. Si una variable tiene valores mucho mayores que otra (ej: ingresos en miles vs edad en decenas), dominará la varianza y sesgará los resultados.

### ¿Cuántas componentes debo retener?

**Respuesta:** Depende del objetivo:

- **Visualización**: 2-3 componentes
- **Regla de Kaiser**: Componentes con autovalor > 1
- **Varianza Acumulada**: Retener hasta alcanzar 80-95% de varianza

### ¿K-Means siempre encuentra los clusters correctos?

**Respuesta:** No. K-Means tiene limitaciones:

- Asume clusters esféricos
- Sensible a inicialización (usar `n_init` alto)
- Requiere especificar K de antemano

### ¿Qué pasa si tengo más de 3 especies?

**Respuesta:** El proceso es el mismo:

1. Usar Elbow + Silhouette para determinar K óptimo
2. Validar con métricas (pureza, confusion matrix)
3. Visualizar en 2D con PCA (aunque haya más de 3 clusters)

﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​​‌​‍​​‌‌​​‌​‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌​‌‌‌‍​‌‌​​‌​‌‍​‌‌​​‌​‌‍​​‌‌​​​​﻿---

**FIN DEL DOCUMENTO**
