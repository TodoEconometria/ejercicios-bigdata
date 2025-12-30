# Arquitectura del Proyecto - Pipeline ETL QoG

Este documento especifica la **estructura de carpetas y archivos** que debe tener tu proyecto.

---

## Estructura Esperada

```
tu_apellido_nombre/
├── README.md                       # Documentación del proyecto
├── requirements.txt                # Dependencias Python
├── .env.example                    # Variables de entorno (ejemplo)
├── config.py                       # Configuración centralizada
│
├── src/                            # Código fuente principal
│   ├── __init__.py
│   │
│   ├── database/                   # Módulo de base de datos
│   │   ├── __init__.py
│   │   ├── connection.py           # Conexión a PostgreSQL
│   │   ├── models.py               # Definición de tablas (opcional: SQLAlchemy)
│   │   └── queries.py              # Queries SQL reutilizables
│   │
│   ├── etl/                        # Módulo ETL
│   │   ├── __init__.py
│   │   ├── extract.py              # Descarga y extracción de datos
│   │   ├── transform.py            # Limpieza y transformación
│   │   ├── load.py                 # Carga a PostgreSQL
│   │   └── validators.py           # Validaciones de integridad
│   │
│   ├── analysis/                   # Módulo de análisis
│   │   ├── __init__.py
│   │   ├── descriptive.py          # Estadísticas descriptivas
│   │   ├── panel_data.py           # Preparación para regresiones panel
│   │   └── exports.py              # Exportar resultados
│   │
│   └── utils/                      # Utilidades
│       ├── __init__.py
│       ├── logger.py               # Sistema de logging
│       └── helpers.py              # Funciones auxiliares
│
├── scripts/                        # Scripts ejecutables (CLI)
│   ├── setup_database.py           # Crear schema PostgreSQL
│   ├── run_etl.py                  # Ejecutar pipeline completo
│   ├── update_data.py              # Actualización incremental
│   └── generate_report.py          # Generar reporte de análisis
│
├── sql/                            # Scripts SQL
│   ├── schema.sql                  # DDL - Creación de tablas
│   ├── views.sql                   # Vistas analíticas
│   └── queries/                    # Consultas SQL complejas
│       ├── tema1_analisis.sql
│       └── tema2_analisis.sql
│
├── tests/                          # Tests (opcional pero recomendado)
│   ├── __init__.py
│   ├── test_extract.py
│   ├── test_transform.py
│   └── test_load.py
│
├── data/                           # Datos (NO subir a Git)
│   ├── raw/                        # Datos crudos descargados
│   ├── processed/                  # Datos procesados
│   └── cache/                      # Cache temporal
│
├── logs/                           # Logs de ejecución (NO subir a Git)
│   └── pipeline.log
│
└── output/                         # Resultados (NO subir a Git)
    ├── reports/
    └── exports/
```

---

## Explicación de Módulos

### 1. `src/database/`

**Responsabilidad:** Gestión de conexiones y esquema de base de datos.

**Archivos:**
- `connection.py` - Maneja conexión a PostgreSQL (connection pooling)
- `models.py` - Define estructura de tablas (ORM o diccionarios)
- `queries.py` - Queries SQL reutilizables como funciones

### 2. `src/etl/`

**Responsabilidad:** Pipeline de Extract-Transform-Load.

**Archivos:**
- `extract.py` - Descarga datos de QoG, cacheo local
- `transform.py` - Limpieza, renombrado, creación de variables
- `load.py` - Inserción eficiente en PostgreSQL
- `validators.py` - Validaciones de calidad de datos

### 3. `src/analysis/`

**Responsabilidad:** Análisis de datos cargados.

**Archivos:**
- `descriptive.py` - Estadísticas por país, región, año
- `panel_data.py` - Preparar datos para modelos econométricos
- `exports.py` - Exportar a CSV, Excel, Stata (.dta)

### 4. `src/utils/`

**Responsabilidad:** Funciones auxiliares transversales.

**Archivos:**
- `logger.py` - Configurar logging (consola + archivo)
- `helpers.py` - Funciones genéricas (fechas, validaciones, etc.)

### 5. `scripts/`

**Responsabilidad:** Puntos de entrada ejecutables.

**Ejemplo de uso:**
```bash
python scripts/setup_database.py      # Crear tablas
python scripts/run_etl.py --tema 1    # ETL tema 1
python scripts/generate_report.py     # Generar reporte
```

### 6. `sql/`

**Responsabilidad:** SQL complejo separado del código Python.

**Ventaja:** Queries complejas son más legibles en archivos .sql

---

## Buenas Prácticas

### Modularidad
✅ Cada archivo tiene UNA responsabilidad clara
✅ Funciones pequeñas y reutilizables
✅ NO mezclar lógica de negocio con acceso a datos

### Configuración
✅ Variables de entorno en `.env` (NO commitear)
✅ Configuración centralizada en `config.py`
✅ Paths relativos, NO absolutos

### Logging
✅ Logging en todos los pasos críticos
✅ Niveles: DEBUG, INFO, WARNING, ERROR
✅ Logs a archivo + consola

### Error Handling
✅ Try-except en operaciones I/O
✅ Mensajes de error descriptivos
✅ NO fallar silenciosamente

### Git
✅ `.gitignore` para data/, logs/, output/
✅ Commits pequeños y descriptivos
✅ NO subir credenciales ni datos crudos

---

## Ejemplo de Flujo de Ejecución

```bash
# 1. Configurar entorno
cp .env.example .env
# Editar .env con tus credenciales PostgreSQL

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Crear base de datos
python scripts/setup_database.py

# 4. Ejecutar ETL completo
python scripts/run_etl.py --tema 1

# 5. Generar análisis
python scripts/generate_report.py --tema 1 --output reports/tema1.csv
```

---

## Notas Importantes

### ¿Por qué esta estructura?

**Separación de responsabilidades:**
- ETL ≠ Análisis ≠ Base de datos
- Cada módulo puede evolucionar independientemente

**Escalabilidad:**
- Fácil agregar nuevos temas (nuevo archivo en `analysis/`)
- Fácil cambiar de BD (solo modificar `database/`)

**Mantenibilidad:**
- Código organizado es fácil de debuggear
- Nuevos colaboradores entienden rápidamente

**Profesionalismo:**
- Esta estructura es estándar en la industria
- Preparado para producción (Airflow, Docker, etc.)

---

## Preparación para Docker (Futuro)

Esta arquitectura está diseñada para ser **dockerizada** fácilmente:

```
Futuro:
├── Dockerfile                  # Imagen Python
├── docker-compose.yml          # PostgreSQL + aplicación
└── .dockerignore
```

Tu código NO necesitará cambios, solo agregar archivos Docker.

---

## ¿Tengo que seguir EXACTAMENTE esta estructura?

**Mínimo requerido:**
- Separación ETL (extract, transform, load)
- Conexión a PostgreSQL modular
- Scripts ejecutables independientes
- README con instrucciones de uso

**Opcional pero valorado:**
- Tests
- Logging robusto
- Análisis modular
- SQL en archivos separados

**Criterio de evaluación:**
- ¿El código es fácil de entender?
- ¿Las responsabilidades están separadas?
- ¿Se puede ejecutar sin modificar rutas?
- ¿Está documentado?

---

**Última actualización:** 2025-12-17
