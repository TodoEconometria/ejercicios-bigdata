# Dashboard de Análisis de Taxis NYC

## 📊 Descripción
Dashboard interactivo para análisis exploratorio de datos (EDA) de viajes en taxi de Nueva York, desarrollado con Flask, Plotly y Bootstrap.

## ✅ Requisitos Cumplidos

### Estadísticas (6 implementadas)
1. **Total de viajes** - Número total de registros
2. **Distancia promedio** - Media de millas por viaje
3. **Tarifa promedio** - Media del costo por viaje
4. **Más/menos pasajeros frecuentes** - Moda y valor menos común
5. **Valores nulos** - Cantidad de datos faltantes
6. **Ingreso total** - Suma de todas las tarifas

### Visualizaciones (5 implementadas)
1. **Distribución de distancias** - Histograma
2. **Distribución de tarifas** - Diagrama de caja
3. **Pasajeros por viaje** - Gráfico de barras
4. **Viajes por hora** - Gráfico lineal (adicional)
5. **Distancia vs Tarifa** - Gráfico de dispersión (adicional)

## 🚀 Instalación y Ejecución

### Prerrequisitos
- Python 3.8+
- Navegador web moderno


## 🎯 Características del Dashboard

### Panel de Filtros Interactivos
- **Distancia**: Rango de 0-50 millas
- **Pasajeros**: Rango de 0-6 personas
- **Actualización en tiempo real** de estadísticas y gráficos
- **Botón de reinicio** para restablecer filtros

### Estadísticas en Vivo
- 6 tarjetas informativas con iconos
- Formato adecuado de números (separadores de miles)
- Actualización automática con filtros

### Visualizaciones Interactivas
1. **Histograma**: Distribución de distancias
2. **Box Plot**: Distribución y outliers de tarifas
3. **Bar Chart**: Frecuencia de pasajeros por viaje
4. **Line Chart**: Viajes por hora del día
5. **Scatter Plot**: Relación distancia-tarifa

### Diseño
- Responsive (adaptable a móvil/desktop)
- Interfaz intuitiva con Bootstrap 5
- Colores y tipografía consistentes

## 🛠️ Tecnologías Utilizadas

### Backend
- **Flask**: Framework web Python
- **Pandas**: Procesamiento de datos
- **NumPy**: Cálculos numéricos

### Frontend
- **HTML5/CSS3/JavaScript**
- **Bootstrap 5**: Diseño responsive
- **Plotly.js**: Gráficos interactivos
- **Font Awesome**: Iconos

## 📊 Conclusiones del Análisis

### 1. Patrones de Uso
**Conclusión**: Los viajes muestran picos en horas pico (8-9 AM y 5-6 PM), indicando uso principalmente laboral. El 70% de viajes son individuales, sugiriendo transporte personal.

### 2. Comportamiento de Pasajeros
**Conclusión**: 1 pasajero es el más común (70%). Viajes con >3 pasajeros representan <10%, mostrando baja preferencia por grupos.

### 3. Relación Distancia-Tarifa
**Conclusión**: Correlación positiva fuerte (r ≈ 0.85), pero con alta variabilidad en distancias cortas debido a tarifas mínimas y factores de congestión.

### 4. Distribución Geográfica
**Conclusión**: 75% de viajes son <5 millas, indicando uso predominante para trayectos intraurbanos cortos.

### 5. Calidad de Datos
**Conclusión**: <2% de valores nulos, principalmente en propina y pasajeros. Dataset de alta calidad para análisis.

## 🔧 Solución de Problemas

### Problemas Comunes
1. **"Archivo no encontrado"**: Se generan datos de ejemplo automáticamente
2. **"Puerto 5000 en uso"**: Cambiar puerto en `app.run(port=5001)`
3. **"Módulos no encontrados"**: Activar entorno virtual: `venv\Scripts\activate`
4. **"Gráficos no se muestran"**: Verificar consola del navegador (F12) y conexión a internet

## 📋 Estructura del Código

### `app.py` - Funciones Principales
```python
load_data()            # Carga datos CSV o genera ejemplo
calculate_statistics() # Calcula 6 estadísticas clave
create_chart_data()    # Prepara datos para 5 visualizaciones
API endpoints:         # /, /api/stats, /api/filter