# Ejercicio 5.1: Análisis de Datos con Excel y Python

> **Estado:** En construcción

---

## Descripción General

Aprenderás a **analizar datos de Excel** usando Python, comparando el análisis manual vs automatizado.

**Duración estimada:** 3-4 horas
**Nivel:** Básico-Intermedio
**Prerequisitos:** Python básico, pandas

---

## Objetivos de Aprendizaje

Al completar este ejercicio serás capaz de:

- ✅ Leer archivos Excel con pandas y openpyxl
- ✅ Realizar análisis exploratorio de datos (EDA)
- ✅ Generar estadísticas descriptivas
- ✅ Crear visualizaciones (gráficos)
- ✅ Automatizar análisis que harías manualmente en Excel
- ✅ Exportar resultados a Excel formateado
- ✅ Comparar análisis manual vs programático

---

## Archivo de Datos

Trabajarás con: `datos/Ejercicio-de-Excel-resuelto-nivel-medio.xlsx`

Este archivo contiene datos reales que normalmente analizarías en Excel.

---

## Contenido del Ejercicio

El ejercicio completo está en:

```
ejercicios/01_bases_de_datos/5.1_analisis_excel/
```

### Archivos

- `analisis_exploratorio.py` - Plantilla de script
- `INSTRUCCIONES.md` - Guía paso a paso
- `informe_analisis.md` - Plantilla para tu informe

---

## Proceso de Análisis

### 1. Exploración Inicial

```python
import pandas as pd

# Leer Excel
df = pd.read_excel('datos/Ejercicio-de-Excel-resuelto-nivel-medio.xlsx')

# Ver estructura
print(df.info())
print(df.describe())
print(df.head())
```

### 2. Limpieza de Datos

- Detectar valores nulos
- Corregir tipos de datos
- Eliminar duplicados
- Normalizar texto

### 3. Estadísticas Descriptivas

- Medidas de tendencia central (media, mediana)
- Dispersión (desviación estándar, cuartiles)
- Correlaciones
- Distribuciones

### 4. Visualizaciones

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

### 5. Exportar Resultados

```python
# Crear Excel con formato
with pd.ExcelWriter('analisis_resultados.xlsx', engine='openpyxl') as writer:
    df_resumen.to_excel(writer, sheet_name='Resumen')
    df_detalle.to_excel(writer, sheet_name='Detalle')
```

---

## Tareas a Realizar

### Parte 1: Análisis Exploratorio

Crear `analisis_exploratorio.py` que:

1. Lee el archivo Excel
2. Realiza EDA completo
3. Genera estadísticas descriptivas
4. Crea visualizaciones
5. Exporta resultados a Excel formateado

### Parte 2: Informe de Análisis

Crear `informe_analisis.md` con:

1. **Resumen Ejecutivo**
   - Hallazgos principales
   - Datos clave

2. **Análisis Detallado**
   - Estructura de los datos
   - Calidad de datos
   - Patrones encontrados

3. **Visualizaciones**
   - Incluir gráficos generados
   - Interpretar resultados

4. **Comparación Manual vs Automatizado**
   - ¿Qué es más rápido?
   - ¿Qué es más preciso?
   - ¿Cuándo usar cada uno?

5. **Conclusiones**

---

## Requisitos Técnicos

### Librerías Python

```bash
pip install pandas openpyxl matplotlib seaborn jupyter
```

### Software Opcional

- Excel o LibreOffice Calc (para comparar análisis manual)
- Jupyter Notebook (para análisis interactivo)

---

## Comparación: Excel vs Python

### Ventajas de Excel

- ✅ Interfaz visual intuitiva
- ✅ Rápido para análisis ad-hoc pequeños
- ✅ No requiere programación
- ✅ Gráficos interactivos fáciles

### Ventajas de Python

- ✅ Escalable a millones de filas
- ✅ Reproducible (script = documentación)
- ✅ Automatizable
- ✅ Más análisis estadísticos avanzados
- ✅ Integración con bases de datos
- ✅ Control de versiones (Git)

### ¿Cuándo usar cada uno?

**Usa Excel cuando:**
- Dataset pequeño (< 100k filas)
- Análisis rápido one-time
- Audiencia no técnica

**Usa Python cuando:**
- Dataset grande (> 100k filas)
- Análisis repetitivo
- Necesitas automatización
- Análisis complejo

---

## Entregas

Consulta las [instrucciones de entrega](../../entregas/01_bases_de_datos/) para saber qué archivos debes subir.

**Carpeta de entrega:**
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

## Recursos de Apoyo

### Documentación

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Openpyxl Documentation](https://openpyxl.readthedocs.io/)
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/index.html)
- [Seaborn Examples](https://seaborn.pydata.org/examples/index.html)

### Tutoriales

- [Pandas Tutorial](https://www.kaggle.com/learn/pandas)
- [Excel con Python](https://realpython.com/openpyxl-excel-spreadsheets-python/)
- [Análisis Exploratorio con Pandas](https://realpython.com/pandas-python-explore-dataset/)

### Videos

- [Análisis de Datos con Pandas](https://www.youtube.com/results?search_query=pandas+data+analysis+tutorial)

---

## Próximos Pasos

Después de completar este ejercicio, habrás cubierto:

- Bases de datos (SQLite, PostgreSQL, Oracle, SQL Server)
- Análisis de datos (Python + Excel)

Siguiente nivel: **Big Data** con PySpark, Dask, etc.

---

**Fecha de publicación:** Por definir
**Última actualización:** 2025-12-17
