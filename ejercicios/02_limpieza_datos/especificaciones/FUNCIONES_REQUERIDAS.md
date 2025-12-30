# Funciones Requeridas - Especificación de Interfaces

Este documento define las **firmas de funciones** (input/output) que tu código debe implementar.

Piensa en esto como un **contrato**: defines QUÉ hace cada función, nosotros implementamos CÓMO.

---

## Módulo: `src/etl/extract.py`

### 1. `download_qog_data()`

**Descripción:** Descarga el dataset QoG desde la web oficial.

**Firma:**
```python
def download_qog_data(
    url: str = "https://www.qogdata.pol.gu.se/data/qog_std_ts_jan23.csv",
    cache_dir: str = "data/raw",
    force_download: bool = False
) -> pd.DataFrame:
    """
    Descarga datos QoG y retorna DataFrame.

    Args:
        url: URL del dataset QoG
        cache_dir: Directorio para cachear archivo descargado
        force_download: Si True, descarga aunque exista cache

    Returns:
        DataFrame con datos crudos QoG

    Raises:
        ConnectionError: Si falla la descarga
        ValueError: Si el CSV está corrupto

    Comportamiento esperado:
        - Si existe cache y force_download=False: leer del cache
        - Logging: "Descargando desde {url}..."
        - Logging: "Dataset descargado: {filas} filas, {columnas} columnas"
    """
    pass
```

**Ejemplo de uso:**
```python
df = download_qog_data()
print(df.shape)  # (17891, 1289)
```

---

### 2. `filter_by_theme()`

**Descripción:** Filtra el dataset por tema de análisis.

**Firma:**
```python
def filter_by_theme(
    df: pd.DataFrame,
    theme: int,  # 1 o 2
    start_year: int = 1990,
    end_year: int = 2023
) -> pd.DataFrame:
    """
    Filtra datos por tema y período temporal.

    Args:
        df: DataFrame QoG completo
        theme: 1 (instituciones) o 2 (recursos naturales)
        start_year: Año inicial (inclusivo)
        end_year: Año final (inclusivo)

    Returns:
        DataFrame filtrado con columnas relevantes al tema

    Raises:
        ValueError: Si theme no es 1 o 2

    Comportamiento esperado:
        - Filtrar por año: start_year <= year <= end_year
        - Seleccionar solo columnas relevantes (ver VARIABLES_TEMA*.md)
        - Eliminar filas donde TODAS las variables temáticas son NULL
        - Logging: "Tema {theme}: {filas} observaciones, {países} países únicos"
    """
    pass
```

**Ejemplo de uso:**
```python
df_tema1 = filter_by_theme(df, theme=1, start_year=2000, end_year=2020)
```

---

### 3. `validate_data_quality()`

**Descripción:** Valida calidad del dataset filtrado.

**Firma:**
```python
def validate_data_quality(
    df: pd.DataFrame,
    max_missing_pct: float = 0.5
) -> Dict[str, Any]:
    """
    Valida calidad de datos y retorna reporte.

    Args:
        df: DataFrame a validar
        max_missing_pct: % máximo de valores nulos permitido por columna

    Returns:
        Diccionario con métricas de calidad:
        {
            'total_rows': int,
            'total_cols': int,
            'missing_by_column': dict,  # {col: pct_missing}
            'duplicates': int,
            'valid': bool,  # True si pasa validaciones
            'warnings': list  # Lista de warnings
        }

    Comportamiento esperado:
        - Contar valores nulos por columna
        - Detectar filas duplicadas (país + año)
        - Warning si alguna columna > max_missing_pct
        - Logging de todas las métricas
    """
    pass
```

**Ejemplo de uso:**
```python
report = validate_data_quality(df_tema1)
if not report['valid']:
    print("ADVERTENCIA:", report['warnings'])
```

---

## Módulo: `src/etl/transform.py`

### 4. `rename_columns()`

**Descripción:** Renombra columnas QoG a nombres legibles.

