# Guía Completa de Desarrollo de Ejercicios
## Manual de Flujo de Trabajo Autónomo

**Última actualización:** 2025-12-10
**Versión:** 1.0
**Autor:** Profesor

---

## 📋 TABLA DE CONTENIDOS

1. [Filosofía del Sistema](#filosofía-del-sistema)
2. [Arquitectura del Repositorio](#arquitectura-del-repositorio)
3. [Checklist de Inicio de Sesión](#checklist-de-inicio-de-sesión)
4. [Flujos de Trabajo Completos](#flujos-de-trabajo-completos)
5. [Crear un Nuevo Ejercicio](#crear-un-nuevo-ejercicio)
6. [Sincronización entre Ordenadores](#sincronización-entre-ordenadores)
7. [Publicar Ejercicio a Alumnos](#publicar-ejercicio-a-alumnos)
8. [Revisar PRs de Alumnos](#revisar-prs-de-alumnos)
9. [Solución de Problemas](#solución-de-problemas)
10. [Referencias y Recursos](#referencias-y-recursos)

---

## 🎯 FILOSOFÍA DEL SISTEMA

### Principios Fundamentales

```
┌─────────────────────────────────────────────────────────┐
│  REGLA DE ORO: NUNCA SUBIR A GITHUB SIN ORDEN EXPLÍCITA │
└─────────────────────────────────────────────────────────┘

Workflow:
1. Trabajar localmente en .profesor/
2. Commitear cambios (solo local o repo privado)
3. Revisar y validar TODO
4. Solo cuando des la orden: publicar a GitHub público
```

### Separación de Responsabilidades

```
┌──────────────────────────────────────────────────────────┐
│                   ARQUITECTURA DEL SISTEMA               │
├──────────────────────────────────────────────────────────┤
│                                                          │
│  GitHub PÚBLICO (origin/main)                            │
│  ├─ Esqueleto limpio para alumnos                        │
│  ├─ Solo ejercicios base (plantillas vacías)             │
│  └─ Sin soluciones, sin archivos privados                │
│                                                          │
│  GitHub PRIVADO (desarrollo/desarrollo)                  │
│  ├─ Todo el contenido del público +                      │
│  ├─ .profesor/ (carpeta completa privada)                │
│  ├─ Ejercicios en desarrollo                             │
│  ├─ Soluciones completas                                 │
│  └─ Materiales del profesor                              │
│                                                          │
│  Repositorio LOCAL                                       │
│  ├─ Branch 'main' → sincroniza con público               │
│  ├─ Branch 'desarrollo' → sincroniza con privado         │
│  └─ Siempre trabajar en 'desarrollo'                     │
│                                                          │
└──────────────────────────────────────────────────────────┘
```

---

## 🏗️ ARQUITECTURA DEL REPOSITORIO

### Estructura Completa

```
ejercicios-bigdata/
│
├── .profesor/                          # 🔒 CARPETA PRIVADA (ignorada en público)
│   ├── README.md                       # Este archivo
│   ├── ejercicios_en_desarrollo/       # Ejercicios en construcción
│   │   ├── README.md                   # Este archivo que estás leyendo
│   │   ├── 01_tienda_informatica/      # Ejercicio 01 completo
│   │   │   ├── ENUNCIADO.md           # ✅ Público (para alumnos)
│   │   │   ├── AYUDA.md               # ✅ Público (pistas)
│   │   │   ├── README.md              # ✅ Público (instrucciones)
│   │   │   ├── plantilla_base.py      # ✅ Público (código inicial)
│   │   │   ├── INSTRUCCIONES_PROFESOR.md  # 🔒 PRIVADO (solo tú)
│   │   │   ├── ISSUE_TEMPLATE.md      # 🔒 PRIVADO (plantilla issues)
│   │   │   ├── datos/                 # Datos del ejercicio
│   │   │   │   ├── .gitkeep          # ✅ Público
│   │   │   │   └── csv_tienda_informatica.zip  # 🔒 PRIVADO (datos)
│   │   │   └── soluciones_ejemplo/    # 🔒 PRIVADO (soluciones)
│   │   │       ├── solucion_01.py
│   │   │       └── solucion_02.py
│   │   ├── 02_[nombre_ejercicio]/     # Siguiente ejercicio...
│   │   └── ...
│   ├── evaluaciones/                   # Rúbricas y criterios
│   ├── notas/                          # Notas personales
│   └── recursos/                       # Materiales adicionales
│
├── ejercicios/                         # 📂 Ejercicios públicos (esqueleto)
│   ├── 01_cargar_sqlite.py
│   ├── 02_limpieza_datos.py
│   ├── 03_parquet_dask.py
│   └── 04_pyspark_query.py
│
├── datos/                              # 📊 Datasets públicos
├── dashboards/                         # 📈 Dashboards de ejemplo
├── docs/                               # 📚 Documentación
├── sync.py                             # 🔄 Script de sincronización
└── .gitignore                          # 🚫 Ignora .profesor/ en público

```

### Archivos Ignorados (.gitignore)

El `.gitignore` en la raíz protege:
```
.profesor/          # Toda la carpeta privada
scripts/            # Scripts del profesor
*.profesor.md       # Archivos con extensión .profesor.md
evaluaciones/       # Carpeta de evaluaciones
```

Cada ejercicio tiene su propio `.gitignore` dentro de `01_tienda_informatica/`:
```
INSTRUCCIONES_PROFESOR.md
ISSUE_TEMPLATE.md
*.zip
datos/*.csv
soluciones/
```

---

## ✅ CHECKLIST DE INICIO DE SESIÓN

### Cada vez que inicies a trabajar, ejecuta esto:

```bash
# ════════════════════════════════════════════════════════
# CHECKLIST DE INICIO - EJECUTAR SIEMPRE
# ════════════════════════════════════════════════════════

# 1. Ir al directorio del proyecto (la que pertenezca obvio)
cd C:/Users/jmarc/PycharmProjects/ejercicios-bigdata

# 2. Verificar en qué branch estás
git branch
# Debe mostrar: * desarrollo

# 3. Si NO estás en 'desarrollo', cambia:
git checkout desarrollo

# 4. Ver estado del repositorio
git status
# Debe mostrar: working tree clean

# 5. (OPCIONAL) Si vienes del otro ordenador, sincroniza:
python sync.py pull

# 6. Verificar que tienes los archivos del profesor
ls -la .profesor/

# ════════════════════════════════════════════════════════
# LISTO - Ahora puedes trabajar
# ════════════════════════════════════════════════════════
```

### Script de Inicio Automático (opcional)

Crea un archivo `inicio.sh` o `inicio.bat`:

```bash
#!/bin/bash
# inicio.sh - Script de inicio automático

echo "═══════════════════════════════════════════════"
echo "  Inicializando entorno de desarrollo"
echo "═══════════════════════════════════════════════"

cd C:/Users/jmarc/PycharmProjects/ejercicios-bigdata

echo ""
echo "✓ Directorio: $(pwd)"

echo ""
echo "Branch actual:"
git branch | grep '*'

echo ""
echo "Estado del repositorio:"
git status -s

echo ""
echo "Archivos en .profesor/:"
ls -la .profesor/ | head -10

echo ""
echo "═══════════════════════════════════════════════"
echo "  ✓ Sistema listo para trabajar"
echo "═══════════════════════════════════════════════"
```

---

## 🔄 FLUJOS DE TRABAJO COMPLETOS

### FLUJO 1: Desarrollar un Ejercicio Nuevo

```
┌─────────────────────────────────────────────────────┐
│  FLUJO: Crear y Desarrollar un Ejercicio Nuevo      │
└─────────────────────────────────────────────────────┘

Paso 1: DISEÑO Y PLANIFICACIÓN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
□ Definir objetivo del ejercicio
□ Elegir datasets necesarios
□ Diseñar enunciado y pistas
□ Planificar estructura de archivos

Paso 2: CREAR ESTRUCTURA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
$ cd .profesor/ejercicios_en_desarrollo/
$ mkdir 0X_nombre_ejercicio
$ cd 0X_nombre_ejercicio/

Paso 3: CREAR ARCHIVOS BASE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
$ touch ENUNCIADO.md              # Público
$ touch AYUDA.md                  # Público
$ touch README.md                 # Público
$ touch plantilla_base.py         # Público
$ touch INSTRUCCIONES_PROFESOR.md # Privado
$ touch ISSUE_TEMPLATE.md         # Privado
$ touch .gitignore                # Configuración

Paso 4: ESCRIBIR CONTENIDO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
□ ENUNCIADO.md → Descripción completa del problema
□ AYUDA.md → Pistas y consejos para alumnos
□ README.md → Instrucciones de configuración
□ plantilla_base.py → Código inicial con TODOs
□ INSTRUCCIONES_PROFESOR.md → Solución completa, rúbrica
□ ISSUE_TEMPLATE.md → Template para que alumnos reporten

Paso 5: AGREGAR DATOS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
$ mkdir datos
$ cp /ruta/a/datos.csv datos/
$ echo "*.csv" >> .gitignore       # Ignorar CSVs grandes
$ echo "datos/*.csv" >> .gitignore

Paso 6: CREAR SOLUCIONES DE EJEMPLO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
$ mkdir soluciones_ejemplo
$ touch soluciones_ejemplo/solucion_completa.py
$ echo "soluciones_ejemplo/" >> .gitignore

Paso 7: COMMITEAR LOCALMENTE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
$ cd ../../..  # Volver a raíz del repo
$ git status
$ git add .profesor/ejercicios_en_desarrollo/0X_nombre_ejercicio/
$ git commit -m "WIP: Ejercicio 0X - [nombre] - Estructura inicial"

Paso 8: DESARROLLO ITERATIVO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Mientras desarrollas]
□ Editar archivos
□ Probar soluciones
□ Refinar enunciado
□ Commitear frecuentemente:
  $ git add .profesor/ejercicios_en_desarrollo/0X_*/
  $ git commit -m "WIP: Ejercicio 0X - [cambio específico]"

Paso 9: SINCRONIZAR (si usas múltiples ordenadores)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
$ python sync.py push

Paso 10: REVISIÓN FINAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
□ Verificar ortografía y formato
□ Probar plantilla_base.py
□ Probar solución completa
□ Verificar .gitignore
□ Commitear versión final:
  $ git commit -m "FEAT: Ejercicio 0X - [nombre] - Listo para publicar"

Paso 11: ESPERAR ORDEN DE PUBLICACIÓN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️  NO PUBLICAR TODAVÍA
    Esperar instrucción explícita del profesor
    Solo entonces ejecutar FLUJO 2 (Publicar)
```

---

### FLUJO 2: Publicar Ejercicio a GitHub Público

```
┌─────────────────────────────────────────────────────┐
│  FLUJO: Publicar Ejercicio al Repositorio Público   │
└─────────────────────────────────────────────────────┘

⚠️  SOLO EJECUTAR CUANDO DÉS LA ORDEN EXPLÍCITA

Paso 1: VERIFICACIÓN PRE-PUBLICACIÓN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
□ Ejercicio está completo y revisado
□ Archivos privados están en .gitignore
□ No hay soluciones en archivos públicos
□ Datos sensibles están protegidos

Paso 2: PREPARAR VERSIÓN PÚBLICA
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
$ git checkout main  # Cambiar a branch público

Paso 3: COPIAR SOLO ARCHIVOS PÚBLICOS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Crear carpeta del ejercicio en público
$ mkdir -p ejercicios/0X_nombre_ejercicio/

# Copiar SOLO archivos públicos:
$ cp .profesor/ejercicios_en_desarrollo/0X_*/ENUNCIADO.md \
     ejercicios/0X_nombre_ejercicio/
$ cp .profesor/ejercicios_en_desarrollo/0X_*/AYUDA.md \
     ejercicios/0X_nombre_ejercicio/
$ cp .profesor/ejercicios_en_desarrollo/0X_*/README.md \
     ejercicios/0X_nombre_ejercicio/
$ cp .profesor/ejercicios_en_desarrollo/0X_*/plantilla_base.py \
     ejercicios/0X_nombre_ejercicio/
$ cp .profesor/ejercicios_en_desarrollo/0X_*/.gitignore \
     ejercicios/0X_nombre_ejercicio/

# Copiar estructura de datos (sin archivos)
$ mkdir -p ejercicios/0X_nombre_ejercicio/datos/
$ touch ejercicios/0X_nombre_ejercicio/datos/.gitkeep

Paso 4: VERIFICAR QUE NO HAY ARCHIVOS PRIVADOS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
$ cd ejercicios/0X_nombre_ejercicio/
$ ls -la
# NO debe haber:
#   - INSTRUCCIONES_PROFESOR.md
#   - ISSUE_TEMPLATE.md
#   - soluciones_ejemplo/
#   - datos/*.csv

Paso 5: COMMITEAR EN MAIN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
$ cd ../..  # Volver a raíz
$ git add ejercicios/0X_nombre_ejercicio/
$ git commit -m "FEAT: Agregar Ejercicio 0X - [nombre]"

Paso 6: ÚLTIMA VERIFICACIÓN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
$ git log --oneline -3
$ git diff HEAD~1

⚠️  REVISAR CUIDADOSAMENTE EL DIFF
    Asegurar que NO hay archivos privados

Paso 7: PUBLICAR A GITHUB PÚBLICO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
$ git push origin main

Paso 8: VOLVER A DESARROLLO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
$ git checkout desarrollo

Paso 9: SINCRONIZAR CAMBIOS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
$ git merge main  # Integrar cambios de main
$ python sync.py push  # Subir a repo privado

Paso 10: VERIFICACIÓN POST-PUBLICACIÓN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
□ Ir a GitHub y verificar que solo hay archivos públicos
□ Verificar que los alumnos pueden hacer fork
□ Probar que la plantilla_base.py funciona
```

---

### FLUJO 3: Sincronización entre Ordenadores

```
┌─────────────────────────────────────────────────────┐
│  FLUJO: Sincronizar Trabajo entre Ordenadores       │
└─────────────────────────────────────────────────────┘

ESCENARIO A: Trabajar en Ordenador Principal → Portátil
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[En Ordenador Principal - ANTES de salir]
$ git checkout desarrollo
$ git status  # Verificar cambios
$ git add .
$ git commit -m "Cambios [descripción] - Antes de salir"
$ python sync.py push

[En Portátil - AL LLEGAR]
$ git checkout desarrollo
$ python sync.py pull
$ git log --oneline -5  # Verificar que tienes los últimos cambios

[En Portátil - Trabajar...]
$ # Hacer cambios...
$ git add .
$ git commit -m "Cambios desde portátil"
$ python sync.py push

[En Ordenador Principal - AL LLEGAR A CASA]
$ git checkout desarrollo
$ python sync.py pull


ESCENARIO B: Conflictos de Sincronización
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Si python sync.py pull da error:

$ python sync.py pull
# ERROR: merge conflict...

Solución:
1. Ver archivos en conflicto:
   $ git status

2. Abrir archivos con marcadores <<<<<<< ======= >>>>>>>

3. Resolver conflictos manualmente
   (elige qué versión mantener)

4. Commitear resolución:
   $ git add .
   $ git commit -m "Resolver conflictos de sincronización"
   $ python sync.py push
```

---

### FLUJO 4: Revisar PRs de Alumnos

```
┌─────────────────────────────────────────────────────┐
│  FLUJO: Revisar Pull Requests de Alumnos            │
└─────────────────────────────────────────────────────┘

Paso 1: RECIBIR NOTIFICACIÓN DE PR
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
□ Alumno hace PR desde su fork
□ Recibes notificación por email/GitHub

Paso 2: REVISAR PR EN GITHUB
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
$ # Ir a: https://github.com/TodoEconometria/ejercicios-bigdata/pulls
□ Ver cambios del alumno
□ Leer descripción del PR
□ Verificar archivos modificados

Paso 3: DESCARGAR SOLUCIÓN DEL ALUMNO (opcional)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
$ # Fetch del PR
$ gh pr checkout [número_PR]
$ # O manualmente:
$ git fetch origin pull/[número]/head:pr-[número]
$ git checkout pr-[número]

Paso 4: EJECUTAR Y PROBAR SOLUCIÓN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
$ cd ejercicios/0X_nombre_ejercicio/
$ python solucion_alumno.py
□ Verificar que funciona
□ Comparar con solución esperada
□ Verificar buenas prácticas

Paso 5: COMPARAR CON SOLUCIÓN OFICIAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
$ cd ../../.profesor/ejercicios_en_desarrollo/0X_*/
$ cat INSTRUCCIONES_PROFESOR.md  # Ver rúbrica
$ cat soluciones_ejemplo/solucion_completa.py
□ Comparar enfoques
□ Evaluar según rúbrica

Paso 6: DAR FEEDBACK EN GITHUB
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
□ Agregar comentarios en líneas específicas
□ Sugerir mejoras
□ Aprobar o solicitar cambios

Paso 7: VOLVER A DESARROLLO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
$ git checkout desarrollo
```

---

## 📝 CREAR UN NUEVO EJERCICIO - TEMPLATE

### Template de Estructura de Carpetas

```bash
# Ejecuta esto para crear estructura automática:

NOMBRE_EJERCICIO="02_nombre_ejercicio"
cd .profesor/ejercicios_en_desarrollo/

mkdir -p "$NOMBRE_EJERCICIO"/{datos,soluciones_ejemplo}
cd "$NOMBRE_EJERCICIO"

# Crear archivos públicos
cat > ENUNCIADO.md << 'EOF'
# Ejercicio XX: [Nombre del Ejercicio]

## Objetivo
[Describe el objetivo de aprendizaje]

## Contexto
[Explica el contexto del problema]

## Tareas
1. [ ] Tarea 1
2. [ ] Tarea 2
3. [ ] Tarea 3

## Datos
Los datos están en `datos/[nombre].csv`

## Entrega
Completa el archivo `solucion.py`
EOF

cat > AYUDA.md << 'EOF'
# Pistas y Ayuda

## Pista 1: [Tema]
[Explicación]

## Pista 2: [Tema]
[Explicación]

## Recursos Útiles
- [Enlace a documentación]
- [Tutorial relevante]
EOF

cat > README.md << 'EOF'
# Ejercicio XX: [Nombre]

## Instrucciones de Configuración

### Requisitos
```bash
pip install pandas numpy
```

### Estructura de Archivos
```
XX_nombre_ejercicio/
├── ENUNCIADO.md
├── AYUDA.md
├── plantilla_base.py
└── datos/
```

### Cómo Empezar
1. Lee ENUNCIADO.md
2. Abre plantilla_base.py
3. Completa los TODOs
EOF

cat > plantilla_base.py << 'EOF'
"""
Ejercicio XX: [Nombre del Ejercicio]
Alumno: [TU NOMBRE]
Fecha: [FECHA]
"""

import pandas as pd
import numpy as np

# TODO 1: [Descripción de qué hacer]


# TODO 2: [Descripción de qué hacer]


if __name__ == "__main__":
    print("Ejercicio XX: [Nombre]")
    # TODO: Implementar lógica principal
EOF

# Crear archivos privados
cat > INSTRUCCIONES_PROFESOR.md << 'EOF'
# INSTRUCCIONES PARA EL PROFESOR

## Objetivo Pedagógico
[Qué deben aprender los alumnos]

## Solución Esperada
[Descripción de la solución]

## Rúbrica de Evaluación

| Criterio | Puntos | Descripción |
|----------|--------|-------------|
| Funcionalidad correcta | 40 | Código ejecuta sin errores |
| Buenas prácticas | 30 | Código limpio, comentado |
| Eficiencia | 20 | Uso adecuado de estructuras |
| Documentación | 10 | README y comentarios |

## Errores Comunes
1. [Error común 1]
2. [Error común 2]

## Conceptos Clave
- [Concepto 1]
- [Concepto 2]
EOF

cat > ISSUE_TEMPLATE.md << 'EOF'
## Descripción del Problema
[Descripción clara del problema]

## Código que Produce el Error
```python
[código aquí]
```

## Mensaje de Error
```
[mensaje de error aquí]
```

## Lo que Ya Intenté
- [ ] [Cosa 1]
- [ ] [Cosa 2]

## Pregunta Específica
[Tu pregunta]
EOF

cat > .gitignore << 'EOF'
# Archivos privados del profesor
INSTRUCCIONES_PROFESOR.md
ISSUE_TEMPLATE.md

# Datos grandes
*.csv
*.zip
datos/*.csv

# Soluciones
soluciones_ejemplo/

# Python
__pycache__/
*.pyc
EOF

touch datos/.gitkeep

echo "✓ Estructura del ejercicio $NOMBRE_EJERCICIO creada"
```

---

## 🔧 COMANDOS ÚTILES

### Git Quick Reference

```bash
# Ver estado
git status
git log --oneline -10
git branch -a

# Cambiar de branch
git checkout desarrollo
git checkout main

# Commits
git add .
git add .profesor/
git commit -m "Mensaje descriptivo"

# Sincronización
python sync.py status
python sync.py pull
python sync.py push

# Ver diferencias
git diff
git diff HEAD~1
git diff main desarrollo

# Deshacer cambios (¡cuidado!)
git restore [archivo]         # Deshacer cambios no commiteados
git reset HEAD~1               # Deshacer último commit (mantiene cambios)
git reset --hard HEAD~1        # Deshacer último commit (BORRA cambios)
```

### Verificación de Seguridad

```bash
# Verificar qué archivos subirías a GitHub
git diff --name-only main

# Verificar que .profesor/ está ignorado
git check-ignore .profesor/
# Debe devolver: .profesor/

# Ver archivos rastreados en un commit
git ls-tree -r HEAD --name-only | grep profesor
# NO debe devolver nada (en branch main)

# Ver archivos rastreados en desarrollo
git checkout desarrollo
git ls-tree -r HEAD --name-only | grep profesor
# Debe mostrar archivos de .profesor/
```

---

## 🆘 SOLUCIÓN DE PROBLEMAS

### Problema 1: Estoy en el branch equivocado

```bash
# Síntoma: Ves que estás en 'main' cuando deberías estar en 'desarrollo'
git branch  # Muestra: * main

# Solución:
git checkout desarrollo
```

### Problema 2: Subí archivos privados a GitHub público por error

```bash
# ⚠️  ACCIÓN INMEDIATA

# 1. Verificar qué se subió
git log --oneline -1
git diff HEAD~1 --name-only

# 2. Si contiene archivos privados, revertir INMEDIATAMENTE
git reset --hard HEAD~1  # Deshace el commit
git push --force origin main  # Fuerza el push (PELIGROSO)

# 3. Avisar a alumnos (si ya vieron los cambios)
```

### Problema 3: Conflictos de merge al sincronizar

```bash
# Síntoma: python sync.py pull da error

# Solución:
git status  # Ver archivos en conflicto

# Abrir archivos con conflictos, buscar:
<<<<<<< HEAD
[Tu versión]
=======
[Versión del otro ordenador]
>>>>>>> rama

# Editar manualmente, elegir qué mantener
# Luego:
git add [archivo_resuelto]
git commit -m "Resolver conflicto"
python sync.py push
```

### Problema 4: No encuentro mis cambios

```bash
# Verificar en qué branch estás
git branch
# Si estás en 'main', tus cambios están en 'desarrollo'

git checkout desarrollo
git log --oneline -10  # Ver últimos commits
```

---

## 📚 REFERENCIAS Y RECURSOS

### Documentación Interna

```
.profesor/
├── README.md                      # Información general
├── ejercicios_en_desarrollo/
│   └── README.md                  # Este archivo (flujos de trabajo)
├── evaluaciones/
│   └── rubricas_generales.md     # Rúbricas
└── recursos/
    ├── plantillas/               # Templates reutilizables
    └── guias/                    # Guías adicionales
```

### Comandos Rápidos de Referencia

```bash
# Alias útiles (agregar a ~/.bashrc o ~/.zshrc)
alias gst='git status'
alias gco='git checkout'
alias gcm='git commit -m'
alias gp='python sync.py push'
alias gl='python sync.py pull'
alias gdev='git checkout desarrollo'
```

### Checklist de Calidad para Ejercicios

```
□ ENUNCIADO.md está claro y sin ambigüedades
□ AYUDA.md tiene al menos 3 pistas útiles
□ README.md tiene instrucciones de setup
□ plantilla_base.py tiene TODOs claros
□ INSTRUCCIONES_PROFESOR.md tiene solución completa
□ INSTRUCCIONES_PROFESOR.md tiene rúbrica detallada
□ .gitignore protege archivos privados
□ Datos están en carpeta datos/
□ Soluciones están en soluciones_ejemplo/
□ Ejercicio fue probado de principio a fin
```

---

## 🎓 ENSEÑAR A LOS ALUMNOS

### Template de Guía para Alumnos

Crear en el repositorio público: `docs/COMO_TRABAJAR_EJERCICIOS.md`

```markdown
# Cómo Trabajar con los Ejercicios

## 1. Hacer Fork del Repositorio
1. Ir a https://github.com/TodoEconometria/ejercicios-bigdata
2. Click en "Fork"
3. Crear fork en tu cuenta

## 2. Clonar tu Fork
```bash
git clone https://github.com/TU_USUARIO/ejercicios-bigdata.git
cd ejercicios-bigdata
```

## 3. Trabajar en un Ejercicio
```bash
cd ejercicios/01_nombre_ejercicio/
# Leer ENUNCIADO.md
# Leer AYUDA.md si necesitas pistas
# Editar plantilla_base.py
```

## 4. Hacer Commits
```bash
git add .
git commit -m "Ejercicio 01: [descripción de cambios]"
git push origin main
```

## 5. Crear Pull Request
1. Ir a tu fork en GitHub
2. Click en "Pull Request"
3. Seleccionar base: TodoEconometria/main
4. Completar descripción del PR
5. Submit
```

---

## 🏗️ ARQUITECTURA Y MEJORES PRÁCTICAS

### SpecDriven Development

**¿Qué es SpecDriven (Specification-Driven Development)?**

Es un enfoque donde defines **especificaciones formales ANTES de implementar**.

```
┌──────────────────────────────────────────────────┐
│         SPEC-DRIVEN DEVELOPMENT WORKFLOW         │
├──────────────────────────────────────────────────┤
│                                                   │
│  1. ESPECIFICAR                                   │
│     ├─ Definir estructura del repositorio        │
│     ├─ Definir workflows                         │
│     ├─ Definir políticas (público vs privado)    │
│     └─ Crear templates y scripts                 │
│                                                   │
│  2. DISEÑAR                                       │
│     ├─ Esquemas de carpetas                      │
│     ├─ .gitignore                                │
│     └─ Scripts de sincronización                 │
│                                                   │
│  3. DOCUMENTAR                                    │
│     ├─ README exhaustivo                         │
│     ├─ Flujos de trabajo                         │
│     └─ Checklists                                │
│                                                   │
│  4. IMPLEMENTAR                                   │
│     └─ Seguir las especificaciones al pie        │
│                                                   │
│  5. VALIDAR                                       │
│     └─ Probar que cumple las especificaciones    │
│                                                   │
└──────────────────────────────────────────────────┘
```

### Especificaciones que Hubieran Ahorrado Tiempo

#### SPEC 1: Estructura del Repositorio

```yaml
# .repo-spec.yml
repository:
  name: ejercicios-bigdata
  visibility: public

  remotes:
    origin:
      url: https://github.com/TodoEconometria/ejercicios-bigdata.git
      purpose: "Repositorio público para alumnos"

    desarrollo:
      url: https://github.com/TodoEconometria/ejercicios-bigdata-profesor.git
      visibility: private
      purpose: "Repositorio privado para desarrollo del profesor"

  branches:
    main:
      remote: origin
      content: "Esqueleto limpio (sin .profesor/)"

    desarrollo:
      remote: desarrollo
      content: "Todo (con .profesor/)"

  directories:
    .profesor:
      visibility: private
      ignored_in: [origin]
      synced_to: [desarrollo]

    ejercicios:
      visibility: public
      synced_to: [origin, desarrollo]
```

#### SPEC 2: Política de Archivos

```yaml
# .file-policy.yml
files:
  public:  # Van al repositorio público
    - ENUNCIADO.md
    - AYUDA.md
    - README.md
    - plantilla_base.py
    - datos/.gitkeep

  private:  # Solo en repositorio privado
    - INSTRUCCIONES_PROFESOR.md
    - ISSUE_TEMPLATE.md
    - soluciones_ejemplo/*
    - datos/*.csv
    - datos/*.zip
```

#### SPEC 3: Workflow de Publicación

```yaml
# .workflows/publicar-ejercicio.yml
workflow:
  name: "Publicar Ejercicio"
  trigger: manual  # Solo cuando profesor da orden

  steps:
    - validate:
        - ejercicio_completo: true
        - archivos_privados_protegidos: true
        - tests_passed: true

    - prepare:
        - checkout: main
        - copy_public_files_only: true

    - verify:
        - no_private_files: true
        - gitignore_correct: true

    - publish:
        - commit: true
        - push: origin/main

    - sync:
        - merge_to: desarrollo
        - push: desarrollo/desarrollo
```

### Herramientas SpecDriven para el Futuro

```bash
# Validar que el repositorio cumple la especificación
$ validate-repo-spec .repo-spec.yml

# Generar estructura automáticamente desde spec
$ generate-from-spec .repo-spec.yml

# Verificar políticas antes de commit
$ pre-commit-check --policy .file-policy.yml

# Ejecutar workflow de publicación
$ run-workflow .workflows/publicar-ejercicio.yml
```

---

## 🔄 INTEGRACIÓN CON MÓDULO DE CONTEXTO

### Placeholder para Módulo Portable

```
┌──────────────────────────────────────────────────┐
│  MÓDULO DE CONTEXTO PORTABLE (desde casa)        │
├──────────────────────────────────────────────────┤
│                                                   │
│  [PENDIENTE: Integrar cuando traigas de casa]   │
│                                                   │
│  Funcionalidad esperada:                         │
│  - Generar memoria de contexto                   │
│  - Mantener estado entre sesiones                │
│  - Facilitar trabajo autónomo                    │
│                                                   │
└──────────────────────────────────────────────────┘

Instrucciones de integración:
1. Copiar módulo a .profesor/tools/
2. Actualizar esta sección con documentación
3. Crear scripts de integración
```

---

## ✅ CHECKLIST FINAL ANTES DE CERRAR SESIÓN

```bash
# ════════════════════════════════════════════════════════
# CHECKLIST DE CIERRE - EJECUTAR SIEMPRE ANTES DE SALIR
# ════════════════════════════════════════════════════════

□ 1. Ver estado actual
     $ git status

□ 2. Si hay cambios sin commitear:
     $ git add .
     $ git commit -m "Cambios del [fecha] - [descripción]"

□ 3. Sincronizar si usas múltiples ordenadores:
     $ python sync.py push

□ 4. Verificar que se subió:
     $ python sync.py status

□ 5. Verificar branch correcto (desarrollo):
     $ git branch
     # Debe mostrar: * desarrollo

□ 6. Log de últimos cambios:
     $ git log --oneline -3

# ════════════════════════════════════════════════════════
# LISTO - Puedes cerrar el ordenador
# ════════════════════════════════════════════════════════
```

---

**FIN DEL MANUAL - Versión 1.0**

**Próximas actualizaciones:**
- Integración módulo de contexto portable
- Scripts de automatización adicionales
- Templates para más tipos de ejercicios
