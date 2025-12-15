# 👨‍🏫 Instrucciones para el Profesor - Ejercicio 01

> ⚠️ **IMPORTANTE - Protección de Rama Activa**
>
> La rama `main` del repositorio público está **PROTEGIDA**.
> **NO puedes hacer `git push origin main` directo.**
>
> **Flujo obligatorio:**
> 1. Trabajas en `desarrollo` (repo privado)
> 2. Push a `desarrollo/desarrollo`
> 3. Creas Pull Request: desarrollo → main
> 4. Mergeas el PR (desde GitHub Web o con `gh pr merge`)
>
> **¿Por qué?** Evita errores, permite revisión, historial limpio.

---

## 📋 Resumen del Ejercicio

**Ejercicio 01**: Base de Datos Relacional - Tienda Informática

Este ejercicio requiere que los alumnos:
1. Analicen 25 archivos CSV con datos de productos (~15,000 registros)
2. Diseñen un esquema relacional normalizado
3. Implementen la base de datos en SQLite/PostgreSQL
4. Realicen consultas SQL avanzadas

**Tiempo estimado**: 11-16 horas (2-3 semanas)
**Puntos**: 100 pts + hasta 15 pts bonus

---

## 🚀 Pasos de Implementación

### 1. Preparar los Datos

Los datos **NO están en el repositorio** de GitHub por su tamaño (~25 MB descomprimidos).

**Opción A: Distribuir por Google Drive / OneDrive**

```bash
# Ya tienes el archivo: csv_tienda_informatica.zip
# Súbelo a Google Drive u OneDrive
# Genera un link compartido
# Comparte el link con los alumnos
```

**Opción B: Subir a servidor de la universidad**

Si tu universidad tiene un servidor de archivos, sube ahí el ZIP.

### 2. Crear el Issue en GitHub

1. Ve a: https://github.com/TodoEconometria/ejercicios-bigdata/issues
2. Clic en "New Issue"
3. Usa el contenido de [`ISSUE_TEMPLATE.md`](./ISSUE_TEMPLATE.md)
4. **IMPORTANTE**: Actualiza estos campos:
   - `[LINK A PROPORCIONAR POR EL PROFESOR]` → Tu link de descarga
   - `[A definir por el profesor]` → Fecha de apertura
   - `[A definir por el profesor]` → Fecha de entrega
5. Etiquetas recomendadas: `tarea`, `ejercicio-05`, `sql`, `base-de-datos`

### 3. Anunciar en Clase

**Mensaje recomendado**:

```
📢 NUEVO EJERCICIO: Base de Datos Relacional

Se ha publicado el Ejercicio 01 sobre diseño e implementación de bases de datos.

📍 Issue: https://github.com/TodoEconometria/ejercicios-bigdata/issues/[NÚMERO]
📥 Datos: [TU_LINK_DE_DESCARGA]
📅 Entrega: [FECHA], 23:59
⏱️ Tiempo estimado: 11-16 horas

Este ejercicio es más complejo que los anteriores. Lean toda la documentación antes de empezar.

¡Buena suerte! 💪
```

---

## 📂 Estructura del Ejercicio en el Repositorio

```
ejercicios/01_tienda_informatica/
├── datos/
│   └── .gitkeep                      ← Solo esto va a GitHub
│
├── soluciones/                       ← Se creará con las entregas
│   ├── alumno1_apellido/
│   ├── alumno2_apellido/
│   └── ...
│
├── ENUNCIADO.md                      ← Descripción completa
├── AYUDA.md                          ← Consejos paso a paso
├── plantilla_base.py                 ← Código de ejemplo
├── README.md                         ← Instrucciones de entrega
├── ISSUE_TEMPLATE.md                 ← Para crear el issue en GitHub
├── INSTRUCCIONES_PROFESOR.md         ← Este archivo
└── .gitignore                        ← Ignora datos y DBs
```

---

## 📤 Gestión de Entregas

### Los Alumnos Deben:

1. **Hacer fork** del repositorio
2. **Crear rama** con formato: `apellido-ejercicio01`
3. **Trabajar en**: `ejercicios/01_tienda_informatica/soluciones/su_apellido_nombre/`
4. **Hacer PR** desde su fork a tu repositorio principal

### Tú Debes:

1. **Revisar los PRs** uno por uno
2. **Verificar** que la estructura sea correcta
3. **Ejecutar** el código para confirmar que funciona
4. **Evaluar** según la rúbrica (ver sección abajo)
5. **Aprobar y mergear** o pedir correcciones

