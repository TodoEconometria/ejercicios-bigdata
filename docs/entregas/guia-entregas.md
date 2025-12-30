# Guía General de Entregas

Esta guía se aplica a **TODOS** los ejercicios del curso.

---

## Estructura de Carpetas por Alumno

Cada alumno debe crear **UNA carpeta personal** dentro de la carpeta de entrega del ejercicio correspondiente.

### Formato del Nombre

```
apellido_nombre
```

**Reglas:**
- Todo en minúsculas
- Sin tildes ni caracteres especiales
- Separado por guión bajo `_`
- Formato: `apellido_nombre` (apellido primero)

**Ejemplos válidos:**
- `garcia_maria/`
- `lopez_juan/`
- `martinez_ana/`
- `rodriguez_carlos/`

**Ejemplos NO válidos:**
- ❌ `María García/` (mayúsculas, tildes, espacios)
- ❌ `maria_garcia/` (nombre primero)
- ❌ `garcia-maria/` (guión en lugar de guión bajo)

---

## Ubicación de las Entregas

```
entregas/
├── 1.1_sqlite/                  # Ejercicio 1.1
│   ├── garcia_maria/            # Carpeta del alumno
│   │   ├── archivo1.py
│   │   ├── archivo2.md
│   │   └── ...
│   └── lopez_juan/              # Otro alumno
│       └── ...
│
├── 2.1_postgresql_hr/           # Ejercicio 2.1
│   └── garcia_maria/
│       └── ...
│
└── ...                          # Más ejercicios
```

---

## Múltiples Archivos por Alumno

### ✅ Permitido

- Subir **múltiples archivos** dentro de tu carpeta
- Actualizar archivos (hacer nuevos commits)
- Agregar archivos adicionales (capturas, PDFs, etc.)
- Organizar en subcarpetas si lo necesitas

**Ejemplo:**
```
entregas/01_bases_de_datos/garcia_maria/
└── 1.1_sqlite/
    ├── solucion_modelo_a.py
    ├── solucion_modelo_b.py
    ├── ANALISIS_DATOS.md
    ├── consultas.sql
    ├── capturas/
    │   ├── screenshot1.png
    │   └── screenshot2.png
    └── notas_personales.txt
```

### ❌ NO Permitido

- ❌ Subir archivos `.db` (bases de datos binarias)
- ❌ Subir archivos `.csv` grandes (datos)
- ❌ Subir archivos temporales (`.pyc`, `__pycache__/`, `.DS_Store`)
- ❌ Subir carpetas `venv/`, `node_modules/`

---

## Opciones de Entrega

### Opción 1: Archivos Sueltos (Recomendada)

Sube tus archivos directamente en tu carpeta:

```bash
git add entregas/X.X_ejercicio/tu_apellido_nombre/
git commit -m "Entrega X.X - Tu Nombre"
git push origin tu-rama
```

### Opción 2: Archivo ZIP

Si prefieres, puedes comprimir todo en un ZIP:

```
entregas/01_bases_de_datos/garcia_maria.zip
```

**Nota:** La Opción 1 es preferida porque permite revisión más fácil.

---

## Workflow Completo de Entrega

### Paso 1: Fork del Repositorio (Solo la primera vez)

1. Ve a: https://github.com/TodoEconometria/ejercicios-bigdata
2. Haz clic en **"Fork"** (arriba a la derecha)
3. Ahora tienes tu copia: `https://github.com/TU_USUARIO/ejercicios-bigdata`

### Paso 2: Clonar TU Fork

```bash
git clone https://github.com/TU_USUARIO/ejercicios-bigdata.git
cd ejercicios-bigdata
```

### Paso 3: Sincronizar con el Repositorio Original

**IMPORTANTE:** Antes de cada nueva entrega, sincroniza tu fork.

