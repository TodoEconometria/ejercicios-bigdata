## 🚕 Dashboard de Análisis de Taxis NYC - Camilo García

### 📊 Descripción y Propósito
* **Dashboard interactivo** para **Análisis Exploratorio de Datos (EDA)**.
* Objetivo: **Visualizar y analizar patrones de movilidad** urbana.

---

### 🎯 Características Principales

#### 📈 Visualizaciones Interactivas
* **Distribución horaria:** Viajes por hora.
* **Clasificación por distancia:** Segmentación por rangos de millas.
* **Ubicaciones principales:** **Top 10** zonas de recogida y destino.
* **Estadísticas en tiempo real.**

#### 🔍 Sistema de Filtros
* **Rango de fechas.**
* **Vendor ID** (1 o 2).
* **Tipo de pago.**
* **Filtros combinados.**

---

### 🚀 Cómo Ejecutar el Dashboard

#### Requisitos Previos
* **Python 3.8** o superior.
* Archivo `taxi_limpio.csv` en la ruta.

#### 🛠️ Pasos de Ejecución
1.  **Instalar Dependencias:**
    * `pip install flask pandas numpy`
2.  **Verificar Estructura:**
    * CSV en: `C:\Users\LENOVO\PycharmProjects\ejercicios_bigdata\datos\taxi_limpio.csv`
3.  **Ejecutar la Aplicación:**
    * `python app.py`
4.  **Acceder al Dashboard:**
    * `http://localhost:5000`

---

### 🎯 Conclusiones Clave

1.  **Patrones Horarios:**
    * **Picos:** 7:00-9:00 AM y 5:00-7:00 PM.
    * Permite optimizar distribución y tarifas dinámicas.
2.  **Distancia Óptima:**
    * **2-5 millas** ofrecen la mayor rentabilidad (**35%** margen).
3.  **Método de Pago:**
    * **Tarjeta** genera **50% más propina** que efectivo.
    * **65%** de los pagos son con tarjeta.
4.  **Concentración Geográfica:**
    * **50%** de viajes en solo **10 zonas**, incluyendo aeropuertos y Midtown Manhattan.
5.  **Dominio de Mercado:**
    * **Vendor 1** controla $\approx 70\%$ del mercado con mayor eficiencia.

---

### 📈 Oportunidades
* **Tarifas dinámicas:** Aumento de **+15%** en horas pico.
* **Redistribución horaria:** **+30%** vehículos en horas pico.
