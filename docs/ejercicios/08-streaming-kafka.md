# Modulo 08: Streaming de Datos con Apache Kafka﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌​‌‌​‍​​‌‌​‌​​‍​​‌‌‌​​‌‍​​‌‌‌​​‌‍​‌‌​​​‌‌‍​‌‌​​​​‌‍​‌‌​​‌​​‍​‌‌​​​‌​﻿

## Introduccion

El **streaming de datos** es el procesamiento continuo de datos en tiempo real, a diferencia del procesamiento por lotes (batch) donde los datos se acumulan y procesan periodicamente. En aplicaciones modernas como deteccion de fraudes, monitoreo de sensores IoT, o alertas sismicas, el tiempo de respuesta es critico.﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌​‌‌​‍​​‌‌​‌​​‍​​‌‌‌​​‌‍​​‌‌‌​​‌‍​‌‌​​​‌‌‍​‌‌​​​​‌‍​‌‌​​‌​​‍​‌‌​​​‌​﻿

**Apache Kafka** es una plataforma distribuida de streaming que permite publicar, almacenar y procesar flujos de datos en tiempo real. Desarrollado originalmente por LinkedIn y donado a Apache, Kafka se ha convertido en el estandar de facto para arquitecturas de datos en streaming.

### Formatos de Datos para Ingesta

![Anatomia del Dato: JSON vs XML](../assets/slides/m2_flujo_p03.jpg)

---

## Arquitectura de Kafka

```
┌─────────────┐     ┌─────────────────────────────────────┐     ┌─────────────┐
│  PRODUCTOR  │────>│            KAFKA CLUSTER            │────>│ CONSUMIDOR  │
│  (Python)   │     │  ┌─────────────────────────────┐    │     │  (Python)   │
└─────────────┘     │  │  Topic: sismos              │    │     └─────────────┘
                    │  │  ├── Partition 0            │    │
┌─────────────┐     │  │  ├── Partition 1            │    │     ┌─────────────┐
│  PRODUCTOR  │────>│  │  └── Partition 2            │    │────>│ CONSUMIDOR  │
│   (API)     │     │  └─────────────────────────────┘    │     │  (Spark)    │
└─────────────┘     └─────────────────────────────────────┘     └─────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │   KRaft Mode    │
                    │  (sin ZooKeeper)│
                    └─────────────────┘
```

### Conceptos Clave

| Concepto | Descripcion |
|----------|-------------|
| **Broker** | Servidor Kafka que almacena y sirve mensajes |
| **Topic** | Canal logico donde se publican mensajes (como una tabla) |
| **Partition** | Division de un topic para paralelismo y escalabilidad |
| **Producer** | Aplicacion que envia mensajes a un topic |
| **Consumer** | Aplicacion que lee mensajes de un topic |
| **Consumer Group** | Conjunto de consumidores que comparten la carga de un topic |
| **Offset** | Posicion de un mensaje dentro de una partition |

### KRaft Mode vs ZooKeeper

Desde Kafka 3.x, el modo **KRaft** (Kafka Raft) reemplaza a ZooKeeper para la gestion de metadatos, simplificando la arquitectura:

```
# Antes (con ZooKeeper) - 2 servicios
kafka + zookeeper

# Ahora (KRaft mode) - 1 servicio autocontenido
kafka
```

### Garantias de Entrega

Kafka ofrece tres semanticas de entrega:

| Semantica | Descripcion | Uso tipico |
|-----------|-------------|------------|
| **At-most-once** | Mensaje puede perderse, nunca duplicarse | Logs no criticos |
| **At-least-once** | Mensaje puede duplicarse, nunca perderse | Procesamiento con idempotencia |
| **Exactly-once** | Mensaje se entrega exactamente una vez | Transacciones financieras |

---

## Herramientas Necesarias

- **Docker** y **Docker Compose**: Para levantar la infraestructura
- **Python 3.9+**: Lenguaje principal
- **confluent-kafka**: Cliente Python oficial para Kafka
- **requests**: Para consumir APIs externas

