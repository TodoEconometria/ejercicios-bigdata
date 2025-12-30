# Validaciones Requeridas

Este documento especifica las **validaciones obligatorias** que tu código debe implementar.

---

## 1. Validaciones de Datos (ETL)

### Extract Phase

```python
def validate_download(df: pd.DataFrame) -> None:
    """Validar dataset descargado."""
    # Check 1: No está vacío
    assert len(df) > 0, "Dataset vacío"

    # Check 2: Tiene columnas esperadas
    required_cols = ['cname', 'year', 'ccodealp']
    missing = set(required_cols) - set(df.columns)
    assert not missing, f"Faltan columnas: {missing}"

    # Check 3: Años son válidos
    assert df['year'].min() >= 1900, "Años inválidos (< 1900)"
    assert df['year'].max() <= 2030, "Años inválidos (> 2030)"

    # Check 4: No hay duplicados (país, año)
    if 'ccodealp' in df.columns:
        dupes = df.duplicated(subset=['ccodealp', 'year']).sum()
        assert dupes == 0, f"{dupes} filas duplicadas detectadas"
```

---

### Transform Phase

```python
def validate_transformations(df_before: pd.DataFrame,
                            df_after: pd.DataFrame) -> None:
    """Validar que transformaciones no corrompieron datos."""
    # Check 1: No se perdieron filas críticas
    rows_lost_pct = (len(df_before) - len(df_after)) / len(df_before)
    assert rows_lost_pct < 0.5, f"Se perdió {rows_lost_pct:.1%} de filas"

    # Check 2: Identificadores siguen siendo únicos
    assert df_after[['country_code', 'year']].duplicated().sum() == 0

    # Check 3: Variables numéricas tienen rangos válidos
    if 'ti_cpi' in df_after.columns:
        assert df_after['ti_cpi'].between(0, 100).all() or df_after['ti_cpi'].isna().all()

    if 'vdem_polyarchy' in df_after.columns:
        assert df_after['vdem_polyarchy'].between(0, 1).all() or df_after['vdem_polyarchy'].isna().all()
```

---

### Load Phase

```python
def validate_database_load(conn, table_name: str,
                          expected_rows: int) -> None:
    """Validar que carga a PostgreSQL fue exitosa."""
    cursor = conn.cursor()

    # Check 1: Tabla existe
    cursor.execute(f"""
        SELECT EXISTS (
            SELECT FROM information_schema.tables
            WHERE table_name = '{table_name}'
        );
    """)
    exists = cursor.fetchone()[0]
    assert exists, f"Tabla {table_name} no existe"

    # Check 2: Número de filas
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    actual_rows = cursor.fetchone()[0]
    tolerance = 0.1  # 10% tolerancia
    assert abs(actual_rows - expected_rows) / expected_rows < tolerance, \
        f"Esperadas ~{expected_rows} filas, encontradas {actual_rows}"

    # Check 3: No hay valores NULL en columnas críticas
    cursor.execute(f"""
        SELECT COUNT(*) FROM {table_name}
        WHERE country_code IS NULL OR year IS NULL
    """)
    nulls = cursor.fetchone()[0]
    assert nulls == 0, f"{nulls} filas con NULL en identificadores"
```

---

## 2. Validaciones de Configuración

### Variables de Entorno

```python
import os
from dotenv import load_dotenv

def validate_env_vars() -> None:
    """Validar que variables de entorno necesarias existen."""
    load_dotenv()

    required_vars = [
        'DB_HOST',
        'DB_PORT',
        'DB_NAME',
        'DB_USER',
        'DB_PASSWORD'
    ]

    missing = [var for var in required_vars if not os.getenv(var)]

    if missing:
        raise EnvironmentError(
            f"Faltan variables de entorno: {missing}. "
            f"Crea archivo .env basado en .env.example"
        )
```

---

### Conexión PostgreSQL

