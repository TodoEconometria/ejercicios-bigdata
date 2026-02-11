# Trabajo Final: Pipeline de Big Data con Infraestructura Docker

**Alumno:** Carlos Rivasplata
**Curso:** Big Data con Python

---

## Índice

1.  [Tema de Investigación](#1-tema-de-investigación)
2.  [Infraestructura del Proyecto](#2-infraestructura-del-proyecto)
3.  [Resultados y Análisis Visual](#3-resultados-y-análisis-visual)
4.  [Preguntas de Comprensión](#4-preguntas-de-comprensión)
5.  [Cómo Ejecutar este Proyecto](#5-cómo-ejecutar-este-proyecto)

---

## 1. Tema de Investigación

**Título:** Desarrollo Político-Económico en el Magreb: Autoritarismo vs Democracia

**Pregunta de Investigación:**
¿Existe una relación directa entre el desarrollo económico (PIB per cápita) y el nivel de democracia electoral en los países del Magreb? ¿Los países más ricos de la región tienden a ser más democráticos o el autoritarismo persiste independientemente de la riqueza?

### Selección de Datos

#### 1.1 Países (Región Magreb)
He seleccionado los 5 países principales del Magreb debido a su relevancia geopolítica y sus diferentes trayectorias tras la Primavera Árabe:

1.  **Marruecos (MAR):** Monarquía constitucional.
2.  **Argelia (DZA):** República presidencialista con fuerte influencia militar.
3.  **Túnez (TUN):** Única democracia emergente tras 2011 (aunque en retroceso reciente).
4.  **Libia (LBY):** Estado fragmentado tras la guerra civil.
5.  **Mauritania (MRT):** República islámica en transición.

#### 1.2 Variables Seleccionadas (Dataset QoG)

| Variable | Código QoG | Descripción |
|----------|------------|-------------|
| **Democracia** | `vdem_polyarchy` | Índice de democracia electoral de V-Dem (0=Autocracia, 1=Democracia). |
| **Economía** | `wdi_gdppc` | PIB per cápita (USD constantes). Indicador de desarrollo económico. |
| **Corrupción** | `ti_cpi` | Índice de Percepción de la Corrupción (Transparency Int.). |
| **Estabilidad** | `wgi_pv` | Estabilidad política y ausencia de violencia/terrorismo. |
| **Social** | `undp_hdi` / `wdi_lifexp` | Índice de Desarrollo Humano o Esperanza de Vida. |

---

## 2. Infraestructura del Proyecto

### 2.1 Descripción General
Este proyecto se ejecuta sobre un mini-cluster de Big Data orquestado por Docker Compose. La infraestructura levanta un nodo Master de Spark para coordinar tareas, un Worker para el procesamiento, y una base de datos PostgreSQL para un potencial almacenamiento de resultados.

### 2.2 Servicios

#### 2.2.1 PostgreSQL
- **Imagen:** `postgres:16-alpine`
- **Función:** Servir como base de datos relacional para almacenar resultados finales.
- **Configuración clave:** Se exponen los puertos y se utiliza un `healthcheck` para asegurar que el servicio esté listo antes de que otras aplicaciones dependan de él.

#### 2.2.2 Spark Master
- **Imagen:** `apache/spark:3.5.4-python3`
- **Función:** Coordinar el cluster de Spark y distribuir las tareas de procesamiento al Worker.
- **Puertos:** El puerto `8080` se expone para acceder a la Interfaz Gráfica de Usuario (Spark UI) desde el navegador local.

#### 2.2.3 Spark Worker
- **Imagen:** `apache/spark:3.5.4-python3`
- **Función:** Ejecutar las tareas de procesamiento de datos asignadas por el Master.
- **Recursos:** Se le asignan recursos específicos de memoria y CPU para operar.

### 2.3 Volúmenes y Redes
El uso de volúmenes es clave para la comunicación entre la máquina local (host) y los contenedores. Se montan las carpetas locales `datos/`, `src/`, `outputs/` y los archivos `pipeline.py` y `requirements.txt` en la ruta `/workspace` dentro de los contenedores. Esto permite que el código ejecutado en Docker pueda leer los datos de entrada y escribir los resultados (gráficos, Parquet) directamente en el disco local.

### 2.4 Captura de Pantalla (Spark UI)
La siguiente imagen demuestra que la infraestructura está funcionando y que el Spark Worker se ha conectado exitosamente al Master.

![Spark UI](outputs/graficos/spark_ui.jpeg)

---

## 3. Resultados y Análisis Visual

### 3.1 Gráfico 1: Nivel de Democracia en el Magreb

![Gráfico 1](outputs/graficos/01_comparacion_democracia.png)

**Interpretación:**
El gráfico de barras muestra una heterogeneidad significativa en los niveles de democracia electoral en la región.
*   **Mauritania (MRT)** emerge como el país con el índice más alto del grupo, rozando el umbral de "régimen híbrido".
*   **Túnez (TUN)**, a menudo citada como el éxito inicial de la Primavera Árabe, se encuentra en un nivel intermedio, reflejando su reciente retroceso democrático.
*   **Argelia (DZA), Marruecos (MAR) y Libia (LBY)** se agrupan en la categoría de "autoritarios", con Libia mostrando el índice más bajo, lo cual es consistente con su estado de fragmentación política.

### 3.2 Gráfico 2: Relación Democracia vs. Riqueza

![Gráfico 2](outputs/graficos/02_democracia_vs_pib.png)

**Interpretación:**
Este gráfico de dispersión **desafía directamente la hipótesis inicial**. No se observa una correlación positiva clara.
*   **Argelia y Libia** son "outliers" evidentes: poseen un PIB per cápita relativamente alto pero se encuentran entre los regímenes menos democráticos. Esto sugiere un patrón de **estado rentista**, donde la riqueza proveniente de recursos naturales (petróleo/gas) permite sostener el autoritarismo sin necesidad de apertura política.
*   **Mauritania** es el caso opuesto: es el país más pobre del grupo pero el más democrático, rompiendo la supuesta relación riqueza-democracia.

### 3.3 Gráfico 3: Mapa de Calor de Correlación

![Gráfico 3](outputs/graficos/03_heatmap_correlacion.png)

**Interpretación:**
El mapa de calor cuantifica las relaciones entre las variables clave:
*   **Democracia y PIB (`pib_pc`)**: La correlación es de **-0.21**, confirmando la ausencia de una relación positiva y sugiriendo una ligera tendencia inversa en esta muestra.
*   **Correlaciones Fuertes Positivas**: Se observa una fuerte correlación entre **Esperanza de Vida y PIB (0.79)**, lo que indica que la riqueza sí se traduce en mejores indicadores de salud.
*   **Correlaciones Fuertes Negativas**: **Democracia y Estabilidad (-0.81)** muestran una fuerte correlación negativa. Esto es clave: en el Magreb, los regímenes más autoritarios (menos democráticos) son percibidos como más estables, un hallazgo típico en regiones con "pactos autoritarios".

### 3.4 Gráfico 4: Comparativa Institucional (Estabilidad vs. Corrupción)

![Gráfico 4](outputs/graficos/04_estabilidad_vs_corrupcion.png)

**Interpretación:**
Este gráfico compara la calidad de dos instituciones clave (normalizadas para poder compararlas).
*   Se observa que la percepción de **Control de Corrupción** (barra naranja) es consistentemente baja en toda la región, siendo un desafío transversal.
*   En contraste, el índice de **Estabilidad Política** (barra morada) varía más, siendo más alto en los regímenes monárquicos/presidencialistas fuertes (Argelia, Marruecos) y más bajo en los estados en transición o conflicto (Libia).

### 3.5 Gráfico 5: Impacto Social del Desarrollo

![Gráfico 5](outputs/graficos/05_bubble_social.png)

**Interpretación:**
Este gráfico de burbujas ofrece una visión multidimensional:
*   **Eje X vs Eje Y**: Hay una clara tendencia positiva entre el PIB per cápita y la Esperanza de Vida. Los países más ricos tienden a tener una población más longeva.
*   **Tamaño de la Burbuja (Democracia)**: Las burbujas más grandes (más democráticas), como la de Mauritania, no se encuentran necesariamente en la parte superior derecha. Esto refuerza la idea de que el desarrollo social (salud) en la región está más ligado a la riqueza económica que al tipo de régimen político.

### 3.6 Conclusiones del Análisis

La hipótesis inicial de que un mayor desarrollo económico se correlaciona con una mayor democracia **es rechazada** para la región del Magreb. Los datos sugieren que:
1.  La riqueza, a menudo derivada de recursos naturales, no solo no fomenta la democracia, sino que puede ser un pilar para sostener regímenes autoritarios (la "maldición de los recursos").
2.  El desarrollo social (medido en esperanza de vida) está más fuertemente ligado al PIB que al nivel democrático.
3.  La estabilidad en la región parece estar inversamente correlacionada con la democracia, lo que sugiere que los regímenes autoritarios han logrado mantener un control más estricto, aunque a costa de libertades políticas.

---

## 4. Preguntas de Comprensión

### 4.1 Infraestructura
**Pregunta:** Si tu worker tiene 2 GB de RAM y el CSV pesa 3 GB, ¿qué pasa? ¿Cómo lo solucionarías?

**Respuesta:**
Si el worker tiene menos memoria que el tamaño del dataset, Spark intentará procesar los datos en memoria (RAM). Al no caber, ocurrirá un **desbordamiento a disco (spilling)**, lo que ralentizará enormemente el proceso. Si la memoria es insuficiente incluso para las operaciones básicas (como un `join` o `groupBy`), el worker fallará con un error `OutOfMemoryError (OOM)`.

**Solución:**
1.  **Aumentar particiones:** Usar `repartition()` para dividir el dataset en trozos más pequeños que quepan en la memoria disponible de cada ejecutor.
2.  **Escalar horizontalmente:** Añadir más nodos (workers) al cluster para distribuir la carga.
3.  **Optimizar formato:** Usar formatos columnares comprimidos como Parquet en lugar de CSV, que ocupan mucho menos espacio y permiten leer solo las columnas necesarias.

### 4.2 ETL
**Pregunta:** ¿Por qué `spark.read.csv()` no ejecuta nada hasta que llamas `.count()` o `.show()`?

**Respuesta:**
Spark utiliza un modelo de ejecución **perezosa (lazy evaluation)**. Cuando llamas a `read.csv` o aplicas transformaciones (`filter`, `select`, `withColumn`), Spark solo construye un **Plan Lógico** (DAG - Grafo Acíclico Dirigido) de lo que *debería* hacer, pero no procesa ningún dato real.

Solo cuando se invoca una **acción** (como `count()`, `show()`, `write()`, `collect()`), Spark optimiza ese plan lógico, lo convierte en un plan físico y ejecuta las tareas necesarias. Esto permite a Spark optimizar consultas completas (ej: filtrar antes de hacer un join costoso) en lugar de ejecutar paso a paso ciegamente.

### 4.3 Análisis
**Pregunta:** Interpreta tu gráfico principal: ¿qué patrón ves y por qué crees que ocurre?

**Respuesta:**
En el gráfico de dispersión (Scatter Plot) de **Democracia vs PIB per Cápita** en el Magreb, observamos un patrón interesante y contraintuitivo:
*   **Mauritania (MRT)**, a pesar de tener el PIB per cápita más bajo del grupo (~3,600 USD), muestra el índice de democracia más alto (~0.40).
*   **Argelia (DZA)** y **Libia (LBY)**, con PIBs mucho más altos gracias al petróleo/gas (~13,000 USD), tienen índices democráticos muy bajos (~0.20-0.26).

**Interpretación:** Esto sugiere que en la región del Magreb, la riqueza económica (impulsada por recursos naturales) no se traduce automáticamente en democracia. De hecho, podría indicar la "maldición de los recursos": los estados rentistas (petroleros) pueden usar sus ingresos para sostener regímenes autoritarios y comprar paz social sin necesidad de apertura política. Mauritania, con menos recursos para cooptar, ha tenido una transición política más dinámica (aunque frágil).

### 4.4 Escalabilidad
**Pregunta:** Si tuvieras que repetir este ejercicio con un dataset de 50 GB, ¿qué cambiarías en tu infraestructura?

**Respuesta:**
Con 50 GB, mi infraestructura actual (Docker local con 1 Master y 1 Worker de 2GB) colapsaría. Haría los siguientes cambios:

1.  **Infraestructura Distribuida:** Migraría de Docker local a un cluster real en la nube (ej: AWS EMR, Databricks o Google Dataproc) con múltiples nodos workers (ej: 3-5 nodos de 16GB RAM cada uno).
2.  **Almacenamiento Distribuido:** No usaría el sistema de archivos local (`/workspace/datos`), sino un sistema distribuido como HDFS o almacenamiento de objetos (S3/GCS) para que todos los nodos accedan a los datos simultáneamente.
3.  **Formato de Datos:** Convertiría el CSV a **Parquet particionado** (por año o región) antes de procesar. Parquet es columnar y permite "predicate pushdown" (filtrar datos antes de leerlos), lo cual es crítico para datasets grandes.
4.  **Optimización de Spark:** Ajustaría la configuración de memoria (`spark.executor.memory`, `spark.driver.memory`) y el paralelismo (`spark.default.parallelism`) para aprovechar los recursos del cluster.

---

## 5. Cómo Ejecutar este Proyecto

1.  **Levantar la infraestructura:**
    ```sh
    docker compose up -d
    ```
2.  **Instalar dependencias:**
    ```sh
    docker compose exec -u 0 spark-master pip install -r /workspace/requirements.txt
    ```
3.  **Ejecutar el pipeline completo (Descarga -> ETL -> Análisis):**
    ```sh
    docker compose exec spark-master /opt/spark/bin/spark-submit /workspace/pipeline.py
    ```
4.  **Ver los resultados:** Los gráficos generados se encontrarán en la carpeta `outputs/graficos`.
