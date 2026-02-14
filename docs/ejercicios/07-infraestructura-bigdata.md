# Modulo 07: Infraestructura Big Data﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌​‌‌‌‍​‌‌​​​​‌‍​‌‌​​​‌​‍​‌‌​​​‌‌‍​​‌‌​​​​‍​​‌‌​​​​‍​​‌‌​‌​​‍​​‌‌​​‌​﻿

**Nivel:** Intermedio-Avanzado | **Tipo:** Teorico-Conceptual con ejemplos practicos

---

## Objetivo

Entender **como se construye** la infraestructura que soporta el procesamiento de grandes volumenes de datos. No solo usar las herramientas, sino comprender por que existen, como se conectan entre si y como se orquestan.﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌​‌‌‌‍​‌‌​​​​‌‍​‌‌​​​‌​‍​‌‌​​​‌‌‍​​‌‌​​​​‍​​‌‌​​​​‍​​‌‌​‌​​‍​​‌‌​​‌​﻿

Este modulo sienta las bases para el **Trabajo Final**, donde cada alumno construye su propia infraestructura Docker + Spark desde cero.

![Infraestructura para Big Data: Contenedores y Orquestacion](../assets/slides/m7_infra_p01.jpg)

---

## Estructura del Modulo

| Seccion | Tema | Pregunta que responde |
|---------|------|----------------------|
| **7.1** | Docker Compose | Como empaqueto y conecto servicios? |
| **7.2** | Cluster Apache Spark | Como proceso datos en paralelo? |

!!! tip "Orden de estudio"
    Estudiar en orden. Docker es la base sobre la que se monta Spark.

---

## 7.1 Docker Compose: Contenedores y Orquestacion

### El Problema: Dependency Hell

![El Problema: Dependency Hell y la Fragilidad del Entorno](../assets/slides/m7_infra_p02.jpg)

### Contenedores vs Maquinas Virtuales

![Contenedores vs Maquinas Virtuales](../assets/slides/m7_infra_p03.jpg)

### Imagenes vs Contenedores

![El Plano de Construccion: Imagenes vs Contenedores](../assets/slides/m7_infra_p04.jpg)

### Orquestacion con Docker Compose

![Orquestacion: El Director de la Orquesta de Datos](../assets/slides/m7_infra_p05.jpg)

### Que aprenderas

- Que es Docker y por que resuelve el "dependency hell"
- Diferencia entre **contenedores** y **maquinas virtuales**
- **Imagenes**, **contenedores** y **Dockerfile** (capas, cache, Docker Hub)
- **Docker Compose**: orquestar multiples servicios con un solo archivo YAML
- Directivas clave: `services`, `image`, `build`, `ports`, `environment`, `volumes`, `networks`, `depends_on`, `healthcheck`, `restart`
- **Redes en Docker**: tipos (bridge, host, overlay), DNS interno, comunicacion por nombre de servicio
- **Volumenes**: named volumes, bind mounts, tmpfs, persistencia de datos
- **Comandos esenciales**: `docker compose up/down/ps/logs/exec`
- **Errores comunes**: puerto ocupado, connection refused, datos perdidos, depends_on sin healthcheck
- **Principio de orquestacion**: Docker Compose vs Docker Swarm vs Kubernetes
- **Patrones utiles**: archivos `.env`, `docker-compose.override.yml`, multi-stage builds, profiles

### Ejemplo: Stack completo Docker Compose

```yaml
services:
  postgres:
    image: postgres:16
    container_name: bigdata_postgres
    environment:
      POSTGRES_USER: alumno
      POSTGRES_PASSWORD: bigdata2026
      POSTGRES_DB: curso_bigdata
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data
    networks:
      - red_bigdata
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U alumno"]
      interval: 10s
      timeout: 5s
      retries: 5

  pgadmin:
    image: dpage/pgadmin4
    ports:
      - "8080:80"
    depends_on:
      postgres:
        condition: service_healthy
    networks:
      - red_bigdata

volumes:
  pgdata:

networks:
  red_bigdata:
    driver: bridge
```

### Conceptos clave de Docker

| Concepto | Descripcion |
|----------|-------------|
| **Imagen** | Plantilla inmutable con todo lo necesario para ejecutar una app |
| **Contenedor** | Instancia en ejecucion de una imagen |
| **Dockerfile** | Receta para construir una imagen (capas cacheables) |
| **Volume** | Persistencia de datos mas alla del ciclo de vida del contenedor |
| **Network** | Red interna para comunicacion entre contenedores (DNS automatico) |
| **Healthcheck** | Verificacion de que un servicio esta listo para recibir conexiones |

---

## 7.2 Cluster Apache Spark: Arquitectura y Computacion Distribuida

### Que aprenderas

- Historia de Spark: de MapReduce a procesamiento en memoria (100x mas rapido)
- **Arquitectura Master-Worker**: Driver, SparkSession, Cluster Manager, Workers, Executors, Tasks
- **Spark Standalone Mode**: master, workers, asignacion de recursos, Web UI
- **Construir un cluster con Docker**: contenedores como nodos, volumenes compartidos, imagen `apache/spark` (oficial)
- **SparkSession**: punto de entrada, modos local vs cluster, configuraciones clave
- **Lazy Evaluation y DAG**: transformaciones vs acciones, optimizador Catalyst, predicate pushdown
- **Modos de despliegue**: Local, Standalone, YARN, Kubernetes
- **Tuning basico**: dimensionar executors, particiones, small file problem, data locality
- **Monitorizacion con Spark UI**: Jobs, Stages, Storage, Executors, REST API
- **Spark + PostgreSQL**: JDBC connector, leer y escribir datos entre Spark y PostgreSQL
- **De Standalone a produccion**: Kubernetes, servicios gestionados (EMR, Dataproc, Databricks)

