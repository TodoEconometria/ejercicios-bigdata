# 📚 EJERCICIO 01: Diseño e Implementación de Base de Datos Relacional

## 🎯 Objetivo del Ejercicio

**Diseñar e implementar una base de datos relacional** para una tienda de componentes informáticos, aplicando principios de normalización y buenas prácticas de diseño de bases de datos.

---

## 📝 Descripción del Problema

Te han contratado como Data Engineer en una tienda de componentes informáticos. Actualmente tienen los datos en **25 archivos CSV separados** (uno por categoría de producto), y necesitan:

1. ✅ Consolidar toda la información en una **base de datos relacional**
2. ✅ Aplicar **normalización** para evitar redundancia
3. ✅ Diseñar **relaciones** entre tablas
4. ✅ Implementar **claves primarias y foráneas**
5. ✅ Facilitar **consultas eficientes** para el negocio

---

## 📦 Datos Proporcionados

**25 archivos CSV** con información de productos:

### Componentes Principales
- `cpu.csv` - Procesadores (~700 productos)
- `video_card.csv` - Tarjetas gráficas (~3,600)
- `memory.csv` - Memoria RAM (~7,500)
- `monitor.csv` - Monitores (~2,000)
- `motherboard.csv` - Placas base (~2,300)

### Periféricos
- `keyboard.csv`, `mouse.csv`, `headphones.csv`
- `webcam.csv`, `speakers.csv`

### Almacenamiento
- `internal_hard_drive.csv`
- `external_hard_drive.csv`

### Otros (15 archivos más)
- Fuentes de alimentación, refrigeración, cajas, tarjetas de red, etc.

**Total**: ~15,000 productos

---

## 🎯 Tu Tarea

### Parte 1: Análisis Exploratorio (20 pts)

1. **Explora los archivos CSV**:
   - ¿Qué columnas tiene cada archivo?
   - ¿Qué tipos de datos?
   - ¿Hay datos faltantes?
   - ¿Hay inconsistencias?

2. **Identifica patrones**:
   - ¿Qué campos se repiten entre archivos?
   - ¿Qué información podría extraerse a tablas separadas?
   - ¿Qué relaciones existen entre los datos?

3. **Entrega**: Documento con análisis (puede ser Jupyter Notebook o Markdown)

### Parte 2: Diseño de la Base de Datos (30 pts)

1. **Diseña el esquema relacional**:
   - Identifica las entidades principales
   - Define las relaciones entre entidades
   - Aplica normalización (mínimo 3FN)
   - Diseña claves primarias y foráneas

2. **Crea un diagrama ER** (Entity-Relationship):
   - Puedes usar draw.io, dbdiagram.io, o similar
   - Incluye todas las tablas y sus relaciones
   - Marca las cardinalidades (1:1, 1:N, N:M)

3. **Justifica tus decisiones**:
   - ¿Por qué elegiste esta estructura?
   - ¿Qué tablas creaste adicionales?
   - ¿Qué datos normalizaste?

4. **Entrega**: 
   - Diagrama ER (imagen o PDF)
   - Documento justificando el diseño
   - Script SQL con `CREATE TABLE` statements

### Parte 3: Implementación (30 pts)

1. **Elige tu tecnología**:
   - **Opción A**: SQLite (más simple, un solo archivo)
   - **Opción B**: PostgreSQL (más profesional, cliente-servidor)

2. **Escribe el código de carga**:
   - Script Python que lea los CSVs
   - Transforme los datos según tu diseño
   - Inserte en la base de datos
   - Maneje errores y datos faltantes

3. **Implementa**:
   - Todas las tablas de tu diseño
   - Claves primarias
   - Claves foráneas
   - Constraints apropiados (NOT NULL, UNIQUE, CHECK)
   - Índices si es necesario

4. **Entrega**:
   - Script(s) Python de carga
   - Base de datos poblada
   - Log de ejecución (evidencia de que funcionó)

### Parte 4: Consultas y Análisis (15 pts)

1. **Escribe mínimo 8 consultas SQL** que demuestren:
   - JOINs entre tablas relacionadas
   - Agregaciones (GROUP BY, HAVING)
   - Subconsultas
   - Análisis de negocio útil

