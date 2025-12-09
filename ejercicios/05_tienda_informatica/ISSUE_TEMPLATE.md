# Tarea 2 - Ejercicio 05: Base de Datos Relacional - Tienda Informática

## 🎯 Objetivo Principal

Diseñar e implementar una base de datos relacional para una tienda de componentes informáticos, aplicando principios de normalización y buenas prácticas de diseño de bases de datos.

---

## 📦 Descripción

Te han contratado como Data Engineer en una tienda de componentes informáticos. Tienen los datos en **25 archivos CSV separados** (~15,000 productos) y necesitan consolidarlos en una base de datos relacional bien diseñada.

---

## 📋 Requisitos Mínimos

### Parte 1: Análisis Exploratorio (20 pts)
- Explorar los 25 archivos CSV
- Identificar patrones, inconsistencias y datos faltantes
- Determinar qué información puede extraerse a tablas separadas
- **Entrega**: Documento de análisis (Markdown o Jupyter Notebook)

### Parte 2: Diseño Relacional (30 pts)
- Diseñar esquema relacional normalizado (mínimo 3FN)
- Crear diagrama ER con todas las relaciones
- Definir claves primarias y foráneas
- **Entrega**: Diagrama ER, justificación de diseño, script SQL (`schema.sql`)

### Parte 3: Implementación (30 pts)
- Script Python que cargue los datos en SQLite o PostgreSQL
- Implementar todas las tablas, constraints e índices
- Manejo de errores y datos faltantes
- **Entrega**: Script(s) Python, `requirements.txt`, logs de ejecución

### Parte 4: Consultas SQL (15 pts)
- Mínimo 8 consultas SQL que demuestren:
  - JOINs entre tablas
  - Agregaciones (GROUP BY, HAVING)
  - Subconsultas
  - Análisis útil para el negocio
- **Entrega**: Archivo SQL con consultas y resultados

### Parte 5: Documentación (5 pts)
- README.md con instrucciones de instalación y ejecución
- Código bien comentado
- **Entrega**: README completo en tu carpeta de solución

---

## 📂 Estructura de Carpeta

```
ejercicios/05_tienda_informatica/
└── soluciones/
    └── tu-apellido-nombre/
        ├── analisis/
        │   └── exploracion_datos.md
        ├── diseño/
        │   ├── diagrama_er.png
        │   ├── justificacion_diseño.md
        │   └── schema.sql
        ├── implementacion/
        │   ├── cargar_datos.py
        │   └── requirements.txt
        ├── consultas/
        │   ├── consultas.sql
        │   └── resultados.md
        ├── base_datos/
        │   └── tienda.db
        └── README.md
```

---

## 📥 Instrucciones de Entrega

### 1. Obtener los Datos
```bash
# Descargar csv_tienda_informatica.zip desde:
# [LINK A PROPORCIONAR POR EL PROFESOR]

cd ejercicios/05_tienda_informatica
mkdir -p datos/csv_tienda_informatica
unzip csv_tienda_informatica.zip -d datos/
```

### 2. Crear Rama de Trabajo
```bash
git checkout -b tu-apellido-ejercicio05
```

### 3. Crear Tu Carpeta de Solución
```bash
mkdir -p soluciones/tu_apellido_nombre
cd soluciones/tu_apellido_nombre
mkdir analisis diseño implementacion consultas base_datos
```

