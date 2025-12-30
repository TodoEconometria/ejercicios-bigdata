# Instrucciones de Entrega - Ejercicio 02

**Ejercicio:** 02 - Pipeline ETL Quality of Government
**Modalidad:** Grupal (2 grupos de 4-5) o Individual
**Fecha límite:** Por definir

---

## 📁 Estructura de Entrega

Crea tu carpeta en: `entregas/02_limpieza_datos/apellido_nombre/`

**Formato del nombre:**
- **Individual:** `apellido_nombre/` (ej: `garcia_maria/`)
- **Grupal:** `apellido1_apellido2_apellido3/` (ej: `garcia_lopez_martinez/`)

---

## 📦 Archivos Requeridos

### Mínimo Obligatorio

```
apellido_nombre/
├── README.md                    # Documentación del proyecto
├── requirements.txt             # Dependencias Python
├── .env.example                 # Plantilla variables entorno
│
├── src/                         # Código fuente
│   ├── __init__.py
│   ├── database/
│   │   ├── __init__.py
│   │   └── connection.py        # MÍNIMO
│   ├── etl/
│   │   ├── __init__.py
│   │   ├── extract.py           # OBLIGATORIO
│   │   ├── transform.py         # OBLIGATORIO
│   │   └── load.py              # OBLIGATORIO
│   └── utils/
│       ├── __init__.py
│       └── logger.py            # Recomendado
│
├── scripts/
│   ├── setup_database.py        # OBLIGATORIO
│   └── run_etl.py               # OBLIGATORIO
│
├── sql/
│   ├── schema.sql               # Ya proporcionado (copia del esquema)
│   └── queries/                 # Tus queries de análisis
│       └── analisis_tema.sql
│
└── docs/
    └── METODOLOGIA.md           # OBLIGATORIO
```

---

## 📄 Contenido de Archivos Clave

### README.md

Debe incluir:

```markdown
# Proyecto: [Título del Tema Elegido]

## Integrantes
- Apellido1 Nombre1
- Apellido2 Nombre2
...

## Tema Elegido
[Tema 1 o Tema 2]

## Descripción
[Breve descripción del análisis]

## Instalación

### Requisitos
- Python 3.11+
- PostgreSQL 14+

### Setup
\`\`\`bash
# 1. Crear virtual environment
python -m venv venv
source venv/bin/activate

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Configurar PostgreSQL
cp .env.example .env
# Editar .env con tus credenciales

# 4. Crear base de datos
python scripts/setup_database.py

# 5. Ejecutar ETL
python scripts/run_etl.py --tema 1
\`\`\`

## Uso

[Instrucciones de uso de tus scripts]

## Estructura del Proyecto

[Explicar organización de carpetas]

## Variables Seleccionadas

[Lista de variables QoG que usaste y por qué]

## Decisiones de Diseño

[Explicar decisiones técnicas importantes]

## Resultados

[Hallazgos principales del análisis]
```

---

### requirements.txt

Mínimo:
```
pandas>=2.0.0
psycopg2-binary>=2.9.0
python-dotenv>=1.0.0
```

Recomendado adicional:
```
sqlalchemy>=2.0.0
pytest>=7.0.0
black>=23.0.0
```

---

### .env.example

```bash
# PostgreSQL Configuration
DB_HOST=localhost
DB_PORT=5432
DB_NAME=qog_research
DB_USER=tu_usuario
DB_PASSWORD=tu_password

# QoG Dataset
QOG_URL=https://www.qogdata.pol.gu.se/data/qog_std_ts_jan23.csv
CACHE_DIR=data/raw

# Analysis Config
TEMA=1
YEAR_START=1990
YEAR_END=2023
```

---

### METODOLOGIA.md

Documenta tus decisiones:

```markdown
# Metodología y Decisiones de Diseño

## Tema Elegido
[Tema 1 o 2 y justificación]

## Variables Seleccionadas

### Variables Dependientes
[Lista con justificación]

### Variables Independientes
[Lista con justificación]

### Variables de Control
[Lista con justificación]

## Decisiones de Limpieza

### Valores Faltantes
[Estrategia usada y por qué]

### Outliers
[Cómo los manejaste]

### Transformaciones
[Qué variables derivadas creaste]

## Decisiones Técnicas

### Arquitectura
[Por qué esta estructura]

### PostgreSQL
[Por qué usar BD relacional vs CSV]

### Performance
[Optimizaciones aplicadas]

## Limitaciones

[Qué limitaciones tiene tu análisis]

## Trabajo Futuro

[Qué mejorarías con más tiempo]
```

---

## 🚫 NO Incluir

**Archivos prohibidos en Git:**

```gitignore
# Datos
data/
*.csv
*.dta
*.parquet

# Bases de datos
*.db
*.sqlite
*.sql.gz

# Logs
logs/
*.log

# Entornos virtuales
venv/
.venv/
env/

# Cache Python
__pycache__/
*.pyc
*.pyo

# Configuración local
.env

# IDEs
.vscode/
.idea/
*.swp

# OS
.DS_Store
Thumbs.db
```

**Crea archivo `.gitignore` con esto.**

---

## ✅ Checklist Pre-Entrega

### Código

- [ ] Todo el código ejecuta sin errores
- [ ] Scripts tienen argumentos CLI documentados
- [ ] Funciones tienen type hints
- [ ] Docstrings en todas las funciones principales
- [ ] Código formateado (Black o autopep8)
- [ ] NO hay credenciales hardcodeadas

