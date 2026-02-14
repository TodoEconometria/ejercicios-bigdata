# Exercise 01: Introduction to SQLite﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌​‌​‌‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌‌​​​‍​‌‌​​‌​‌﻿

Learn how to load and query data using SQLite and Pandas.﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌​‌​‌‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌‌​​​‍​‌‌​​‌​‌﻿

---

## General Information

| Field | Value |
|-------|-------|
| **Level** | 🟢 Basic |
| **Estimated time** | 2-3 hours |
| **Technologies** | Python, SQLite, Pandas |
| **Dataset** | NYC Taxi (10MB sample) |
| **Prerequisites** | Basic Python, basic SQL knowledge |

---

## Learning Objectives

Upon completing this exercise, you will be able to:

- [x] Load large CSV files into SQLite using chunks
- [x] Create and manage SQLite databases
- [x] Execute basic and advanced SQL queries
- [x] Optimize performance with indexes
- [x] Export query results to CSV

---

## The Problem

You have a CSV file with **100,000 records** of NYC taxi trips. If you try to load it all into memory with Pandas, your computer may run out of memory.

**Your mission:** Load this data into a SQLite database efficiently and perform analysis.

---

## Dataset

### NYC Taxi Trip Records

- **File:** `datos/muestra_taxi.csv`
- **Size:** ~10 MB
- **Records:** ~100,000 trips
- **Period:** January 2021

### Data Structure

```python
Columnas:
- tpep_pickup_datetime    # Fecha/hora de inicio del viaje
- tpep_dropoff_datetime   # Fecha/hora de fin del viaje
- passenger_count         # Numero de pasajeros
- trip_distance           # Distancia en millas
- pickup_longitude        # Longitud de origen
- pickup_latitude         # Latitud de origen
- dropoff_longitude       # Longitud de destino
- dropoff_latitude        # Latitud de destino
- payment_type            # Tipo de pago (1=Credit, 2=Cash, ...)
- fare_amount             # Tarifa base
- tip_amount              # Propina
- total_amount            # Total pagado
```

---

## Tasks

### Task 1: Load CSV into SQLite in Chunks

**Objective:** Load the complete CSV into SQLite without running out of memory.

**Requirements:**

- Use `pandas.read_csv()` with the `chunksize` parameter
- Process the CSV in chunks of 10,000 records
- Insert each chunk into the `trips` table
- Display loading progress

**Initial code example:**

```python
import sqlite3
import pandas as pd

def cargar_datos_sqlite(csv_path, db_path, chunksize=10000):
    """
    Carga un CSV grande a SQLite en chunks

    Args:
        csv_path: Ruta al archivo CSV
        db_path: Ruta a la base de datos SQLite
        chunksize: Numero de registros por chunk
    """
    conn = sqlite3.connect(db_path)

    # TODO: Implementar carga por chunks
    # Pista: usa pd.read_csv con chunksize
    # y itera sobre los chunks

    conn.close()
```

!!! tip "Hint"
    ```python
    chunks = pd.read_csv(csv_path, chunksize=chunksize)
    for i, chunk in enumerate(chunks):
        # Insertar chunk en SQLite
        chunk.to_sql('trips', conn, if_exists='append', index=False)
        print(f"Chunk {i+1} cargado")
    ```

---

### Task 2: Create Indexes

**Objective:** Optimize queries by adding indexes to frequently queried columns.

**Requirements:**

- Create an index on `tpep_pickup_datetime`
- Create an index on `payment_type`
- Measure query time before and after creating indexes

**Example:**

```python
def crear_indices(db_path):
    """
    Crea indices para optimizar queries
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # TODO: Crear indices
    # Ejemplo:
    # cursor.execute("CREATE INDEX idx_pickup ON trips(tpep_pickup_datetime)")

    conn.commit()
    conn.close()
```

---

### Task 3: Analysis Queries

**Objective:** Extract insights from the data using SQL.

#### Query 1: Average Revenue by Hour of Day

Calculate the average revenue for each hour of the day.

**Expected SQL:**

```sql
SELECT
    strftime('%H', tpep_pickup_datetime) as hora,
    AVG(total_amount) as promedio_ingreso,
    COUNT(*) as num_viajes
FROM trips
GROUP BY hora
ORDER BY hora
```

**Expected result:**

```
hora  promedio_ingreso  num_viajes
00    15.23             2340
01    14.89             1982
02    16.45             1657
...
```

#### Query 2: Payment Method Distribution

Calculate the percentage of each payment method.

```sql
SELECT
    payment_type,
    COUNT(*) as total,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM trips), 2) as porcentaje
FROM trips
GROUP BY payment_type
ORDER BY total DESC
```

#### Query 3: Top 10 Most Profitable Routes

Find the routes (pickup → dropoff) with the highest average revenue.

!!! warning "Challenge"
    This query requires grouping by rounded coordinates. Think about how to do it.

---

### Task 4: Export Results

**Objective:** Save your analysis results to CSV files.

```python
def exportar_resultados(db_path, query, output_path):
    """
    Ejecuta una query y exporta a CSV

    Args:
        db_path: Ruta a la BD SQLite
        query: Query SQL a ejecutar
        output_path: Ruta del CSV de salida
    """
    conn = sqlite3.connect(db_path)

    # TODO: Ejecutar query y exportar
    # Pista: usa pd.read_sql_query() y df.to_csv()

    conn.close()
```

---

## Evaluation Criteria

### Functionality (40 points)

- [ ] Complete data loading without errors (10 pts)
- [ ] Indexes created correctly (10 pts)
- [ ] Queries execute and return correct results (15 pts)
- [ ] Export works (5 pts)

