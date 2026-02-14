# Global Seismic Observatory﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​​‍​​‌‌​​​​‍​‌‌​​‌​‌‍​​‌‌​​​​‍​​‌‌​​​​‍​​‌‌​‌‌​‍​​‌‌‌​​​﻿

**Interactive dashboard of worldwide seismic activity in real time**

---

## Description

This dashboard displays seismic activity from the last 24 hours using data﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​​‍​​‌‌​​​​‍​‌‌​​‌​‌‍​​‌‌​​​​‍​​‌‌​​​​‍​​‌‌​‌‌​‍​​‌‌‌​​​﻿
from the **USGS Earthquake Hazards Program** (United States Geological Survey).

## Features

- **Interactive global map** with all detected earthquakes
- **Real-time statistics**: total earthquakes, maximum magnitude, average
- **Activity timeline** by hour
- **Top 10 regions** with the highest seismic activity
- **Classification by magnitude**: Micro, Minor, Light, Moderate, Major

## View Dashboard

<div style="text-align: center; margin: 30px 0;">
    <a href="../dashboard_sismos_global.html" target="_blank"
       style="background: linear-gradient(135deg, #667eea, #764ba2);
              color: white; padding: 15px 40px; border-radius: 30px;
              text-decoration: none; font-size: 1.2em; font-weight: bold;">
        Open Seismic Observatory
    </a>
</div>

## Data Source

Data comes from the USGS public API:

- **URL**: [earthquake.usgs.gov](https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php)
- **Format**: GeoJSON
- **Update frequency**: Every minute
- **Coverage**: Global

## Magnitude Scale

| Category | Magnitude | Color | Description |
|----------|----------|-------|-------------|
| **MICRO** | < 2.5 | Green | Not felt, only detected by instruments |
| **MINOR** | 2.5 - 4.0 | Blue | Generally not felt, but recorded |
| **LIGHT** | 4.0 - 5.0 | Orange | Felt, minor damage unlikely |
| **MODERATE** | 5.0 - 7.0 | Red | Can cause significant damage |
| **MAJOR** | > 7.0 | Purple | Major earthquake, potential severe damage |

## Technologies Used

- **Apache Kafka**: Real-time data streaming
- **Spark Structured Streaming**: Distributed processing
- **PostgreSQL**: Alert storage
- **Plotly**: Interactive visualizations
- **USGS API**: Official data source

﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​​‍​​‌‌​​​​‍​‌‌​​‌​‌‍​​‌‌​​​​‍​​‌‌​​​​‍​​‌‌​‌‌​‍​​‌‌‌​​​﻿---

**Course:** Big Data with Python - From Zero to Production
**Professor:** Juan Marcelo Gutierrez Miranda | @TodoEconometria