---

## 📊 Rúbrica de Evaluación

### Parte 1: Análisis Exploratorio (20 pts)

| Criterio | Excelente (20) | Bueno (15) | Suficiente (10) | Insuficiente (0-5) |
|----------|----------------|------------|-----------------|-------------------|
| **Profundidad** | Análisis detallado de los 25 CSVs | Análisis de la mayoría | Análisis superficial | Muy incompleto |
| **Identificación de problemas** | Encuentra inconsistencias y datos faltantes | Encuentra algunos problemas | Pocos problemas identificados | No identifica problemas |
| **Propuesta de normalización** | Identifica claramente qué normalizar | Identifica algunas áreas | Propuesta vaga | Sin propuesta |

**Formato**: Markdown o Jupyter Notebook bien documentado

### Parte 2: Diseño Relacional (30 pts)

| Criterio | Excelente (30) | Bueno (22) | Suficiente (15) | Insuficiente (0-10) |
|----------|----------------|------------|-----------------|-------------------|
| **Diagrama ER** | Completo, claro, con cardinalidades | Completo pero mejorable | Básico | Incompleto o confuso |
| **Normalización** | 3FN o superior aplicado correctamente | 3FN con algunos errores | 2FN | Sin normalización |
| **Claves PK/FK** | Todas bien definidas | La mayoría correctas | Algunas correctas | Mal definidas |
| **Justificación** | Excelente justificación de decisiones | Buena justificación | Justificación básica | Sin justificación |

**Archivos**: `diagrama_er.png`, `justificacion_diseño.md`, `schema.sql`

### Parte 3: Implementación (30 pts)

| Criterio | Excelente (30) | Bueno (22) | Suficiente (15) | Insuficiente (0-10) |
|----------|----------------|------------|-----------------|-------------------|
| **Código funcional** | Funciona sin errores | Errores menores | Errores pero funciona | No funciona |
| **Manejo de errores** | Robusto, loguea errores | Manejo básico | Poco manejo | Sin manejo |
| **Eficiencia** | Código optimizado | Código aceptable | Ineficiente pero funciona | Muy ineficiente |
| **Código limpio** | Bien organizado y comentado | Organizado | Poco organizado | Desorganizado |

**Archivos**: `cargar_datos.py`, `requirements.txt`, logs

### Parte 4: Consultas SQL (15 pts)

| Criterio | Excelente (15) | Bueno (11) | Suficiente (8) | Insuficiente (0-5) |
|----------|----------------|------------|----------------|-------------------|
| **Cantidad** | 8+ consultas útiles | 8 consultas | 5-7 consultas | < 5 consultas |
| **Complejidad** | JOINs, subconsultas, agregaciones | JOINs y agregaciones | SELECTs básicos | Muy simples |
| **Utilidad** | Consultas útiles para el negocio | Consultas razonables | Consultas genéricas | Poco útiles |
| **Correctitud** | Todas correctas | La mayoría correctas | Algunas correctas | Muchos errores |

**Archivos**: `consultas.sql`, `resultados.md`

### Parte 5: Documentación (5 pts)

| Criterio | Excelente (5) | Bueno (4) | Suficiente (2) | Insuficiente (0-1) |
|----------|---------------|-----------|----------------|-------------------|
| **README.md** | Completo, claro, reproducible | Claro pero falta algo | Básico | Muy incompleto |
| **Comentarios** | Código bien comentado | Comentarios adecuados | Pocos comentarios | Sin comentarios |

### Puntos Bonus (+15 máximo)

- **+5 pts**: PostgreSQL en lugar de SQLite (verificar conexión y schema)
- **+5 pts**: Índices implementados y optimización demostrada
- **+5 pts**: Script de backup/restore funcional
- **+3 pts**: Tests unitarios para validación de datos
- **+2 pts**: Dashboard o visualización de datos

---

## ✅ Checklist de Revisión

Para cada entrega, verifica:

### Estructura
- [ ] Carpeta en `soluciones/apellido_nombre/`
- [ ] 5 subcarpetas: analisis, diseño, implementacion, consultas, base_datos
- [ ] README.md presente y completo

