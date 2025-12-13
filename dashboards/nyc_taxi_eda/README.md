# Dashboard EDA - NYC Taxi Dataset

Dashboard interactivo de ejemplo que muestra un análisis exploratorio de datos (EDA) del dataset NYC Taxi.

## Estructura

```
nyc_taxi_eda/
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

1. Asegúrate de tener Flask instalado:
```bash
pip install flask
```

2. Navega a la carpeta del dashboard:
```bash
cd dashboards/nyc_taxi_eda
```

3. Ejecuta la aplicación:
```bash
python app.py
```

4. Abre tu navegador en: http://localhost:5000

## API Endpoints

- `GET /` - Página principal del dashboard
- `GET /api/graficos` - Datos para gráficos en formato JSON
- `GET /api/estadisticas` - Estadísticas del dataset en formato JSON

## Visualizaciones incluidas

1. **Distribución de Distancias**: Gráfico de barras mostrando la distribución de distancias de viaje
2. **Distribución de Tarifas**: Gráfico de líneas con las tarifas de los viajes
3. **Pasajeros por Viaje**: Gráfico de dona mostrando la distribución de pasajeros

## Tecnologías utilizadas

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Visualizaciones**: Chart.js
- **Análisis de datos**: Pandas

## Notas para alumnos

Este es un ejemplo de referencia. Pueden:
- Modificar los colores y estilos
- Agregar más visualizaciones
- Crear nuevos endpoints
- Añadir filtros interactivos
- Implementar más análisis estadísticos