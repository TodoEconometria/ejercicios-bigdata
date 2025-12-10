# 📚 Ejercicio 01: Base de Datos Relacional - Tienda Informática

## 📁 Estructura del Ejercicio

```
01_tienda_informatica/
├── datos/
│   ├── .gitkeep
│   └── csv_tienda_informatica/     ← Aquí colocas los CSVs (25 archivos)
│       ├── cpu.csv
│       ├── video_card.csv
│       ├── memory.csv
│       └── ... (22 archivos más)
│
├── ENUNCIADO.md                     ← Lee esto primero
├── AYUDA.md                         ← Consejos y guías
├── plantilla_base.py                ← Código de ejemplo para empezar
├── .gitignore                       ← Ya configurado
└── README.md                        ← Estás aquí
```

---

## 🚀 Inicio Rápido

### 1. Obtener los Datos

**Los datos NO están en el repositorio** (son archivos grandes). Descárgalos desde:

📥 **Link de descarga**: [**A proporcionar por el profesor**]

El archivo se llama `csv_tienda_informatica.zip` (~15 MB)

### 2. Configurar el Entorno

```bash
# 1. Navega al ejercicio
cd ejercicios/01_tienda_informatica

# 2. Crea la carpeta de datos si no existe
mkdir -p datos/csv_tienda_informatica

# 3. Descomprime el ZIP dentro de datos/
unzip csv_tienda_informatica.zip -d datos/

# 4. Verifica que los archivos están ahí
ls datos/csv_tienda_informatica/
# Deberías ver 25 archivos .csv
```

### 3. Empieza a Trabajar

```bash
# Lee el enunciado completo
cat ENUNCIADO.md

# Revisa la plantilla base
cat plantilla_base.py

# Ejecuta tu primer análisis
python tu_script.py
```

---

## 📋 ¿Qué Tienes Que Hacer?

Lee el archivo [`ENUNCIADO.md`](./ENUNCIADO.md) para el detalle completo.

### Resumen de Tareas

| Parte | Descripción | Puntos |
|-------|-------------|--------|
| **1. Análisis Exploratorio** | Explora los CSVs, identifica patrones y problemas | 20 pts |
| **2. Diseño Relacional** | Diagrama ER, esquema SQL, normalización | 30 pts |
| **3. Implementación** | Código Python que cargue los datos en SQLite/PostgreSQL | 30 pts |
| **4. Consultas SQL** | Mínimo 8 consultas útiles para el negocio | 15 pts |
| **5. Documentación** | README, comentarios, instrucciones | 5 pts |
| **TOTAL** | | **100 pts** |

**Puntos Bonus**: Hasta +15 pts por PostgreSQL, optimización, tests, etc.

---

## 📤 Formato de Entrega

### Estructura Esperada

**IMPORTANTE**: Los alumnos deben crear su solución en un **fork del repositorio** siguiendo esta estructura:

```
ejercicios/01_tienda_informatica/
│
└── soluciones/
    └── apellido_nombre/              ← TU CARPETA PERSONAL
        │
        ├── analisis/
        │   └── exploracion_datos.md (o .ipynb)
        │
        ├── diseño/
        │   ├── diagrama_er.png
        │   ├── justificacion_diseño.md
        │   └── schema.sql
        │
        ├── implementacion/
        │   ├── cargar_datos.py
        │   ├── requirements.txt
        │   └── logs/ (opcional)
        │
        ├── consultas/
        │   ├── consultas.sql
        │   └── resultados.md
        │
        ├── base_datos/
        │   └── tienda.db (o instrucciones para PostgreSQL)
        │
        └── README.md
```

### Ejemplo de Nombre de Carpeta

- ✅ `garcia_maria/`
- ✅ `rodriguez_juan/`
- ❌ `Maria/` (falta apellido)
- ❌ `mi_solucion/` (no es tu nombre)

---

## 🎓 Instrucciones de Entrega (Paso a Paso)

### Paso 1: Fork del Repositorio

```bash
# En GitHub, haz clic en "Fork" en el repositorio principal
# https://github.com/TodoEconometria/ejercicios-bigdata

# Clona TU fork (no el original)
git clone https://github.com/TU_USUARIO/ejercicios-bigdata.git
cd ejercicios-bigdata
```

### Paso 2: Descarga los Datos

```bash
# Descarga el ZIP desde el link proporcionado
# Colócalo en ejercicios/01_tienda_informatica/

cd ejercicios/01_tienda_informatica
unzip csv_tienda_informatica.zip -d datos/
```

### Paso 3: Crea Tu Rama de Trabajo

```bash
# Formato: tu-apellido-ejercicio01
git checkout -b garcia-maria-ejercicio01

# Verifica que estás en la rama correcta
git branch
```

### Paso 4: Crea Tu Carpeta de Solución

```bash
# Crea tu carpeta personal dentro de soluciones/
mkdir -p soluciones/garcia_maria

# Crea la estructura completa
cd soluciones/garcia_maria
mkdir analisis diseño implementacion consultas base_datos
```

### Paso 5: Desarrolla Tu Solución

Trabaja en tu solución siguiendo el enunciado. Los archivos principales:

```python
# implementacion/cargar_datos.py
import sqlite3
import pandas as pd

# ... tu código aquí ...
```

```sql
-- diseño/schema.sql
CREATE TABLE categorias (
    id_categoria INTEGER PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

-- ... más tablas ...
```

### Paso 6: Commit y Push