**Firma:**
```python
def rename_columns(
    df: pd.DataFrame,
    mapping: Optional[Dict[str, str]] = None
) -> pd.DataFrame:
    """
    Renombra columnas cripticas a nombres descriptivos.

    Args:
        df: DataFrame con columnas QoG
        mapping: Diccionario {nombre_viejo: nombre_nuevo}
                 Si None, usar mapping por defecto

    Returns:
        DataFrame con columnas renombradas

    Comportamiento esperado:
        - Aplicar renombrado
        - Logging: "Renombradas {n} columnas"
        - NO modificar df original (retornar copia)

    Ejemplo mapping:
        {
            'vdem_polyarchy': 'democracy_index',
            'ti_cpi': 'corruption_index',
            'wdi_gdppc': 'gdp_per_capita'
        }
    """
    pass
```

---

### 5. `create_derived_variables()`

**Descripción:** Crea variables derivadas útiles para análisis.

**Firma:**
```python
def create_derived_variables(
    df: pd.DataFrame,
    theme: int
) -> pd.DataFrame:
    """
    Crea variables derivadas según el tema.

    Args:
        df: DataFrame con datos limpios
        theme: 1 o 2

    Returns:
        DataFrame con nuevas columnas agregadas

    Variables a crear:

    TEMA 1 (Instituciones):
        - regime_type: 'Democracia', 'Híbrido', 'Autocracia' (basado en polity2)
        - gdp_decile: Deciles de PIB per cápita (1-10)
        - corruption_level: 'Alto', 'Medio', 'Bajo' (basado en ti_cpi)

    TEMA 2 (Recursos):
        - resource_dependence: 'Alta', 'Media', 'Baja' (basado en wdi_nrrent)
        - basic_services_index: Promedio de wdi_water y wdi_sanit
        - oil_gas_total: Suma de ross_oil_value + ross_gas_value

    Comportamiento esperado:
        - NO eliminar columnas originales
        - Manejar valores nulos apropiadamente
        - Logging: "Creadas {n} variables derivadas"
    """
    pass
```

**Ejemplo de uso:**
```python
df_tema1 = create_derived_variables(df_tema1, theme=1)
print(df_tema1.columns)  # Incluye 'regime_type', 'gdp_decile', etc.
```

---

### 6. `handle_missing_values()`

**Descripción:** Maneja valores faltantes con estrategia apropiada.

**Firma:**
```python
def handle_missing_values(
    df: pd.DataFrame,
    strategy: str = 'forward_fill'  # 'forward_fill', 'drop', 'interpolate'
) -> pd.DataFrame:
    """
    Maneja valores faltantes según estrategia.

    Args:
        df: DataFrame con valores nulos
        strategy: Estrategia a usar
            - 'forward_fill': Rellenar con valor anterior (dentro de país)
            - 'drop': Eliminar filas con nulos
            - 'interpolate': Interpolación lineal (dentro de país)

    Returns:
        DataFrame procesado

    Comportamiento esperado:
        - Agrupar por país antes de forward_fill o interpolate
        - NO rellenar entre países diferentes
        - Logging: "{strategy}: {filas_antes} -> {filas_después} filas"
        - Logging: "Valores nulos restantes: {n}"
    """
    pass
```

---

## Módulo: `src/etl/load.py`

### 7. `create_connection()`

**Descripción:** Crea conexión a PostgreSQL.

**Firma:**
```python
def create_connection(
    host: str = 'localhost',
    port: int = 5432,
    database: str = 'qog_research',
    user: str = None,  # Leer de .env
    password: str = None  # Leer de .env
) -> psycopg2.connection:
    """
    Crea y retorna conexión a PostgreSQL.

    Args:
        host, port, database, user, password: Credenciales de conexión

    Returns:
        Objeto conexión psycopg2

    Raises:
        psycopg2.OperationalError: Si falla conexión

    Comportamiento esperado:
        - Intentar conexión con retry (3 intentos)
        - Logging: "Conectado a PostgreSQL: {database}@{host}"
        - Logging: "Error de conexión: {error}" si falla
    """
    pass
```

---

### 8. `load_to_postgres()`

**Descripción:** Carga DataFrame a PostgreSQL.