### Contenido
- [ ] Análisis exploratorio presente
- [ ] Diagrama ER incluido y legible
- [ ] `schema.sql` con CREATE TABLE statements
- [ ] Código Python funcional
- [ ] `requirements.txt` correcto
- [ ] Al menos 8 consultas SQL
- [ ] Base de datos `.db` generada (o instrucciones para PostgreSQL)

### Calidad
- [ ] Código ejecuta sin errores
- [ ] Diseño aplicado correctamente (normalización)
- [ ] Consultas devuelven resultados lógicos
- [ ] Documentación clara y completa

### Git
- [ ] PR desde fork del alumno
- [ ] Rama con nombre correcto
- [ ] Commits descriptivos
- [ ] No incluye archivos CSV o DBs grandes (excepto si es necesario)

---

## 🔧 Cómo Probar una Entrega

```bash
# 1. Hacer checkout del PR
git fetch origin pull/[PR_NUMBER]/head:review-[APELLIDO]
git checkout review-[APELLIDO]

# 2. Navegar a la solución del alumno
cd ejercicios/01_tienda_informatica/soluciones/apellido_nombre/

# 3. Instalar dependencias
pip install -r implementacion/requirements.txt

# 4. Colocar los datos (si no están)
# (Asegúrate de tener csv_tienda_informatica.zip)
cd ../..
unzip csv_tienda_informatica.zip -d datos/

# 5. Ejecutar el código del alumno
cd soluciones/apellido_nombre/implementacion/
python cargar_datos.py

# 6. Verificar la base de datos
ls ../base_datos/
# Debería haber un archivo .db

# 7. Probar las consultas
sqlite3 ../base_datos/tienda.db < ../consultas/consultas.sql

# 8. Revisar el código y documentación
cat README.md
cat ../diseño/justificacion_diseño.md
```

---

## 📝 Comentarios Tipo para los PRs

### Si está Todo Correcto

```markdown
## ✅ Aprobado - [PUNTUACIÓN]/100

Excelente trabajo. Tu solución cumple todos los requisitos:

- ✅ Análisis exploratorio completo y bien documentado
- ✅ Diseño relacional sólido, buena normalización
- ✅ Código funciona correctamente
- ✅ Consultas útiles y bien escritas
- ✅ Documentación clara

**Puntos por sección**:
- Análisis: [X]/20
- Diseño: [X]/30
- Implementación: [X]/30
- Consultas: [X]/15
- Documentación: [X]/5
- Bonus: [X]/15 (si aplica)

**Puntos destacables**:
- [Menciona algo específico que hizo bien]

**Sugerencias de mejora** (opcional):
- [Alguna sugerencia constructiva]

¡Felicidades! 🎉
```

### Si Necesita Correcciones

```markdown
## ⚠️ Requiere Correcciones

Gracias por tu entrega. He revisado tu trabajo y necesita algunas correcciones antes de aprobar:

**Problemas Encontrados**:
1. [Problema específico 1]
2. [Problema específico 2]
3. [Problema específico 3]

**Qué Hacer**:
1. Corrige los puntos mencionados
2. Haz commit de los cambios
3. Empuja los cambios a tu rama
4. El PR se actualizará automáticamente
5. Avísame cuando esté listo para revisar de nuevo

**Recursos**:
- [Link a documentación relevante]

Si necesitas ayuda, pregunta en clase o por email.
```

---

## 📊 Gestión de Notas

Crea una hoja de cálculo con:

| Alumno | PR # | Análisis | Diseño | Implementación | Consultas | Documentación | Bonus | Total | Fecha Entrega | Observaciones |
|--------|------|----------|--------|----------------|-----------|---------------|-------|-------|---------------|---------------|
| García M. | #15 | 18 | 28 | 27 | 14 | 5 | +5 | 97 | 15/01/2025 | PostgreSQL |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | ... | ... |

---

## ⚠️ Problemas Comunes

### Problema 1: Alumno subió los CSVs al repositorio

**Solución**: Pídele que:
```bash
git rm --cached datos/csv_tienda_informatica/*.csv
git commit -m "Eliminar CSVs del repositorio"
git push
```

### Problema 2: El código no funciona

**Solución**:
1. Pide logs de error
2. Verifica `requirements.txt`
3. Confirma que los datos están en el lugar correcto
4. Prueba en tu máquina

### Problema 3: Estructura de carpetas incorrecta

**Solución**: Marca como "requiere correcciones" y explica la estructura esperada.

### Problema 4: Diagrama ER ilegible

**Solución**: Pide una versión en mayor resolución o formato PDF.

---

