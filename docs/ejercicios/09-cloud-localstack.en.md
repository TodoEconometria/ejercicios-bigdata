# Module 09: Cloud Engineering with LocalStack﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌​​‌‌‍​‌‌​​​​‌‍​​‌‌​​​‌‍​‌‌​​​‌​‍​​‌‌‌​​‌‍​‌‌​​‌‌​‍​​‌‌​​‌​‍​​‌‌​​​​﻿

## Introduction

**Cloud Computing** has revolutionized the way we deploy and scale applications. However, learning AWS, Azure, or GCP has a barrier: cost. A mistake in production can generate unexpected bills.

**LocalStack** solves this problem by simulating AWS services locally. You can learn S3, Lambda, DynamoDB, Kinesis, and more without spending a cent. If it works on LocalStack, it works on real AWS.

**Terraform** is the standard tool for "Infrastructure as Code" (IaC). Instead of clicking through web consoles, you define your infrastructure in text files that you can version, review, and reuse.

---

## Fundamental Concepts

### Cloud Computing: The 3 Models

| Model | Description | Example |
|-------|-------------|---------|
| **IaaS** | Infrastructure as a Service | EC2, VMs |
| **PaaS** | Platform as a Service | Elastic Beanstalk, Heroku |
| **SaaS** | Software as a Service | Gmail, Salesforce |

### Key AWS Services for Big Data

| Service | Purpose | Open Source Equivalent |
|---------|---------|------------------------|
| **S3** | Object storage (Data Lake) | MinIO |
| **Lambda** | Serverless functions | OpenFaaS |
| **Kinesis** | Data streaming | Kafka |
| **DynamoDB** | NoSQL database | MongoDB |
| **EventBridge** | Event orchestration | Cron + Kafka |
| **IAM** | Access control | - |

### Data Lake Architecture (Medallion)

```
┌─────────────────────────────────────────────────────────────┐﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌​​‌‌‍​‌‌​​​​‌‍​​‌‌​​​‌‍​‌‌​​​‌​‍​​‌‌‌​​‌‍​‌‌​​‌‌​‍​​‌‌​​‌​‍​​‌‌​​​​﻿
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

## Required Tools

- **Docker** and **Docker Compose**: For LocalStack
- **Python 3.9+**: Main language
- **Terraform**: Infrastructure as code
- **awscli-local**: AWS CLI for LocalStack
- **boto3**: AWS SDK for Python

### Dependency Installation

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

## Challenge 1: Set Up LocalStack

**Objective:** Create a functional LocalStack environment with Docker.

**Difficulty:** Basic

### Instructions

1. Create a directory for the project:
   ```bash
   mkdir cloud-localstack
   cd cloud-localstack
   ```

2. Create a `docker-compose.yml` file with LocalStack

3. The service must:
   - Use image `localstack/localstack:latest`
   - Expose port 4566 (unified gateway)
   - Enable services: s3, lambda, dynamodb, events
   - Mount a volume for persistence

4. Start and verify:
   ```bash
   docker-compose up -d
   curl http://localhost:4566/_localstack/health
   ```

### Success Criteria

- [ ] LocalStack container running
- [ ] Health endpoint responds with active services
- [ ] You can list S3 buckets (empty): `awslocal s3 ls`

### Hints

- The `SERVICES` variable defines which services to activate
- `LOCALSTACK_HOST=localhost` for local connections
- Port 4566 is the gateway for all services

### Resources

- [LocalStack Documentation](https://docs.localstack.cloud/)
- [Docker Hub - LocalStack](https://hub.docker.com/r/localstack/localstack)

---

## Challenge 2: Create an S3 Bucket with Terraform

**Objective:** Define an S3 bucket using Terraform and deploy it to LocalStack.

**Difficulty:** Basic

### Instructions

1. Create a `main.tf` file

2. Configure the AWS provider for LocalStack:
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

3. Define an S3 bucket:
   ```hcl
   resource "aws_s3_bucket" "data_lake" {
     bucket = "mi-data-lake"
     # ... completa la configuracion
   }
   ```

4. Run Terraform:
   ```bash
   terraform init
   terraform plan
   terraform apply
   ```

### Success Criteria

- [ ] `terraform init` downloads the provider
- [ ] `terraform plan` shows the bucket to be created
- [ ] `terraform apply` creates the bucket
- [ ] `awslocal s3 ls` shows "mi-data-lake"

### Hints

- Endpoints must point to `http://localhost:4566`
- `access_key` and `secret_key` can be any value in LocalStack
- Use `terraform destroy` to clean up resources

