# 📤 Instrucciones de Entrega - Ejercicio 1.1

**Ejercicio:** 1.1 - Introducción a SQLite - Análisis Exploratorio
**Puntos:** 100 pts
**Tipo de entrega:** Documentos Markdown (.md)

---

## 🎯 ¿Qué debes entregar?

Debes crear **3 archivos Markdown** con tu análisis:

1. **`ANALISIS_DATOS.md`** - Tus hallazgos del análisis exploratorio
2. **`resumen_eda.md`** - Resumen ejecutivo del análisis
3. **`REFLEXION.md`** - Respuestas a preguntas de reflexión

---

## 📁 ¿Dónde subirlos?

Crea una carpeta con tu apellido y nombre en:

```
entregas/1.1_sqlite/tu_apellido_nombre/
```

**Ejemplos:**
- `entregas/1.1_sqlite/garcia_maria/`
- `entregas/1.1_sqlite/lopez_juan/`
- `entregas/1.1_sqlite/martinez_ana/`

**Estructura final:**
```
entregas/
└── 1.1_sqlite/
    └── garcia_maria/              ← Tu carpeta
        ├── ANALISIS_DATOS.md
        ├── resumen_eda.md
        └── REFLEXION.md
```

---

## 🚀 Paso a Paso: Cómo Entregar

### **Paso 1: Hacer Fork del Repositorio**
(Haz esto si no tienes aun nada del repositorio, de otra forma empieza en el paso 3)

**¿Qué es un fork?** Es tu copia personal del repositorio.

1. Ve a: https://github.com/TodoEconometria/ejercicios-bigdata
2. Haz clic en el botón **"Fork"** (arriba a la derecha)
3. Espera unos segundos
4. Ahora tienes tu copia en: `https://github.com/TU_USUARIO/ejercicios-bigdata`

---

### **Paso 2: Clonar TU Fork a tu computadora**

**Windows (PyCharm o Git Bash):**
```bash
git clone https://github.com/TU_USUARIO/ejercicios-bigdata.git
cd ejercicios-bigdata
```

**Mac/Linux (Terminal):**
```bash
git clone https://github.com/TU_USUARIO/ejercicios-bigdata.git
cd ejercicios-bigdata
```

---

### **Paso 3: Crear una rama para trabajar**

```bash
git checkout -b apellido-ejercicio-1.1
```

**Ejemplo:**
```bash
git checkout -b garcia-ejercicio-1.1
```

---

### **Paso 4: Crear tu carpeta de entrega**

**Desde la raíz del proyecto:**

```bash
mkdir -p entregas/1.1_sqlite/tu_apellido_nombre
```

**Ejemplo:**
```bash
mkdir -p entregas/1.1_sqlite/garcia_maria
```

**En Windows (si no funciona mkdir):**
- Crea las carpetas manualmente:
  - `entregas` (si no existe)
  - `entregas/1.1_sqlite` (si no existe)
  - `entregas/1.1_sqlite/garcia_maria`

---

### **Paso 5: Completar tus archivos**

Copia las plantillas y complétalas:

```bash
# Copiar plantillas a tu carpeta
cp ejercicios/01_bases_de_datos/1.1_introduccion_sqlite/ANALISIS_DATOS.md \
   entregas/1.1_sqlite/tu_apellido_nombre/

cp ejercicios/01_bases_de_datos/1.1_introduccion_sqlite/REFLEXION.md \
   entregas/1.1_sqlite/tu_apellido_nombre/
```

**Si ejecutaste el script EDA (opcional):**
```bash
# Copiar el resumen generado
cp ejercicios/01_bases_de_datos/1.1_introduccion_sqlite/resumen_eda.md \
   entregas/1.1_sqlite/tu_apellido_nombre/
```

**Si NO ejecutaste el script:**
- Crea `resumen_eda.md` manualmente siguiendo el formato

---

### **Paso 6: Completar los archivos con tu análisis**

Abre los archivos con tu editor favorito (PyCharm, VS Code, etc.) y completa:

**`ANALISIS_DATOS.md`:**
- Resumen Ejecutivo (estadísticas de los CSVs)
- Análisis de Estructura (columnas comunes, tabla resumen)
- Análisis de Calidad (valores nulos, duplicados)
- Identificación de Entidades (fabricantes, colores, categorías)
- Diagramas ER (Modelos A y B) - Ya están en la plantilla, ajústalos si es necesario
- Conclusiones para el Diseño

**`resumen_eda.md`:**
- Tabla resumen con todos los CSVs
- Estadísticas generales
- Fabricantes y colores identificados

**`REFLEXION.md`:**
- Respuestas a las 6 preguntas de reflexión
- Justifica tus respuestas

---

### **Paso 7: Verificar que los archivos sean correctos**

```bash
# Ver tus archivos
ls -la entregas/1.1_sqlite/tu_apellido_nombre/

# Debería mostrar:
# ANALISIS_DATOS.md
# resumen_eda.md
# REFLEXION.md
```

**Verifica que:**
- ✅ Los archivos .md se ven bien en tu editor
- ✅ Los diagramas Mermaid están completos
- ✅ Las tablas están bien formateadas
- ✅ Respondiste TODAS las preguntas

---

### **Paso 8: Guardar tus cambios (Commit)**

```bash
# Ver qué archivos cambiaste
git status

# Agregar tus archivos
git add entregas/1.1_sqlite/tu_apellido_nombre/

# Guardar con un mensaje
git commit -m "Entrega ejercicio 1.1 - Tu Nombre"
```

