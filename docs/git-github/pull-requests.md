# Crear Pull Requests

Guia completa para entregar tus ejercicios al profesor mediante Pull Requests.

---

## Que es un Pull Request?

```
┌─────────────────────────────────────────────────────────────┐
│            QUE ES UN PULL REQUEST?                         │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Un Pull Request (PR) es como decir:                        │
│  "Profe, termine mi ejercicio. Puedes revisarlo?"          │
│                                                              │
│  ┌──────────────────────────────┐                          │
│  │  Tu Fork                      │                          │
│  │  (Ya tiene tu codigo listo)   │                          │
│  └──────────────────────────────┘                          │
│                  │                                           │
│                  │ Pull Request                             │
│                  │ (Solicitud de revision)                  │
│                  ↓                                           │
│  ┌──────────────────────────────┐                          │
│  │  Repo del Profesor            │                          │
│  │  (Espera para revisar)        │                          │
│  └──────────────────────────────┘                          │
│                  │                                           │
│                  ↓                                           │
│  👨‍🏫 Profesor revisa:                                        │
│     - Ve tu codigo linea por linea                          │
│     - Deja comentarios si hay que mejorar algo             │
│     - Aprueba cuando esta bien                              │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## Antes de Crear el Pull Request

### Checklist Pre-Entrega

Verifica que:

- [ ] El codigo ejecuta sin errores
- [ ] Todas las tareas del ejercicio estan completas
- [ ] El codigo esta documentado (comentarios, docstrings)
- [ ] Los commits tienen mensajes descriptivos
- [ ] El codigo sigue las mejores practicas de Python
- [ ] Probaste con el dataset completo
- [ ] Hiciste commit de todos los cambios
- [ ] Subiste tu rama a GitHub (`git push`)

---

## PASO 1: Verificar que tu Codigo Funciona

```bash
# Ejecuta tu ejercicio una ultima vez
python ejercicios/01_cargar_sqlite.py

# Funciona sin errores? ✅ Continua
# Tiene errores? 🐛 Corrigelos primero
```

---

## PASO 2: Asegurate de Haber Hecho Commit

```bash
# Ver si hay cambios sin guardar
git status

# Si hay cambios, guardalos:
git add .
git commit -m "Ejercicio 01 completado"
```

---

## PASO 3: Subir a GitHub

```bash
# Subir tu rama a GitHub
git push origin garcia-ejercicio-01
```

!!! info "Primera vez haciendo push?"
    Git te pedira autenticacion. Usa tu usuario y password de GitHub, o configura SSH keys.

---

## PASO 4: Ir a GitHub

Abre tu navegador y ve a tu fork:

```
https://github.com/TU_USUARIO/ejercicios-bigdata
```

---

## PASO 5: Crear el Pull Request

### Opcion A: Desde el Banner Amarillo

GitHub te mostrara un banner amarillo:

```
┌───────────────────────────────────────────────────┐
│  ⚠️ main had recent pushes                        │
│  [Compare & pull request]  ← CLICK AQUI          │
└───────────────────────────────────────────────────┘
```

Click en **"Compare & pull request"**

### Opcion B: Manual

Si no ves el banner:

1. Click en **"Pull requests"**
2. Click en **"New pull request"**
3. Click en **"compare across forks"**
4. Selecciona:
    - **Base repository:** `TodoEconometria/ejercicios-bigdata`
    - **Base branch:** `main`
    - **Head repository:** `TU_USUARIO/ejercicios-bigdata`
    - **Compare branch:** `garcia-ejercicio-01`

---

## PASO 6: Completar la Informacion del PR

### Plantilla Recomendada

```markdown
**Titulo:**
Ejercicio 01 - [Tu Nombre Completo]

**Descripcion:**

## ✅ Que hice
- Implemente la carga de datos desde CSV a SQLite usando chunks
- Agregue indices para optimizar las queries
- Complete el analisis de ingresos por hora del dia
- Exporte los resultados a CSV

## 🧪 Pruebas
- ✅ Funciona sin errores
- ✅ Probado con dataset completo (100,000 registros)
- ✅ Queries optimizadas con indices

## 💭 Preguntas (opcional)
- Hay una forma mas eficiente de hacer la carga por chunks?
- Los indices estan bien ubicados?