### Ejemplo: Cluster Spark con Docker Compose

```yaml
services:
  spark-master:
    image: apache/spark:3.5.4-python3
    container_name: spark-master
    command: /opt/spark/bin/spark-class org.apache.spark.deploy.master.Master
    environment:
      - SPARK_NO_DAEMONIZE=true
    ports:
      - "7077:7077"    # Comunicacion del cluster
      - "8080:8080"    # Web UI del Master

  spark-worker-1:
    image: apache/spark:3.5.4-python3
    command: >
      /opt/spark/bin/spark-class org.apache.spark.deploy.worker.Worker
      spark://spark-master:7077
    environment:
      - SPARK_WORKER_MEMORY=4G
      - SPARK_WORKER_CORES=2
      - SPARK_NO_DAEMONIZE=true
    depends_on:
      - spark-master
```

!!! warning "Imagen oficial"
    Usamos `apache/spark` (imagen oficial de Apache). La imagen `bitnami/spark` fue **descontinuada en septiembre 2025** y ya no recibe actualizaciones.

### Arquitectura Spark

```
Driver Program (tu script Python)
    │
    ▼
SparkSession → SparkContext
    │
    ▼
Cluster Manager (Standalone / YARN / K8s)
    │
    ├── Worker 1 → Executor → Tasks (procesan particiones)
    ├── Worker 2 → Executor → Tasks
    └── Worker N → Executor → Tasks
```

### Transformaciones vs Acciones

| Transformaciones (LAZY) | Acciones (disparan ejecucion) |
|--------------------------|-------------------------------|
| `select()`, `filter()`, `groupBy()` | `show()`, `count()`, `collect()` |
| `join()`, `orderBy()`, `withColumn()` | `write`, `toPandas()`, `take(n)` |
| No ejecutan nada inmediatamente | Disparan toda la cadena de transformaciones |

---

## Relacion con otros modulos

| Modulo | Conexion |
|--------|----------|
| Modulo 2 (ETL) | Pipelines ETL sobre la infraestructura Docker |
| Modulo 3 (Procesamiento Distribuido) | Ejercicios practicos de PySpark y Dask |
| Modulo 4 (Panel Data) | Pipeline Spark completo sobre dataset QoG |
| Modulo 6 (Streaming) | Kafka y Spark Streaming sobre Docker |
| Trabajo Final | El alumno construye infraestructura Docker + Spark desde cero |

---

## Requisitos

- Docker Desktop instalado
- Haber completado al menos el Modulo 1 (Bases de Datos)
- Conocimientos basicos de terminal/PowerShell

---

## Material del Modulo

El contenido completo de cada seccion esta en los README de la carpeta del modulo:

- [7.1 Docker Compose](https://github.com/TodoEconometria/ejercicios-bigdata/tree/main/ejercicios/07_infraestructura_bigdata/7.1_docker_compose) - Contenedores, imagenes, orquestacion, redes, volumenes
- [7.2 Cluster Spark](https://github.com/TodoEconometria/ejercicios-bigdata/tree/main/ejercicios/07_infraestructura_bigdata/7.2_cluster_spark) - Arquitectura distribuida, Docker cluster, tuning, JDBC

---

## Glosario

| Termino | Definicion |
|---------|-----------|
| **Contenedor** | Instancia aislada que comparte el kernel del host (ligero, rapido) |
| **Imagen** | Plantilla inmutable para crear contenedores (capas cacheables) |
| **Docker Compose** | Herramienta para orquestar multiples contenedores con un YAML |
| **Driver** | Proceso principal de Spark que coordina el cluster |
| **Executor** | Proceso JVM en un Worker que ejecuta tareas |
| **Task** | Unidad minima de trabajo; procesa una particion |
| **DAG** | Grafo dirigido aciclico del plan de ejecucion |
| **Lazy Evaluation** | Transformaciones no se ejecutan hasta que una accion las dispara |
| **Catalyst** | Optimizador de queries de Spark SQL |
| **Shuffle** | Redistribucion de datos entre nodos (costoso en red) |

﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌​‌‌‌‍​‌‌​​​​‌‍​‌‌​​​‌​‍​‌‌​​​‌‌‍​​‌‌​​​​‍​​‌‌​​​​‍​​‌‌​‌​​‍​​‌‌​​‌​﻿---

**Curso:** Big Data con Python - De Cero a Produccion
**Profesor:** Juan Marcelo Gutierrez Miranda | @TodoEconometria
**Hash ID:** 4e8d9b1a5f6e7c3d2b1a0f9e8d7c6b5a4f3e2d1c0b9a8f7e6d5c4b3a2f1e0d9c
**Metodologia:** Ejercicios progresivos con datos reales y herramientas profesionales

**Referencias academicas:**
- Kleppmann, M. (2017). *Designing Data-Intensive Applications*. O'Reilly Media.
- Zaharia, M., et al. (2016). Apache Spark: A unified engine for big data processing. *Communications of the ACM*, 59(11), 56-65.
- Merkel, D. (2014). Docker: Lightweight Linux Containers for Consistent Development and Deployment. *Linux Journal*, 2014(239), 2.
- Chambers, B., & Zaharia, M. (2018). *Spark: The Definitive Guide*. O'Reilly Media.
- Dean, J. & Ghemawat, S. (2008). MapReduce: Simplified data processing on large clusters. *Communications of the ACM*, 51(1), 107-113.
