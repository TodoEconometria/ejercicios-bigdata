# Trabajo Final: Pipeline de Big Data con Infraestructura Docker﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​​​‌‍​‌‌​​‌​‌‍​‌‌​​‌​‌‍​​‌‌​​‌​‍​‌‌​​​​‌‍​‌‌​​‌​​﻿

**Curso:** Big Data con Python - Prof. Juan Marcelo Gutierrez Miranda (@TodoEconometria)

---

## Objetivo

Construir **desde cero** una infraestructura de procesamiento de datos usando Docker,﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​​​‌‍​‌‌​​‌​‌‍​‌‌​​‌​‌‍​​‌‌​​‌​‍​‌‌​​​​‌‍​‌‌​​‌​​﻿
Apache Spark y PostgreSQL. A partir del dataset Quality of Government (QoG),
disenar y ejecutar un pipeline ETL + analisis que responda una pregunta de
investigacion formulada por ti.

**Lo que se evalua:** No solo el codigo, sino tu **proceso de aprendizaje**.
Puedes usar herramientas de IA (ChatGPT, Copilot, Claude, etc.) pero debes
documentar como las usaste y que aprendiste.

---

## Dataset

**Quality of Government Standard Dataset (QoG)** - Enero 2024

- ~15,500 filas (paises x anios) x ~1,990 columnas
- Variables: democracia, corrupcion, PIB, salud, educacion, estabilidad politica...
- Documentacion: [QoG Data](https://www.gu.se/en/quality-government/qog-data)

---

## Estructura: 4 Bloques

### Bloque A: Infraestructura Docker (30%)

Escribir un `docker-compose.yml` que levante un mini-cluster:

| Servicio | Requisito minimo |
|----------|-----------------|
| PostgreSQL | Base de datos para almacenar resultados |
| Spark Master | Coordinador del cluster |
| Spark Worker | Al menos 1 nodo de procesamiento |

**Pasos:**

1. Investiga que es Docker Compose y como se estructura un archivo YAML
2. Escribe tu `docker-compose.yml` con los 3 servicios minimos
3. Agrega `healthcheck` al menos para PostgreSQL
4. Ejecuta `docker compose up -d` y verifica que todo arranca
5. Abre el Spark UI y toma una **captura de pantalla** mostrando el worker conectado
6. Escribe `02_INFRAESTRUCTURA.md` explicando **cada seccion** de tu YAML con tus palabras

**Pistas:**

- Imagen Spark: `apache/spark:3.5.4-python3` (o `bitnami/spark:3.5`)
- Imagen PostgreSQL: `postgres:15-alpine`
- El Master de Spark usa el puerto 7077 para comunicacion y 8080 para la UI web

**Entregables:** `docker-compose.yml` + `02_INFRAESTRUCTURA.md`

---

### Bloque B: Pipeline ETL con Spark (25%)

Escribir un script Python que procese QoG usando Apache Spark.

**Pasos:**

1. Elige **5 paises** que te interesen (no pueden ser los del ejemplo del profesor: KAZ, UZB, TKM, KGZ, TJK)
2. Elige **5 variables numericas** del dataset QoG
3. Formula una **pregunta de investigacion**
4. Escribe `pipeline.py` que:
    - Cree una SparkSession
    - Lea el CSV con `spark.read.csv()`
    - Seleccione tus paises y variables
    - Filtre un rango de anios (ej: 2000-2023)
    - Cree al menos 1 variable derivada
    - Guarde el resultado como Parquet

**Importante:** Tu seleccion de paises y variables debe ser UNICA. Si dos alumnos
entregan los mismos 5 paises, se considerara copia.

**Entregable:** `pipeline.py`

---

### Bloque C: Analisis y Visualizacion (25%)

Analizar tus datos procesados y responder tu pregunta de investigacion.

**Elige UNA opcion:**

| Opcion | Que hacer | Ejemplo |
|--------|-----------|---------|
| **Clustering** | K-Means sobre tus paises | "Que paises se parecen segun democracia + PIB?" |
| **Serie temporal** | Grafico de evolucion por pais | "Como cambio la corrupcion entre 2000-2023?" |
| **Comparacion** | Antes/despues de un evento | "Cambio el PIB tras la crisis de 2008?" |

**Requisitos minimos:**

- 2 graficos (matplotlib, plotly, o seaborn)
- Cada grafico con titulo, ejes etiquetados, y leyenda
- Parrafo de interpretacion por cada grafico

**Entregable:** Graficos e interpretacion en `03_RESULTADOS.md`

---

### Bloque D: Reflexion IA - "3 Momentos Clave" (20%)

Documentar tu proceso de aprendizaje y compartir tus prompts.

Para **cada bloque** (A, B, C), responde:

| Momento | Pregunta |
|---------|----------|
| **Arranque** | Que fue lo primero que le pediste a la IA (o buscaste)? |
| **Error** | Que fallo y como lo resolviste? |
| **Aprendizaje** | Que aprendiste que NO sabias antes? |

Ademas, pega el **texto exacto** del prompt de IA que mas te ayudo en cada bloque.

**Se evalua:**

- Que tus prompts sean **reales** (pegados tal cual, no inventados despues)
- Que tus respuestas sean **especificas**
- Que los errores sean **reales** (documentarlos no baja nota)
- Que el proceso sea **coherente** con tu codigo

**Entregable:** `04_REFLEXION_IA.md`

---

## Preguntas de Comprension (obligatorias)

Responde en `05_RESPUESTAS.md`:

1. **Infraestructura:** Si tu worker tiene 2 GB de RAM y el CSV pesa 3 GB, que pasa? Como lo solucionarias?
2. **ETL:** Por que `spark.read.csv()` no ejecuta nada hasta que llamas `.count()` o `.show()`?
3. **Analisis:** Interpreta tu grafico principal: que patron ves y por que crees que ocurre?
4. **Escalabilidad:** Si tuvieras que repetir con un dataset de 50 GB, que cambiarias en tu infraestructura?

---

## Formato de Entrega

```
entregas/trabajo_final/apellido_nombre/
    PROMPTS.md                 <- LO MAS IMPORTANTE (tus prompts de IA)
    01_README.md               <- Tus datos + pregunta de investigacion
    02_INFRAESTRUCTURA.md      <- Explicacion YAML
    03_RESULTADOS.md           <- Graficos + interpretacion
    04_REFLEXION_IA.md         <- 3 Momentos Clave x 3 bloques
    05_RESPUESTAS.md           <- 4 preguntas de comprension
    docker-compose.yml         <- Tu YAML funcional
    pipeline.py                <- ETL + Analisis
    requirements.txt           <- Dependencias (pip freeze)
    .gitignore                 <- Excluir datos, venv, __pycache__
```

Copia la plantilla desde `trabajo_final/plantilla/` a tu carpeta de entrega.

### Proceso (SIN Pull Request)

1. Sincroniza tu fork: `git fetch upstream && git merge upstream/main`
2. Copia la plantilla: `cp -r trabajo_final/plantilla/ entregas/trabajo_final/apellido_nombre/`
3. **Completa PROMPTS.md mientras trabajas** - Este archivo es lo que se evalua
4. Completa los archivos (01 al 05) + `docker-compose.yml` + `pipeline.py`
5. Sube a tu fork: `git add . && git commit -m "Trabajo Final" && git push`
6. **Listo!** El sistema evalua tu PROMPTS.md automaticamente

!!! success "No necesitas crear Pull Request"
    El sistema automatico evalua tu archivo **PROMPTS.md** directamente en tu fork.
    Solo asegurate de subir tu trabajo con `git push`.

### Prohibido incluir

- Archivos de datos (.csv, .parquet, .db)
- Entornos virtuales (venv/, .venv/)
- Archivos .env con credenciales reales
- Carpetas __pycache__/

---

## Evaluacion

| Bloque | Peso | Que se evalua |
|--------|------|---------------|
| A. Infraestructura | 30% | YAML funcional + explicacion con tus palabras |
| B. Pipeline ETL | 25% | Spark API + paises/variables propios + pregunta |
| C. Analisis | 25% | Graficos + interpretacion que responda tu pregunta |
| D. Reflexion IA | 20% | Proceso de aprendizaje real y especifico |

**Penalizaciones:**

- Copiar los mismos paises/variables que otro alumno: -50%
- Copiar los paises del ejemplo del profesor (Asia Central): -30%
- YAML que no funciona sin explicacion de por que: -15%
- Reflexion IA ausente o generica: -20%

---

## Recursos

- **Spark Documentation:** [spark.apache.org](https://spark.apache.org/docs/3.5.4/)
- **Docker Compose:** [docs.docker.com/compose](https://docs.docker.com/compose/)
- **QoG Codebook:** [qog.pol.gu.se](https://www.gu.se/en/quality-government/qog-data) (descargar codebook para ver variables)
- **Guia de Inicio Rapido:** `trabajo_final/GUIA_INICIO_RAPIDO.md`

﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​​​‌‍​‌‌​​‌​‌‍​‌‌​​‌​‌‍​​‌‌​​‌​‍​‌‌​​​​‌‍​‌‌​​‌​​﻿---

**Curso:** Big Data con Python - De Cero a Produccion
**Profesor:** Juan Marcelo Gutierrez Miranda | @TodoEconometria
**Hash ID:** 4e8d9b1a5f6e7c3d2b1a0f9e8d7c6b5a4f3e2d1c0b9a8f7e6d5c4b3a2f1e0d9c
**Metodologia:** Ejercicios progresivos con datos reales y herramientas profesionales

**Referencias academicas:**

- Zaharia, M., et al. (2016). Apache Spark: A unified engine for big data processing. Communications of the ACM, 59(11), 56-65.
- Teorell, J., et al. (2024). The Quality of Government Standard Dataset. University of Gothenburg.
- Merkel, D. (2014). Docker: Lightweight Linux Containers for Consistent Development and Deployment. Linux Journal, 2014(239), 2.
