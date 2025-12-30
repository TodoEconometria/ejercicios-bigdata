# Ejercicio 02: Pipeline ETL Profesional - Quality of Government

> **Nivel:** Avanzado
> **Duración estimada:** 15-20 horas
> **Modalidad:** Grupal (2 grupos) o Individual

---

## 🎯 Objetivos de Aprendizaje

Al completar este ejercicio serás capaz de:

- ✅ Diseñar e implementar un pipeline ETL profesional
- ✅ Trabajar con PostgreSQL para análisis de datos longitudinales
- ✅ Limpiar y transformar datasets complejos (1000+ variables)
- ✅ Preparar datos en formato panel para análisis econométrico
- ✅ Aplicar buenas prácticas de ingeniería de software
- ✅ Escribir código modular, testeable y documentado
- ✅ Trabajar con datos reales de investigación académica

---

## 📊 Dataset: Quality of Government (QoG)

**¿Qué es QoG?**

El Quality of Government Standard Dataset es una base de datos longitudinal mantenida por la Universidad de Gotemburgo que agrega más de **1000 variables** de múltiples fuentes sobre calidad institucional, democracia, desarrollo económico y social.

**Características:**
- **Cobertura temporal:** 1946-2023 (según variable)
- **Cobertura geográfica:** 194+ países
- **Variables:** 1289 en la última versión
- **Fuentes:** World Bank, V-Dem, Transparency International, Freedom House, UNDP, etc.

**Usos:**
- Investigación académica en ciencia política y economía
- Análisis comparativo de países
- Estudios de desarrollo institucional
- Regresiones de datos de panel

**Descargar:** https://www.qogdata.pol.gu.se/data/qog_std_ts_jan23.csv

---

## 🎭 Temas de Análisis

Debes elegir **UNO** de los siguientes temas:

### Tema 1: Evolución Institucional Post-Autoritaria

**Pregunta de investigación:**
¿Cómo evoluciona la calidad institucional en países que transitan desde regímenes autoritarios?

**Aspectos a analizar:**
- Trayectorias de democratización
- Relación entre desarrollo económico y calidad democrática
- Factores que explican éxitos o fracasos en transiciones
- Análisis comparativo por regiones

**Variables clave:**
- Índices de democracia (V-Dem, Polity, Freedom House)
- Calidad institucional (Transparency International, World Bank Governance)
- Desarrollo económico (PIB, HDI, Gini)

**Ver:** `especificaciones/VARIABLES_TEMA1.md`

---

### Tema 2: Recursos Naturales y Desarrollo Regional

**Pregunta de investigación:**
¿La dependencia de recursos naturales afecta el desarrollo económico e institucional?

**Aspectos a analizar:**
- "Maldición de los recursos" (resource curse)
- Relación entre hidrocarburos y corrupción
- Acceso a servicios básicos (agua, saneamiento)
- Dependencia agrícola y desarrollo

**Variables clave:**
- Producción de petróleo/gas (Ross dataset)
- Rentas de recursos naturales (World Bank)
- Acceso a agua y saneamiento
- Calidad institucional

**Ver:** `especificaciones/VARIABLES_TEMA2.md`

---

## 🏗️ Arquitectura del Proyecto

Este ejercicio requiere una arquitectura **modular y profesional**.

**Estructura esperada:**
```
tu_apellido_nombre/
├── README.md
├── requirements.txt
├── config.py
├── src/
│   ├── database/          # Conexión PostgreSQL
│   ├── etl/               # Extract, Transform, Load
│   ├── analysis/          # Análisis de datos
│   └── utils/             # Utilidades (logging, etc.)
├── scripts/               # Scripts ejecutables
├── sql/                   # Queries SQL
├── tests/                 # Tests (opcional)
└── docs/                  # Documentación
```

**Ver detalles completos:** `especificaciones/ARQUITECTURA.md`

---

## 🔧 Tecnologías Requeridas

### Obligatorias

- **Python 3.11+**
- **PostgreSQL 14+** (instalación local)
- **pandas** - Manipulación de datos
- **psycopg2** - Conexión PostgreSQL
- **python-dotenv** - Variables de entorno

### Opcionales pero Recomendadas

- **SQLAlchemy** - ORM para PostgreSQL
- **pytest** - Testing
- **logging** - Sistema de logs
- **click** - CLIs elegantes

---

## 📋 Tareas a Realizar

### Fase 0: Setup

1. Instalar PostgreSQL (ver `docs/POSTGRESQL_SETUP.md`)
2. Crear base de datos `qog_research`
3. Ejecutar `especificaciones/ESQUEMA_DB.sql`
4. Configurar variables de entorno (`.env`)

### Fase 1: Extract (ETL - E)

**Módulo:** `src/etl/extract.py`

**Tareas:**
- Descargar dataset QoG desde URL oficial
- Implementar caché local (no descargar cada vez)
- Filtrar por tema elegido (1 o 2)
- Filtrar por período temporal (ej: 1990-2023)
- Validar integridad del dataset

**Funciones a implementar:**
- `download_qog_data()`
- `filter_by_theme()`
- `validate_data_quality()`