## 🎯 Consejos para la Evaluación

1. **Sé consistente**: Usa la misma rúbrica para todos
2. **Sé constructivo**: Da feedback específico y útil
3. **Valora el esfuerzo**: Reconoce el trabajo bien hecho
4. **Sé justo**: Si alguien se esforzó pero tiene errores, guíalo
5. **Documenta**: Mantén registro de las puntuaciones y criterios

---

## 📅 Cronograma Sugerido

| Semana | Actividad |
|--------|-----------|
| **Semana 1** | Publicar ejercicio, compartir datos, explicar en clase |
| **Semana 2** | Responder dudas, revisar progreso |
| **Semana 3** | Fecha límite de entrega, empezar revisiones |
| **Semana 4** | Completar revisiones, dar feedback |

---

## 📧 Email Tipo para los Alumnos

**Asunto**: Ejercicio 01: Base de Datos Relacional - Tienda Informática

```
Hola a todos,

Se ha publicado el **Ejercicio 01** sobre diseño e implementación de bases de datos relacionales.

📍 **Issue en GitHub**: https://github.com/TodoEconometria/ejercicios-bigdata/issues/[NÚMERO]
📥 **Datos (CSV)**: [TU_LINK_DE_DESCARGA]
📅 **Fecha de entrega**: [FECHA], 23:59
⏱️ **Tiempo estimado**: 11-16 horas

Este ejercicio es **más complejo** que los anteriores. Requiere:
- Análisis exploratorio de 25 archivos CSV
- Diseño de esquema relacional (diagrama ER)
- Implementación en SQLite o PostgreSQL
- Consultas SQL avanzadas

**Recomendaciones**:
1. Lean TODA la documentación antes de empezar
2. Comiencen pronto (no lo dejen para el último día)
3. Hagan commits frecuentes
4. Pregunten sus dudas en clase

Documentación completa en:
https://github.com/TodoEconometria/ejercicios-bigdata/tree/main/ejercicios/01_tienda_informatica

¡Buena suerte!

[Tu nombre]
```

---

## 🆘 Soporte

Si encuentras problemas al implementar el ejercicio:

1. Verifica que la estructura de archivos sea correcta
2. Confirma que el .gitignore esté funcionando
3. Prueba clonar el repo en limpio y seguir las instrucciones
4. Contacta si necesitas ayuda adicional

---

## 🎯 CHEATSHEET GIT - Tu Flujo de Trabajo Paso a Paso

**Para que nunca te pierdas** - Guía paso a paso del flujo diario

---

### 📍 ANTES DE HACER NADA

#### ✅ Paso 0: ¿Dónde estoy?

```bash
# SIEMPRE ejecuta esto primero:
git branch --show-current
```

**Deberías ver:**
- `desarrollo` → ✅ BIEN (es tu rama de trabajo)
- `main` → ⚠️ CUIDADO (solo para publicar)

**Si estás en `main`:**
```bash
git checkout desarrollo
```

---

### 🆕 ESCENARIO 1: CREAR EJERCICIO NUEVO

**Situación:** Quieres crear un ejercicio nuevo desde cero

#### 📋 Checklist paso a paso:

```bash
# ✅ PASO 1: Asegúrate de estar en desarrollo
git branch --show-current
# Debe decir: desarrollo

# Si NO estás en desarrollo:
git checkout desarrollo

# ✅ PASO 2: Asegúrate de tener lo último
git pull desarrollo desarrollo

# ✅ PASO 3: Crea tu ejercicio en .profesor/
# Abre tu editor y crea archivos en:
# .profesor/ejercicios_en_desarrollo/XX_nombre_ejercicio/
#   ├── INSTRUCCIONES_PROFESOR.md
#   ├── ENUNCIADO.md
#   ├── AYUDA.md
#   └── ...

# ✅ PASO 4: Guarda tus cambios
git add .
git status  # Revisa qué vas a guardar

# ✅ PASO 5: Haz commit
git commit -m "ADD: Ejercicio XX nombre"

# ✅ PASO 6: Sube a tu repo PRIVADO
git push desarrollo desarrollo

# 🎉 LISTO! Tu ejercicio está guardado en tu repo privado
```

---

### 📢 ESCENARIO 2: PUBLICAR EJERCICIO PARA ALUMNOS

**Situación:** Ya tienes el ejercicio listo y quieres que los alumnos lo vean

#### 📋 Checklist paso a paso:

