# Ejercicio 01: Introduccion a SQLite

Aprende a cargar y consultar datos usando SQLite y Pandas.

---

## Informacion General

| Campo | Valor |
|-------|-------|
| **Nivel** | 🟢 Basico |
| **Tiempo estimado** | 2-3 horas |
| **Tecnologias** | Python, SQLite, Pandas |
| **Dataset** | NYC Taxi (muestra 10MB) |
| **Prerequisitos** | Python basico, conocimientos de SQL basico |

---

## Objetivos de Aprendizaje

Al completar este ejercicio, seras capaz de:

- [x] Cargar archivos CSV grandes a SQLite usando chunks
- [x] Crear y gestionar bases de datos SQLite
- [x] Ejecutar queries SQL basicas y avanzadas
- [x] Optimizar rendimiento con indices
- [x] Exportar resultados de queries a CSV

---

## El Problema

Tienes un archivo CSV con **100,000 registros** de viajes de taxi de NYC. Si intentas cargarlo todo en memoria con Pandas, tu computadora puede quedarse sin memoria.

**Tu mision:** Cargar estos datos a una base de datos SQLite de forma eficiente y realizar analisis.

---

## Dataset

### NYC Taxi Trip Records

- **Archivo:** `datos/muestra_taxi.csv`
- **Tamano:** ~10 MB
- **Registros:** ~100,000 viajes
- **Periodo:** Enero 2021

### Estructura de Datos

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

## Tareas

### Tarea 1: Cargar CSV a SQLite en Chunks

**Objetivo:** Cargar el CSV completo a SQLite sin quedarte sin memoria.

**Requisitos:**

- Usar `pandas.read_csv()` con parametro `chunksize`
- Procesar el CSV en chunks de 10,000 registros
- Insertar cada chunk en la tabla `trips`
- Mostrar progreso de carga

**Ejemplo de codigo inicial:**

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

!!! tip "Pista"
    ```python
    chunks = pd.read_csv(csv_path, chunksize=chunksize)
    for i, chunk in enumerate(chunks):
        # Insertar chunk en SQLite
        chunk.to_sql('trips', conn, if_exists='append', index=False)
        print(f"Chunk {i+1} cargado")
    ```

---

### Tarea 2: Crear Indices

**Objetivo:** Optimizar queries agregando indices a columnas frecuentemente consultadas.

**Requisitos:**

- Crear indice en `tpep_pickup_datetime`
- Crear indice en `payment_type`
- Medir tiempo de query antes y despues de indices

**Ejemplo:**

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

### Tarea 3: Queries de Analisis

**Objetivo:** Extraer insights de los datos usando SQL.

#### Query 1: Ingresos Promedio por Hora del Dia

Calcular el ingreso promedio para cada hora del dia.

**SQL esperado:**

```sql
SELECT
    strftime('%H', tpep_pickup_datetime) as hora,
    AVG(total_amount) as promedio_ingreso,
    COUNT(*) as num_viajes
FROM trips
GROUP BY hora
ORDER BY hora
```

**Resultado esperado:**

```
hora  promedio_ingreso  num_viajes
00    15.23             2340
01    14.89             1982
02    16.45             1657
...
```

#### Query 2: Distribucion de Metodos de Pago

Calcular el porcentaje de cada metodo de pago.

```sql
SELECT
    payment_type,
    COUNT(*) as total,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM trips), 2) as porcentaje
FROM trips
GROUP BY payment_type
ORDER BY total DESC
```

#### Query 3: Top 10 Rutas Mas Rentables

Encontrar las rutas (pickup → dropoff) con mayor ingreso promedio.

!!! warning "Desafio"
    Esta query requiere agrupar por coordenadas redondeadas. Piensa como hacerlo.

---

### Tarea 4: Exportar Resultados

**Objetivo:** Guardar los resultados de tus analisis en archivos CSV.

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

## Criterios de Evaluacion

### Funcionalidad (40 puntos)

- [ ] Carga completa de datos sin errores (10 pts)
- [ ] Indices creados correctamente (10 pts)
- [ ] Queries ejecutan y devuelven resultados correctos (15 pts)
- [ ] Exportacion funciona (5 pts)

### Codigo Limpio (30 puntos)

- [ ] Funciones bien documentadas (10 pts)
- [ ] Codigo legible y organizado (10 pts)
- [ ] Manejo de errores (10 pts)

### Rendimiento (20 puntos)

- [ ] Carga eficiente con chunks (10 pts)
- [ ] Indices mejoran rendimiento medible (10 pts)

### Analisis (10 puntos)

- [ ] Interpretacion de resultados (5 pts)
- [ ] Insights adicionales (5 pts)

---

## Entregables

Debes entregar via Pull Request:

1. **Codigo Python:** `01_cargar_sqlite.py`
2. **Base de datos:** `datos/taxi.db` (NO subir a GitHub, muy grande)
3. **Resultados:** Carpeta `resultados/` con CSVs exportados
4. **Analisis:** `ANALISIS.md` con tus hallazgos

### Estructura de carpeta

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

## Ejemplo de Solucion (Parcial)

!!! example "Codigo de Ejemplo"

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

## Preguntas para Reflexion

Responde en tu `ANALISIS.md`:

1. **Rendimiento:**
    - Cuanto tiempo tomo cargar 100,000 registros?
    - Cuanto mejoraron los indices el tiempo de query?

2. **Insights:**
    - A que hora del dia los taxis ganan mas?
    - Cual es el metodo de pago mas comun?
    - Que patron observas en los datos?

3. **Mejoras:**
    - Como optimizarias aun mas la carga?
    - Que otros analisis se podrian hacer?
    - Que limitaciones tiene SQLite para este dataset?

---

## Recursos Adicionales

### Documentacion

- [SQLite Python Tutorial](https://docs.python.org/3/library/sqlite3.html)
- [Pandas to_sql Documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html)
- [SQL Tutorial](https://www.sqlitetutorial.net/)

### Tutoriales

- [Working with Large CSV Files](https://pythonspeed.com/articles/pandas-read-csv-fast/)
- [SQLite Indexes](https://www.sqlitetutorial.net/sqlite-index/)

---

## Problemas Comunes

??? question "Error: MemoryError al cargar CSV"

    **Causa:** Intentando cargar todo el archivo de una vez.

    **Solucion:** Usa chunks:
    ```python
    chunks = pd.read_csv(csv_path, chunksize=10000)
    ```

??? question "Query muy lenta"

    **Causa:** Falta indice en columnas consultadas.

    **Solucion:** Crea indices:
    ```python
    cursor.execute("CREATE INDEX idx_nombre ON tabla(columna)")
    ```

??? question "Error: database is locked"

    **Causa:** Otro proceso tiene la BD abierta.

    **Solucion:**
    - Cierra todas las conexiones: `conn.close()`
    - Asegurate de no tener la BD abierta en otro programa

---

## Proximos Pasos

Una vez completado este ejercicio:

- [Ejercicio 02: Limpieza de Datos](index.md) - Siguiente ejercicio
- [Crear Pull Request](../git-github/pull-requests.md) - Entregar tu trabajo
- [Roadmap](../guia-inicio/roadmap.md) - Ver todos los ejercicios