2. **Ejemplos de consultas esperadas**:
   - ¿Cuál es el producto más caro de cada categoría?
   - ¿Qué marca tiene más productos?
   - Top 10 productos con mejor relación calidad/precio
   - Estadísticas por categoría y fabricante
   - Productos compatibles (ej: CPUs compatibles con cierta placa base)

3. **Entrega**: Archivo SQL con las consultas y sus resultados

### Parte 5: Documentación (5 pts)

1. **README.md** con:
   - Instrucciones de instalación
   - Cómo ejecutar tu código
   - Estructura de la base de datos
   - Decisiones de diseño

2. **Comentarios en el código**:
   - Código bien documentado
   - Explicaciones de decisiones técnicas

---

## 🛠️ Tecnologías Permitidas

### Base de Datos (Elige una)

#### SQLite (Recomendado para empezar)
```python
import sqlite3
conn = sqlite3.connect('tienda.db')
```
**Ventajas**: Simple, un solo archivo, no requiere servidor
**Desventajas**: Menos features que PostgreSQL

#### PostgreSQL (Más profesional)
```python
import psycopg2
conn = psycopg2.connect(
    host="localhost",
    database="tienda",
    user="tu_usuario",
    password="tu_password"
)
```
**Ventajas**: Más robusto, más features, usado en producción
**Desventajas**: Requiere instalación y configuración

### Python
```python
import pandas as pd           # Para leer CSVs
from sqlalchemy import create_engine  # ORM (opcional)
import sqlite3 / psycopg2    # Drivers de BD
```

---

## 📐 Sugerencias de Diseño

### Tablas Básicas (Punto de Partida)

```sql
-- Ejemplo de estructura (¡tú debes diseñar la tuya!)

-- Tabla de categorías (normalización)
CREATE TABLE categorias (
    id_categoria INTEGER PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT
);

-- Tabla de fabricantes
CREATE TABLE fabricantes (
    id_fabricante INTEGER PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE
);

-- Tabla de productos (maestra)
CREATE TABLE productos (
    id_producto INTEGER PRIMARY KEY,
    nombre VARCHAR(500) NOT NULL,
    precio DECIMAL(10,2),
    id_categoria INTEGER,
    id_fabricante INTEGER,
    FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria),
    FOREIGN KEY (id_fabricante) REFERENCES fabricantes(id_fabricante)
);

-- Tablas específicas por tipo (con detalles técnicos)
CREATE TABLE cpus (
    id_cpu INTEGER PRIMARY KEY,
    id_producto INTEGER UNIQUE,
    core_count INTEGER,
    core_clock DECIMAL(4,2),
    tdp INTEGER,
    FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
);

-- ... y así para cada categoría
```

### Preguntas Clave para tu Diseño

1. **¿Creo una tabla maestra "productos" o cada CSV es independiente?**
2. **¿Cómo extraigo fabricantes/marcas que están en el nombre?**
3. **¿Cómo manejo las especificaciones técnicas únicas de cada categoría?**
4. **¿Necesito tablas intermedias para relaciones N:M?**
5. **¿Qué constraints son apropiados para cada campo?**

---

## 🚫 Restricciones

- ❌ NO puedes usar los scripts proporcionados en los materiales de clase (si los hay)
- ❌ NO puedes simplemente hacer `df.to_sql()` sin diseño previo
- ✅ DEBES diseñar la estructura tú mismo
- ✅ DEBES aplicar normalización
- ✅ DEBES crear relaciones con claves foráneas

---

## 📤 Formato de Entrega

```
apellido_nombre_ejercicio01.zip
│
├── analisis/
│   └── exploracion_datos.md (o .ipynb)
│
├── diseño/
│   ├── diagrama_er.png
│   ├── justificacion_diseño.md
│   └── schema.sql (CREATE TABLE statements)
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

---

## 📊 Criterios de Evaluación

| Criterio | Puntos | Descripción |
|----------|--------|-------------|
| **Análisis Exploratorio** | 20 | Profundidad del análisis, identificación de problemas |
| **Diseño Relacional** | 30 | Calidad del diagrama ER, normalización, justificación |
| **Implementación** | 30 | Código funcional, manejo de errores, eficiencia |
| **Consultas SQL** | 15 | Complejidad, utilidad de negocio, correctitud |
| **Documentación** | 5 | Claridad, completitud, reproducibilidad |
| **TOTAL** | 100 | |

### Puntos Bonus (+15 pts máximo)
- **+5 pts**: Uso de PostgreSQL en lugar de SQLite
- **+5 pts**: Implementación de índices y optimización de consultas
- **+5 pts**: Script de backup/restore o migración de datos
- **+3 pts**: Tests unitarios para validación de datos
- **+2 pts**: Dashboard o visualización de datos

---

## 💡 Consejos

### Para el Análisis
```python
# Explora cada CSV
import pandas as pd