### Documentación

- [ ] README.md completo y claro
- [ ] METODOLOGIA.md con decisiones justificadas
- [ ] requirements.txt con versiones específicas
- [ ] .env.example con todas las variables
- [ ] Comentarios en código complejo

### PostgreSQL

- [ ] schema.sql incluido
- [ ] Scripts de setup funcionan
- [ ] Queries SQL están documentadas
- [ ] Vistas y funciones utilizadas

### Datos

- [ ] Pipeline carga >1000 observaciones
- [ ] Mínimo 50 países
- [ ] Período mínimo 20 años
- [ ] Panel balanceado (sin muchos NULLs)

### Git

- [ ] .gitignore configurado
- [ ] NO hay datos en commits
- [ ] Commits descriptivos
- [ ] Sin archivos binarios grandes

---

## 🔍 Cómo se Evaluará

### 1. Funcionalidad (40%)

**Verificaremos:**
```bash
# Clonar tu entrega
cd entregas/02_limpieza_datos/tu_apellido/

# Crear entorno
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Setup DB
python scripts/setup_database.py
# ¿Funciona sin errores?

# Ejecutar ETL
python scripts/run_etl.py --tema 1
# ¿Se cargan datos correctamente?

# Verificar PostgreSQL
psql -d qog_research -c "SELECT COUNT(*) FROM qog_data;"
# ¿Hay datos?
```

**Puntos:**
- Pipeline ejecuta sin errores: 20 pts
- Datos cargados correctamente: 10 pts
- Resultados son correctos: 10 pts

---

### 2. Arquitectura y Código (25%)

**Evaluamos:**
- Separación de responsabilidades (ETL separado)
- Modularidad (funciones reutilizables)
- Manejo de errores (try-except apropiados)
- Logging (información útil)
- Configuración externa (.env)

**Puntos:**
- Arquitectura modular: 10 pts
- Código limpio y legible: 8 pts
- Manejo de errores: 7 pts

---

### 3. SQL y Base de Datos (20%)

**Evaluamos:**
- Uso correcto del esquema proporcionado
- Queries SQL complejas (CTEs, window functions)
- Uso de vistas
- Integridad referencial
- Optimización (índices)

**Puntos:**
- Schema correctamente usado: 8 pts
- Queries SQL avanzadas: 7 pts
- Vistas y funciones: 5 pts

---

### 4. Documentación (10%)

**Evaluamos:**
- README completo y claro
- METODOLOGIA.md con decisiones justificadas
- Código comentado donde necesario
- Instrucciones reproducibles

**Puntos:**
- README: 4 pts
- METODOLOGIA.md: 3 pts
- Comentarios código: 3 pts

---

### 5. Innovación y Análisis (5%)

**Puntos extra por:**
- Tests automatizados (pytest)
- Visualizaciones de datos
- Análisis adicionales
- Optimizaciones de performance
- Exportación a múltiples formatos

---

## 📅 Flujo de Entrega

### Paso 1: Preparar Entrega
```bash
# En tu proyecto local
cd entregas/02_limpieza_datos/
mkdir apellido_nombre
cp -r tu_proyecto/* apellido_nombre/

# Verificar .gitignore
cat apellido_nombre/.gitignore

# Limpiar (NO subir datos)
rm -rf apellido_nombre/data/
rm -rf apellido_nombre/logs/
rm -rf apellido_nombre/venv/
```

### Paso 2: Git Commit
```bash
git add entregas/02_limpieza_datos/apellido_nombre/
git commit -m "Entrega Ejercicio 02 - Apellido Nombre - Tema X"
```

### Paso 3: Push a tu Fork
```bash
git push origin tu-rama-ejercicio-02
```

### Paso 4: Pull Request
1. Ve a tu fork en GitHub
2. Crear Pull Request al repo original
3. Título: `[02] Apellido Nombre - Tema X`
4. Descripción: Resumen de tu análisis

---

## ❓ Preguntas Frecuentes

**P: ¿Puedo usar librerías adicionales?**
R: Sí, pero justifícalas en README y agrégalas a requirements.txt

**P: ¿Cuántos integrantes máximo por grupo?**
R: 5 máximo, 2 mínimo

**P: ¿Qué hago si mi pipeline tarda mucho?**
R: Optimiza con batches, usa índices en PostgreSQL, filtra datos antes

**P: ¿Puedo subir un subset de datos de ejemplo?**
R: Sí, pero pequeño (<1MB), en `data/sample/`

**P: Mi análisis encontró algo interesante, ¿lo incluyo?**
R: ¡Sí! Documéntalo en METODOLOGIA.md o README

---

## 🆘 Problemas Comunes

### Error: "ModuleNotFoundError"
```bash
# Verificar virtual environment activado
which python  # Debe mostrar ruta en venv/

# Reinstalar dependencias
pip install -r requirements.txt
```

### Error: "Connection refused" PostgreSQL
```bash
# Verificar PostgreSQL corriendo
# Windows:
sc query postgresql-x64-14

# Linux/Mac:
sudo systemctl status postgresql
```

### Error: Git rechaza archivos grandes
```bash
# Verificar tamaño
du -sh entregas/02_limpieza_datos/tu_apellido/

# Limpiar archivos grandes
git rm --cached archivo_grande.csv
```

---

**¿Dudas?** Pregunta en el foro del curso o en clase.

**Última actualización:** 2025-12-17
