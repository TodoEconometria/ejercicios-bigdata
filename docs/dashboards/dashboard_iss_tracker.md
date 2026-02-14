# ISS Tracker - Estacion Espacial Internacional﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​​​‌‍​​‌‌​​​‌‍​‌‌​​‌‌​‍​​‌‌​‌​​‍​‌‌​​​‌​‍​‌‌​​​‌​‍​‌‌​​‌​​‍​​‌‌‌​​‌﻿

**Seguimiento en tiempo real de la Estacion Espacial Internacional**

---

## Descripcion

Este dashboard permite rastrear la posicion de la **Estacion Espacial Internacional (ISS)**﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​​​‌‍​​‌‌​​​‌‍​‌‌​​‌‌​‍​​‌‌​‌​​‍​‌‌​​​‌​‍​‌‌​​​‌​‍​‌‌​​‌​​‍​​‌‌‌​​‌﻿
en tiempo real, ver su trayectoria orbital, y predecir cuando pasara sobre tu ubicacion.

## Caracteristicas

- **Mapa en tiempo real** con la posicion actual de la ISS
- **Trayectoria orbital** pasada y futura
- **Predictor de pases**: ingresa tu ciudad y descubre cuando ver la ISS
- **Datos en vivo**: latitud, longitud, altitud, velocidad
- **Tripulacion actual**: astronautas a bordo de la ISS

## Ver Dashboard

<div style="text-align: center; margin: 30px 0;">
    <a href="../dashboard_iss_tracker.html" target="_blank"
       style="background: linear-gradient(135deg, #00f2fe, #4facfe);
              color: white; padding: 15px 40px; border-radius: 30px;
              text-decoration: none; font-size: 1.2em; font-weight: bold;">
        Abrir ISS Tracker
    </a>
</div>

## Como Ver la ISS

La ISS es visible a simple vista cuando pasa sobre tu ubicacion durante la noche.
Se ve como una **estrella brillante moviéndose rapidamente** a traves del cielo.

**Consejos:**
1. Usa el predictor del dashboard para saber cuando pasara
2. Busca un lugar oscuro, lejos de luces de la ciudad
3. Mira hacia la direccion indicada (N, NE, E, etc.)
4. La ISS aparecera como un punto brillante moviéndose de horizonte a horizonte

## Datos de la ISS

| Caracteristica | Valor |
|----------------|-------|
| **Altitud** | ~420 km sobre la Tierra |
| **Velocidad** | 27,600 km/h (7.66 km/s) |
| **Periodo orbital** | 92.68 minutos |
| **Orbitas por dia** | 15.5 |
| **Inclinacion** | 51.6 grados |
| **Tamaño** | 109m x 73m (campo de futbol) |

## APIs Utilizadas

- **[Where The ISS At](https://wheretheiss.at/)**: Posicion en tiempo real
- **[Open Notify](http://open-notify.org/)**: Astronautas y posicion
- **[Nominatim](https://nominatim.org/)**: Geocodificacion de direcciones

## Tecnologias Utilizadas

- **LocalStack**: Simulacion de AWS (S3, Lambda, DynamoDB)
- **Terraform**: Infraestructura como Codigo
- **Kinesis**: Streaming de posiciones
- **Plotly**: Visualizaciones interactivas

﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​​​‌‍​​‌‌​​​‌‍​‌‌​​‌‌​‍​​‌‌​‌​​‍​‌‌​​​‌​‍​‌‌​​​‌​‍​‌‌​​‌​​‍​​‌‌‌​​‌﻿---

**Curso:** Big Data con Python - De Cero a Produccion
**Profesor:** Juan Marcelo Gutierrez Miranda | @TodoEconometria