## 📊 Resultados
- Tiempo de carga: 15 segundos
- Tiempo de query: 0.5 segundos
- Tamano de BD: 25 MB
```

### Ejemplo Visual

!!! example "Ejemplo de PR Bien Documentado"

    **Titulo:** Ejercicio 01 - Juan Garcia

    **Descripcion:**

    ## ✅ Que hice

    Implemente la solucion completa del ejercicio 01 con las siguientes funcionalidades:

    1. **Carga de datos:** Leer CSV en chunks de 10,000 registros para evitar problemas de memoria
    2. **Base de datos:** Crear base SQLite con tabla `trips`
    3. **Indices:** Agregar indices en columnas `pickup_datetime` y `payment_type`
    4. **Analisis:** Queries para calcular:
        - Promedio de tarifas por hora
        - Distribucion de metodos de pago
        - Top 10 rutas mas frecuentes

    ## 🧪 Pruebas

    - ✅ Probado con dataset completo (100,000 registros)
    - ✅ Sin errores ni warnings
    - ✅ Tiempo de ejecucion: ~15 segundos
    - ✅ Resultados validados manualmente

    ## 📊 Resultados Clave

    - Hora mas rentable: 23:00 ($18.50 promedio)
    - Metodo de pago mas usado: Tarjeta de credito (67%)
    - Ruta mas frecuente: JFK → Manhattan

    ## 💭 Preguntas

    - Los indices mejoraron el rendimiento en ~40%. Hay otras optimizaciones que deberia considerar?

---

## PASO 7: Click "Create pull request"

Revisa una ultima vez y click en el boton verde **"Create pull request"**

:white_check_mark: **Pull Request Creado!**

El profesor recibira una notificacion y revisara tu trabajo.

---

## Que Pasa Despues?

### Escenario 1: El Profesor Pide Cambios

```
┌─────────────────────────────────────────┐
│  👨‍🏫 Profesor comenta:                   │
│  "En la linea 15, usa mejor metodo X"  │
└─────────────────────────────────────────┘
              ↓
    Tu corriges en tu PC
              ↓
    git commit -m "Correcciones"
    git push origin tu-rama
              ↓
    El PR se actualiza automaticamente ✨
              ↓
    Profesor revisa de nuevo
```

### Como Aplicar Correcciones

```bash
# 1. Asegurate de estar en tu rama
git checkout garcia-ejercicio-01

# 2. Edita el codigo segun el feedback

# 3. Guarda los cambios
git add .
git commit -m "Aplicar feedback: optimizar carga de datos"

# 4. Sube los cambios
git push origin garcia-ejercicio-01
```

!!! tip "El PR se actualiza solo"
    Cuando haces push a la misma rama, el Pull Request se actualiza automaticamente. NO necesitas crear un nuevo PR.

### Escenario 2: El Profesor Aprueba

```
┌─────────────────────────────────────────┐
│  ✅ Ejercicio aprobado                   │
│  🎉 Felicitaciones!                     │
└─────────────────────────────────────────┘
```

- :white_check_mark: Veras un check verde en el PR
- :white_check_mark: El profesor puede hacer merge (o tu, si te da permisos)
- :white_check_mark: Ejercicio completado!

---

## Anatomia de un Buen Pull Request

### Titulo Claro

```
✅ BIEN:
"Ejercicio 01 - Juan Garcia"
"Ejercicio 03: Procesamiento con Dask - Maria Lopez"

❌ MAL:
"Update"
"Ejercicio"
"Cambios"
```

### Descripcion Completa

!!! success "Buena Descripcion"

    - Explica QUE hiciste
    - Menciona COMO lo hiciste
    - Lista pruebas realizadas
    - Comparte resultados relevantes
    - Haz preguntas si tienes dudas

!!! failure "Mala Descripcion"

    - "Hice el ejercicio"
    - "Listo"
    - (vacio)

### Commits Limpios

```bash
# ✅ BIEN - Commits especificos
git commit -m "Agregar funcion de carga de datos"
git commit -m "Implementar creacion de indices"
git commit -m "Agregar queries de analisis"

