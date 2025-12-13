# Dashboard EDA - NYC Taxi Dataset

Dashboard interactivo de ejemplo que muestra un Análisis Exploratorio de Datos (EDA) del dataset NYC Taxi mediante 
un **dashboard** en Flask.  
El análisis incluye estadísticas descriptivas, distribuciones de pasajeros, distancias y tarifas, así como correlaciones entre distancia y precio.


## Estructura

```
lucia-dashboard/
├── app.py              # Aplicación Flask principal
├── templates/          # Plantillas HTML
│   └── index.html      # Página principal del dashboard
├── static/             # Archivos estáticos (CSS, JS, imágenes)
└── README.md           # Este archivo
```

## Características

- Estadísticas descriptivas del dataset
- Visualizaciones interactivas con Chart.js
- API endpoints para consumir datos
- Diseño responsive
- Código comentado para facilitar el aprendizaje

## Cómo ejecutar
## Descargar los datos

El dataset se descarga automáticamente usando el script `descargar_datos.py` que se encuentra en `scripts/`.  

1. Asegúrate de tener Flask instalado y los requirements: 
```bash
pip install -r requirements.txt
```

## Visualizaciones incluidas

1. Gráfico de barras mostrando la distribución de distancias de viaje
2. Gráfico de  tarifas de los viajes
3. **Pasajeros por Viaje**: Gráfico de dona mostrando la distribución de pasajeros

