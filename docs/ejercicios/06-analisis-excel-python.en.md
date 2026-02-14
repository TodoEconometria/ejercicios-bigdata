# Exercise 5.1: Data Analysis with Excel and Python﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​​​‌‍​‌‌​​‌​‌‍​​‌‌​‌​‌‍​‌‌​​‌​​‍​‌‌​​​‌‌‍​‌‌​​​‌‌‍​​‌‌​​​‌‍​‌‌​​‌​​﻿

> **Status:** Available

---

## General Description

You will learn to **analyze Excel data** using Python, comparing manual vs automated analysis.﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​​​‌‍​‌‌​​‌​‌‍​​‌‌​‌​‌‍​‌‌​​‌​​‍​‌‌​​​‌‌‍​‌‌​​​‌‌‍​​‌‌​​​‌‍​‌‌​​‌​​﻿

**Estimated duration:** 3-4 hours
**Level:** Basic-Intermediate
**Prerequisites:** Basic Python, pandas

---

## Learning Objectives

Upon completing this exercise you will be able to:

- ✅ Read Excel files with pandas and openpyxl
- ✅ Perform exploratory data analysis (EDA)
- ✅ Generate descriptive statistics
- ✅ Create visualizations (charts)
- ✅ Automate analysis you would do manually in Excel
- ✅ Export results to formatted Excel
- ✅ Compare manual vs programmatic analysis

---

## Data File

You will work with: `datos/Ejercicio-de-Excel-resuelto-nivel-medio.xlsx`

This file contains real data that you would normally analyze in Excel.

---

## Exercise Content

The complete exercise is in:

```
ejercicios/01_bases_de_datos/5.1_analisis_excel/
```

### Files

- `analisis_exploratorio.py` - Script template
- `INSTRUCCIONES.md` - Step-by-step guide
- `informe_analisis.md` - Template for your report

---

## Analysis Process

### 1. Initial Exploration

```python
import pandas as pd

# Leer Excel
df = pd.read_excel('datos/Ejercicio-de-Excel-resuelto-nivel-medio.xlsx')

# Ver estructura
print(df.info())
print(df.describe())
print(df.head())
```

### 2. Data Cleaning

- Detect null values
- Fix data types
- Remove duplicates
- Normalize text

### 3. Descriptive Statistics

- Measures of central tendency (mean, median)
- Dispersion (standard deviation, quartiles)
- Correlations
- Distributions

### 4. Visualizations

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Gráfico de barras
df.groupby('categoria')['ventas'].sum().plot(kind='bar')

# Histograma
df['precio'].hist(bins=20)

# Heatmap de correlación
sns.heatmap(df.corr(), annot=True)
```

### 5. Export Results

```python
# Crear Excel con formato
with pd.ExcelWriter('analisis_resultados.xlsx', engine='openpyxl') as writer:
    df_resumen.to_excel(writer, sheet_name='Resumen')
    df_detalle.to_excel(writer, sheet_name='Detalle')
```

---

## Tasks to Complete

### Part 1: Exploratory Analysis

Create `analisis_exploratorio.py` that:

1. Reads the Excel file
2. Performs a complete EDA
3. Generates descriptive statistics
4. Creates visualizations
5. Exports results to formatted Excel

### Part 2: Analysis Report

Create `informe_analisis.md` with:

1. **Executive Summary**
   - Key findings
   - Key data points

2. **Detailed Analysis**
   - Data structure
   - Data quality
   - Patterns found

3. **Visualizations**
   - Include generated charts
   - Interpret results

4. **Manual vs Automated Comparison**
   - Which is faster?
   - Which is more accurate?
   - When to use each?

5. **Conclusions**

---

## Technical Requirements

### Python Libraries

```bash
pip install pandas openpyxl matplotlib seaborn jupyter
```

### Optional Software

- Excel or LibreOffice Calc (to compare manual analysis)
- Jupyter Notebook (for interactive analysis)

---

## Comparison: Excel vs Python

### Advantages of Excel

- ✅ Intuitive visual interface
- ✅ Fast for small ad-hoc analysis
- ✅ No programming required
- ✅ Easy interactive charts

### Advantages of Python

- ✅ Scalable to millions of rows
- ✅ Reproducible (script = documentation)
- ✅ Automatable
- ✅ More advanced statistical analysis
- ✅ Integration with databases
- ✅ Version control (Git)

### When to Use Each?

**Use Excel when:**
- Small dataset (< 100k rows)
- Quick one-time analysis
- Non-technical audience

**Use Python when:**
- Large dataset (> 100k rows)
- Repetitive analysis
- You need automation
- Complex analysis

---

## Submissions

Check the [submission instructions](../../entregas/01_bases_de_datos/) to learn which files you need to upload.

**Submission folder:**
```
entregas/01_bases_de_datos/tu_apellido_nombre/5.1_analisis_excel/
├── analisis_exploratorio.py
├── informe_analisis.md
├── graficos/
│   ├── distribucion.png
│   ├── correlacion.png
│   └── tendencias.png
└── analisis_resultados.xlsx
```

---

## Support Resources

### Documentation

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Openpyxl Documentation](https://openpyxl.readthedocs.io/)
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/index.html)
- [Seaborn Examples](https://seaborn.pydata.org/examples/index.html)

### Tutorials

- [Pandas Tutorial](https://www.kaggle.com/learn/pandas)
- [Excel with Python](https://realpython.com/openpyxl-excel-spreadsheets-python/)
- [Exploratory Analysis with Pandas](https://realpython.com/pandas-python-explore-dataset/)

### Videos

- [Data Analysis with Pandas](https://www.youtube.com/results?search_query=pandas+data+analysis+tutorial)

---

## Next Steps

After completing this exercise, you will have covered:

- Databases (SQLite, PostgreSQL, Oracle, SQL Server)
- Data analysis (Python + Excel)

Next level: **Big Data** with PySpark, Dask, etc.

﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​​​‌‍​‌‌​​‌​‌‍​​‌‌​‌​‌‍​‌‌​​‌​​‍​‌‌​​​‌‌‍​‌‌​​​‌‌‍​​‌‌​​​‌‍​‌‌​​‌​​﻿---

**Publication date:** To be defined
**Last updated:** 2025-12-17