**Ver:** `especificaciones/FUNCIONES_REQUERIDAS.md`

---

### Fase 2: Transform (ETL - T)

**Módulo:** `src/etl/transform.py`

**Tareas:**
- Renombrar columnas crípticas a nombres legibles
- Crear variables derivadas (deciles, categorías, índices)
- Manejar valores faltantes estratégicamente
- Detectar y corregir outliers (si aplica)
- Normalizar formatos de datos

**Funciones a implementar:**
- `rename_columns()`
- `create_derived_variables()`
- `handle_missing_values()`

**Consideraciones:**
- NO eliminar países sin recursos (son grupo de control)
- Valores faltantes: forward-fill **dentro de país** (no entre países)
- Logging detallado de cada transformación

---

### Fase 3: Load (ETL - L)

**Módulo:** `src/etl/load.py`

**Tareas:**
- Conectar a PostgreSQL con manejo de errores
- Cargar datos a tabla `qog_data` eficientemente
- Cargar catálogo de países a tabla `countries`
- Insertar metadata de variables
- Verificar integridad referencial

**Funciones a implementar:**
- `create_connection()`
- `load_to_postgres()`

**Optimizaciones:**
- Usar batches para inserciones grandes
- Transactions para atomicidad
- Logging de progreso

---

### Fase 4: Analysis

**Módulo:** `src/analysis/panel_data.py`

**Tareas:**
- Preparar panel balanceado (países con datos completos)
- Calcular estadísticas descriptivas por región/año
- Exportar datos limpios para análisis:
  - CSV para Python/R
  - .dta para Stata
  - Parquet para Big Data
- Generar reporte de calidad de datos

**Funciones a implementar:**
- `prepare_panel_data()`
- `export_for_stata()`
- `generate_summary_stats()`

---

### Fase 5: Scripts Ejecutables

**Scripts en:** `scripts/`

**Requeridos:**

1. **`setup_database.py`**
   - Crear schema PostgreSQL
   - Verificar conexión
   - Inicializar tablas

2. **`run_etl.py`**
   - Pipeline completo: Extract → Transform → Load
   - Argumentos: `--tema 1`, `--year-start 2000`, `--year-end 2020`
   - Logging completo de progreso

3. **`generate_report.py`**
   - Generar reporte de análisis
   - Estadísticas descriptivas
   - Export a CSV/Excel

**Ejemplo de uso:**
```bash
python scripts/setup_database.py
python scripts/run_etl.py --tema 1 --year-start 1990
python scripts/generate_report.py --tema 1 --output reports/
```

---

### Fase 6: SQL Avanzado

**Ubicación:** `sql/`

**Tareas:**
- Escribir queries complejas en archivos .sql
- Usar las vistas creadas en el esquema
- Análisis con CTEs, window functions, agregaciones

**Ejemplos de queries:**

**Para Tema 1:**
```sql
-- Evolución de democracia por región
-- Comparativa: países que democratizaron vs que no
-- Relación PIB y calidad institucional
```

**Para Tema 2:**
```sql
-- Top 10 países dependientes de recursos
-- Correlación recursos-corrupción
-- Evolución acceso a agua por región
```

---

## 📚 Especificaciones Técnicas

**Lee TODOS estos documentos antes de empezar:**

1. **`especificaciones/ARQUITECTURA.md`**
   - Estructura de carpetas esperada
   - Separación de responsabilidades
   - Buenas prácticas

2. **`especificaciones/ESQUEMA_DB.sql`**
   - Schema PostgreSQL completo
   - Tablas, vistas, funciones
   - Comentarios explicativos

3. **`especificaciones/FUNCIONES_REQUERIDAS.md`**
   - Firmas de funciones (input/output)
   - Comportamiento esperado
   - Ejemplos de uso

4. **`especificaciones/VARIABLES_TEMA*.md`**
   - Variables sugeridas por tema
   - Prompts para investigar más
   - Recursos bibliográficos

5. **`especificaciones/VALIDACIONES.md`**
   - Checks de calidad obligatorios
   - Asserts y excepciones
   - Logging requerido

---

## 🎓 Datos de Panel - Información Importante

Este ejercicio te prepara para **análisis econométrico con datos de panel**.

**¿Qué es panel data?**

```
Panel = Cross-section (países) × Time-series (años)

| country | year | var1 | var2 |
|---------|------|------|------|
| ESP     | 2000 | 100  | 50   |
| ESP     | 2001 | 102  | 51   |
| USA     | 2000 | 200  | 80   |
| USA     | 2001 | 205  | 82   |
```

**¿Para qué sirve?**
- Controlar heterogeneidad no observada (Fixed Effects)
- Estudiar efectos causales (Difference-in-Differences)
- Mayor poder estadístico
- Modelar dinámicas temporales

**Tu pipeline debe:**
- Asegurar (país, año) sea único
- Mantener datos balanceados (mismos años para todos)
- Facilitar export a Stata/R para regresiones

---

## ✅ Criterios de Evaluación

### Funcionalidad (40%)
- Pipeline ejecuta sin errores
- Datos se cargan correctamente a PostgreSQL
- Resultados son correctos
- Scripts CLI funcionan

