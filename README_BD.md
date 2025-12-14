# 🚀 Portafolio de Big Data: Análisis de Bases de Datos con Python y SQLite

**Alumno:** Alexis Mendoza Corne  
**Curso:** Especialista en Big Data

---

## 👋 Presentación

¡Hola! Bienvenido a mi repositorio de prácticas. Este proyecto forma parte de mi formación como **Especialista en Big Data**. 

El objetivo principal de este módulo ha sido comprender y aplicar conceptos fundamentales de ingeniería de datos, específicamente:
1.  **Modelado de Datos:** Diferencias prácticas entre modelos desnormalizados (Estrella/Sábana) y normalizados (3NF).
2.  **ETL con Python:** Extracción de datos desde CSVs, transformación con Pandas y carga en SQLite.
3.  **Visualización de Datos:** Creación de dashboards interactivos utilizando Streamlit y Plotly.

---

## 🛠️ Pre-requisitos e Instalación

Para ejecutar los scripts y dashboards de este proyecto, se requiere tener instalado **Python** y las siguientes librerías.

Puedes instalarlas ejecutando el siguiente comando en tu terminal:

```bash
pip install pandas streamlit plotly
```

---

## 📂 Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

```text
Ejercicio_bd/
├── datos/
│   └── csv_tienda_informatica/      # Fuente de datos (Archivos CSV)
├── ejercicios/
│   └── 01_bases_de_datos/
│       └── 1.1_introduccion_sqlite/
│           ├── solucion_modelo_a.py       # Script ETL para Modelo Desnormalizado
│           ├── solucion_modelo_b.py       # Script ETL para Modelo Normalizado
│           ├── consultas_comparativas.py  # Comparación de SQL (Simple vs JOINs)
│           ├── dashboard_modelo_a.py      # Dashboard "Trading" (Modelo A)
│           ├── dashboard.py               # Dashboard Analítico (Modelo B)
│           ├── tienda_modelo_a.db         # Base de datos generada (Modelo A)
│           └── tienda_modelo_b.db         # Base de datos generada (Modelo B)
├── img/
│   ├── dasboardA.png                  # Captura del Dashboard Modelo A
│   └── dashboard.png                  # Captura del Dashboard Modelo B
└── README_BD.md                           # Este archivo
```

---

## 🔍 Consultas Comparativas (`consultas_comparativas.py`)

Este script es el núcleo del análisis técnico. En él, demuestro cómo interactuar con ambos paradigmas de bases de datos:

*   **Modelo A (Desnormalizado):** Realizo consultas directas y rápidas sobre tablas individuales (ej. `SELECT * FROM cpu`). Ideal para lecturas rápidas pero con redundancia de datos.
*   **Modelo B (Normalizado):** Implemento consultas complejas utilizando `JOIN` para unir tablas de `productos`, `fabricantes` y `categorias`. Esto garantiza la integridad de los datos y evita duplicidad.

**Resultado:** El script utiliza `pandas` para imprimir en consola tablas comparativas limpias de los resultados obtenidos en ambos modelos.

---

## 📊 Visualización y Dashboards

He desarrollado dos dashboards interactivos con enfoques visuales distintos para presentar los datos.

### 1. Dashboard "Market Terminal" (Modelo A)
**Archivo:** `dashboard_modelo_a.py`

Este dashboard adopta un estilo financiero ("Trading") para analizar los componentes de hardware como si fueran activos en la bolsa de valores.

*   **Live Ticker:** Animación de las 5 categorías "Blue Chip" (más valiosas).
*   **Análisis de Volatilidad:** Uso de Diagramas de Caja (Box Plots) para entender la dispersión de precios.
*   **Ranking:** Top 10 de productos más costosos.
*   **Estilo:** Dark Mode con acentos neón.


![Dashboard Modelo A](./img/dasboardA.png)
---

### 2. Dashboard Analítico General (Modelo B)
**Archivo:** `dashboard.py`

Este dashboard se enfoca en un análisis descriptivo clásico, aprovechando la estructura normalizada de la base de datos.

*   **Distribución por Categoría:** Gráficos de barras para ver el volumen de inventario.
*   **Líderes del Mercado:** Análisis de los fabricantes con mayor presencia.
*   **Explorador de Precios:** Histogramas interactivos para ver la distribución de costos por categoría.

![Dashboard Modelo B](./img/dashboard.png)

---

## 🚀 Cómo Ejecutar los Dashboards

Para visualizar los reportes, es necesario ejecutar los scripts a través del servidor de Streamlit desde la terminal:

**Para el Modelo A (Trading):**
```bash
streamlit run ejercicios/01_bases_de_datos/1.1_introduccion_sqlite/dashboard_modelo_a.py
```

**Para el Modelo B (Analítico):**
```bash
streamlit run ejercicios/01_bases_de_datos/1.1_introduccion_sqlite/dashboard.py
```

---

## 📚 Recursos de Apoyo

*   **Python & Pandas:** Para la manipulación y limpieza de datos.
*   **SQLite:** Motor de base de datos ligero y eficiente.
*   **Streamlit:** Framework para la creación rápida de Web Apps de Data Science.
*   **Plotly:** Librería para gráficos interactivos y animados.

---
*Proyecto desarrollado por Alexis Mendoza Corne - 2025*