### 4. Desarrollar Tu Solución
- Sigue el [ENUNCIADO.md](https://github.com/TodoEconometria/ejercicios-bigdata/blob/main/ejercicios/05_tienda_informatica/ENUNCIADO.md)
- Consulta [AYUDA.md](https://github.com/TodoEconometria/ejercicios-bigdata/blob/main/ejercicios/05_tienda_informatica/AYUDA.md) cuando lo necesites

### 5. Commit y Push
```bash
git add soluciones/tu_apellido_nombre/
git commit -m "Ejercicio 05: BD Tienda Informática - Tu Nombre"
git push origin tu-apellido-ejercicio05
```

### 6. Pull Request
- Crea PR desde tu fork al repositorio principal
- Título: `Ejercicio 05 - Apellido Nombre`
- Base: `TodoEconometria/ejercicios-bigdata` (main)
- Compare: `tu-usuario/ejercicios-bigdata` (tu-rama)

---

## 📊 Criterios de Evaluación

| Aspecto | Peso | Descripción |
|---------|------|-------------|
| **Análisis Exploratorio** | 20% | Profundidad del análisis, identificación de problemas |
| **Diseño Relacional** | 30% | Diagrama ER, normalización, justificación |
| **Implementación** | 30% | Código funcional, manejo de errores, eficiencia |
| **Consultas SQL** | 15% | Complejidad, utilidad, correctitud |
| **Documentación** | 5% | Claridad, completitud, reproducibilidad |

### Puntos Bonus (+15 pts máximo)
- **+5 pts**: Uso de PostgreSQL en lugar de SQLite
- **+5 pts**: Implementación de índices y optimización
- **+5 pts**: Script de backup/restore
- **+3 pts**: Tests unitarios para validación
- **+2 pts**: Dashboard o visualización

---

## 🛠️ Tecnologías Permitidas

### Base de Datos (Elige una)
- **SQLite** (recomendado): Simple, un solo archivo, no requiere servidor
- **PostgreSQL** (+5 pts bonus): Más profesional, pero requiere configuración

### Python
```python
import pandas as pd              # Leer CSVs
import sqlite3                   # SQLite
# o
import psycopg2                  # PostgreSQL
from sqlalchemy import create_engine  # ORM (opcional)
```

---

## ⏱️ Tiempo Estimado

- **Análisis**: 2-3 horas
- **Diseño**: 3-4 horas
- **Implementación**: 4-6 horas
- **Consultas**: 1-2 horas
- **Documentación**: 1 hora

**Total**: 11-16 horas (hazlo en varias sesiones)

---

## 📚 Recursos

- **Documentación Completa**: [`ejercicios/05_tienda_informatica/ENUNCIADO.md`](https://github.com/TodoEconometria/ejercicios-bigdata/blob/main/ejercicios/05_tienda_informatica/ENUNCIADO.md)
- **Guía de Ayuda**: [`ejercicios/05_tienda_informatica/AYUDA.md`](https://github.com/TodoEconometria/ejercicios-bigdata/blob/main/ejercicios/05_tienda_informatica/AYUDA.md)
- **Plantilla Base**: [`plantilla_base.py`](https://github.com/TodoEconometria/ejercicios-bigdata/blob/main/ejercicios/05_tienda_informatica/plantilla_base.py)
- **Diagramas ER**: [dbdiagram.io](https://dbdiagram.io/)
- **Normalización**: [Database Normalization Guide](https://www.essentialsql.com/get-ready-to-learn-sql-database-normalization-explained-in-simple-english/)

---

## ⚠️ Importante

- ❌ **NO subas archivos CSV** al repositorio (usa .gitignore)
- ❌ **NO subas bases de datos (.db)** al repositorio
- ❌ **NO copies soluciones** de otros compañeros
- ✅ **SÍ justifica** todas tus decisiones de diseño
- ✅ **SÍ documenta** tu código claramente
- ✅ **SÍ prueba** que todo funcione antes de entregar

---

## 📅 Fechas

- **Apertura**: [A definir por el profesor]
- **Entrega**: [A definir por el profesor], 23:59
- **Duración estimada**: 2-3 semanas

---

## ❓ Preguntas Frecuentes

**P: ¿Dónde descargo los datos?**
R: El profesor compartirá el link en clase. Archivo: `csv_tienda_informatica.zip`

**P: ¿Puedo usar ChatGPT/Claude?**
R: Sí, como herramienta de ayuda. Pero debes entender y justificar cada decisión.

**P: ¿Cuántas tablas debo crear?**
R: Depende de tu diseño. Entre 5 y 15 es razonable.

**P: ¿SQLite o PostgreSQL?**
R: SQLite es más fácil. PostgreSQL da +5 pts extra pero requiere más setup.

---

## 🎯 Objetivos de Aprendizaje

Al completar este ejercicio habrás aprendido:
- ✅ Análisis exploratorio de datos
- ✅ Diseño de bases de datos relacionales
- ✅ Normalización (1FN, 2FN, 3FN)
- ✅ Implementación de esquemas SQL
- ✅ ETL con Python
- ✅ SQL avanzado (JOINs, subconsultas, agregaciones)

---

**¡Buena suerte! 💪**

**Repositorio**: https://github.com/TodoEconometria/ejercicios-bigdata
**Ejercicio**: 05 - Base de Datos Relacional