```bash
# ✅ PASO 1: Asegúrate de estar en desarrollo
git branch --show-current
# Debe decir: desarrollo

# ✅ PASO 2: Copia archivos públicos de .profesor/ a ejercicios/
# Copia manualmente (o con script):
#   .profesor/ejercicios_en_desarrollo/XX/
#   → ejercicios/categoria/XX/

# Por ejemplo:
# .profesor/ejercicios_en_desarrollo/01_tienda_informatica/ENUNCIADO.md
# → ejercicios/01_bases_de_datos/1.1_introduccion_sqlite/README.md

# ✅ PASO 3: Guarda estos archivos públicos
git add ejercicios/
git commit -m "PUBLISH: Ejercicio 1.1 para alumnos"

# ✅ PASO 4: Sube a repo privado primero (backup)
git push desarrollo desarrollo

# ✅ PASO 5: Publicar a repo PÚBLICO
# NOTA: La rama main está PROTEGIDA (no se puede push directo)
# Debes crear un Pull Request

# Opción A: Desde GitHub Web (MÁS RÁPIDO)
# 1. Ve a: https://github.com/TodoEconometria/ejercicios-bigdata-profesor
# 2. Click "Compare & pull request" (banner amarillo)
# 3. Base: TodoEconometria/ejercicios-bigdata (main)
#    Compare: TodoEconometria/ejercicios-bigdata-profesor (desarrollo)
# 4. Click "Create pull request"
# 5. Click "Merge pull request" → "Confirm merge"

# Opción B: Desde terminal con gh
gh pr create --repo TodoEconometria/ejercicios-bigdata \
  --base main \
  --head TodoEconometria:desarrollo \
  --title "PUBLISH: Ejercicio 1.1 para alumnos" \
  --body "Publicar ejercicio 1.1"

# Luego mergear el PR:
gh pr merge --repo TodoEconometria/ejercicios-bigdata --merge

# ✅ PASO 6: Vuelve a desarrollo (tu rama de trabajo)
git checkout desarrollo

# 🎉 LISTO! Los alumnos pueden ver el ejercicio en GitHub
```

---

### 📝 ESCENARIO 3: REVISAR ENTREGA (Solo .md - GitHub Web)

**Situación:** Un alumno envió su entrega con archivos .md (como ejercicio 1.1)

#### 📋 Checklist paso a paso:

```bash
# ✅ PASO 1: NO NECESITAS GIT LOCAL!
# Ve a GitHub en el navegador:
# https://github.com/TodoEconometria/ejercicios-bigdata/pulls

# ✅ PASO 2: Abre el Pull Request del alumno
# Ej: "PR #15: garcia_maria - Ejercicio 1.1"

# ✅ PASO 3: Revisa los archivos
# Haz clic en "Files changed"
# Lee ANALISIS_DATOS.md, resumen_eda.md, REFLEXION.md

# ✅ PASO 4: Usa tu checklist de revisión (ver sección abajo)
# Evalúa según rúbrica

# ✅ PASO 5A: Si apruebas → Merge
# Botón verde "Merge pull request"

# ✅ PASO 5B: Si necesita correcciones
# Comentario: "Necesitas corregir X, Y, Z"
# El alumno actualiza su PR

# 🎉 LISTO! Entrega revisada sin tocar Git local
```

---

### 💻 ESCENARIO 4: REVISAR ENTREGA (Con código - Ejecutar localmente)

**Situación:** Un alumno envió código Python que necesitas ejecutar

#### 📋 Checklist paso a paso:

```bash
# ✅ PASO 1: Asegúrate de estar en desarrollo
git branch --show-current
# Debe decir: desarrollo

# ✅ PASO 2: Descarga el PR del alumno
# Reemplaza "15" con el número del PR
git fetch origin pull/15/head:review-garcia
git checkout review-garcia

# ✅ PASO 3: Ve a la carpeta del alumno
cd entregas/1.1_sqlite/garcia_maria/

# ✅ PASO 4: Ejecuta el código
python solucion.py
# (O lo que sea necesario)

# ✅ PASO 5: Revisa resultados
# Abre archivos, revisa bases de datos, etc.

# ✅ PASO 6: Toma notas de tu evaluación
# Usa el checklist de revisión (sección abajo)

# ✅ PASO 7: Vuelve a desarrollo
cd ../../..  # Vuelve a la raíz
git checkout desarrollo

# ✅ PASO 8: Ve a GitHub y comenta en el PR
# https://github.com/TodoEconometria/ejercicios-bigdata/pull/15

# ✅ PASO 9: Aprueba o pide correcciones
# Desde GitHub Web

# 🎉 LISTO! Código ejecutado y entrega revisada
```