### Instalacion de Dependencias

```bash
pip install confluent-kafka requests
```

---

## Reto 1: Levantar Kafka con Docker Compose

**Objetivo:** Crear un cluster Kafka funcional en tu maquina local usando Docker.

**Dificultad:** Basica

### Instrucciones

1. Crea un directorio para el proyecto:
   ```bash
   mkdir kafka-streaming
   cd kafka-streaming
   ```

2. Crea un archivo `docker-compose.yml` con un broker Kafka en modo KRaft

3. El broker debe cumplir:
   - Imagen: `apache/kafka:latest`
   - Puerto 9092 expuesto
   - Modo KRaft habilitado (sin ZooKeeper)
   - Variables de entorno configuradas correctamente

4. Levanta y verifica:
   ```bash
   docker-compose up -d
   docker-compose logs -f kafka
   ```

### Criterios de Exito

- [ ] El contenedor Kafka esta corriendo sin errores
- [ ] Los logs muestran "Kafka Server started"
- [ ] El puerto 9092 responde

### Pistas

- Consulta la documentacion de la imagen `apache/kafka` en Docker Hub
- Variables clave: `KAFKA_NODE_ID`, `KAFKA_PROCESS_ROLES`, `KAFKA_LISTENERS`
- El modo KRaft requiere `KAFKA_CONTROLLER_QUORUM_VOTERS`

### Recursos

