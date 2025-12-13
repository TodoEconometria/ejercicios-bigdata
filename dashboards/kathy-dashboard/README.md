# 🚕 Dashboard NYC Taxi — Kathy

Dashboard interactivo en **Flask** para realizar un **Análisis Exploratorio de Datos (EDA)** sobre un dataset de viajes de taxi en Nueva York (~**1.369.765 registros**).

La aplicación muestra indicadores clave, gráficos estadísticos y visualizaciones interactivas desarrolladas con **Chart.js**.

---

## 📊 Funcionalidades principales

### ✅ Indicadores (KPIs)

En la parte superior del dashboard se muestran:

- **Total de viajes:** 1.369.765  
- **Número de variables en el dataset:** 18  
- **Distancia media:** 4.63 millas  
- **Distancia mediana:** 1.70 millas  
- **Tarifa media:** 12.10 $  
- **Pasajeros más frecuentes:** 1 pasajero (aparece 966.233 veces)

---

### ✅ Gráficos incluidos (Chart.js)

1. **Distribución de distancias**
   - Histograma con 20 intervalos
   - Distancias extremas recortadas para evitar outliers muy grandes

2. **Distribución de tarifas (`fare_amount`)**
   - Histograma con 20 intervalos
   - Se recortan valores extremos (percentil 99) para mejorar la lectura

3. **Pasajeros por viaje**
   - Gráfico tipo donut con el número de viajes para cada `passenger_count`

4. **Gráfico dinámico por número de pasajeros**
   - Filtro con *slider* para seleccionar un número de pasajeros (1, 2, 3, …)  
   - Muestra cuántos viajes hay exactamente con ese número de pasajeros

5. **Gráfico de dispersión: distancia vs propina**
   - Eje X: `trip_distance`  
   - Eje Y: `tip_amount`  
   - Se realiza un muestreo máximo de **1000 puntos** para no sobrecargar el navegador

---

## 🗂️ Estructura del proyecto

```text
ejercicios-bigdata/
├── dashboards/
│   ├── EDA/
│   │   └── analisis_avanzado_plotly.py
│   └── kathy-dashboard/
│       ├── templates/
│       │   └── index.html
│       ├── app.py
│       └── README.md   ✅ (este archivo)
└── nyc_taxi_eda/