---

### 🔄 ESCENARIO 5: SINCRONIZAR REPOS (Manual)

**Situación:** Ya aprobaste entregas en repo público y quieres backup en privado

#### 📋 Checklist paso a paso:

```bash
# ✅ PASO 1: Asegúrate de estar en desarrollo
git branch --show-current
# Debe decir: desarrollo

# ✅ PASO 2: Trae cambios del repo público
git pull origin main

# ✅ PASO 3: Sube a tu repo privado (backup)
git push desarrollo desarrollo

# 🎉 LISTO! Entregas sincronizadas en ambos repos
```

---

### 🔄 ESCENARIO 5B: SINCRONIZAR con sync.py (Automático)

**Situación:** Usar script para sincronizar automáticamente

#### 📋 Checklist paso a paso:

```bash
# ✅ Traer entregas de público → privado
python sync.py pull

# ✅ Enviar ejercicios de privado → público
python sync.py push

# 🎉 LISTO! Sincronización automática
```

---

### ✏️ ESCENARIO 6: MODIFICAR EJERCICIO YA PUBLICADO

**Situación:** Necesitas corregir algo en un ejercicio público

#### 📋 Checklist paso a paso:

```bash
# ✅ PASO 1: Asegúrate de estar en desarrollo
git branch --show-current
# Debe decir: desarrollo

# ✅ PASO 2: Modifica el archivo
# Edita ejercicios/01_bases_de_datos/1.1_introduccion_sqlite/README.md

# ✅ PASO 3: Guarda cambios
git add ejercicios/
git commit -m "FIX: Corregir instrucciones ejercicio 1.1"

# ✅ PASO 4: Sube a repo privado
git push desarrollo desarrollo

# ✅ PASO 5: Publica al repo público (vía PR)
# NOTA: main está protegida, usar PR

# Opción A: GitHub Web
# 1. Ve a https://github.com/TodoEconometria/ejercicios-bigdata-profesor
# 2. "Compare & pull request" → Crear PR → Merge

# Opción B: Terminal
gh pr create --repo TodoEconometria/ejercicios-bigdata \
  --base main --head TodoEconometria:desarrollo \
  --title "FIX: Corregir ejercicio 1.1" --body "Correcciones"
gh pr merge --repo TodoEconometria/ejercicios-bigdata --merge

# 🎉 LISTO! Cambios publicados
```

---

### 🆘 COMANDOS DE EMERGENCIA

#### "¡No sé dónde estoy!"

```bash
# Ver en qué rama estás:
git branch --show-current

# Ver qué repositorios remotos tienes:
git remote -v

# Ver qué cambios tienes sin guardar:
git status
```

#### "¡Hice cambios en la rama equivocada!"

```bash
# Si estás en main pero debías estar en desarrollo:

# 1. Guarda tus cambios temporalmente
git stash

# 2. Cambia a desarrollo
git checkout desarrollo

# 3. Recupera tus cambios
git stash pop

# 4. Ahora haz commit normalmente
git add .
git commit -m "Tu mensaje"
```

#### "¡Quiero descartar todos mis cambios!"

```bash
# CUIDADO: Esto BORRA todos los cambios sin guardar
git restore .

# O si ya hiciste add:
git reset --hard
```

---

### 📋 RECORDATORIOS IMPORTANTES

#### ✅ SIEMPRE:

1. **Antes de hacer nada:** `git branch --show-current`
2. **Trabaja en:** `desarrollo`
3. **Publica a alumnos:** `main` (solo cuando estés listo)
4. **Guarda siempre primero en:** `desarrollo` (privado)
5. **Luego publica en:** `origin main` (público)

#### ❌ NUNCA:

1. **Trabajes directamente en `main`**
2. **Hagas push a `origin main` sin mergear desde `desarrollo`**
3. **Borres la carpeta `.profesor/`** (está en .gitignore del público)

---

## ✅ CHECKLIST DE REVISIÓN - Ejercicio 1.1 (Solo .md)

**Alumno:** ___________________
**PR #:** ___________________
**Fecha revisión:** ___________________