### Arquitectura (25%)
- Separación de responsabilidades (ETL, DB, análisis)
- Código modular y reutilizable
- Manejo de errores robusto
- Configuración externalizada

### Calidad de Código (20%)
- PEP 8 / Black formatting
- Type hints en funciones
- Docstrings completos
- Nombres descriptivos

### Documentación (10%)
- README claro
- Comentarios donde necesario
- Instrucciones de uso
- Explicación de decisiones

### Innovación (5%)
- Tests automatizados
- Visualizaciones
- Análisis adicionales
- Optimizaciones

---

## 📦 Entregables

**Carpeta de entrega:** `entregas/02_limpieza_datos/tu_apellido_nombre/`

**Estructura mínima:**
```
apellido_nombre/
├── README.md                    # Documentación proyecto
├── requirements.txt             # Dependencias
├── .env.example                 # Variables entorno (ejemplo)
├── src/                         # Código fuente
├── scripts/                     # Scripts ejecutables
├── sql/                         # Queries SQL
├── docs/                        # Documentación adicional
└── METODOLOGIA.md               # Decisiones de diseño
```

**NO incluir:**
- Datos crudos (data/raw/)
- Archivos .db o dumps PostgreSQL
- Logs (logs/)
- Virtual environments (venv/, .venv/)
- __pycache__/

---

## 🚀 Cómo Empezar

### 1. Lee TODA la documentación
No empieces a codear antes de entender el alcance completo.

### 2. Setup del entorno
```bash
# Crear carpeta
mkdir apellido_nombre
cd apellido_nombre

# Virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instalar PostgreSQL (ver docs/POSTGRESQL_SETUP.md)

# Crear base de datos
psql -U postgres
CREATE DATABASE qog_research;
\c qog_research
-- Ejecutar especificaciones/ESQUEMA_DB.sql
```

### 3. Investigar variables
- Lee el codebook QoG
- Usa los prompts en VARIABLES_TEMA*.md
- Selecciona variables para tu tema

### 4. Implementar paso a paso
- Empieza por Extract
- Luego Transform
- Luego Load
- Finalmente Analysis

### 5. Testear frecuentemente
No esperes a tener todo para probar.

---

## 🆘 Recursos de Apoyo

### Dataset QoG
- **Website:** https://www.qog.pol.gu.se/
- **Codebook:** https://www.qogdata.pol.gu.se/data/codebook_std_jan23.pdf
- **Download:** https://www.qogdata.pol.gu.se/data/qog_std_ts_jan23.csv

### PostgreSQL
- **Documentación:** https://www.postgresql.org/docs/
- **Tutorial:** https://www.postgresqltutorial.com/

### Python Libraries
- **pandas:** https://pandas.pydata.org/docs/
- **psycopg2:** https://www.psycopg.org/docs/
- **SQLAlchemy:** https://docs.sqlalchemy.org/

### Panel Data
- **linearmodels:** https://bashtage.github.io/linearmodels/
- **Stata export:** pandas.DataFrame.to_stata()

---

## ❓ Preguntas Frecuentes

**P: ¿Tengo que usar TODAS las variables sugeridas?**
R: No. Son SUGERENCIAS. Investiga y elige las más relevantes para tu análisis.

**P: ¿Puedo cambiar de tema a mitad del proyecto?**
R: Sí, pero perderás tiempo. Elige bien desde el inicio.

**P: ¿El proyecto es individual o grupal?**
R: Puedes elegir. Grupos de 4-5 o individual.

**P: ¿Cuántas filas/países debo analizar?**
R: Mínimo 50 países, 20 años (1000+ observaciones).

**P: ¿Tengo que implementar TODO lo que está en FUNCIONES_REQUERIDAS.md?**
R: Las funciones básicas sí. Las avanzadas son opcionales.

**P: ¿Puedo usar Docker?**
R: Para este ejercicio NO. PostgreSQL local. Docker será en ejercicios futuros.

**P: ¿Qué hago si no encuentro una variable en QoG?**
R: Usa los prompts en VARIABLES_TEMA*.md para buscar alternativas.

---

## 🎯 Consejos Finales

1. **Empieza simple:** Pipeline básico primero, optimizaciones después
2. **Logging es tu amigo:** Log todo, te salvará en debugging
3. **Git desde día 1:** Commits frecuentes y descriptivos
4. **Documenta mientras codeas:** README no es lo último
5. **Pregunta temprano:** Si algo no está claro, pregunta
6. **Lee el codebook QoG:** Es tu biblia para este ejercicio
7. **Testea con datos pequeños:** No cargues 1M de filas de golpe

---

## 🔮 Preparación para Docker (Futuro)

Este proyecto está diseñado para ser **dockerizado** en ejercicios futuros.

Tu arquitectura modular facilitará:
- Contenedor PostgreSQL
- Contenedor aplicación Python
- docker-compose para orquestar

**Por ahora:** PostgreSQL local es suficiente.

---

**¡Buena suerte!** 🚀

Este ejercicio es desafiante pero te dará habilidades de nivel profesional.

---

**Creado:** 2025-12-17
**Última actualización:** 2025-12-17