**Firma:**
```python
def load_to_postgres(
    df: pd.DataFrame,
    table_name: str,
    conn: psycopg2.connection,
    if_exists: str = 'replace',  # 'replace', 'append', 'fail'
    batch_size: int = 1000
) -> int:
    """
    Carga datos a PostgreSQL de forma eficiente.

    Args:
        df: DataFrame a cargar
        table_name: Nombre de la tabla destino
        conn: Conexión PostgreSQL activa
        if_exists: Comportamiento si tabla existe
        batch_size: Filas por batch (para grandes volúmenes)

    Returns:
        Número de filas insertadas

    Raises:
        psycopg2.Error: Si falla inserción

    Comportamiento esperado:
        - Usar pandas.to_sql() o psycopg2 copy
        - Insertar en batches si df > 10k filas
        - Logging: "Cargando {filas} filas a tabla '{table_name}'..."
        - Logging: "Carga completada: {filas} filas en {tiempo}s"
        - Commit automático
    """
    pass
```

**Ejemplo de uso:**
```python
conn = create_connection()
rows = load_to_postgres(df_tema1, 'qog_data', conn)
print(f"Insertadas {rows} filas")
conn.close()
```

---

## Módulo: `src/analysis/panel_data.py`

### 9. `prepare_panel_data()`

**Descripción:** Prepara datos en formato panel balanceado.

**Firma:**
```python
def prepare_panel_data(
    df: pd.DataFrame,
    entity_col: str = 'country_code',
    time_col: str = 'year',
    min_periods: int = 5
) -> pd.DataFrame:
    """
    Prepara panel balanceado para regresiones.

    Args:
        df: DataFrame con estructura panel
        entity_col: Columna de entidad (país)
        time_col: Columna temporal (año)
        min_periods: Mínimo de períodos para incluir entidad

    Returns:
        DataFrame panel balanceado (solo países con >= min_periods observaciones)

    Comportamiento esperado:
        - Verificar que (entity_col, time_col) sea único
        - Eliminar países con < min_periods observaciones
        - Eliminar columnas con >50% valores nulos
        - Ordenar por entity, time
        - Logging: "Panel: {entidades} países × {períodos} años = {obs} observaciones"
    """
    pass
```

**Ejemplo de uso:**
```python
panel = prepare_panel_data(df, min_periods=10)
# Listo para usar con linearmodels, statsmodels, etc.
```

---

### 10. `export_for_stata()`

**Descripción:** Exporta datos en formato Stata (.dta).

**Firma:**
```python
def export_for_stata(
    df: pd.DataFrame,
    output_path: str,
    variable_labels: Optional[Dict[str, str]] = None
) -> None:
    """
    Exporta DataFrame a formato Stata con labels.

    Args:
        df: DataFrame a exportar
        output_path: Ruta del archivo .dta
        variable_labels: Diccionario {columna: label descriptivo}

    Returns:
        None

    Comportamiento esperado:
        - Usar pandas.DataFrame.to_stata()
        - Agregar labels de variables si se proveen
        - Verificar que tipos de datos sean compatibles
        - Logging: "Exportado a Stata: {output_path}"
    """
    pass
```

---

## Módulo: `src/utils/logger.py`

### 11. `setup_logger()`

**Descripción:** Configura sistema de logging.

**Firma:**
```python
def setup_logger(
    name: str,
    log_file: str = 'logs/pipeline.log',
    level: int = logging.INFO
) -> logging.Logger:
    """
    Configura logger con output a consola y archivo.

    Args:
        name: Nombre del logger
        log_file: Ruta del archivo de log
        level: Nivel de logging (DEBUG, INFO, WARNING, ERROR)

    Returns:
        Objeto Logger configurado

    Comportamiento esperado:
        - Crear carpeta logs/ si no existe
        - Formato: '[%(asctime)s] %(levelname)s - %(message)s'
        - Handler de consola (nivel INFO)
        - Handler de archivo (nivel DEBUG)
        - Rotación de logs (máx 10MB, 5 archivos)
    """
    pass
```