df = pd.read_csv('cpu.csv')
print(df.info())
print(df.describe())
print(df.head())
print(df['name'].str.split().str[0].value_counts())  # Fabricantes
```

### Para el Diseño
- Empieza simple, luego normaliza
- Dibuja en papel antes de usar software
- Piensa en qué consultas hará el negocio

### Para la Implementación
- Prueba con un CSV primero
- Valida los datos antes de insertar
- Usa transacciones para consistencia
- Loguea errores para debugging

---

## 📚 Recursos Recomendados

### Normalización de Bases de Datos
- [Database Normalization Explained](https://www.essentialsql.com/get-ready-to-learn-sql-database-normalization-explained-in-simple-english/)
- [Normal Forms (1FN, 2FN, 3FN)](https://www.guru99.com/database-normalization.html)

### Diseño de Diagramas ER
- [dbdiagram.io](https://dbdiagram.io/) - Online ER designer
- [draw.io](https://draw.io/) - Diagramas generales
- [QuickDBD](https://www.quickdatabasediagrams.com/)

### SQLAlchemy (ORM)
- [SQLAlchemy Tutorial](https://docs.sqlalchemy.org/en/14/tutorial/)
- Útil para generar tablas desde código Python

### PostgreSQL
- [Instalación PostgreSQL](https://www.postgresql.org/download/)
- [psycopg2 Documentation](https://www.psycopg.org/docs/)

---

## ⏱️ Tiempo Estimado

- **Análisis**: 2-3 horas
- **Diseño**: 3-4 horas  
- **Implementación**: 4-6 horas
- **Consultas**: 1-2 horas
- **Documentación**: 1 hora

**Total**: 11-16 horas (hazlo en varias sesiones)

---

## ❓ Preguntas Frecuentes

**P: ¿Puedo usar ChatGPT/Claude para ayuda?**
R: Sí, pero debes entender y justificar cada decisión. El código debe ser tuyo.

**P: ¿Cuántas tablas debo crear?**
R: Depende de tu diseño. Entre 5 y 15 es razonable.

**P: ¿Es obligatorio normalizar TODO?**
R: Debes normalizar lo suficiente para demostrar que entiendes el concepto (mínimo 3FN para algunas tablas).

**P: ¿SQLite o PostgreSQL?**
R: SQLite es más fácil. PostgreSQL da puntos extra pero requiere más setup.

**P: ¿Qué hago con datos faltantes?**
R: Documenta tu decisión: ¿los eliminas? ¿Usas valores por defecto? ¿Los dejas como NULL?

---

## 🎯 Objetivos de Aprendizaje

Al completar este ejercicio habrás aprendido:

✅ Análisis exploratorio de datos
✅ Diseño de bases de datos relacionales
✅ Normalización (1FN, 2FN, 3FN)
✅ Implementación de claves primarias y foráneas
✅ ETL (Extract, Transform, Load) con Python
✅ SQL avanzado (JOINs, subconsultas, agregaciones)
✅ Buenas prácticas de documentación

---

## 🚀 ¡Manos a la Obra!

Este es un ejercicio **complejo pero realista**. Te preparará para:
- Entrevistas técnicas de Data Engineer
- Proyectos reales de bases de datos
- Diseño de sistemas escalables

**¡No te rindas!** Es normal encontrar desafíos. Busca ayuda cuando la necesites, pero asegúrate de **entender** cada decisión que tomes.

---

**Fecha de entrega**: [A definir por el profesor]  
**Repositorio**: https://github.com/TodoEconometria/ejercicios-bigdata  
**Ejercicio**: 05 - Base de Datos Relacional

---

**¡Buena suerte! 💪**
