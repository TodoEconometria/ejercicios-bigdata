# Dashboard de Análisis Exploratorio de Datos (EDA) - Taxis de NYC

**Autora**: Aurora Esther FZ

## 1. Descripción del Proyecto

Este proyecto consiste en un dashboard web interactivo desarrollado con Flask y Plotly que realiza un análisis exploratorio sobre el conjunto de datos de los taxis de Nueva York.

La interfaz, diseñada con Bootstrap, es limpia y responsive, y presenta las siguientes visualizaciones y estadísticas clave:

### Estadísticas Principales
- **Total de Viajes**: Conteo total de los trayectos analizados.
- **Distancia Promedio**: Media de la distancia de todos los viajes (en millas).
- **Tarifa Promedio**: Coste medio de un viaje en dólares.
- **Pasajeros Frecuentes**: El número más común de pasajeros por viaje.
- **Valores Nulos**: Conteo de datos faltantes en el conjunto de datos procesado.

### Visualizaciones Interactivas
1.  **Distribución de Distancias de Viaje**: Un histograma que muestra la frecuencia de los viajes según su distancia.
2.  **Distribución de Tarifas**: Un histograma que revela cómo se agrupan los precios de los viajes.
3.  **Pasajeros por Viaje**: Un gráfico de barras que cuenta cuántos viajes se realizan para cada número de pasajeros (1, 2, 3, etc.).

---

## 2. Estructura del Proyecto

La estructura de la carpeta de este dashboard es la siguiente:

```
dashboards/AuroraEstherFZ-dashboard/
├── app.py              # Aplicación Flask principal
├── templates/
│   └── index.html      # Plantilla HTML del dashboard
└── README.md           # Documentación del proyecto
```

El archivo de datos `taxi_limpio.csv` se encuentra en la raíz del proyecto, en la carpeta `datos/`.

---

## 3. Arquitectura del Proyecto

El dashboard sigue una arquitectura cliente-servidor básica:

*   **Backend (Servidor)**: Implementado con **Flask** (Python).
    *   Carga y procesa el dataset de taxis usando **Pandas**.
    *   Calcula las estadísticas descriptivas.
    *   Genera los gráficos interactivos utilizando la librería **Plotly**.
    *   Envía los datos y los gráficos (en formato HTML) a la plantilla.
*   **Frontend (Cliente)**: La interfaz de usuario se construye con **HTML**, **CSS** (Bootstrap para el diseño y Font Awesome para los iconos) y **JavaScript** (para renderizar los gráficos de Plotly).
    *   Recibe los gráficos pre-renderizados en HTML desde Flask y los muestra.

---

## 4. Cómo Ejecutar el Dashboard

Para visualizar el dashboard en tu máquina local, sigue estos pasos:

### Prerrequisitos
- Python 3.x instalado.
- Git instalado.

### Pasos
1.  **Clonar el repositorio (si es necesario):**
    ```bash
    git clone <URL-del-repositorio>
    cd <nombre-del-repositorio>
    ```

2.  **Instalar las dependencias:**
    Se recomienda crear un entorno virtual primero.
    ```bash
    pip install -r requirements.txt
    ```

3.  **Obtener el conjunto de datos:**
    El archivo `taxi_limpio.csv` es necesario. Para generarlo, ejecuta el script que se encuentra en la carpeta `datos`:
    ```bash
    python datos/descargar_datos.py
    ```
    Esto descargará los datos originales y los guardará como `datos/taxi_limpio.csv`.

4.  **Ejecutar la aplicación Flask:**
    Desde la raíz del proyecto, ejecuta el siguiente comando:
    ```bash
    python dashboards/AuroraEstherFZ-dashboard/app.py
    ```

5.  **Abrir en el navegador:**
    Abre tu navegador web y ve a la siguiente dirección:
    ```
    http://127.0.0.1:5000/
    ```

---

## 5. Conclusiones del Análisis

A partir de las visualizaciones y estadísticas presentadas en el dashboard, se pueden extraer las siguientes conclusiones iniciales:

1.  **Los viajes cortos dominan la ciudad**: El histograma de distancias muestra una concentración muy alta de viajes en el rango de 0 a 5 millas. Esto sugiere que el servicio de taxi se utiliza principalmente para trayectos cortos dentro de la ciudad, más que para largas distancias.

2.  **La mayoría de los viajes son individuales**: El gráfico de barras de pasajeros revela que la gran mayoría de los viajes son realizados por un solo pasajero. Los viajes con 2 pasajeros son el segundo caso más común, pero los viajes con 3 o más personas son significativamente menos frecuentes. Esto podría indicar un uso predominante por parte de personas que viajan solas por trabajo o motivos personales.

3.  **Las tarifas se corresponden con las distancias cortas**: Al igual que las distancias, la distribución de tarifas está fuertemente sesgada hacia valores bajos. La mayoría de las tarifas se encuentran por debajo de los 20$, lo cual es coherente con la predominancia de viajes cortos.

4.  **Pocos pasajeros por taxi**: El número más frecuente de pasajeros es 1. Esto podría tener implicaciones para la optimización de rutas o para campañas de marketing enfocadas en viajes compartidos, ya que la mayoría de los vehículos viajan con mucha capacidad libre.

---

## 6. Pendientes / Mejoras Futuras

Este dashboard es una base sólida para un análisis más profundo. Algunas ideas para futuras mejoras incluyen:

*   **Filtros Interactivos**: Añadir opciones para filtrar datos por rango de fechas, número de pasajeros, etc.
*   **Más Visualizaciones**: Incluir gráficos de series temporales (viajes por día/mes), mapas de calor de recogida/destino.
*   **Análisis Avanzado**: Implementar detección de anomalías, correlaciones entre variables (ej. propina vs. distancia).
*   **Conexión a Base de Datos**: En lugar de leer un CSV estático, conectar el dashboard a una base de datos en tiempo real.
*   **Despliegue en la Nube**: Publicar la aplicación en plataformas como Heroku, AWS o Google Cloud.
*   **Mejoras de UI/UX**: Refinar el diseño y la experiencia de usuario.

---

## 7. Licencia

Este proyecto está bajo la Licencia MIT. Eres libre de usar, modificar y distribuir este código.

```
MIT License

Copyright (c) 2025 Aurora Esther FZ

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