---

## Challenge 3: Your First Lambda (Hello World)

**Objective:** Create a Lambda function and deploy it with Terraform.

**Difficulty:** Intermediate

### Instructions

1. Create a `lambdas/` folder with a `hello.py` file:
   ```python
   def handler(event, context):
       """Tu primera Lambda"""
       # Implementa: retorna un saludo con datos del evento
       return {
           "statusCode": 200,
           "body": "..."
       }
   ```

2. Package the Lambda into a ZIP:
   ```bash
   cd lambdas && zip hello.zip hello.py && cd ..
   ```

3. Add to `main.tf`:
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

4. Apply and test:
   ```bash
   terraform apply
   awslocal lambda invoke --function-name hello-lambda output.json
   cat output.json
   ```

### Success Criteria

- [ ] Lambda created in LocalStack
- [ ] Invocation returns statusCode 200
- [ ] The body contains your message

### Hints

- In LocalStack, the role can be a fictitious ARN
- The handler is `filename.function_name`
- Use `source_code_hash` to detect changes in the ZIP

---

## Challenge 4: Lambda that Consumes an External API

**Objective:** Create a Lambda that captures ISS data in real time.

**Difficulty:** Intermediate

### Instructions

1. Create `lambdas/capturar_iss.py`:
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

2. Note: Lambda does not have `requests`, use `urllib.request`:
   ```python
   with urllib.request.urlopen(ISS_API) as response:
       data = json.loads(response.read().decode())
   ```

3. Deploy and test the Lambda

### Success Criteria

- [ ] Lambda deploys correctly
- [ ] Returns the current ISS position
- [ ] Data includes lat, lon, alt, velocity

### Hints

- Lambda has library limitations - use the standard library
- The default timeout is 3 seconds, it may need more
- Handle network exceptions

---

## Challenge 5: Save Data to S3

**Objective:** Modify the Lambda to save ISS data to S3.

**Difficulty:** Intermediate

### Instructions

1. Modify `capturar_iss.py` to:
   - Connect to S3 using boto3
   - Save each capture as JSON in the bucket
   - Use path: `raw/iss/{date}/{timestamp}.json`

2. Structure of the saved file:
   ```json
   {
     "timestamp": "2024-01-15T10:30:00Z",
     "latitude": 45.123,
     "longitude": -93.456,
     "altitude": 420.5,
     "velocity": 27580.3
   }
   ```

3. Configure boto3 for LocalStack:
   ```python
   import boto3

   s3 = boto3.client('s3',
       endpoint_url='http://host.docker.internal:4566',
       aws_access_key_id='test',
       aws_secret_access_key='test'
   )
   ```

### Success Criteria

- [ ] Lambda saves file to S3
- [ ] Path includes date and timestamp
- [ ] File contains valid ISS data
- [ ] You can list files: `awslocal s3 ls s3://bucket/raw/iss/ --recursive`

### Hints

- In Docker, use `host.docker.internal` to access LocalStack
- `s3.put_object(Bucket, Key, Body)` to save
- `Body` must be a string or bytes

---

## Challenge 6: Scheduling with EventBridge

**Objective:** Schedule the Lambda to run automatically every minute.

**Difficulty:** Advanced

### Instructions

1. Add an EventBridge rule to `main.tf`:
   ```hcl
   resource "aws_cloudwatch_event_rule" "cada_minuto" {
     name                = "captura-iss-schedule"
     description         = "Ejecuta Lambda cada minuto"
     schedule_expression = "rate(1 minute)"
   }
   ```

2. Connect the rule to the Lambda:
   ```hcl
   resource "aws_cloudwatch_event_target" "lambda_target" {
     rule      = aws_cloudwatch_event_rule.cada_minuto.name
     target_id = "captura-iss"
     arn       = aws_lambda_function.capturar_iss.arn
   }
   ```

3. Add permissions so that EventBridge can invoke the Lambda:
   ```hcl
   resource "aws_lambda_permission" "allow_eventbridge" {
     # ... completa
   }
   ```

### Success Criteria

