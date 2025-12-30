# 👨‍🏫 Instrucciones para el Profesor - Ejercicio 01

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

**Repositorio**: https://github.com/TodoEconometria/ejercicios-bigdata
**Ejercicio**: 05 - Base de Datos Relacional
**Creado**: Diciembre 2024

---

¡Éxito con las evaluaciones! 📚
