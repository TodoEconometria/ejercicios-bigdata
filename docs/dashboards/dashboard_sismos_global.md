# Observatorio Sismico Global﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌​‌‌‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​​‌‍​​‌‌​‌‌‌‍​​‌‌‌​​​‍​​‌‌‌​​‌‍​​‌‌​​‌‌﻿

**Dashboard interactivo de actividad sismica mundial en tiempo real**

---

## Descripcion

Este dashboard muestra la actividad sismica de las ultimas 24 horas utilizando datos﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌​‌‌‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​​‌‍​​‌‌​‌‌‌‍​​‌‌‌​​​‍​​‌‌‌​​‌‍​​‌‌​​‌‌﻿
del **USGS Earthquake Hazards Program** (Servicio Geologico de Estados Unidos).

## Caracteristicas

- **Mapa global interactivo** con todos los sismos detectados
- **Estadisticas en tiempo real**: total de sismos, magnitud maxima, promedio
- **Timeline de actividad** por hora
- **Top 10 regiones** con mayor actividad sismica
- **Clasificacion por magnitud**: Micro, Menor, Ligero, Moderado, Mayor

## Ver Dashboard

<div style="text-align: center; margin: 30px 0;">
    <a href="../dashboard_sismos_global.html" target="_blank"
       style="background: linear-gradient(135deg, #667eea, #764ba2);
              color: white; padding: 15px 40px; border-radius: 30px;
              text-decoration: none; font-size: 1.2em; font-weight: bold;">
        Abrir Observatorio Sismico
    </a>
</div>

## Fuente de Datos

Los datos provienen de la API publica del USGS:

- **URL**: [earthquake.usgs.gov](https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php)
- **Formato**: GeoJSON
- **Actualizacion**: Cada minuto
- **Cobertura**: Global

## Escala de Magnitud

| Categoria | Magnitud | Color | Descripcion |
|-----------|----------|-------|-------------|
| **MICRO** | < 2.5 | Verde | No se siente, solo detectado por instrumentos |
| **MENOR** | 2.5 - 4.0 | Azul | Generalmente no se siente, pero se registra |
| **LIGERO** | 4.0 - 5.0 | Naranja | Se siente, danos menores poco probables |
| **MODERADO** | 5.0 - 7.0 | Rojo | Puede causar danos significativos |
| **MAYOR** | > 7.0 | Morado | Terremoto mayor, danos severos potenciales |

## Tecnologias Utilizadas

- **Apache Kafka**: Streaming de datos en tiempo real
- **Spark Structured Streaming**: Procesamiento distribuido
- **PostgreSQL**: Almacenamiento de alertas
- **Plotly**: Visualizaciones interactivas
- **USGS API**: Fuente de datos oficial

﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌​‌‌‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​​‌‍​​‌‌​‌‌‌‍​​‌‌‌​​​‍​​‌‌‌​​‌‍​​‌‌​​‌‌﻿---

**Curso:** Big Data con Python - De Cero a Produccion
**Profesor:** Juan Marcelo Gutierrez Miranda | @TodoEconometria
