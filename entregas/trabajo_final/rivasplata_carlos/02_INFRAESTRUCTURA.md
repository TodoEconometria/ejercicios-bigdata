# Arquitectura de Infraestructura Big Data con Docker

## 1. Descripción General

Esta infraestructura despliega un **cluster de procesamiento de Big Data** utilizando contenedores Docker. El objetivo es crear un entorno aislado y reproducible para ejecutar tareas de ETL y análisis con Apache Spark. El cluster consta de tres servicios principales: un nodo maestro de Spark (Master), un nodo trabajador (Worker) y una base de datos PostgreSQL para persistencia de datos relacionales. Todo el conjunto se orquesta mediante Docker Compose, permitiendo levantar y detener el entorno con un solo comando.

## 2. Servicios

### 2.1 PostgreSQL
- **Imagen:** `postgres:16-alpine` (Versión ligera basada en Alpine Linux).
- **Función:** Actuar como almacén de datos persistente para resultados estructurados o metadatos del proyecto.
- **Configuración clave:**
    - **Puertos:** Expone el puerto `5432` del contenedor al puerto `5432` de la máquina local (host), permitiendo conexiones desde herramientas externas como DBeaver o pgAdmin.
    - **Volúmenes:** Utiliza un volumen nombrado `postgres_data` para persistir los datos de la base de datos incluso si el contenedor se destruye. También monta scripts de inicialización en `/docker-entrypoint-initdb.d`.
    - **Healthcheck:** Implementa un comando `pg_isready` para verificar que la base de datos esté lista para aceptar conexiones antes de dar el servicio por iniciado.

### 2.2 Spark Master
- **Imagen:** `apache/spark:3.5.4-python3`
- **Función:** Es el cerebro del cluster. Se encarga de coordinar los recursos, programar las aplicaciones y distribuir las tareas entre los workers disponibles.
- **Puertos:**
    - `7077`: Puerto interno para la comunicación entre el Master y los Workers (o drivers externos).
    - `8080`: Puerto para la Interfaz Web (Spark UI), accesible desde el navegador para monitorear el estado del cluster y los trabajos en ejecución.

### 2.3 Spark Worker
- **Imagen:** `apache/spark:3.5.4-python3`
- **Función:** Es el músculo del cluster. Ejecuta las tareas de cómputo (Tasks) que le asigna el Master y reporta el estado y los resultados.
- **Recursos:**
    - **Memoria:** Limitada a `2GB` (`SPARK_WORKER_MEMORY=2g`) para asegurar un rendimiento estable en entornos de desarrollo locales.
    - **Cores:** Configurado para usar `2` núcleos de CPU (`SPARK_WORKER_CORES=2`), permitiendo paralelismo en la ejecución de tareas.
- **Conexión:** Se conecta al Master utilizando la URL `spark://spark-master:7077`.

## 3. Volúmenes y Redes

La configuración de volúmenes es crítica para este proyecto, ya que permite la interacción fluida entre el código en desarrollo y el entorno de ejecución en Docker.

**Mapeo de Volúmenes (`volumes`):**
- `./datos:/workspace/datos`: Permite que Spark lea los datasets (CSV) descargados en tu máquina local.
- `./src:/workspace/src`: Mapea el código fuente, permitiendo editar scripts en tu IDE y ejecutarlos en el contenedor sin reconstruir la imagen.
- `./outputs:/workspace/outputs`: Asegura que los resultados (archivos Parquet, gráficos PNG) generados por Spark se guarden directamente en tu disco duro local.
- `./pipeline.py:/workspace/pipeline.py`: Monta el script principal de ejecución.
- `./requirements.txt:/workspace/requirements.txt`: Permite instalar las dependencias de Python exactas dentro del contenedor.

## 4. Prompts de IA Usados (Bloque A)

**Prompt 1:**
> `docker compose exec spark-master pip install -r /workspace/requirements.txt` me sale esto: `ERROR: Could not open requirements file: [Errno 2] No such file or directory: '/workspace/requirements.txt'`

**Respuesta IA (Resumen):**
> La IA diagnosticó que el error se debía a que el archivo `requirements.txt`, aunque existía en mi carpeta local, no estaba siendo "montado" como un volumen en el contenedor. Por lo tanto, para el contenedor, el archivo no existía en la ruta `/workspace/`.
>
> La solución fue modificar el `docker-compose.yml` para añadir una línea en la sección `volumes` de los servicios de Spark, asegurando que el archivo local fuera visible dentro del contenedor.
>
> **Código sugerido:**
> ```yaml
> services:
>   spark-master:
>     volumes:
>       - ./datos:/workspace/datos
>       - ./src:/workspace/src
>       - ./outputs:/workspace/outputs
>       - ./requirements.txt:/workspace/requirements.txt  # <-- Línea añadida
> ```

---

## Captura de Pantalla (Spark UI)

Pega aquí una captura de pantalla de http://localhost:8080 demostrando que el Worker está vivo.

![Spark UI](outputs/graficos/spark_ui.jpeg)
