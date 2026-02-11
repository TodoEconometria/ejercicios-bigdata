# Reflexión Metodológica y Proceso de Aprendizaje

## Bloque A: Infraestructura (Docker)

### 1. Arranque
**Pregunta:** "¿Cómo puedo descargar la base de datos QoG automáticamente sin modificar mi estructura de Docker actual?"
**Respuesta:** La IA sugirió un script Python (`00_descargar_qog.py`) que utiliza la librería `requests` para bajar el CSV directamente a la carpeta mapeada `./datos`, evitando configuraciones complejas de `curl` o `wget` dentro del contenedor.

### 2. Error
**Error:** Al ejecutar el script de descarga, fallaba con `FileNotFoundError` porque intentaba escribir en `/workspace/datos` (ruta interna del contenedor) mientras lo ejecutaba desde mi terminal local (donde esa ruta no existe).
**Solución:** Entendí que debía usar rutas relativas locales (`./datos`) cuando ejecuto scripts en mi máquina, o ejecutar el script *dentro* del contenedor usando `docker compose exec`. Optamos por ajustar el script para que detecte el entorno o usar rutas relativas compatibles.

### 3. Aprendizaje
**Aprendizaje:** Aprendí la diferencia crucial entre el **sistema de archivos del host** (mi Mac) y el **sistema de archivos del contenedor**. Los volúmenes en `docker-compose.yml` son el puente que conecta ambos mundos, permitiendo que un archivo descargado localmente sea visible instantáneamente para Spark en `/workspace`.

**Prompt CLAVE (Bloque A):**
> "deseo ejecutar la descarga de la base de datos, ojo que estoy trabajando en docker, pero me esta saliendo error"

---

## Bloque B: Pipeline ETL (Spark)

### 1. Arranque
**Pregunta:** "¿Cómo adapto el pipeline para usar el dataset Cross-Section (CS) en lugar de Time-Series, ya que mi análisis es comparativo y no temporal?"
**Respuesta:** La IA modificó el script para eliminar el filtrado por años (que no existen en CS) y en su lugar enfocarse en la selección correcta de variables (PIB, Democracia, etc.) y la creación de métricas derivadas estáticas.

### 2. Error
**Error:** `pyspark.errors.exceptions.captured.AnalysisException: [UNSUPPORTED_DATA_TYPE_FOR_DATASOURCE] The Parquet datasource doesn't support the column pib_pc of the type "VOID".`
**Solución:** Spark asignaba el tipo `VoidType` (nulo puro) a las columnas que no encontraba en el CSV y llenaba con `F.lit(None)`. Parquet no soporta columnas sin tipo definido. La solución fue hacer un cast explícito: `F.lit(None).cast("double")`.

### 3. Aprendizaje
**Aprendizaje:** Descubrí que Spark necesita un esquema estricto para guardar en Parquet. No basta con tener "nulos", esos nulos deben tener un "tipo" (nulo de string, nulo de entero, etc.). También aprendí a manejar la falta de columnas en datasets cambiantes usando lógica condicional en el ETL.

**Prompt CLAVE (Bloque B):**
> "el error es: pyspark.errors.exceptions.captured.AnalysisException: [UNSUPPORTED_DATA_TYPE_FOR_DATASOURCE] The Parquet datasource doesn't support the column pib_pc of the type 'VOID'."

---

## Bloque C: Análisis (Gráficos)

### 1. Arranque
**Pregunta:** "Quiero unificar todo en un solo archivo `pipeline.py` y añadir gráficos avanzados como un mapa de calor y un bubble plot para enriquecer el análisis del Magreb."
**Respuesta:** La IA reestructuró el proyecto en un único script secuencial (Descarga -> ETL -> Visualización) e integró `seaborn` para generar 5 gráficos automáticos, incluyendo el heatmap de correlación y el gráfico de burbujas.

### 2. Error
**Error:** `ModuleNotFoundError: No module named 'requests'` y `Permission denied` al intentar instalar librerías con `pip` dentro del contenedor.
**Solución:** El usuario `spark` por defecto no tiene permisos para instalar paquetes globales. La solución fue usar el flag `-u 0` (`docker compose exec -u 0 ...`) para ejecutar `pip install` como root y asegurar que todas las dependencias (`pandas`, `seaborn`, `requests`) estuvieran disponibles.

### 3. Aprendizaje
**Aprendizaje:** Aprendí a gestionar dependencias en entornos Docker efímeros. Si el contenedor se destruye, las librerías se pierden, por lo que es vital tener un `requirements.txt` y un proceso de instalación automatizado (o construir una imagen propia). También aprendí que `matplotlib` necesita un backend no interactivo (`Agg`) o guardar en disco cuando se ejecuta en un servidor sin pantalla (headless).

**Prompt CLAVE (Bloque C):**
> "en mi archivo pipeline.py me gustaria anador por lo menos 2 graficos mas que sustentes mas mi investigacion sobre el tema del magregreb"
