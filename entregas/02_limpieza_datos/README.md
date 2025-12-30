# Entregas - Ejercicio 02: Pipeline ETL QoG

Este ejercicio se realiza en **MODALIDAD GRUPAL**.

---

## 👥 Grupos Formados

Este ejercicio cuenta con **2 grupos de trabajo**:

### Grupo 01
📁 **Carpeta:** `entregas/02_limpieza_datos/grupo_01/`

**Integrantes:** [Ver README del grupo]

**Tema:** [Por definir por el grupo]

---

### Grupo 02
📁 **Carpeta:** `entregas/02_limpieza_datos/grupo_02/`

**Integrantes:** [Ver README del grupo]

**Tema:** [Por definir por el grupo]

---

## 📋 Instrucciones de Entrega

👉 **[Guía General de Entregas](https://todoeconometria.github.io/ejercicios-bigdata/entregas/guia-entregas/)**

👉 **[Instrucciones específicas del ejercicio](../../ejercicios/02_limpieza_datos/INSTRUCCIONES_ENTREGA.md)**

---

## 🎯 Temas Disponibles

Cada grupo debe elegir **UNO** de los siguientes temas:

### Tema 1: Evolución Institucional Post-Autoritaria

**Pregunta:** ¿Cómo evoluciona la calidad institucional en transiciones democráticas?

**Variables clave:**
- Índices de democracia (V-Dem, Polity)
- Calidad institucional (Transparency International)
- Desarrollo económico (PIB, HDI)

**Casos de estudio sugeridos:** Europa del Este, América Latina, Asia Central

**Documentación:** `ejercicios/02_limpieza_datos/especificaciones/VARIABLES_TEMA1.md`

---

### Tema 2: Recursos Naturales y Desarrollo

**Pregunta:** ¿La dependencia de recursos naturales afecta el desarrollo?

**Variables clave:**
- Producción petróleo/gas (Ross dataset)
- Rentas recursos naturales (World Bank)
- Acceso servicios básicos (agua, saneamiento)
- Calidad institucional

**Casos de estudio sugeridos:** Países petroleros, resource curse, seguridad hídrica

**Documentación:** `ejercicios/02_limpieza_datos/especificaciones/VARIABLES_TEMA2.md`

---

## 📁 Estructura de Carpetas

```
entregas/02_limpieza_datos/
├── README.md                    # Este archivo
│
├── grupo_01/                    # GRUPO 1
│   ├── README.md                # Integrantes, tema, workflow Git
│   ├── requirements.txt
│   ├── .env.example
│   ├── src/
│   │   ├── database/
│   │   ├── etl/
│   │   ├── analysis/
│   │   └── utils/
│   ├── scripts/
│   ├── sql/
│   ├── tests/                   # (Opcional)
│   └── docs/
│       └── METODOLOGIA.md
│
└── grupo_02/                    # GRUPO 2
    ├── README.md                # Integrantes, tema, workflow Git
    ├── requirements.txt
    ├── .env.example
    ├── src/
    │   ├── database/
    │   ├── etl/
    │   ├── analysis/
    │   └── utils/
    ├── scripts/
    ├── sql/
    ├── tests/                   # (Opcional)
    └── docs/
        └── METODOLOGIA.md
```

---

## 🔄 Workflow de Git para Grupos

### Paso 1: Coordinador Inicializa el Proyecto

El **coordinador** de cada grupo crea la estructura inicial:

```bash
cd entregas/02_limpieza_datos/grupo_XX/

# Crear estructura
mkdir -p src/{database,etl,analysis,utils}
mkdir -p scripts sql/queries tests docs/capturas

# Crear archivos base
touch requirements.txt .env.example .gitignore
touch src/__init__.py

# Commit inicial
git add entregas/02_limpieza_datos/grupo_XX/
git commit -m "GRUPO-XX: Estructura inicial del proyecto"
git push origin main
```

### Paso 2: Miembros Trabajan en Ramas

Cada miembro crea su propia rama para trabajar:

```bash
# Sincronizar primero
git pull origin main

# Crear rama personal
git checkout -b grupo01-extract-maria
# o
git checkout -b grupo02-transform-juan

# Trabajar en tus archivos
# ... código ...

# Commit con formato grupal
git add src/etl/extract.py
git commit -m "GRUPO-01: Implementar extract.py (María García)

- Función download_qog_data() completa
- Validaciones de descarga incluidas
- Logging configurado"

# Push a tu rama
git push origin grupo01-extract-maria
```

### Paso 3: Pull Request y Review

1. Crear **Pull Request** en GitHub desde tu rama
2. Otro miembro del grupo **revisa el código**
3. Si está OK → **Merge a main**
4. Todos sincronizan: `git pull origin main`

### Formato de Commits Grupales

**Obligatorio usar el prefijo del grupo:**

```
GRUPO-01: [Descripción] (Autor)
GRUPO-02: [Descripción] (Autor)
```

**Ejemplos:**
```bash
git commit -m "GRUPO-01: Implementar fase Extract (María García)"
git commit -m "GRUPO-01: Crear schema PostgreSQL (Juan López)"
git commit -m "GRUPO-02: Añadir validaciones Transform (Pedro Sánchez)"
git commit -m "GRUPO-02: Documentar metodología (Ana Martín)"
```

---

## ✅ Checklist de Entrega (Por Grupo)

### Código y Funcionalidad
- [ ] Pipeline ETL completo (Extract → Transform → Load)
- [ ] Todas las funciones según `FUNCIONES_REQUERIDAS.md`
- [ ] Validaciones según `VALIDACIONES.md`
- [ ] Logging profesional en todos los pasos
- [ ] Type hints y docstrings completos
- [ ] Código sigue PEP 8

### Base de Datos
- [ ] Schema PostgreSQL implementado
- [ ] Datos cargados correctamente
- [ ] Índices optimizados
- [ ] Panel data balanceado generado
- [ ] Queries SQL para análisis

### Documentación
- [ ] **README.md del grupo** con:
  - Lista completa de integrantes
  - Tema seleccionado y pregunta de investigación
  - División de responsabilidades
  - Instrucciones para ejecutar el proyecto
- [ ] **METODOLOGIA.md** con decisiones de diseño
- [ ] requirements.txt actualizado
- [ ] .env.example con todas las variables necesarias

### Git y Colaboración
- [ ] Commits con formato grupal (`GRUPO-XX: ...`)
- [ ] Todos los miembros hicieron commits
- [ ] Pull Requests utilizadas para cambios importantes
- [ ] Histórico de Git refleja trabajo colaborativo

### Tests y Validación
- [ ] Pipeline ejecuta sin errores end-to-end
- [ ] Todas las validaciones pasan
- [ ] Datos en PostgreSQL verificados
- [ ] Tests unitarios (opcional pero recomendado)

---

## ⚠️ Reglas Importantes para Trabajo Grupal

### 1. Comunicación
- Definir un canal de comunicación (WhatsApp, Discord, Slack)
- Avisar antes de hacer push a `main`
- Coordinar quién trabaja en qué para evitar conflictos

### 2. Git Hygiene
- **SIEMPRE** hacer `git pull` antes de empezar a trabajar
- Usar ramas para features nuevas
- Commits descriptivos con nombre del autor
- No hacer force push a `main`

### 3. División del Trabajo
- Cada miembro debe tener responsabilidades claras
- Documentar en el README del grupo quién hace qué
- Todos deben contribuir con código, no solo documentación

### 4. Code Review
- Usar Pull Requests para cambios importantes
- Otro miembro debe revisar antes de merge
- Resolver conflictos en equipo

### 5. Coordinación
- Establecer reuniones regulares
- Actualizar tabla de progreso en README del grupo
- Reportar problemas bloqueantes rápidamente

---

## 🚫 ¿Qué NO Subir?

**IMPORTANTE:** NO incluir en el repositorio:

- ❌ Datos descargados (`data/`, `*.csv`, `*.xlsx`)
- ❌ Bases de datos (dumps, `*.db`)
- ❌ Logs (`logs/`, `*.log`)
- ❌ Virtual environments (`venv/`, `env/`)
- ❌ Archivo `.env` con credenciales (solo `.env.example`)
- ❌ Archivos temporales (`__pycache__/`, `*.pyc`)
- ❌ Archivos del IDE (`.vscode/`, `.idea/`)

**Crear `.gitignore`:**
```
# Datos
data/
*.csv
*.xlsx
*.db

# Logs
logs/
*.log

# Python
venv/
__pycache__/
*.pyc
*.pyo

# Secrets
.env

# IDE
.vscode/
.idea/
*.swp
```

---

## 📊 Evaluación Grupal

| Criterio | Peso | Qué se evalúa |
|----------|------|---------------|
| **Funcionalidad** | 40% | Pipeline ejecuta sin errores, datos correctos en PostgreSQL |
| **Arquitectura** | 25% | Código modular, separación de responsabilidades, buenas prácticas |
| **Calidad Código** | 20% | PEP 8, type hints, docstrings, claridad |
| **Documentación** | 10% | README completo, METODOLOGIA.md, comentarios útiles |
| **Colaboración** | 5% | Uso efectivo de Git, contribución equilibrada de miembros |

**Nota:** La calificación es **grupal**. Todos los miembros reciben la misma nota.

---

## 📞 Soporte

**Dudas técnicas:** Consulta las [instrucciones específicas](../../ejercicios/02_limpieza_datos/INSTRUCCIONES_ENTREGA.md)

**Problemas de Git:** Ver [guía de sincronización](../../docs/git-github/sincronizar-fork.md)

**Consultas al profesor:** [Crear issue en GitHub] o preguntar en clase

---

## 🎯 Recursos Útiles

### Especificaciones Técnicas
- `ejercicios/02_limpieza_datos/especificaciones/ARQUITECTURA.md`
- `ejercicios/02_limpieza_datos/especificaciones/ESQUEMA_DB.sql`
- `ejercicios/02_limpieza_datos/especificaciones/FUNCIONES_REQUERIDAS.md`
- `ejercicios/02_limpieza_datos/especificaciones/VALIDACIONES.md`

### Variables por Tema
- `ejercicios/02_limpieza_datos/especificaciones/VARIABLES_TEMA1.md`
- `ejercicios/02_limpieza_datos/especificaciones/VARIABLES_TEMA2.md`

### Documentación General
- `ejercicios/02_limpieza_datos/docs/POSTGRESQL_SETUP.md`
- `ejercicios/02_limpieza_datos/README.md`

### Dataset
- [QoG Website](https://www.qog.pol.gu.se/)
- [Codebook PDF](https://www.qogdata.pol.gu.se/data/codebook_std_jan23.pdf)
- [Download CSV](https://www.qogdata.pol.gu.se/data/qog_std_ts_jan23.csv)

---

**Última actualización:** 2025-12-18