# ❌ MAL - Commits poco descriptivos
git commit -m "update"
git commit -m "fix"
git commit -m "changes"
```

---

## Interaccion con el Profesor

### Como Responder a Comentarios

Cuando el profesor deje comentarios en tu codigo:

1. **Lee cuidadosamente** el comentario
2. **Haz las correcciones** sugeridas
3. **Commit y push** los cambios
4. **Responde al comentario** explicando que hiciste

!!! example "Ejemplo de Respuesta"

    **Profesor:**
    > En la linea 15, seria mejor usar `pd.read_csv()` con el parametro `dtype` para optimizar memoria.

    **Tu respuesta:**
    > Gracias! Aplique el cambio. Ahora especifico los tipos de datos en `dtype={'passenger_count': 'int8', 'trip_distance': 'float32'}`. Redujo el uso de memoria en un 30%.
    >
    > Commit: abc123d

### Etiquetar al Profesor

Si tienes una pregunta urgente, puedes mencionar al profesor:

```markdown
@TodoEconometria tengo una duda sobre la linea 25...
```

---

## Buenas Practicas

### 1. Un PR por Ejercicio

```
✅ BIEN:
- PR #1: Ejercicio 01
- PR #2: Ejercicio 02
- PR #3: Ejercicio 03

❌ MAL:
- PR #1: Ejercicios 01, 02, 03, 04 (todo junto)
```

### 2. Mantener el PR Actualizado

Si el profesor agrega cambios al repo principal mientras tu PR esta abierto:

```bash
# Actualizar tu rama
git checkout main
git pull upstream main
git checkout garcia-ejercicio-01
git merge main
git push origin garcia-ejercicio-01
```

### 3. No Hacer Force Push

```bash
# ❌ MAL - Nunca hagas esto en un PR abierto
git push --force origin garcia-ejercicio-01

# ✅ BIEN - Push normal
git push origin garcia-ejercicio-01
```

!!! danger "Evita Force Push"
    `git push --force` reescribe el historial y puede causar problemas en PRs abiertos.

---

## Plantillas de PR

### Para Ejercicios Basicos

```markdown
## ✅ Tareas Completadas
- [ ] Tarea 1: Descripcion
- [ ] Tarea 2: Descripcion
- [ ] Tarea 3: Descripcion

## 🧪 Pruebas
- [ ] Funciona sin errores
- [ ] Probado con dataset completo
- [ ] Validado manualmente

## 💭 Notas
Alguna nota o comentario adicional
```

### Para Proyectos Avanzados

```markdown
## 📋 Resumen
Breve descripcion del proyecto/ejercicio

## 🚀 Funcionalidades
- Funcionalidad 1
- Funcionalidad 2
- Funcionalidad 3

## 🏗️ Arquitectura
Descripcion de la arquitectura implementada

## 🧪 Testing
- Tipos de pruebas realizadas
- Coverage
- Resultados

## 📊 Metricas
- Rendimiento
- Uso de memoria
- Tiempo de ejecucion

## 📸 Screenshots (si aplica)
![descripcion](url-imagen)

## 💭 Preguntas/Dudas
Lista de preguntas para el revisor
```

---

## Problemas Comunes

??? question "No puedo crear el PR: 'There isn't anything to compare'"

    **Causa:** No hay diferencias entre tu rama y la rama base.

    **Solucion:**

    - Verifica que hiciste commit de tus cambios
    - Asegurate de haber hecho push: `git push origin tu-rama`
    - Verifica que estas comparando las ramas correctas

??? question "El PR muestra archivos que no modifique"

    **Causa:** Tu rama no esta actualizada con main.

    **Solucion:**

    ```bash
    git checkout main
    git pull upstream main
    git checkout tu-rama
    git merge main
    git push origin tu-rama
    ```

??? question "Quiero cambiar el titulo/descripcion del PR"

    **Solucion:** Puedes editarlos en cualquier momento:

    1. Ve a tu PR en GitHub
    2. Click en "Edit" junto al titulo
    3. O edita la descripcion directamente

---

## Proximos Pasos

Despues de crear tu PR:

- [Sincronizar Fork](sincronizar-fork.md) - Si el profesor agrega ejercicios nuevos
- [Comandos Utiles](comandos-utiles.md) - Cheatsheet de Git
- [Tu Primer Ejercicio](../guia-inicio/primer-ejercicio.md) - Para repasar el flujo completo
