# Grupo 01 - Pipeline ETL QoG

## 👥 Integrantes del Grupo

**IMPORTANTE:** Completar con los nombres de todos los integrantes:

| Nombre Completo | GitHub Username | Email | Rol Principal |
|-----------------|-----------------|-------|---------------|
| _Ejemplo: García López, María_ | _@mariagl_ | _maria.garcia@email.com_ | _Coordinadora / ETL_ |
| | | | |
| | | | |
| | | | |
| | | | |

---

## 📋 Tema Seleccionado

**Marcar el tema elegido:**

- [ ] **Tema 1:** Evolución Institucional Post-Autoritaria
- [ ] **Tema 2:** Recursos Naturales y Desarrollo

**Pregunta de investigación específica:**
```
[Escribir aquí la pregunta específica que van a responder]
Ejemplo: ¿Cómo evolucionó la calidad institucional en países de Europa del Este
         tras la caída del comunismo (1990-2020)?
```

---

## 🎯 División de Responsabilidades

### Fase Extract
**Responsable(s):**
- [ ] Implementar `download_qog_data()`
- [ ] Implementar `filter_by_theme()`
- [ ] Validaciones de descarga

### Fase Transform
**Responsable(s):**
- [ ] Renombrar columnas
- [ ] Crear variables derivadas
- [ ] Manejo de valores faltantes

### Fase Load
**Responsable(s):**
- [ ] Conexión PostgreSQL
- [ ] Carga de datos
- [ ] Optimización (índices, batch)

### Análisis
**Responsable(s):**
- [ ] Estadísticas descriptivas
- [ ] Panel balanceado
- [ ] Queries SQL avanzadas

### Documentación
**Responsable(s):**
- [ ] README principal
- [ ] METODOLOGIA.md
- [ ] Docstrings y comentarios

### Testing
**Responsable(s):**
- [ ] Tests unitarios (opcional)
- [ ] Validaciones end-to-end

---

## 📁 Estructura del Proyecto

```
grupo_01/
├── README.md                    # Este archivo
├── requirements.txt
├── .env.example
├── .gitignore
│
├── src/
│   ├── __init__.py
│   ├── database/
│   │   ├── __init__.py
│   │   ├── connection.py       # get_connection()
│   │   └── models.py           # (opcional) SQLAlchemy models
│   ├── etl/
│   │   ├── __init__.py
│   │   ├── extract.py          # download_qog_data(), filter_by_theme()
│   │   ├── transform.py        # clean_data(), create_derived_vars()
│   │   └── load.py             # load_to_postgres()
│   ├── analysis/
│   │   ├── __init__.py
│   │   ├── descriptive.py      # estadísticas descriptivas
│   │   └── panel.py            # preparar panel balanceado
│   └── utils/
│       ├── __init__.py
│       ├── logger.py           # setup_logger()
│       └── config.py           # cargar .env
│
├── scripts/
│   ├── run_etl.py              # Script principal ETL
│   ├── run_analysis.py         # Script análisis
│   └── setup_database.py       # Crear schema PostgreSQL
│
├── sql/
│   ├── schema.sql              # CREATE TABLES
│   ├── indices.sql             # CREATE INDEX
│   └── queries/
│       ├── descriptive_stats.sql
│       └── panel_data.sql
│
├── tests/                      # (Opcional pero recomendado)
│   ├── __init__.py
│   ├── test_extract.py
│   ├── test_transform.py
│   └── test_load.py
│
└── docs/
    ├── METODOLOGIA.md          # Decisiones de diseño
    ├── ANALISIS.md             # Resultados del análisis
    └── capturas/
        └── (screenshots si aplica)
```

---

## 🔄 Workflow de Git para Trabajo Grupal

### Configuración Inicial

**1. Un miembro (coordinador) crea la estructura base:**
```bash
cd entregas/02_limpieza_datos/grupo_01/

# Crear estructura de carpetas
mkdir -p src/database src/etl src/analysis src/utils
mkdir -p scripts sql/queries tests docs/capturas

# Crear archivos iniciales
touch requirements.txt .env.example .gitignore
touch src/__init__.py src/database/__init__.py src/etl/__init__.py
touch src/analysis/__init__.py src/utils/__init__.py

# Commit inicial
git add .
git commit -m "GRUPO-01: Estructura inicial del proyecto"
git push origin main
```

**2. Otros miembros sincronizan:**
```bash
git pull origin main
```

### Trabajo Colaborativo

**Cada miembro trabaja en su área:**