**Ejemplo:**
```bash
git commit -m "Entrega ejercicio 1.1 - María García"
```

---

### **Paso 9: Subir a TU Fork en GitHub**

```bash
git push origin apellido-ejercicio-1.1
```

**Ejemplo:**
```bash
git push origin garcia-ejercicio-1.1
```

---

### **Paso 10: Crear Pull Request (PR)**

1. Ve a TU fork en GitHub: `https://github.com/TU_USUARIO/ejercicios-bigdata`

2. Verás un banner amarillo que dice:
   **"apellido-ejercicio-1.1 had recent pushes"**
   → Haz clic en **"Compare & pull request"**

3. **Completa el formulario del PR:**
   - **Título:** `[1.1] Tu Apellido Nombre - Introducción SQLite`
   - **Ejemplo:** `[1.1] García María - Introducción SQLite`

4. **Completa el checklist** que aparece automáticamente:
   ```markdown
   - [x] Creé la carpeta correcta: entregas/1.1_sqlite/garcia_maria/
   - [x] Subí ANALISIS_DATOS.md
   - [x] Subí resumen_eda.md
   - [x] Subí REFLEXION.md
   - [x] Completé todas las secciones
   - [x] Los diagramas ER están incluidos
   - [x] NO incluí archivos .db
   - [x] NO incluí archivos .csv
   ```

5. Haz clic en **"Create pull request"**

---

## ✅ Checklist Final (Antes de Enviar)

Antes de crear el PR, verifica:

### Estructura
- [ ] Mi carpeta está en `entregas/1.1_sqlite/apellido_nombre/`
- [ ] Incluí los 3 archivos obligatorios
- [ ] Los nombres de archivos son exactos (mayúsculas/minúsculas)

### Contenido de ANALISIS_DATOS.md
- [ ] Resumen Ejecutivo con estadísticas
- [ ] Tabla resumen de archivos CSV
- [ ] Análisis de columnas comunes
- [ ] Análisis de calidad (nulos, duplicados)
- [ ] Lista de fabricantes identificados
- [ ] Lista de colores identificados
- [ ] Diagramas ER para Modelo A y Modelo B (Mermaid)
- [ ] Conclusiones justificadas

### Contenido de resumen_eda.md
- [ ] Tabla resumen con todos los CSVs
- [ ] Estadísticas de filas y columnas
- [ ] Fabricantes únicos
- [ ] Colores únicos

### Contenido de REFLEXION.md
- [ ] Respondí las 6 preguntas
- [ ] Cada respuesta está justificada
- [ ] Usé ejemplos concretos

### Formato
- [ ] Los archivos .md se visualizan correctamente en GitHub
- [ ] Las tablas Markdown están bien formateadas
- [ ] Los diagramas Mermaid se renderizan correctamente

### Archivos prohibidos
- [ ] NO incluí archivos `.db` (bases de datos)
- [ ] NO incluí archivos `.csv` (datos)
- [ ] NO incluí archivos `.py` (código Python)

---

## ❓ Preguntas Frecuentes

### **P: ¿Tengo que ejecutar el script `eda_exploratorio.py`?**
R: No es obligatorio. Puedes:
- **Opción A:** Ejecutarlo y usar el `resumen_eda.md` que genera
- **Opción B:** Crear `resumen_eda.md` manualmente siguiendo el formato

### **P: ¿Puedo modificar los diagramas ER de la plantilla?**
R: Sí, puedes ajustarlos según tu análisis, pero deben estar en formato Mermaid.

### **P: ¿Qué pasa si me equivoco en el nombre de la carpeta?**
R: El sistema de validación automática te avisará. Debes corregir y hacer push de nuevo.

### **P: ¿Puedo ver las entregas de otros compañeros?**
R: Sí, los PRs son públicos. Pero NO copies, el profesor detecta plagios.

### **P: ¿Cuántas veces puedo actualizar mi PR?**
R: Las que necesites antes de la fecha límite. Cada push actualiza automáticamente el PR.

### **P: ¿Cómo actualizo mi PR si el profesor pide correcciones?**
R: Simplemente edita tus archivos, haz commit y push:
```bash
git add entregas/1.1_sqlite/tu_apellido/
git commit -m "Correcciones solicitadas"
git push origin apellido-ejercicio-1.1
```

### **P: No sé usar Git, ¿hay otra forma?**
R: Puedes usar GitHub Desktop (interfaz gráfica) o pregunta al profesor en clase.

---

## 🆘 Ayuda

**Si tienes problemas:**
1. Revisa esta guía de nuevo
2. Pregunta a tus compañeros
3. Pregunta al profesor en clase
4. Envía un email al profesor con capturas de pantalla del error

**Recursos útiles:**
- [Tutorial Git en español](https://git-scm.com/book/es/v2)
- [Guía Markdown](https://www.markdownguide.org/basic-syntax/)
- [Diagramas Mermaid](https://mermaid.js.org/syntax/entityRelationshipDiagram.html)

---

## 📅 Fechas Importantes

- **Publicación:** [A DEFINIR]
- **Fecha límite:** [A DEFINIR]
- **Penalización por retraso:** -10 pts por día

---

**¡Buena suerte!** 🚀

Si sigues esta guía paso a paso, tu entrega será exitosa.

---

**Última actualización:** 2025-12-15