```bash
# Añade tus archivos
git add soluciones/garcia_maria/

# Commit con mensaje descriptivo
git commit -m "Ejercicio 01: Implementación base de datos tienda informática - García María"

# Push a TU fork
git push origin garcia-maria-ejercicio01
```

### Paso 7: Pull Request

1. Ve a **tu fork** en GitHub
2. Haz clic en "Compare & pull request"
3. **Base repository**: `TodoEconometria/ejercicios-bigdata` (main)
4. **Head repository**: `TU_USUARIO/ejercicios-bigdata` (tu-rama)
5. Título: `Ejercicio 01 - Apellido Nombre`
6. Descripción: Resumen de tu trabajo
7. Crea el Pull Request

---

## ✅ Checklist Antes de Entregar

- [ ] He leído completamente el ENUNCIADO.md
- [ ] Mi carpeta está en `soluciones/apellido_nombre/`
- [ ] Tengo las 5 carpetas requeridas (analisis, diseño, implementacion, consultas, base_datos)
- [ ] Mi diagrama ER está incluido
- [ ] Mi código funciona sin errores
- [ ] He escrito al menos 8 consultas SQL
- [ ] Mi README.md explica cómo ejecutar mi código
- [ ] He hecho commit de todos los archivos necesarios
- [ ] He creado el Pull Request correctamente

---

## ⚠️ Errores Comunes a Evitar

### ❌ NO Hagas Esto

1. **NO subas los archivos CSV al repositorio**
   - Son archivos grandes
   - Ya están en el .gitignore
   - Descarga el ZIP cada vez que lo necesites

2. **NO subas las bases de datos (.db) al repositorio**
   - También son archivos grandes
   - El profesor las generará desde tu código

3. **NO trabajes en la rama `main`**
   - Crea tu propia rama de trabajo
   - Usa el formato: `tu-apellido-ejercicio01`

4. **NO copies soluciones de otros**
   - Está prohibido
   - Se detectará fácilmente
   - Justifica tus decisiones de diseño

5. **NO olvides el README.md en tu solución**
   - Debe explicar cómo ejecutar tu código
   - Debe incluir requisitos (requirements.txt)

### ✅ SÍ Haz Esto

1. **Trabaja en tu propia carpeta**
   - `soluciones/tu_apellido_nombre/`
   - No toques las carpetas de otros

2. **Documenta tu código**
   - Comentarios explicativos
   - Justifica decisiones de diseño

3. **Prueba que funcione**
   - Ejecuta tu código antes de entregar
   - Verifica que las consultas devuelvan resultados

4. **Haz commits frecuentes**
   - No esperes al último día
   - Commits pequeños y descriptivos

---

## 📚 Recursos Adicionales

### Dentro de Este Ejercicio

- [`ENUNCIADO.md`](./ENUNCIADO.md) - Descripción completa del ejercicio
- [`AYUDA.md`](./AYUDA.md) - Consejos y guías paso a paso
- [`plantilla_base.py`](./plantilla_base.py) - Código de ejemplo

### Documentación Externa

- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [SQL Tutorial - W3Schools](https://www.w3schools.com/sql/)
- [dbdiagram.io](https://dbdiagram.io/) - Para diagramas ER online
- [Database Normalization](https://www.essentialsql.com/get-ready-to-learn-sql-database-normalization-explained-in-simple-english/)

---

## ❓ Preguntas Frecuentes

**P: No encuentro el archivo CSV. ¿Dónde lo descargo?**
R: El profesor compartirá el link en clase/aula virtual. El archivo se llama `csv_tienda_informatica.zip`.

**P: ¿Puedo usar PostgreSQL en lugar de SQLite?**
R: Sí, incluso da puntos bonus (+5 pts). Pero asegúrate de documentar cómo conectarse.

**P: ¿Cuántas tablas debo crear?**
R: Depende de tu diseño. Entre 5 y 15 es razonable. Enfócate en la normalización.

**P: ¿Puedo usar ChatGPT/Claude?**
R: Sí, como herramienta de ayuda. Pero debes entender y justificar cada decisión.

**P: ¿Qué hago si encuentro errores en los datos?**
R: Documéntalos en tu análisis exploratorio y explica cómo los manejaste.

**P: ¿Tengo que hacer exactamente 8 consultas?**
R: Mínimo 8. Más consultas útiles pueden dar puntos bonus.

---

## 📅 Información de Entrega

- **Fecha límite**: [**A definir por el profesor**]
- **Método**: Pull Request desde tu fork
- **Formato**: Carpeta `soluciones/apellido_nombre/`
- **Repositorio**: https://github.com/TodoEconometria/ejercicios-bigdata

---

## 🆘 ¿Necesitas Ayuda?

1. **Lee primero** el ENUNCIADO.md y AYUDA.md completos
2. **Revisa** la documentación de las bibliotecas
3. **Consulta** con tus compañeros (sin copiar código)
4. **Pregunta** en clase o aula virtual
5. **Usa** IA como herramienta de aprendizaje (no para copiar)

---

## 🎯 Objetivos de Aprendizaje

Al completar este ejercicio dominarás:

- ✅ Análisis exploratorio de datos
- ✅ Diseño de bases de datos relacionales
- ✅ Normalización (1FN, 2FN, 3FN)
- ✅ Implementación de esquemas SQL
- ✅ ETL (Extract, Transform, Load) con Python
- ✅ Consultas SQL avanzadas (JOINs, agregaciones, subconsultas)
- ✅ Documentación técnica

---

**¡Buena suerte! 💪**

**Repositorio**: https://github.com/TodoEconometria/ejercicios-bigdata
**Ejercicio**: 05 - Base de Datos Relacional - Tienda Informática