```python
import psycopg2

def validate_db_connection(conn_params: dict) -> None:
    """Validar conexión a PostgreSQL."""
    try:
        conn = psycopg2.connect(**conn_params)
        cursor = conn.cursor()
        cursor.execute("SELECT version();")
        version = cursor.fetchone()[0]

        # Check: PostgreSQL versión >= 14
        major_version = int(version.split()[1].split('.')[0])
        assert major_version >= 14, \
            f"PostgreSQL {major_version} < 14 (versión mínima requerida)"

        cursor.close()
        conn.close()

    except psycopg2.OperationalError as e:
        raise ConnectionError(
            f"No se pudo conectar a PostgreSQL: {e}\n"
            f"Verifica que PostgreSQL está corriendo y .env es correcto"
        )
```

---

## 3. Validaciones de Argumentos

### CLI Arguments

```python
import argparse

def validate_cli_args(args: argparse.Namespace) -> None:
    """Validar argumentos de línea de comandos."""
    # Check 1: Tema válido
    if hasattr(args, 'tema'):
        assert args.tema in [1, 2], \
            f"Tema debe ser 1 o 2, recibido: {args.tema}"

    # Check 2: Años válidos
    if hasattr(args, 'year_start') and hasattr(args, 'year_end'):
        assert args.year_start >= 1900, "year_start >= 1900"
        assert args.year_end <= 2030, "year_end <= 2030"
        assert args.year_start < args.year_end, \
            "year_start debe ser < year_end"
```

---

## 4. Validaciones de Calidad de Datos

### Missing Values

```python
def validate_missing_values(df: pd.DataFrame,
                           max_missing_pct: float = 0.7) -> None:
    """Validar que no hay demasiados valores faltantes."""
    for col in df.columns:
        if col in ['country_code', 'year', 'cname']:
            # Identificadores: 0% missing permitido
            missing_pct = df[col].isna().sum() / len(df)
            assert missing_pct == 0, \
                f"Columna '{col}' tiene {missing_pct:.1%} valores NULL (debe ser 0%)"
        else:
            # Otras variables: max_missing_pct permitido
            missing_pct = df[col].isna().sum() / len(df)
            if missing_pct > max_missing_pct:
                logger.warning(
                    f"Columna '{col}' tiene {missing_pct:.1%} valores NULL "
                    f"(>{max_missing_pct:.0%}). Considera eliminarla."
                )
```

---

### Data Types

```python
def validate_data_types(df: pd.DataFrame) -> None:
    """Validar tipos de datos correctos."""
    # Check 1: year es integer
    assert pd.api.types.is_integer_dtype(df['year']), \
        "Columna 'year' debe ser integer"

    # Check 2: Variables numéricas son numeric
    numeric_vars = ['wdi_gdppc', 'ti_cpi', 'vdem_polyarchy']
    for var in numeric_vars:
        if var in df.columns:
            assert pd.api.types.is_numeric_dtype(df[var]), \
                f"Columna '{var}' debe ser numeric, es {df[var].dtype}"

    # Check 3: country_code es string
    assert pd.api.types.is_string_dtype(df['country_code']) or \
           pd.api.types.is_object_dtype(df['country_code']), \
        "Columna 'country_code' debe ser string"
```

---

### Ranges

```python
def validate_variable_ranges(df: pd.DataFrame) -> None:
    """Validar que variables están en rangos válidos."""
    checks = {
        'ti_cpi': (0, 100),
        'vdem_polyarchy': (0, 1),
        'fh_pr': (1, 7),
        'fh_cl': (1, 7),
        'polity2': (-10, 10),
        'wbgi_cce': (-2.5, 2.5),
        'wdi_gini': (0, 100),
    }

    for var, (min_val, max_val) in checks.items():
        if var in df.columns:
            # Ignorar NaNs
            series = df[var].dropna()
            if len(series) > 0:
                actual_min = series.min()
                actual_max = series.max()

                assert actual_min >= min_val, \
                    f"{var}: min={actual_min} < {min_val} (inválido)"
                assert actual_max <= max_val, \
                    f"{var}: max={actual_max} > {max_val} (inválido)"
```

---

## 5. Logging Requerido

### Niveles de Logging

