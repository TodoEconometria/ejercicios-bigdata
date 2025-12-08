# Dashboard de Análisis Exploratorio de Datos (EDA) - Taxis de NYC

Este proyecto presenta un dashboard web interactivo para el análisis exploratorio de un dataset de viajes de taxi en la ciudad de Nueva York. La aplicación permite a los usuarios visualizar y filtrar los datos para descubrir patrones y tendencias.

![Vista Previa del Dashboard](URL_A_TU_IMAGEN.png)
*(Nota: Se recomienda tomar una captura de pantalla del dashboard funcionando y reemplazar la URL de arriba para una presentación más visual)*

## 🚀 Características Principales

- **Dashboard Interactivo:** Interfaz web creada con Dash y Plotly para una experiencia de usuario dinámica.
- **Métricas Clave (KPIs):** Visualización en tiempo real del total de viajes, tarifa media y distancia media.
- **Filtros Dinámicos:** Permite filtrar todos los gráficos por día de la semana para un análisis más profundo.
- **Visualizaciones Múltiples:** Incluye histogramas, gráficos de barras, gráficos de pastel, diagramas de dispersión y gráficos de cajas para un análisis completo.

## 🛠️ Stack Tecnológico

- **Lenguaje:** Python 3.13
- **Análisis de Datos:** Pandas
- **Visualización y Dashboard:** Plotly y Dash

## ⚙️ Instalación y Ejecución

Sigue estos pasos para ejecutar el dashboard en tu entorno local.

### 1. Prerrequisitos

- Tener Python 3.13 instalado.
- Disponer del archivo `nyc_taxi.csv` en la carpeta `datos/` del proyecto.

### 2. Configuración del Entorno

Desde la raíz del proyecto (`ejercicios-bigdata`), ejecuta los siguientes comandos:


### 3. Iniciar la Aplicación

Una vez instalado el entorno, inicia el servidor de Dash con el siguiente comando:


### 4. Acceder al Dashboard

Abre tu navegador web y ve a la siguiente dirección:

**http://127.0.0.1:8050/**

Para detener el servidor, vuelve a la terminal y presiona `Ctrl + C`.

## 📊 Interpretación de los Datos y Hallazgos

El análisis exploratorio a través del dashboard revela varias tendencias interesantes sobre los viajes de taxi en NYC:

1.  **Patrón Semanal de Viajes:** Se observa un claro patrón en la actividad a lo largo de la semana. El número de viajes aumenta progresivamente desde el lunes, alcanza su pico los viernes, y desciende durante el fin de semana.

2.  **Distribución del Tipo de Pago:** El pago con **tarjeta de crédito** es el método predominante, seguido por el pago en **efectivo**. Los otros métodos de pago son minoritarios.

3.  **Relación entre Propina y Tipo de Pago:** El análisis de propinas muestra que estas se registran casi exclusivamente en los pagos con **tarjeta**. Los viajes pagados en efectivo rara vez registran una propina en el sistema, lo que sugiere que, si se dan, no son digitalizadas.

4.  **Correlación entre Importe y Propina:** Existe una clara correlación positiva entre el importe total del viaje y la propina. A mayor coste del viaje, mayor tiende a ser la propina, especialmente en los pagos con tarjeta.

5.  **Correlación entre Distancia y Tarifa:** Como es de esperar, hay una fuerte correlación positiva entre la distancia del viaje y la tarifa total. Viajes más largos implican costes más altos.

## 🔮 Futuras Mejoras

- **Filtros Avanzados:** Añadir más filtros, como por hora del día o `RatecodeID`.
- **Análisis Geográfico:** Incorporar un mapa interactivo para visualizar las zonas de origen y destino (`PULocationID`, `DOLocationID`) más populares.
- **Despliegue:** Empaquetar la aplicación en un contenedor Docker y desplegarla en un servicio en la nube (como Heroku o AWS).
