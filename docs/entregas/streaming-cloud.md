# Entregas: Streaming y Cloud (Modulos 08-09)﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌​‌‌‌‍​​‌‌‌​​‌‍​​‌‌​​‌‌‍​​‌‌​‌​‌‍​‌‌​​‌​​‍​‌‌​​​​‌‍​‌‌​​‌​​‍​‌‌​​​​‌﻿

Esta guia explica como entregar los ejercicios de **Streaming con Kafka** y **Cloud con LocalStack**.﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌​‌‌‌‍​​‌‌‌​​‌‍​​‌‌​​‌‌‍​​‌‌​‌​‌‍​‌‌​​‌​​‍​‌‌​​​​‌‍​‌‌​​‌​​‍​‌‌​​​​‌﻿

---

## Resumen

Estos modulos son **opcionales avanzados**. Los completas si quieres ir mas alla del Trabajo Final basico.

| Modulo | Tema | Entrega |
|--------|------|---------|
| **08** | Kafka + Spark Streaming | `entregas/streaming_cloud/kafka/` |
| **09** | LocalStack + Terraform | `entregas/streaming_cloud/localstack/` |

---

## Estructura de Entrega

```
entregas/streaming_cloud/apellido_nombre/
│
├── PROMPTS.md              ← LO MAS IMPORTANTE
│
├── kafka/                  ← Modulo 08 (si lo completaste)
│   ├── docker-compose.yml  ← Kafka en KRaft mode
│   ├── productor.py        ← Tu productor
│   ├── consumidor.py       ← Tu consumidor
│   └── capturas/
│       ├── kafka_ui.png
│       └── alertas.png
│
└── localstack/             ← Modulo 09 (si lo completaste)
    ├── docker-compose.yml  ← LocalStack
    ├── main.tf             ← Tu Terraform
    ├── lambdas/
    │   └── capturar.py
    └── capturas/
        ├── terraform_apply.png
        └── s3_bucket.png
```

---

## El Archivo PROMPTS.md

Igual que el Trabajo Final, lo mas importante es documentar **tus prompts reales**.

### Plantilla

```markdown
# PROMPTS - Streaming y Cloud

**Alumno:** [Tu nombre]
**Fecha:** [Fecha de entrega]
**Modulos completados:** [08 / 09 / ambos]

---

## Parte 1: Mis Prompts (TAL CUAL los escribi)

### Reto 1: Levantar Kafka
[Pega tu prompt real, con errores y todo]

**Respuesta de la IA:**
[Resumen de lo que te respondio]

**Resultado:**
- [ ] Funciono a la primera
- [ ] Tuve que ajustar (explica que)
- [ ] No funciono (explica el error)

### Reto 2: Productor
[...]

### Reto 3: Consumidor
[...]

(continua con cada reto que completaste)

---

## Parte 2: Capturas de Pantalla

Incluye capturas de:
- Kafka UI mostrando mensajes (si hiciste 08)
- Alertas en consola (si hiciste 08)
- `terraform apply` exitoso (si hiciste 09)
- S3 bucket con datos (si hiciste 09)

---

## Parte 3: Reflexion

### Que aprendi sobre streaming/cloud
[2-3 parrafos]

### Diferencia entre batch y streaming
[Tu entendimiento]

### Que haria diferente
[Autocritica]

---

## Parte 4: Blueprint (generado por IA)

Pide a tu IA:
> "Resume en formato profesional los prompts anteriores,
> destacando patrones de aprendizaje y progresion"

[Pega la respuesta aqui]
```

---

## Que se Evalua

| Criterio | Peso | Descripcion |
|----------|------|-------------|
| **Humanidad de prompts** | 40% | Prompts reales, no limpiados |
| **Retos completados** | 30% | Cuantos retos terminaste |
| **Capturas** | 15% | Evidencia visual de que funciona |
| **Reflexion** | 15% | Comprension conceptual |

### Bonus por Dashboard

Si creaste tu propio dashboard de sismos o ISS tracker:

| Criterio | Bonus |
|----------|-------|
| Dashboard funcional | +10% |
| Actualizacion en vivo | +5% |
| Diseño profesional | +5% |

---

## Como Entregar

### Paso 1: Crear tu carpeta