### Clean Code (30 points)

- [ ] Well-documented functions (10 pts)
- [ ] Readable and organized code (10 pts)
- [ ] Error handling (10 pts)

### Performance (20 points)

- [ ] Efficient loading with chunks (10 pts)
- [ ] Indexes improve performance measurably (10 pts)

### Analysis (10 points)

- [ ] Interpretation of results (5 pts)
- [ ] Additional insights (5 pts)

---

## Deliverables

You must submit by pushing to your fork (git push):

1. **Python code:** `01_cargar_sqlite.py`
2. **Database:** `datos/taxi.db` (DO NOT upload to GitHub, too large)
3. **Results:** `resultados/` folder with exported CSVs
4. **Analysis:** `ANALISIS.md` with your findings

### Folder structure

```
entregas/01_sqlite/tu_apellido_nombre/
├── 01_cargar_sqlite.py
├── resultados/
│   ├── ingresos_por_hora.csv
│   ├── distribucion_pagos.csv
│   └── top_rutas.csv
└── ANALISIS.md
```

---

## Partial Solution Example

!!! example "Sample Code"

    ```python
    import sqlite3
    import pandas as pd
    import time

    def cargar_datos_sqlite(csv_path, db_path, chunksize=10000):
        """Carga CSV a SQLite en chunks"""
        conn = sqlite3.connect(db_path)

        chunks = pd.read_csv(csv_path, chunksize=chunksize)

        for i, chunk in enumerate(chunks):
            chunk.to_sql('trips', conn, if_exists='append', index=False)
            print(f"Chunk {i+1} cargado ({len(chunk)} registros)")

        conn.close()
        print("Carga completa!")

    def crear_indices(db_path):
        """Crea indices para optimizacion"""
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        print("Creando indices...")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_pickup ON trips(tpep_pickup_datetime)")
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_payment ON trips(payment_type)")

        conn.commit()
        conn.close()
        print("Indices creados!")

    def analizar_ingresos_por_hora(db_path):
        """Query: Ingresos promedio por hora"""
        conn = sqlite3.connect(db_path)

        query = """
            SELECT
                strftime('%H', tpep_pickup_datetime) as hora,
                ROUND(AVG(total_amount), 2) as promedio_ingreso,
                COUNT(*) as num_viajes
            FROM trips
            GROUP BY hora
            ORDER BY hora
        """

        df = pd.read_sql_query(query, conn)
        conn.close()

        return df

    if __name__ == "__main__":
        # Rutas
        csv_path = "datos/muestra_taxi.csv"
        db_path = "datos/taxi.db"

        # 1. Cargar datos
        print("=== CARGANDO DATOS ===")
        start = time.time()
        cargar_datos_sqlite(csv_path, db_path)
        print(f"Tiempo: {time.time() - start:.2f} segundos\n")

        # 2. Crear indices
        print("=== CREANDO INDICES ===")
        crear_indices(db_path)
        print()

        # 3. Analisis
        print("=== ANALISIS: INGRESOS POR HORA ===")
        df = analizar_ingresos_por_hora(db_path)
        print(df)

        # Exportar
        df.to_csv("resultados/ingresos_por_hora.csv", index=False)
        print("\nResultados exportados!")
    ```

---

## Reflection Questions

Answer in your `ANALISIS.md`:

1. **Performance:**
    - How long did it take to load 100,000 records?
    - How much did the indexes improve query time?

2. **Insights:**
    - At what time of day do taxis earn the most?
    - What is the most common payment method?
    - What pattern do you observe in the data?

3. **Improvements:**
    - How would you further optimize the loading?
    - What other analyses could be done?
    - What limitations does SQLite have for this dataset?

---

## Additional Resources

### Documentation

- [SQLite Python Tutorial](https://docs.python.org/3/library/sqlite3.html)
- [Pandas to_sql Documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html)
- [SQL Tutorial](https://www.sqlitetutorial.net/)

### Tutorials

- [Working with Large CSV Files](https://pythonspeed.com/articles/pandas-read-csv-fast/)
- [SQLite Indexes](https://www.sqlitetutorial.net/sqlite-index/)

---

## Common Issues

??? question "Error: MemoryError when loading CSV"

    **Cause:** Trying to load the entire file at once.

    **Solution:** Use chunks:
    ```python
    chunks = pd.read_csv(csv_path, chunksize=10000)
    ```

??? question "Very slow query"

    **Cause:** Missing index on queried columns.

    **Solution:** Create indexes:
    ```python
    cursor.execute("CREATE INDEX idx_nombre ON tabla(columna)")
    ```

??? question "Error: database is locked"

    **Cause:** Another process has the database open.

    **Solution:**
    - Close all connections: `conn.close()`
    - Make sure the database is not open in another program

---

## The Big Picture: Data Ecosystems

SQLite is just the first step. In this course you will explore complete database ecosystems:

### SQL vs NoSQL

![The Data Schism: Relational vs NoSQL](../assets/slides/m1_ecosistemas_p03.jpg)

### Key-Value and Columnar Models

![Speed and Scale: Redis, DynamoDB, Cassandra](../assets/slides/m1_ecosistemas_p04.jpg)

### The MongoDB Ecosystem

![Document Flexibility: MongoDB Atlas](../assets/slides/m1_ecosistemas_p05.jpg)

﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌​‌​‌‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌‌​​​‍​‌‌​​‌​‌﻿---

## Next Steps

Once you have completed this exercise:

- [Exercise 02: Data Cleaning](index.md) - Next exercise
- [Submission Guide](../entregas/guia-entregas.md) - How to submit your work
- [Roadmap](../guia-inicio/roadmap.md) - See all exercises