- [ ] EventBridge rule created
- [ ] Lambda runs automatically
- [ ] Files appear in S3 every minute

### Hints

- Use `schedule_expression = "rate(1 minute)"` or cron
- The permission requires `statement_id`, `action`, `function_name`, `principal`
- Check logs: `awslocal logs tail /aws/lambda/capturar-iss`

---

## Challenge 7: DynamoDB for Metadata

**Objective:** Create a DynamoDB table to store capture metadata.

**Difficulty:** Advanced

### Instructions

1. Add a DynamoDB table in Terraform:
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

2. Modify the Lambda to save metadata:
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

### Success Criteria

- [ ] DynamoDB table created
- [ ] Lambda saves metadata on each execution
- [ ] You can query items: `awslocal dynamodb scan --table-name capturas-iss`

---

## FINAL Challenge: Tracker Dashboard

**Objective:** Create a web visualization that shows the ISS position in real time.

**Difficulty:** Advanced

### Evaluation Criteria

| Criterion | Points |
|-----------|--------|
| Map with current ISS position | 20 |
| Custom ISS icon | 10 |
| Automatic update (every 5-10 sec) | 20 |
| Trajectory/movement trail | 15 |
| Live data (lat, lon, alt, vel) | 15 |
| Flyover predictor for a city | 10 |
| Professional design | 10 |
| **Total** | **100** |

### Technical Requirements

- HTML5 + vanilla JavaScript
- Leaflet.js for maps
- Fetch API for live data
- No Jupyter/Colab dependencies

### Suggestions

- Use the API directly: `https://api.wheretheiss.at/v1/satellites/25544`
- Nominatim for geocoding cities
- SVG for the ISS icon

### Submission

- Self-contained HTML file
- Screenshot showing it working
- Brief documentation

> **Reference:** You can see an example of a professional tracker at
> [ISS Tracker](../dashboards/dashboard_iss_tracker.md),
> but the challenge is to create your own version.

---

## From LocalStack to Real AWS

When you are ready for production:

### Required Changes

1. **Real credentials:**
   ```bash
   aws configure
   # Ingresa Access Key ID y Secret Access Key reales
   ```

2. **Remove local endpoints:**
   ```hcl
   provider "aws" {
     region = "us-east-1"
     # Sin endpoints personalizados
   }
   ```

3. **Real IAM roles:**
   - Create roles with minimum required permissions
   - Use managed policies when possible

4. **Cost considerations:**
   - S3: $0.023/GB/month
   - Lambda: 1M invocations free, then $0.20/1M
   - DynamoDB: Pay-per-request or provisioned

---

## Resources and References

### Official Documentation

- [LocalStack Documentation](https://docs.localstack.cloud/)
- [Terraform AWS Provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
- [AWS Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
- [boto3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)

### Data APIs

- **ISS Position:** `https://api.wheretheiss.at/v1/satellites/25544`
- **ISS Astronauts:** `http://api.open-notify.org/astros.json`
- **Geocoding:** `https://nominatim.openstreetmap.org/search`

﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌​​‌‌‍​‌‌​​​​‌‍​​‌‌​​​‌‍​‌‌​​​‌​‍​​‌‌‌​​‌‍​‌‌​​‌‌​‍​​‌‌​​‌​‍​​‌‌​​​​﻿---

**Course:** Big Data with Python - From Zero to Production
**Instructor:** Juan Marcelo Gutierrez Miranda | @TodoEconometria
**Hash ID:** 4e8d9b1a5f6e7c3d2b1a0f9e8d7c6b5a4f3e2d1c0b9a8f7e6d5c4b3a2f1e0d9c
**Methodology:** Progressive exercises with real data and professional tools

**Academic References:**

- Wittig, M., & Wittig, A. (2019). *Amazon Web Services in Action* (2nd ed.). Manning Publications. ISBN: 978-1617295119.
- Brikman, Y. (2019). *Terraform: Up & Running* (2nd ed.). O'Reilly Media. ISBN: 978-1492046905.
- Chauhan, A. (2020). Infrastructure as Code (IaC) for Beginners. *Medium - Towards Data Science*.
- Jonas, E., et al. (2019). Cloud programming simplified: A Berkeley view on serverless computing. *arXiv preprint arXiv:1902.03383*.
- LocalStack Team (2024). LocalStack Documentation. https://docs.localstack.cloud/