```bash
# Desde la raiz de tu fork
mkdir -p entregas/streaming_cloud/tu_apellido_nombre
```

### Paso 2: Copiar tus archivos

```bash
# Si hiciste Kafka
mkdir -p entregas/streaming_cloud/tu_apellido_nombre/kafka
cp docker-compose.yml productor.py consumidor.py entregas/.../kafka/

# Si hiciste LocalStack
mkdir -p entregas/streaming_cloud/tu_apellido_nombre/localstack
cp -r *.tf lambdas/ entregas/.../localstack/
```

### Paso 3: Crear PROMPTS.md

Usa la plantilla de arriba y documenta todo tu proceso.

### Paso 4: Subir

```bash
git add .
git commit -m "Entrega Streaming/Cloud - Apellido Nombre"
git push
```

---

## Retos Disponibles

### Modulo 08: Kafka

| Reto | Dificultad | Descripcion |
|------|------------|-------------|
| 1 | Basica | Levantar Kafka con Docker |
| 2 | Basica | Crear productor Python |
| 3 | Basica | Crear consumidor Python |
| 4 | Intermedia | Conectar API USGS |
| 5 | Intermedia | Sistema de alertas |
| 6 | Avanzada | Spark Structured Streaming |
| **Final** | Avanzada | Dashboard propio |

Ver detalles: [Streaming con Kafka](../ejercicios/08-streaming-kafka.md)

### Modulo 09: LocalStack

| Reto | Dificultad | Descripcion |
|------|------------|-------------|
| 1 | Basica | Levantar LocalStack |
| 2 | Basica | Bucket S3 con Terraform |
| 3 | Intermedia | Lambda Hello World |
| 4 | Intermedia | Lambda consume API |
| 5 | Intermedia | Guardar en S3 |
| 6 | Avanzada | EventBridge scheduling |
| 7 | Avanzada | DynamoDB metadatos |
| **Final** | Avanzada | ISS Tracker propio |

Ver detalles: [Cloud con LocalStack](../ejercicios/09-cloud-localstack.md)

---

## Ejemplos de Referencia

Los dashboards de referencia estan disponibles para inspiracion:

- [Observatorio Sismico Global](../dashboards/dashboard_sismos_global.md) - Ejemplo de visualizacion de sismos
- [ISS Tracker](../dashboards/dashboard_iss_tracker.md) - Ejemplo de tracker espacial

!!! warning "No copies"
    Estos son ejemplos del profesor. Tu dashboard debe tener tu estilo propio.
    El sistema detecta similitud excesiva.

---

## Preguntas Frecuentes

### Es obligatorio?

No. Estos modulos son **bonus** para quienes quieran profundizar.

### Puedo hacer solo uno?

Si. Puedes entregar solo Kafka (08) o solo LocalStack (09).

### Como afecta mi nota?

Completa correctamente = **bonus** sobre tu nota del Trabajo Final.

### Necesito Spark para el modulo 08?

El reto de Spark Streaming es avanzado. Puedes hacer los retos 1-5 sin Spark.

### LocalStack es igual a AWS real?

El codigo es identico. La diferencia es que LocalStack corre en tu maquina
sin costos. Si tu codigo funciona en LocalStack, funciona en AWS.

﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌​‌‌‌‍​​‌‌‌​​‌‍​​‌‌​​‌‌‍​​‌‌​‌​‌‍​‌‌​​‌​​‍​‌‌​​​​‌‍​‌‌​​‌​​‍​‌‌​​​​‌﻿---

**Curso:** Big Data con Python - De Cero a Produccion
**Profesor:** Juan Marcelo Gutierrez Miranda | @TodoEconometria
**Hash ID:** 4e8d9b1a5f6e7c3d2b1a0f9e8d7c6b5a4f3e2d1c0b9a8f7e6d5c4b3a2f1e0d9c
**Metodologia:** Ejercicios progresivos con datos reales y herramientas profesionales

**Referencias:**
- Kreps, J., Narkhede, N., & Rao, J. (2011). Kafka: A distributed messaging system for log processing.
- Brikman, Y. (2019). *Terraform: Up & Running* (2nd ed.). O'Reilly Media.
- LocalStack Team (2024). LocalStack Documentation. https://docs.localstack.cloud/