```python
import logging

# Setup
logger = logging.getLogger(__name__)

# En funciones críticas:

# DEBUG: Información detallada
logger.debug(f"Leyendo archivo: {filepath}")
logger.debug(f"DataFrame shape: {df.shape}")

# INFO: Progreso normal
logger.info("Descargando dataset QoG...")
logger.info(f"Dataset descargado: {len(df)} filas, {len(df.columns)} columnas")
logger.info(f"Filtrando por tema {tema}...")
logger.info(f"Conectando a PostgreSQL: {db_name}@{host}")

# WARNING: Algo inesperado pero no crítico
logger.warning(f"Columna '{col}' tiene {pct:.1%} valores nulos")
logger.warning(f"País {country} no tiene datos para {year}")

# ERROR: Error que impide completar operación
logger.error(f"No se pudo conectar a BD: {error}")
logger.error(f"Archivo no encontrado: {filepath}")

# CRITICAL: Error fatal
logger.critical("Base de datos corrupta, abortando...")
```

---

### Puntos de Logging Obligatorios

**En Extract:**
```python
logger.info(f"Iniciando descarga desde {url}")
logger.info(f"Dataset descargado: {filas} filas, {cols} columnas")
logger.info(f"Filtrando por tema {tema}, años {start}-{end}")
logger.info(f"Después del filtro: {filas} filas, {países} países")
```

**En Transform:**
```python
logger.info(f"Renombrando {n} columnas")
logger.info(f"Creando variables derivadas...")
logger.info(f"Manejando valores faltantes (estrategia: {strategy})")
logger.info(f"Filas antes: {antes}, después: {después}")
```

**En Load:**
```python
logger.info(f"Conectando a PostgreSQL: {db}@{host}")
logger.info(f"Cargando {filas} filas a tabla '{table}'...")
logger.info(f"Carga completada: {filas} filas en {tiempo:.2f}s")
```

---

## 6. Error Handling

### Try-Except Patterns

```python
# Pattern 1: Operaciones I/O
try:
    df = pd.read_csv(filepath)
except FileNotFoundError:
    logger.error(f"Archivo no encontrado: {filepath}")
    raise
except pd.errors.EmptyDataError:
    logger.error(f"Archivo vacío: {filepath}")
    raise ValueError(f"CSV vacío: {filepath}")

# Pattern 2: Conexiones BD
try:
    conn = psycopg2.connect(**params)
except psycopg2.OperationalError as e:
    logger.error(f"Error de conexión PostgreSQL: {e}")
    raise ConnectionError(
        "No se pudo conectar a PostgreSQL. "
        "Verifica que está corriendo y .env es correcto."
    )

# Pattern 3: Validaciones
try:
    validate_data_quality(df)
except AssertionError as e:
    logger.error(f"Validación falló: {e}")
    # Continuar o abortar según criticidad
    raise
```

---

## 7. Tests (Opcional pero Recomendado)

### Pytest Examples

```python
# tests/test_extract.py
import pytest
from src.etl.extract import download_qog_data

def test_download_qog_data():
    """Test que descarga funciona."""
    df = download_qog_data()

    assert len(df) > 10000, "Dataset muy pequeño"
    assert 'cname' in df.columns
    assert 'year' in df.columns
    assert df['year'].min() >= 1900

def test_filter_by_theme():
    """Test filtrado por tema."""
    from src.etl.extract import filter_by_theme

    # Crear mock data
    df = pd.DataFrame({
        'country_code': ['ESP', 'USA'] * 10,
        'year': list(range(2000, 2010)) * 2,
        'vdem_polyarchy': [0.8, 0.9] * 10
    })

    result = filter_by_theme(df, theme=1, start_year=2005)

    assert len(result) < len(df)
    assert result['year'].min() >= 2005
```

---

## Resumen de Validaciones Críticas

### Checklist

- [ ] Dataset descargado no está vacío
- [ ] Columnas obligatorias presentes (cname, year, ccodealp)
- [ ] Sin duplicados (country_code, year)
- [ ] Años en rango válido (1900-2030)
- [ ] Variables numéricas en rangos correctos
- [ ] Identificadores sin NULLs
- [ ] Conexión PostgreSQL exitosa
- [ ] Filas insertadas = filas esperadas (±10%)
- [ ] Logging en todos los pasos críticos
- [ ] Try-except en operaciones I/O
- [ ] Variables de entorno validadas

---

**Última actualización:** 2025-12-17