- [Apache Kafka Docker Image](https://hub.docker.com/r/apache/kafka)
- [KRaft Mode Documentation](https://kafka.apache.org/documentation/#kraft)

---

## Reto 2: Tu Primer Productor

**Objetivo:** Crear un script Python que envie mensajes a Kafka.

**Dificultad:** Basica

### Instrucciones

1. Crea `productor_simple.py`

2. El script debe:
   - Conectarse a `localhost:9092`
   - Enviar 10 mensajes al topic `mensajes-test`
   - Cada mensaje debe ser JSON con: `id`, `texto`, `timestamp`
   - Confirmar cada envio exitoso

3. Estructura base:
   ```python
   from confluent_kafka import Producer
   import json
   from datetime import datetime

   def delivery_callback(err, msg):
       """Callback para confirmar envio"""
       # Implementa: imprime error o confirmacion
       pass

   config = {
       'bootstrap.servers': 'localhost:9092',
       'client.id': 'productor-simple'
   }

   producer = Producer(config)

   # Implementa: enviar 10 mensajes
   # Usa: producer.produce(topic, key, value, callback=delivery_callback)
   # No olvides: producer.flush()
   ```

### Criterios de Exito

- [ ] Script ejecuta sin errores
- [ ] 10 mensajes enviados correctamente
- [ ] Cada mensaje tiene estructura JSON valida

### Pistas

- `json.dumps()` para serializar a string
- El `key` puede ser el ID del mensaje
- `flush()` asegura que todos los mensajes se envien antes de terminar

---

## Reto 3: Tu Primer Consumidor

**Objetivo:** Crear un script que lea mensajes de Kafka en tiempo real.

**Dificultad:** Basica

### Instrucciones

1. Crea `consumidor_simple.py`

2. El script debe:
   - Suscribirse al topic `mensajes-test`
   - Leer mensajes en loop infinito
   - Imprimir cada mensaje con su offset y partition
   - Salir limpiamente con Ctrl+C

3. Estructura base:
   ```python
   from confluent_kafka import Consumer, KafkaError
   import json

   config = {
       'bootstrap.servers': 'localhost:9092',
       'group.id': 'mi-grupo-consumidor',
       'auto.offset.reset': 'earliest'  # Leer desde el inicio
   }

   consumer = Consumer(config)
   consumer.subscribe(['mensajes-test'])

   try:
       while True:
           msg = consumer.poll(timeout=1.0)
           # Implementa: verificar errores y procesar mensaje
   except KeyboardInterrupt:
       pass
   finally:
       consumer.close()
   ```

### Criterios de Exito

- [ ] Consumidor se conecta correctamente
- [ ] Lee los mensajes del productor
- [ ] Muestra: partition, offset, key, value
- [ ] Sale limpiamente con Ctrl+C

### Pistas

- Verifica `msg is None` (timeout sin mensaje)
- Verifica `msg.error()` antes de procesar
- Usa `msg.partition()`, `msg.offset()`, `msg.key()`, `msg.value()`

---

## Reto 4: Conectar con API Real (USGS Earthquakes)

**Objetivo:** Crear un productor que consuma datos de sismos en tiempo real.

**Dificultad:** Intermedia

### Instrucciones

1. Crea `productor_sismos.py`

2. El productor debe:
   - Consultar la API de USGS cada 30 segundos
   - Parsear el GeoJSON de respuesta
   - Publicar cada sismo nuevo al topic `sismos`
   - Evitar duplicados (mantener set de IDs procesados)

3. API a usar:
   ```
   https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson
   ```

4. Estructura del mensaje a publicar:
   ```json
   {
     "id": "us7000abcd",
     "magnitud": 4.5,
     "lugar": "10km SSW of Somewhere",
     "latitud": -33.45,
     "longitud": -70.66,
     "profundidad_km": 10.0,
     "timestamp": "2024-01-15T10:30:00.000Z",
     "tsunami": false
   }
   ```

### Criterios de Exito

- [ ] Consulta la API cada 30 segundos
- [ ] Publica sismos al topic `sismos`
- [ ] No publica sismos duplicados
- [ ] Maneja errores de red gracefully
- [ ] Funciona continuamente

### Pistas

- Los sismos estan en `response['features']`
- El ID esta en `feature['id']`
- Las propiedades en `feature['properties']`
- Las coordenadas en `feature['geometry']['coordinates']` (lon, lat, depth)

---

## Reto 5: Sistema de Alertas

**Objetivo:** Crear un consumidor que detecte sismos significativos.

**Dificultad:** Intermedia

### Instrucciones

1. Crea `consumidor_alertas.py`

2. El consumidor debe:
   - Leer del topic `sismos`
   - Filtrar sismos con magnitud >= 4.5
   - Mostrar alerta en consola con formato destacado
   - Guardar alertas en `alertas.log`

3. Formato de alerta:
   ```
   ╔════════════════════════════════════════╗
   ║         ALERTA SISMICA                 ║
   ╠════════════════════════════════════════╣
   ║ Magnitud: 5.2                          ║
   ║ Lugar: 10km S of Tokyo, Japan          ║
   ║ Hora: 2024-01-15 10:30:00              ║
   ║ Coords: (35.6, 139.7)                  ║
   ║ Profundidad: 10.5 km                   ║
   ╚════════════════════════════════════════╝
   ```

### Criterios de Exito

- [ ] Filtra correctamente por magnitud >= 4.5
- [ ] Alertas visibles en consola
- [ ] Alertas guardadas en archivo log
- [ ] Sistema corre continuamente

---

## Reto 6: Agregaciones con Spark Structured Streaming

**Objetivo:** Procesar el stream de sismos con Spark para calcular estadisticas.

**Dificultad:** Avanzada

### Instrucciones

1. Añade un servicio Spark a tu `docker-compose.yml`

2. Crea `spark_streaming_sismos.py`

3. El job debe:
   - Leer del topic `sismos` como stream
   - Parsear los mensajes JSON
   - Calcular por ventana de 5 minutos:
     - Conteo de sismos
     - Magnitud promedio
     - Magnitud maxima
   - Escribir resultados a consola

4. Estructura base:
   ```python
   from pyspark.sql import SparkSession
   from pyspark.sql.functions import *
   from pyspark.sql.types import *

   spark = SparkSession.builder \
       .appName("SismosStreaming") \
       .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0") \
       .getOrCreate()

   # Define schema del mensaje
   schema = StructType([
       StructField("id", StringType()),
       StructField("magnitud", DoubleType()),
       # ... completa el schema
   ])

   # Lee del topic
   df = spark.readStream \
       .format("kafka") \
       .option("kafka.bootstrap.servers", "kafka:9092") \
       .option("subscribe", "sismos") \
       .load()

   # Parsea el JSON
   sismos = df.select(
       from_json(col("value").cast("string"), schema).alias("data")
   ).select("data.*")

   # Implementa: agregaciones por ventana de tiempo
   # Usa: window(), avg(), max(), count()
   ```

### Criterios de Exito

- [ ] Spark lee del topic Kafka
- [ ] Parsea correctamente los mensajes
- [ ] Calcula agregaciones por ventana
- [ ] Muestra resultados en consola

---

## Reto FINAL: Dashboard de Visualizacion

**Objetivo:** Crear una visualizacion web que muestre los sismos en tiempo real.

**Dificultad:** Avanzada

### Criterios de Evaluacion

| Criterio | Puntos |
|----------|--------|
| Mapa interactivo con ubicacion de sismos | 20 |
| Actualizacion automatica sin recargar | 20 |
| Estadisticas en vivo (total, max, promedio) | 15 |
| Filtros por magnitud | 15 |
| Diferenciacion visual por magnitud | 15 |
| Diseño profesional | 15 |
| **Total** | **100** |

### Requisitos Tecnicos

- HTML5 + JavaScript vanilla (sin frameworks)
- Leaflet.js para mapas
- Fetch API para obtener datos
- CSS moderno (flexbox/grid)

### Sugerencias

- Consulta directamente la API de USGS desde JavaScript
- Usa `setInterval()` para actualizacion automatica
- Implementa colores por magnitud (escala de riesgo)

### Entrega

- Archivo HTML autocontenido
- Captura de pantalla funcionando
- Documentacion breve de uso

> **Referencia:** Puedes ver un ejemplo de dashboard en
> [Observatorio Sismico](../dashboards/dashboard_sismos_global.md),
> pero el reto es crear tu propia version con tu estilo.

---

## Recursos y Referencias

### Documentacion Oficial

- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
- [Confluent Python Client](https://docs.confluent.io/kafka-clients/python/current/overview.html)
- [Spark Structured Streaming + Kafka](https://spark.apache.org/docs/latest/structured-streaming-kafka-integration.html)
- [USGS Earthquake API](https://earthquake.usgs.gov/fdsnws/event/1/)

### GeoJSON de Sismos

- Ultima hora: `https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson`
- Ultimo dia: `https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson`
- Ultima semana: `https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson`

﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌​‌‌​‍​​‌‌​‌​​‍​​‌‌‌​​‌‍​​‌‌‌​​‌‍​‌‌​​​‌‌‍​‌‌​​​​‌‍​‌‌​​‌​​‍​‌‌​​​‌​﻿---

**Curso:** Big Data con Python - De Cero a Produccion
**Profesor:** Juan Marcelo Gutierrez Miranda | @TodoEconometria
**Hash ID:** 4e8d9b1a5f6e7c3d2b1a0f9e8d7c6b5a4f3e2d1c0b9a8f7e6d5c4b3a2f1e0d9c
**Metodologia:** Ejercicios progresivos con datos reales y herramientas profesionales

**Referencias Academicas:**

- Kreps, J., Narkhede, N., & Rao, J. (2011). Kafka: A distributed messaging system for log processing. *Proceedings of the NetDB Workshop*.
- Zaharia, M., et al. (2016). Apache Spark: A unified engine for big data processing. *Communications of the ACM, 59*(11), 56-65.
- Kleppmann, M. (2017). *Designing Data-Intensive Applications*. O'Reilly Media. ISBN: 978-1449373320.
- Narkhede, N., Shapira, G., & Palino, T. (2017). *Kafka: The Definitive Guide*. O'Reilly Media. ISBN: 978-1491936160.
- USGS (2024). Earthquake Hazards Program - Real-time Feeds. United States Geological Survey.