### 1. Estructura (10 pts)
- [ ] Carpeta en `entregas/1.1_sqlite/apellido_nombre/` (5 pts)
- [ ] Los 3 archivos presentes (5 pts)

### 2. ANALISIS_DATOS.md (40 pts)
- [ ] Resumen Ejecutivo completo (5 pts)
- [ ] Análisis de Estructura (10 pts)
- [ ] Análisis de Calidad (10 pts)
- [ ] Identificación de Entidades (5 pts)
- [ ] Diagramas ER (Modelos A y B en Mermaid) (10 pts)

### 3. resumen_eda.md (30 pts)
- [ ] Tabla resumen de archivos (10 pts)
- [ ] Estadísticas completas (10 pts)
- [ ] Fabricantes y colores identificados (10 pts)

### 4. REFLEXION.md (20 pts)
- [ ] Pregunta 1: Modelo más fácil (3 pts)
- [ ] Pregunta 2: Ventajas Modelo A (3 pts)
- [ ] Pregunta 3: Desventajas Modelo A (3 pts)
- [ ] Pregunta 4: Cuándo usar Modelo B (4 pts)
- [ ] Pregunta 5: Necesidad Modelo C (4 pts)
- [ ] Pregunta 6: Modificación columnas (3 pts)

### PUNTUACIÓN TOTAL: _____ / 100

### Comentarios para el alumno:
```
[Escribe feedback aquí]
```

---

## 📝 PLANTILLAS DE COMENTARIOS EN PRs

### ✅ Si Apruebas (100-90 pts)

```markdown
## ✅ APROBADO - [PUNTUACIÓN]/100

Excelente trabajo en el ejercicio 1.1.

**Puntos por sección:**
- Estructura: [X]/10
- ANALISIS_DATOS.md: [X]/40
- resumen_eda.md: [X]/30
- REFLEXION.md: [X]/20

**Puntos destacables:**
- [Menciona algo específico que hizo muy bien]

**Sugerencias de mejora:**
- [Algo opcional que podría mejorar]

¡Felicidades! 🎉
```

### ⚠️ Si Necesita Correcciones Menores (89-70 pts)

```markdown
## ⚠️ REQUIERE CORRECCIONES MENORES - [PUNTUACIÓN]/100

Buen trabajo, pero necesitas hacer algunas correcciones:

**Problemas encontrados:**
1. [Problema específico 1]
2. [Problema específico 2]

**Qué hacer:**
1. Corrige los puntos mencionados
2. Haz commit y push a tu rama
3. El PR se actualizará automáticamente
4. Avísame cuando esté listo

**Tiempo:** Tienes [X] días para corregir.
```

### ❌ Si Necesita Rehacer (< 70 pts)

```markdown
## ❌ REQUIERE REHACERSE

Tu entrega tiene problemas significativos que requieren que rehagas varias partes:

**Problemas críticos:**
1. [Problema grave 1]
2. [Problema grave 2]

**Recomendaciones:**
- Revisa las instrucciones del ejercicio
- Consulta el archivo de AYUDA
- Pide ayuda en clase si lo necesitas

**Fecha nueva de entrega:** [FECHA]
```

---

## 🎯 FLUJO VISUAL RESUMIDO

```
┌─────────────────────────────────────────┐
│  1. TÚ DESARROLLAS (desarrollo)         │
│     .profesor/ejercicios_en_desarrollo/ │
│     git push desarrollo desarrollo      │
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│  2. TÚ PUBLICAS (main) - VÍA PR         │
│     git push desarrollo desarrollo      │
│     gh pr create → Merge PR             │
│     (main está protegida)               │
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│  3. ALUMNOS ENTREGAN                    │
│     entregas/1.1_sqlite/apellido/       │
│     Pull Request → origin main          │
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│  4. TÚ REVISAS                          │
│     Opción A: GitHub Web (solo .md)     │
│     Opción B: Local (con código)        │
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│  5. APRUEBAS/RECHAZAS                   │
│     Comentas en PR                      │
│     Merge desde GitHub                  │
└─────────────────────────────────────────┘
```

---

**Repositorio**: https://github.com/TodoEconometria/ejercicios-bigdata
**Ejercicio**: 1.1 - Introducción a SQLite
**Creado**: Diciembre 2024
**Última actualización**: 2025-12-15

---

¡Éxito con las evaluaciones! 📚

💡 **CONSEJO:** Marca esta sección con un bookmark en tu editor para consultarla siempre que trabajes con Git.