👉 **[Ver guía completa de sincronización](https://todoeconometria.github.io/ejercicios-bigdata/git-github/sincronizar-fork/)**

```bash
# Añadir upstream (solo la primera vez)
git remote add upstream https://github.com/TodoEconometria/ejercicios-bigdata.git

# Sincronizar
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

### Paso 4: Crear Rama para tu Entrega

```bash
git checkout -b apellido-ejercicio-X.X
```

**Ejemplo:**
```bash
git checkout -b garcia-ejercicio-1.1
```

### Paso 5: Crear tu Carpeta de Entrega

```bash
mkdir -p entregas/X.X_ejercicio/apellido_nombre
```

**Ejemplo:**
```bash
mkdir -p entregas/01_bases_de_datos/garcia_maria/1.1_sqlite
```

### Paso 6: Completar tus Archivos

Copia plantillas o crea tus archivos desde cero en tu carpeta:

```bash
# Ver qué archivos necesitas entregar
cat ejercicios/01_bases_de_datos/X.X_ejercicio/README.md
```

### Paso 7: Verificar Archivos

```bash
# Ver tus archivos
ls -la entregas/X.X_ejercicio/apellido_nombre/

# Ver estado de Git
git status
```

### Paso 8: Commit

```bash
# Agregar archivos
git add entregas/X.X_ejercicio/apellido_nombre/

# Commit con mensaje descriptivo
git commit -m "Entrega X.X - Nombre Apellido"
```

**Ejemplos de mensajes:**
- `"Entrega 1.1 - María García"`
- `"Entrega 2.1 PostgreSQL HR - Juan López"`

### Paso 9: Push a TU Fork

```bash
git push origin apellido-ejercicio-X.X
```

### Paso 10: Crear Pull Request

1. Ve a TU fork en GitHub
2. Verás un banner: **"apellido-ejercicio-X.X had recent pushes"**
3. Haz clic en **"Compare & pull request"**
4. **Título del PR:** `[X.X] Apellido Nombre - Título del Ejercicio`
5. Completa el checklist automático
6. Haz clic en **"Create pull request"**

---

## Validación Automática

Cuando crees tu PR, un bot automático verificará:

- ✅ Formato del nombre de carpeta
- ✅ Archivos obligatorios presentes
- ✅ Sin archivos prohibidos
- ⚠️ Si tu fork está desactualizado (>5 commits atrás)

**Si tu fork está desactualizado:**
El bot te avisará y agregará una etiqueta. Debes sincronizar antes de continuar.

---

## Actualizar tu PR (Correcciones)

Si el profesor pide correcciones o quieres actualizar:

```bash
# Edita tus archivos localmente

# Commit de nuevo
git add entregas/X.X_ejercicio/apellido_nombre/
git commit -m "Correcciones solicitadas"

# Push (actualiza automáticamente el PR)
git push origin apellido-ejercicio-X.X
```

---

## Preguntas Frecuentes

### ¿Puedo ver las entregas de otros compañeros?

Sí, los PRs son públicos. Pero **NO copies**, el sistema detecta plagios.

### ¿Cuántas veces puedo actualizar mi PR?

Las que necesites antes de la fecha límite. Cada push actualiza el PR automáticamente.

### ¿Qué pasa si me equivoco en el nombre de la carpeta?

El bot de validación te avisará. Puedes renombrar y hacer push de nuevo:

```bash
git mv entregas/X.X/nombre_incorrecto entregas/X.X/apellido_nombre
git commit -m "Corregir nombre de carpeta"
git push origin tu-rama
```

### No sé usar Git, ¿hay otra forma?

Puedes usar **GitHub Desktop** (interfaz gráfica) o pregunta al profesor.

### ¿Puedo organizar mis archivos en subcarpetas?

Sí, siempre que todo esté dentro de `entregas/X.X/apellido_nombre/`.

---

## Ayuda y Recursos

**Si tienes problemas:**
1. Revisa esta guía de nuevo
2. Consulta la guía específica del ejercicio
3. Pregunta a tus compañeros
4. Pregunta al profesor en clase

**Recursos útiles:**
- [Guía Git y GitHub](https://todoeconometria.github.io/ejercicios-bigdata/git-github/)
- [Sincronizar Fork](https://todoeconometria.github.io/ejercicios-bigdata/git-github/sincronizar-fork/)
- [Crear Pull Requests](https://todoeconometria.github.io/ejercicios-bigdata/git-github/pull-requests/)
- [Tutorial Git en español](https://git-scm.com/book/es/v2)

---

## Importante

- ⏰ Respeta las fechas límite (cada ejercicio tiene la suya)
- 🔒 NO subas información personal (contraseñas, tokens)
- 🚫 NO copies código de compañeros
- ✅ Sincroniza tu fork ANTES de cada entrega
- 📝 Lee las instrucciones específicas de cada ejercicio

---

**Última actualización:** 2025-12-17
