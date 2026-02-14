# Modulo 09: Cloud Engineering con LocalStack﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌​​‌‌‍​​‌‌‌​​‌‍​‌‌​​‌​​‍​‌‌​​​‌​‍​‌‌​​​‌‌‍​​‌‌​​‌​‍​‌‌​​​‌​‍​‌‌​​‌​​﻿

## Introduccion

**Cloud Computing** ha revolucionado la forma en que desplegamos y escalamos aplicaciones. Sin embargo, aprender AWS, Azure o GCP tiene una barrera: el costo. Un error en produccion puede generar facturas inesperadas.

**LocalStack** resuelve este problema simulando los servicios de AWS localmente. Puedes aprender S3, Lambda, DynamoDB, Kinesis y mas sin gastar un centavo. Si funciona en LocalStack, funciona en AWS real.

**Terraform** es la herramienta estandar para "Infraestructura como Codigo" (IaC). En lugar de hacer clicks en consolas web, defines tu infraestructura en archivos de texto que puedes versionar, revisar y reutilizar.

---

## Conceptos Fundamentales

### Cloud Computing: Los 3 Modelos

| Modelo | Descripcion | Ejemplo |
|--------|-------------|---------|
| **IaaS** | Infraestructura como Servicio | EC2, VMs |
| **PaaS** | Plataforma como Servicio | Elastic Beanstalk, Heroku |
| **SaaS** | Software como Servicio | Gmail, Salesforce |

### Servicios AWS Clave para Big Data

| Servicio | Proposito | Equivalente Open Source |
|----------|-----------|------------------------|
| **S3** | Almacenamiento de objetos (Data Lake) | MinIO |
| **Lambda** | Funciones serverless | OpenFaaS |
| **Kinesis** | Streaming de datos | Kafka |
| **DynamoDB** | Base de datos NoSQL | MongoDB |
| **EventBridge** | Orquestacion de eventos | Cron + Kafka |
| **IAM** | Control de acceso | - |

### Arquitectura Data Lake (Medallion)

```
┌─────────────────────────────────────────────────────────────┐﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌​​‌‌‍​​‌‌‌​​‌‍​‌‌​​‌​​‍​‌‌​​​‌​‍​‌‌​​​‌‌‍​​‌‌​​‌​‍​‌‌​​​‌​‍​‌‌​​‌​​﻿
│                     DATA LAKE (S3)                          │
├───────────────┬───────────────────┬─────────────────────────┤
│    BRONZE     │      SILVER       │          GOLD           │
│   (Raw Data)  │   (Cleaned Data)  │   (Business-Ready)      │
├───────────────┼───────────────────┼─────────────────────────┤
│ - Datos crudos│ - Datos limpios   │ - Agregaciones          │
│ - JSON/CSV    │ - Parquet         │ - KPIs                  │
│ - Sin esquema │ - Con esquema     │ - Dashboards            │
│ - Append-only │ - Deduplicados    │ - ML-ready              │
└───────────────┴───────────────────┴─────────────────────────┘
```

---

## Herramientas Necesarias

- **Docker** y **Docker Compose**: Para LocalStack
- **Python 3.9+**: Lenguaje principal
- **Terraform**: Infraestructura como codigo
- **awscli-local**: CLI de AWS para LocalStack
- **boto3**: SDK de AWS para Python

### Instalacion de Dependencias

```bash
# Python
pip install boto3 requests

# Terraform (Windows con Chocolatey)
choco install terraform

# Terraform (Linux/Mac)
brew install terraform

# AWS CLI Local
pip install awscli-local
```

---

## Reto 1: Levantar LocalStack

**Objetivo:** Crear un entorno LocalStack funcional con Docker.

**Dificultad:** Basica

### Instrucciones

1. Crea un directorio para el proyecto:
   ```bash
   mkdir cloud-localstack
   cd cloud-localstack
   ```

2. Crea un archivo `docker-compose.yml` con LocalStack

3. El servicio debe:
   - Usar imagen `localstack/localstack:latest`
   - Exponer puerto 4566 (gateway unificado)
   - Habilitar servicios: s3, lambda, dynamodb, events
   - Montar volumen para persistencia

4. Levanta y verifica:
   ```bash
   docker-compose up -d
   curl http://localhost:4566/_localstack/health
   ```