```bash
# 1. Antes de empezar, siempre sincronizar
git pull origin main

# 2. Crear rama para tu tarea
git checkout -b grupo01-extract-maria
# o
git checkout -b grupo01-transform-juan

# 3. Trabajar en tus archivos
# ... editar código ...

# 4. Commit con formato grupal
git add src/etl/extract.py
git commit -m "GRUPO-01: Implementar extract.py (María García)

- Función download_qog_data() completa
- Función filter_by_theme() con validaciones
- Tests básicos incluidos"

# 5. Push a tu rama
git push origin grupo01-extract-maria

# 6. Crear Pull Request en GitHub
# Otro miembro revisa y hace merge a main
```

### Formato de Commits Grupales

**Estructura:**
```
GRUPO-01: [Componente] Descripción breve (Autor)

- Detalle 1
- Detalle 2
- Detalle 3
```

**Ejemplos:**
```
GRUPO-01: Implementar fase Extract (María García)
GRUPO-01: Crear schema PostgreSQL (Juan López)
GRUPO-01: Añadir validaciones Transform (Carlos Ruiz)
GRUPO-01: Documentar metodología (Ana Torres)
```

### Resolución de Conflictos

Si dos personas editan el mismo archivo:

```bash
# 1. Sincronizar con main
git checkout main
git pull origin main

# 2. Fusionar tu rama
git checkout tu-rama
git merge main

# 3. Resolver conflictos manualmente
# Editar archivos marcados con <<<<<<< HEAD

# 4. Commit de resolución
git add .
git commit -m "GRUPO-01: Resolver conflictos merge (Tu Nombre)"
git push origin tu-rama
```

---

## ✅ Checklist de Entrega

### Código
- [ ] Todas las funciones implementadas según `FUNCIONES_REQUERIDAS.md`
- [ ] Validaciones según `VALIDACIONES.md`
- [ ] Logging en todos los pasos críticos
- [ ] Type hints y docstrings completos
- [ ] Código sigue PEP 8

### Base de Datos
- [ ] Schema PostgreSQL implementado
- [ ] Datos cargados correctamente
- [ ] Índices optimizados
- [ ] Panel data balanceado generado

### Documentación
- [ ] README.md completo con instrucciones de uso
- [ ] METODOLOGIA.md con decisiones de diseño
- [ ] Integrantes del grupo listados
- [ ] requirements.txt actualizado
- [ ] .env.example con variables necesarias

### Tests y Validación
- [ ] Pipeline ejecuta sin errores de principio a fin
- [ ] Todas las validaciones pasan
- [ ] Datos en PostgreSQL verificados

---

## 🚀 Cómo Ejecutar el Proyecto

### 1. Instalar Dependencias

```bash
cd entregas/02_limpieza_datos/grupo_01/

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

### 2. Configurar Variables de Entorno

```bash
# Copiar ejemplo
cp .env.example .env

# Editar con tus credenciales PostgreSQL
nano .env  # o tu editor favorito
```

### 3. Setup Base de Datos

```bash
# Crear schema en PostgreSQL
python scripts/setup_database.py
```

### 4. Ejecutar Pipeline ETL

```bash
# Pipeline completo
python scripts/run_etl.py --tema 1 --year-start 1990 --year-end 2020

# O paso a paso:
python scripts/run_etl.py --only-extract
python scripts/run_etl.py --only-transform
python scripts/run_etl.py --only-load
```

### 5. Ejecutar Análisis

```bash
python scripts/run_analysis.py
```

---

## 📞 Comunicación del Grupo

**Canal de comunicación:** [WhatsApp / Slack / Discord / Email]

**Reuniones:**
- **Día/Hora:**
- **Plataforma:** [Zoom / Google Meet / Discord]

**Reglas de trabajo:**
1. Avisar en el grupo antes de hacer push a `main`
2. Siempre hacer `git pull` antes de empezar a trabajar
3. Usar Pull Requests para cambios importantes
4. Comentar código complejo
5. Actualizar README si cambias funcionalidad

---

## 📊 Progreso del Proyecto

| Fase | Estado | Responsable | Fecha Inicio | Fecha Fin |
|------|--------|-------------|--------------|-----------|
| Extract | ⬜ Pendiente | | | |
| Transform | ⬜ Pendiente | | | |
| Load | ⬜ Pendiente | | | |
| Analysis | ⬜ Pendiente | | | |
| Documentación | ⬜ Pendiente | | | |
| Tests | ⬜ Pendiente | | | |

**Leyenda:** ⬜ Pendiente | 🟡 En Progreso | ✅ Completado

---

## 🐛 Problemas Conocidos

_Documentar aquí cualquier bug o limitación conocida:_

1.
2.
3.

---

## 📝 Notas del Grupo

_Espacio libre para notas, decisiones importantes, etc.:_

---

**Última actualización:** [Fecha]
**Versión:** 1.0
