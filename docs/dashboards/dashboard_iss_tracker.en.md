# ISS Tracker - International Space Station﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌​‌‌‌‍​‌‌​​‌​‌‍​​‌‌​​​‌‍​​‌‌‌​​​‍​​‌‌​‌‌‌‍​​‌‌​‌​​‍​​‌‌​​​​‍​​‌‌​​​‌﻿

**Real-time tracking of the International Space Station**

---

## Description

This dashboard allows you to track the position of the **International Space Station (ISS)**﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌​‌‌‌‍​‌‌​​‌​‌‍​​‌‌​​​‌‍​​‌‌‌​​​‍​​‌‌​‌‌‌‍​​‌‌​‌​​‍​​‌‌​​​​‍​​‌‌​​​‌﻿
in real time, view its orbital trajectory, and predict when it will pass over your location.

## Features

- **Real-time map** with the current ISS position
- **Orbital trajectory** past and future
- **Pass predictor**: enter your city and find out when to see the ISS
- **Live data**: latitude, longitude, altitude, speed
- **Current crew**: astronauts aboard the ISS

## View Dashboard

<div style="text-align: center; margin: 30px 0;">
    <a href="../dashboard_iss_tracker.html" target="_blank"
       style="background: linear-gradient(135deg, #00f2fe, #4facfe);
              color: white; padding: 15px 40px; border-radius: 30px;
              text-decoration: none; font-size: 1.2em; font-weight: bold;">
        Open ISS Tracker
    </a>
</div>

## How to See the ISS

The ISS is visible to the naked eye when it passes over your location at night.
It looks like a **bright star moving quickly** across the sky.

**Tips:**
1. Use the dashboard's predictor to know when it will pass
2. Find a dark spot, away from city lights
3. Look toward the indicated direction (N, NE, E, etc.)
4. The ISS will appear as a bright point moving from horizon to horizon

## ISS Data

| Feature | Value |
|---------|-------|
| **Altitude** | ~420 km above Earth |
| **Speed** | 27,600 km/h (7.66 km/s) |
| **Orbital period** | 92.68 minutes |
| **Orbits per day** | 15.5 |
| **Inclination** | 51.6 degrees |
| **Size** | 109m x 73m (football field) |

## APIs Used

- **[Where The ISS At](https://wheretheiss.at/)**: Real-time position
- **[Open Notify](http://open-notify.org/)**: Astronauts and position
- **[Nominatim](https://nominatim.org/)**: Address geocoding

## Technologies Used

- **LocalStack**: AWS simulation (S3, Lambda, DynamoDB)
- **Terraform**: Infrastructure as Code
- **Kinesis**: Position streaming
- **Plotly**: Interactive visualizations

﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌​‌‌‌‍​‌‌​​‌​‌‍​​‌‌​​​‌‍​​‌‌‌​​​‍​​‌‌​‌‌‌‍​​‌‌​‌​​‍​​‌‌​​​​‍​​‌‌​​​‌﻿---

**Course:** Big Data with Python - From Zero to Production
**Professor:** Juan Marcelo Gutierrez Miranda | @TodoEconometria