### Criterios de Exito

- [ ] Contenedor LocalStack corriendo
- [ ] Endpoint de health responde con servicios activos
- [ ] Puedes listar buckets S3 (vacio): `awslocal s3 ls`

### Pistas

- Variable `SERVICES` define que servicios activar
- `LOCALSTACK_HOST=localhost` para conexiones locales
- El puerto 4566 es el gateway para todos los servicios

### Recursos

- [LocalStack Documentation](https://docs.localstack.cloud/)
- [Docker Hub - LocalStack](https://hub.docker.com/r/localstack/localstack)

---

## Reto 2: Crear Bucket S3 con Terraform

**Objetivo:** Definir un bucket S3 usando Terraform y desplegarlo en LocalStack.

**Dificultad:** Basica

### Instrucciones

1. Crea un archivo `main.tf`

2. Configura el provider de AWS para LocalStack:
   ```hcl
   provider "aws" {
     region                      = "us-east-1"
     access_key                  = "test"
     secret_key                  = "test"
     skip_credentials_validation = true
     skip_metadata_api_check     = true
     skip_requesting_account_id  = true

     endpoints {
       s3     = "http://localhost:4566"
       lambda = "http://localhost:4566"
       # ... añade mas endpoints
     }
   }
   ```

3. Define un bucket S3:
   ```hcl
   resource "aws_s3_bucket" "data_lake" {
     bucket = "mi-data-lake"
     # ... completa la configuracion
   }
   ```

4. Ejecuta Terraform:
   ```bash
   terraform init
   terraform plan
   terraform apply
   ```

### Criterios de Exito

- [ ] `terraform init` descarga el provider
- [ ] `terraform plan` muestra el bucket a crear
- [ ] `terraform apply` crea el bucket
- [ ] `awslocal s3 ls` muestra "mi-data-lake"

### Pistas

- Los endpoints deben apuntar a `http://localhost:4566`
- `access_key` y `secret_key` pueden ser cualquier valor en LocalStack
- Usa `terraform destroy` para limpiar recursos

---

## Reto 3: Tu Primera Lambda (Hello World)

**Objetivo:** Crear una funcion Lambda y desplegarla con Terraform.

**Dificultad:** Intermedia

### Instrucciones

1. Crea una carpeta `lambdas/` con un archivo `hello.py`:
   ```python
   def handler(event, context):
       """Tu primera Lambda"""
       # Implementa: retorna un saludo con datos del evento
       return {
           "statusCode": 200,
           "body": "..."
       }
   ```

2. Empaqueta la Lambda en un ZIP:
   ```bash
   cd lambdas && zip hello.zip hello.py && cd ..
   ```

3. Añade a `main.tf`:
   ```hcl
   resource "aws_lambda_function" "hello" {
     filename         = "lambdas/hello.zip"
     function_name    = "hello-lambda"
     role             = "arn:aws:iam::000000000000:role/lambda-role"
     handler          = "hello.handler"
     runtime          = "python3.9"
     # ... completa
   }
   ```

4. Aplica y prueba:
   ```bash
   terraform apply
   awslocal lambda invoke --function-name hello-lambda output.json
   cat output.json
   ```

### Criterios de Exito

- [ ] Lambda creada en LocalStack
- [ ] Invocacion retorna statusCode 200
- [ ] El body contiene tu mensaje

### Pistas

- En LocalStack, el role puede ser un ARN ficticio
- El handler es `nombre_archivo.nombre_funcion`
- Usa `source_code_hash` para detectar cambios en el ZIP

---

## Reto 4: Lambda que Consume API Externa

**Objetivo:** Crear una Lambda que capture datos de la ISS en tiempo real.

**Dificultad:** Intermedia

### Instrucciones

1. Crea `lambdas/capturar_iss.py`:
   ```python
   import json
   import urllib.request

   ISS_API = "https://api.wheretheiss.at/v1/satellites/25544"

   def handler(event, context):
       """Captura posicion actual de la ISS"""
       # Implementa:
       # 1. Hacer request a la API
       # 2. Parsear el JSON
       # 3. Extraer: latitude, longitude, altitude, velocity
       # 4. Retornar los datos formateados
       pass
   ```

2. Nota: Lambda no tiene `requests`, usa `urllib.request`:
   ```python
   with urllib.request.urlopen(ISS_API) as response:
       data = json.loads(response.read().decode())
   ```

3. Despliega y prueba la Lambda

### Criterios de Exito

- [ ] Lambda se despliega correctamente
- [ ] Retorna posicion actual de la ISS
- [ ] Datos incluyen lat, lon, alt, velocidad

### Pistas

- Lambda tiene limitaciones de librerias - usa stdlib
- El timeout default es 3 segundos, puede necesitar mas
- Maneja excepciones de red

---

## Reto 5: Guardar Datos en S3

**Objetivo:** Modificar la Lambda para guardar los datos de la ISS en S3.

**Dificultad:** Intermedia

### Instrucciones

1. Modifica `capturar_iss.py` para:
   - Conectarse a S3 usando boto3
   - Guardar cada captura como JSON en el bucket
   - Usar ruta: `raw/iss/{fecha}/{timestamp}.json`

2. Estructura del archivo guardado:
   ```json
   {
     "timestamp": "2024-01-15T10:30:00Z",
     "latitude": 45.123,
     "longitude": -93.456,
     "altitude": 420.5,
     "velocity": 27580.3
   }
   ```

3. Configura boto3 para LocalStack:
   ```python
   import boto3

   s3 = boto3.client('s3',
       endpoint_url='http://host.docker.internal:4566',
       aws_access_key_id='test',
       aws_secret_access_key='test'
   )
   ```

### Criterios de Exito

- [ ] Lambda guarda archivo en S3
- [ ] Ruta incluye fecha y timestamp
- [ ] Archivo contiene datos validos de la ISS
- [ ] Puedes listar archivos: `awslocal s3 ls s3://bucket/raw/iss/ --recursive`

### Pistas

- En Docker, usa `host.docker.internal` para acceder a LocalStack
- `s3.put_object(Bucket, Key, Body)` para guardar
- `Body` debe ser string o bytes

---

## Reto 6: Scheduling con EventBridge

**Objetivo:** Programar la Lambda para que se ejecute automaticamente cada minuto.

**Dificultad:** Avanzada

### Instrucciones

1. Añade a `main.tf` una regla de EventBridge:
   ```hcl
   resource "aws_cloudwatch_event_rule" "cada_minuto" {
     name                = "captura-iss-schedule"
     description         = "Ejecuta Lambda cada minuto"
     schedule_expression = "rate(1 minute)"
   }
   ```

2. Conecta la regla con la Lambda:
   ```hcl
   resource "aws_cloudwatch_event_target" "lambda_target" {
     rule      = aws_cloudwatch_event_rule.cada_minuto.name
     target_id = "captura-iss"
     arn       = aws_lambda_function.capturar_iss.arn
   }
   ```

3. Añade permisos para que EventBridge invoque Lambda:
   ```hcl
   resource "aws_lambda_permission" "allow_eventbridge" {
     # ... completa
   }
   ```

### Criterios de Exito

- [ ] Regla de EventBridge creada
- [ ] Lambda se ejecuta automaticamente
- [ ] Archivos aparecen en S3 cada minuto

### Pistas

- Usa `schedule_expression = "rate(1 minute)"` o cron
- El permiso requiere `statement_id`, `action`, `function_name`, `principal`
- Verifica logs: `awslocal logs tail /aws/lambda/capturar-iss`

---

## Reto 7: DynamoDB para Metadatos

**Objetivo:** Crear una tabla DynamoDB para almacenar metadatos de las capturas.

**Dificultad:** Avanzada

### Instrucciones

1. Añade tabla DynamoDB en Terraform:
   ```hcl
   resource "aws_dynamodb_table" "capturas_metadata" {
     name           = "capturas-iss"
     billing_mode   = "PAY_PER_REQUEST"
     hash_key       = "capture_id"

     attribute {
       name = "capture_id"
       type = "S"
     }
     # ... añade mas atributos si necesitas
   }
   ```

2. Modifica la Lambda para guardar metadatos:
   ```python
   dynamodb = boto3.resource('dynamodb',
       endpoint_url='http://host.docker.internal:4566',
       # ...
   )

   table = dynamodb.Table('capturas-iss')
   table.put_item(Item={
       'capture_id': timestamp,
       's3_path': f's3://bucket/raw/iss/{fecha}/{timestamp}.json',
       'latitude': data['latitude'],
       'longitude': data['longitude'],
       # ...
   })
   ```

### Criterios de Exito

- [ ] Tabla DynamoDB creada
- [ ] Lambda guarda metadatos en cada ejecucion
- [ ] Puedes consultar items: `awslocal dynamodb scan --table-name capturas-iss`

---

## Reto FINAL: Dashboard de Tracker

**Objetivo:** Crear una visualizacion web que muestre la posicion de la ISS en tiempo real.

**Dificultad:** Avanzada

### Criterios de Evaluacion

| Criterio | Puntos |
|----------|--------|
| Mapa con posicion actual de la ISS | 20 |
| Icono personalizado de la ISS | 10 |
| Actualizacion automatica (cada 5-10 seg) | 20 |
| Trayectoria/rastro de movimiento | 15 |
| Datos en vivo (lat, lon, alt, vel) | 15 |
| Predictor de pases sobre una ciudad | 10 |
| Diseño profesional | 10 |
| **Total** | **100** |

### Requisitos Tecnicos

- HTML5 + JavaScript vanilla
- Leaflet.js para mapas
- Fetch API para datos en vivo
- Sin dependencias de Jupyter/Colab

### Sugerencias

- Usa la API directamente: `https://api.wheretheiss.at/v1/satellites/25544`
- Nominatim para geocodificar ciudades
- SVG para el icono de la ISS

### Entrega

- Archivo HTML autocontenido
- Captura de pantalla funcionando
- Breve documentacion

> **Referencia:** Puedes ver un ejemplo de tracker profesional en
> [ISS Tracker](../dashboards/dashboard_iss_tracker.md),
> pero el reto es crear tu propia version.

---

## De LocalStack a AWS Real

Cuando estes listo para produccion:

### Cambios Necesarios

1. **Credenciales reales:**
   ```bash
   aws configure
   # Ingresa Access Key ID y Secret Access Key reales
   ```

2. **Eliminar endpoints locales:**
   ```hcl
   provider "aws" {
     region = "us-east-1"
     # Sin endpoints personalizados
   }
   ```

3. **IAM roles reales:**
   - Crea roles con permisos minimos necesarios
   - Usa politicas gestionadas cuando sea posible

4. **Consideraciones de costo:**
   - S3: $0.023/GB/mes
   - Lambda: 1M invocaciones gratis, luego $0.20/1M
   - DynamoDB: Pay-per-request o provisioned

---

## Recursos y Referencias

### Documentacion Oficial

- [LocalStack Documentation](https://docs.localstack.cloud/)
- [Terraform AWS Provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
- [AWS Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
- [boto3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)

### APIs de Datos

- **ISS Position:** `https://api.wheretheiss.at/v1/satellites/25544`
- **ISS Astronauts:** `http://api.open-notify.org/astros.json`
- **Geocoding:** `https://nominatim.openstreetmap.org/search`

﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌​​‌‌‍​​‌‌‌​​‌‍​‌‌​​‌​​‍​‌‌​​​‌​‍​‌‌​​​‌‌‍​​‌‌​​‌​‍​‌‌​​​‌​‍​‌‌​​‌​​﻿---

**Curso:** Big Data con Python - De Cero a Produccion
**Profesor:** Juan Marcelo Gutierrez Miranda | @TodoEconometria
**Hash ID:** 4e8d9b1a5f6e7c3d2b1a0f9e8d7c6b5a4f3e2d1c0b9a8f7e6d5c4b3a2f1e0d9c
**Metodologia:** Ejercicios progresivos con datos reales y herramientas profesionales

**Referencias Academicas:**

- Wittig, M., & Wittig, A. (2019). *Amazon Web Services in Action* (2nd ed.). Manning Publications. ISBN: 978-1617295119.
- Brikman, Y. (2019). *Terraform: Up & Running* (2nd ed.). O'Reilly Media. ISBN: 978-1492046905.
- Chauhan, A. (2020). Infrastructure as Code (IaC) for Beginners. *Medium - Towards Data Science*.
- Jonas, E., et al. (2019). Cloud programming simplified: A Berkeley view on serverless computing. *arXiv preprint arXiv:1902.03383*.
- LocalStack Team (2024). LocalStack Documentation. https://docs.localstack.cloud/