**Ejemplo de uso:**
```python
logger = setup_logger('ETL')
logger.info("Iniciando pipeline...")
logger.debug(f"DataFrame shape: {df.shape}")
```

---

## Scripts Ejecutables

### `scripts/run_etl.py`

**Descripción:** Script principal que ejecuta pipeline completo.

**Comportamiento esperado:**
```bash
$ python scripts/run_etl.py --tema 1 --year-start 2000 --year-end 2020

# Output esperado:
[2025-12-17 10:00:01] INFO - Iniciando ETL - Tema 1
[2025-12-17 10:00:02] INFO - Descargando datos QoG...
[2025-12-17 10:00:10] INFO - Dataset descargado: 17891 filas, 1289 columnas
[2025-12-17 10:00:11] INFO - Filtrando por tema 1 (años 2000-2020)...
[2025-12-17 10:00:12] INFO - Tema 1: 3245 observaciones, 156 países únicos
[2025-12-17 10:00:13] INFO - Validando calidad de datos...
[2025-12-17 10:00:14] INFO - Renombrando columnas...
[2025-12-17 10:00:15] INFO - Creando variables derivadas...
[2025-12-17 10:00:16] INFO - Conectando a PostgreSQL: qog_research@localhost
[2025-12-17 10:00:17] INFO - Cargando 3245 filas a tabla 'qog_data'...
[2025-12-17 10:00:20] INFO - Carga completada: 3245 filas en 2.8s
[2025-12-17 10:00:20] INFO - ETL completado exitosamente
```

---

## Validaciones Mínimas (Ver VALIDACIONES.md)

Estas funciones deben incluir:

1. **Type hints** en todas las firmas
2. **Docstrings** con formato Google/NumPy
3. **Logging** en puntos clave
4. **Error handling** con try-except
5. **Validación de inputs** (asserts o raises)

---

## Ejemplo Completo de Función Implementada

```python
import pandas as pd
import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)

def validate_data_quality(
    df: pd.DataFrame,
    max_missing_pct: float = 0.5
) -> Dict[str, Any]:
    """
    Valida calidad de datos y retorna reporte.

    Args:
        df: DataFrame a validar
        max_missing_pct: % máximo de valores nulos permitido por columna

    Returns:
        Diccionario con métricas de calidad

    Example:
        >>> report = validate_data_quality(df)
        >>> if not report['valid']:
        ...     print(report['warnings'])
    """
    logger.info("Iniciando validación de calidad de datos...")

    # Validar inputs
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df debe ser un pandas DataFrame")
    if not 0 <= max_missing_pct <= 1:
        raise ValueError("max_missing_pct debe estar entre 0 y 1")

    # Calcular métricas
    total_rows = len(df)
    total_cols = len(df.columns)

    missing_by_column = (df.isnull().sum() / total_rows).to_dict()

    # Detectar duplicados (país + año)
    if 'country_code' in df.columns and 'year' in df.columns:
        duplicates = df.duplicated(subset=['country_code', 'year']).sum()
    else:
        duplicates = df.duplicated().sum()

    # Generar warnings
    warnings = []
    for col, pct in missing_by_column.items():
        if pct > max_missing_pct:
            warnings.append(f"Columna '{col}': {pct:.1%} valores nulos (>{max_missing_pct:.0%})")

    if duplicates > 0:
        warnings.append(f"{duplicates} filas duplicadas detectadas")

    valid = len(warnings) == 0

    # Logging
    logger.info(f"Filas: {total_rows}, Columnas: {total_cols}")
    logger.info(f"Duplicados: {duplicates}")
    if not valid:
        logger.warning(f"{len(warnings)} warnings detectados")
        for w in warnings:
            logger.warning(f"  - {w}")
    else:
        logger.info("Validación exitosa: sin warnings")

    return {
        'total_rows': total_rows,
        'total_cols': total_cols,
        'missing_by_column': missing_by_column,
        'duplicates': duplicates,
        'valid': valid,
        'warnings': warnings
    }
```

---

**Última actualización:** 2025-12-17
