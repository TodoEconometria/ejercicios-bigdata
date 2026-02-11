# Discusión Teórica y Preguntas de Comprensión

## 1. Infraestructura

**Pregunta:** Si tu worker tiene 2 GB de RAM y el CSV pesa 3 GB, ¿qué pasa? ¿Cómo lo solucionarías?

**Respuesta:**
Si el worker tiene menos memoria que el tamaño del dataset, Spark intentará procesar los datos en memoria (RAM). Al no caber, ocurrirá un **desbordamiento a disco (spilling)**, lo que ralentizará enormemente el proceso. Si la memoria es insuficiente incluso para las operaciones básicas (como un `join` o `groupBy`), el worker fallará con un error `OutOfMemoryError (OOM)`.

**Solución:**
1.  **Aumentar particiones:** Usar `repartition()` para dividir el dataset en trozos más pequeños que quepan en la memoria disponible de cada ejecutor.
2.  **Escalar horizontalmente:** Añadir más nodos (workers) al cluster para distribuir la carga.
3.  **Optimizar formato:** Usar formatos columnares comprimidos como Parquet en lugar de CSV, que ocupan mucho menos espacio y permiten leer solo las columnas necesarias.

## 2. ETL

**Pregunta:** ¿Por qué `spark.read.csv()` no ejecuta nada hasta que llamas `.count()` o `.show()`?

**Respuesta:**
Spark utiliza un modelo de ejecución **perezosa (lazy evaluation)**. Cuando llamas a `read.csv` o aplicas transformaciones (`filter`, `select`, `withColumn`), Spark solo construye un **Plan Lógico** (DAG - Grafo Acíclico Dirigido) de lo que *debería* hacer, pero no procesa ningún dato real.

Solo cuando se invoca una **acción** (como `count()`, `show()`, `write()`, `collect()`), Spark optimiza ese plan lógico, lo convierte en un plan físico y ejecuta las tareas necesarias. Esto permite a Spark optimizar consultas completas (ej: filtrar antes de hacer un join costoso) en lugar de ejecutar paso a paso ciegamente.

## 3. Análisis

**Pregunta:** Interpreta tu gráfico principal: ¿qué patrón ves y por qué crees que ocurre?

**Respuesta:**
En el gráfico de dispersión (Scatter Plot) de **Democracia vs PIB per Cápita** en el Magreb, observamos un patrón interesante y contraintuitivo:
*   **Mauritania (MRT)**, a pesar de tener el PIB per cápita más bajo del grupo (~3,600 USD), muestra el índice de democracia más alto (~0.40).
*   **Argelia (DZA)** y **Libia (LBY)**, con PIBs mucho más altos gracias al petróleo/gas (~13,000 USD), tienen índices democráticos muy bajos (~0.20-0.26).

**Interpretación:** Esto sugiere que en la región del Magreb, la riqueza económica (impulsada por recursos naturales) no se traduce automáticamente en democracia. De hecho, podría indicar la "maldición de los recursos": los estados rentistas (petroleros) pueden usar sus ingresos para sostener regímenes autoritarios y comprar paz social sin necesidad de apertura política. Mauritania, con menos recursos para cooptar, ha tenido una transición política más dinámica (aunque frágil).

## 4. Escalabilidad

**Pregunta:** Si tuvieras que repetir este ejercicio con un dataset de 50 GB, ¿qué cambiarías en tu infraestructura?

**Respuesta:**
Con 50 GB, mi infraestructura actual (Docker local con 1 Master y 1 Worker de 2GB) colapsaría. Haría los siguientes cambios:

1.  **Infraestructura Distribuida:** Migraría de Docker local a un cluster real en la nube (ej: AWS EMR, Databricks o Google Dataproc) con múltiples nodos workers (ej: 3-5 nodos de 16GB RAM cada uno).
2.  **Almacenamiento Distribuido:** No usaría el sistema de archivos local (`/workspace/datos`), sino un sistema distribuido como HDFS o almacenamiento de objetos (S3/GCS) para que todos los nodos accedan a los datos simultáneamente.
3.  **Formato de Datos:** Convertiría el CSV a **Parquet particionado** (por año o región) antes de procesar. Parquet es columnar y permite "predicate pushdown" (filtrar datos antes de leerlos), lo cual es crítico para datasets grandes.
4.  **Optimización de Spark:** Ajustaría la configuración de memoria (`spark.executor.memory`, `spark.driver.memory`) y el paralelismo (`spark.default.parallelism`) para aprovechar los recursos del cluster.
