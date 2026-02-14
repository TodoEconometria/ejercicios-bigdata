# Capstone Project: Big Data Pipeline with Docker Infrastructure﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​‌‌​‍​​‌‌​​‌‌‍​‌‌​​​‌​‍​‌‌​​​​‌‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​​​‍​​‌‌​​‌‌﻿

**Course:** Big Data with Python - Prof. Juan Marcelo Gutierrez Miranda (@TodoEconometria)

---

## Objective

Build **from scratch** a data processing infrastructure using Docker,﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​‌‌​‍​​‌‌​​‌‌‍​‌‌​​​‌​‍​‌‌​​​​‌‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​​​‍​​‌‌​​‌‌﻿
Apache Spark, and PostgreSQL. Starting from the Quality of Government (QoG) dataset,
design and execute an ETL + analysis pipeline that answers a research question
formulated by you.

**What is evaluated:** Not just the code, but your **learning process**.
You may use AI tools (ChatGPT, Copilot, Claude, etc.) but you must
document how you used them and what you learned.

---

## Dataset

**Quality of Government Standard Dataset (QoG)** - January 2024

- ~15,500 rows (countries x years) x ~1,990 columns
- Variables: democracy, corruption, GDP, health, education, political stability...
- Documentation: [QoG Data](https://www.gu.se/en/quality-government/qog-data)

---

## Structure: 4 Blocks

### Block A: Docker Infrastructure (30%)

Write a `docker-compose.yml` that launches a mini-cluster:

| Service | Minimum requirement |
|---------|-----------------|
| PostgreSQL | Database to store results |
| Spark Master | Cluster coordinator |
| Spark Worker | At least 1 processing node |

**Steps:**

1. Research what Docker Compose is and how a YAML file is structured
2. Write your `docker-compose.yml` with the 3 minimum services
3. Add `healthcheck` at least for PostgreSQL
4. Run `docker compose up -d` and verify everything starts
5. Open the Spark UI and take a **screenshot** showing the connected worker
6. Write `02_INFRAESTRUCTURA.md` explaining **each section** of your YAML in your own words

**Hints:**

- Spark image: `apache/spark:3.5.4-python3` (or `bitnami/spark:3.5`)
- PostgreSQL image: `postgres:15-alpine`
- The Spark Master uses port 7077 for communication and 8080 for the web UI

**Deliverables:** `docker-compose.yml` + `02_INFRAESTRUCTURA.md`

---

### Block B: ETL Pipeline with Spark (25%)

Write a Python script that processes QoG using Apache Spark.

**Steps:**

1. Choose **5 countries** that interest you (they cannot be the ones from the instructor's example: KAZ, UZB, TKM, KGZ, TJK)
2. Choose **5 numerical variables** from the QoG dataset
3. Formulate a **research question**
4. Write `pipeline.py` that:
    - Creates a SparkSession
    - Reads the CSV with `spark.read.csv()`
    - Selects your countries and variables
    - Filters a range of years (e.g., 2000-2023)
    - Creates at least 1 derived variable
    - Saves the result as Parquet

**Important:** Your selection of countries and variables must be UNIQUE. If two students
submit the same 5 countries, it will be considered plagiarism.

**Deliverable:** `pipeline.py`

---

### Block C: Analysis and Visualization (25%)

Analyze your processed data and answer your research question.

**Choose ONE option:**

| Option | What to do | Example |
|--------|-----------|---------|
| **Clustering** | K-Means on your countries | "Which countries are similar based on democracy + GDP?" |
| **Time series** | Evolution chart by country | "How did corruption change between 2000-2023?" |
| **Comparison** | Before/after an event | "Did GDP change after the 2008 crisis?" |

**Minimum requirements:**

- 2 charts (matplotlib, plotly, or seaborn)
- Each chart with title, labeled axes, and legend
- Interpretation paragraph for each chart

**Deliverable:** Charts and interpretation in `03_RESULTADOS.md`

---

### Block D: AI Reflection - "3 Key Moments" (20%)

Document your learning process and share your prompts.

For **each block** (A, B, C), answer:

| Moment | Question |
|--------|----------|
| **Start** | What was the first thing you asked the AI (or searched for)? |
| **Error** | What failed and how did you solve it? |
| **Learning** | What did you learn that you did NOT know before? |

Additionally, paste the **exact text** of the AI prompt that helped you the most in each block.

**What is evaluated:**

- That your prompts are **real** (pasted as-is, not made up afterward)
- That your answers are **specific**
- That the errors are **real** (documenting them does not lower your grade)
- That the process is **consistent** with your code

**Deliverable:** `04_REFLEXION_IA.md`

---

## Comprehension Questions (mandatory)

Answer in `05_RESPUESTAS.md`:

1. **Infrastructure:** If your worker has 2 GB of RAM and the CSV weighs 3 GB, what happens? How would you solve it?
2. **ETL:** Why does `spark.read.csv()` not execute anything until you call `.count()` or `.show()`?
3. **Analysis:** Interpret your main chart: what pattern do you see and why do you think it occurs?
4. **Scalability:** If you had to repeat this with a 50 GB dataset, what would you change in your infrastructure?

---

## Submission Format

```
entregas/trabajo_final/apellido_nombre/
    PROMPTS.md                 <- THE MOST IMPORTANT (your AI prompts)
    01_README.md               <- Your data + research question
    02_INFRAESTRUCTURA.md      <- YAML explanation
    03_RESULTADOS.md           <- Charts + interpretation
    04_REFLEXION_IA.md         <- 3 Key Moments x 3 blocks
    05_RESPUESTAS.md           <- 4 comprehension questions
    docker-compose.yml         <- Your working YAML
    pipeline.py                <- ETL + Analysis
    requirements.txt           <- Dependencies (pip freeze)
    .gitignore                 <- Exclude data, venv, __pycache__
```

Copy the template from `trabajo_final/plantilla/` to your submission folder.

### Process (NO Pull Request)

1. Sync your fork: `git fetch upstream && git merge upstream/main`
2. Copy the template: `cp -r trabajo_final/plantilla/ entregas/trabajo_final/apellido_nombre/`
3. **Fill in PROMPTS.md as you work** - This file is what gets evaluated
4. Complete the files (01 through 05) + `docker-compose.yml` + `pipeline.py`
5. Push to your fork: `git add . && git commit -m "Trabajo Final" && git push`
6. **Done!** The system evaluates your PROMPTS.md automatically

!!! success "You do not need to create a Pull Request"
    The automated system evaluates your **PROMPTS.md** file directly in your fork.
    Just make sure to upload your work with `git push`.

### Prohibited items

- Data files (.csv, .parquet, .db)
- Virtual environments (venv/, .venv/)
- .env files with real credentials
- __pycache__/ folders

---

## Evaluation

| Block | Weight | What is evaluated |
|-------|------|---------------|
| A. Infrastructure | 30% | Working YAML + explanation in your own words |
| B. ETL Pipeline | 25% | Spark API + your own countries/variables + question |
| C. Analysis | 25% | Charts + interpretation that answers your question |
| D. AI Reflection | 20% | Real and specific learning process |

**Penalties:**

- Copying the same countries/variables as another student: -50%
- Copying the countries from the instructor's example (Central Asia): -30%
- YAML that does not work without an explanation of why: -15%
- Absent or generic AI reflection: -20%

---

## Resources

- **Spark Documentation:** [spark.apache.org](https://spark.apache.org/docs/3.5.4/)
- **Docker Compose:** [docs.docker.com/compose](https://docs.docker.com/compose/)
- **QoG Codebook:** [qog.pol.gu.se](https://www.gu.se/en/quality-government/qog-data) (download codebook to see variables)
- **Quick Start Guide:** `trabajo_final/GUIA_INICIO_RAPIDO.md`

﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​‌‌​‍​​‌‌​​‌‌‍​‌‌​​​‌​‍​‌‌​​​​‌‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​​​‍​​‌‌​​‌‌﻿---

**Course:** Big Data with Python - From Zero to Production
**Instructor:** Juan Marcelo Gutierrez Miranda | @TodoEconometria
**Hash ID:** 4e8d9b1a5f6e7c3d2b1a0f9e8d7c6b5a4f3e2d1c0b9a8f7e6d5c4b3a2f1e0d9c
**Methodology:** Progressive exercises with real data and professional tools

**Academic references:**

- Zaharia, M., et al. (2016). Apache Spark: A unified engine for big data processing. Communications of the ACM, 59(11), 56-65.
- Teorell, J., et al. (2024). The Quality of Government Standard Dataset. University of Gothenburg.
- Merkel, D. (2014). Docker: Lightweight Linux Containers for Consistent Development and Deployment. Linux Journal, 2014(239), 2.
