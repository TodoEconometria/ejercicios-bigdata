# 📚 Tarea 1 - Ejercicio 01: Base de Datos Relacional - Tienda Informática

## 🎯 Objetivo

Diseñar e implementar una base de datos relacional para una tienda de componentes informáticos, aplicando normalización y SQL avanzado.

---

## 📅 Fechas

- **Publicación**: [A definir por el profesor]
- **Fecha límite**: [A definir por el profesor], 23:59
- **Duración estimada**: 2-3 semanas

---

## 📥 Recursos Necesarios

### Documentación (en el repositorio)
- **Enunciado completo**: [`ejercicios/01_tienda_informatica/ENUNCIADO.md`](https://github.com/TodoEconometria/ejercicios-bigdata/blob/main/ejercicios/01_tienda_informatica/ENUNCIADO.md)
- **Instrucciones de entrega**: [`ejercicios/01_tienda_informatica/README.md`](https://github.com/TodoEconometria/ejercicios-bigdata/blob/main/ejercicios/01_tienda_informatica/README.md)
- **Guía de ayuda**: [`ejercicios/01_tienda_informatica/AYUDA.md`](https://github.com/TodoEconometria/ejercicios-bigdata/blob/main/ejercicios/01_tienda_informatica/AYUDA.md)
- **Código de ejemplo**: [`plantilla_base.py`](https://github.com/TodoEconometria/ejercicios-bigdata/blob/main/ejercicios/01_tienda_informatica/plantilla_base.py)

### Datos
📥 **Descargar CSV**: [**LINK A PROPORCIONAR POR EL PROFESOR**]

Archivo: `csv_tienda_informatica.zip` (~25 MB)
Contiene: 25 archivos CSV con ~15,000 productos de componentes informáticos

---

## 📤 Cómo Entregar

### Paso 1: Actualizar tu fork
```bash
git pull upstream main
```

### Paso 2: Descargar los datos
- Descarga el ZIP del link de arriba
- Colócalo en `ejercicios/01_tienda_informatica/`
- Descomprímelo: `unzip csv_tienda_informatica.zip -d datos/`

### Paso 3: Crear tu rama
```bash
git checkout -b tu-apellido-ejercicio01
```

### Paso 4: Trabajar en tu solución
Crea tu carpeta en:
```
ejercicios/01_tienda_informatica/soluciones/tu_apellido_nombre/
```

Sigue la estructura especificada en el README.md

### Paso 5: Pull Request
- Commit y push a tu fork
- Crea PR desde tu fork a `TodoEconometria/ejercicios-bigdata`
- Título: `Ejercicio 01 - Tu Apellido Nombre`

**Consulta el [README del ejercicio](https://github.com/TodoEconometria/ejercicios-bigdata/blob/main/ejercicios/01_tienda_informatica/README.md) para instrucciones detalladas.**

---

## 📊 Qué Entregar

| Parte | Descripción | Puntos |
|-------|-------------|--------|
| **Análisis Exploratorio** | Exploración de los 25 CSVs, patrones, problemas | 20 pts |
| **Diseño Relacional** | Diagrama ER, esquema SQL, normalización (3FN) | 30 pts |
| **Implementación** | Script Python que carga datos en SQLite/PostgreSQL | 30 pts |
| **Consultas SQL** | Mínimo 8 consultas con JOINs, subconsultas, agregaciones | 15 pts |
| **Documentación** | README, comentarios, instrucciones | 5 pts |
| **Bonus** | PostgreSQL, índices, tests, dashboard | +15 pts |

**Total**: 100 pts + hasta 15 pts bonus

---

## ⚠️ Importante

- ❌ **NO subas los archivos CSV** al repositorio (están en el .gitignore)
- ❌ **NO subas las bases de datos (.db)** al repositorio
- ✅ **SÍ trabaja en tu propia carpeta**: `soluciones/tu_apellido_nombre/`
- ✅ **SÍ documenta** todas tus decisiones de diseño
- ✅ **SÍ justifica** por qué elegiste tu estructura de BD

---

## 📚 Lo Que Aprenderás

- Análisis exploratorio de datos
- Diseño de bases de datos relacionales
- Normalización (1FN, 2FN, 3FN)
- Implementación de esquemas SQL
- ETL (Extract, Transform, Load) con Python
- SQL avanzado (JOINs, subconsultas, agregaciones)
- Documentación técnica

---

## ❓ Preguntas y Dudas

**Usa los comentarios de este issue** para hacer preguntas. Responderé aquí para que todos se beneficien.

**Preguntas comunes**:
- "¿Dónde descargo los datos?" → Ver link de arriba
- "¿Cuántas tablas debo crear?" → Entre 5 y 15 es razonable, depende de tu diseño
- "¿SQLite o PostgreSQL?" → SQLite es más fácil, PostgreSQL da +5 pts extra
- "¿Puedo usar IA?" → Sí, como herramienta de ayuda, pero debes entender todo

---

## 🚀 ¡Empecemos!

1. Lee el **enunciado completo** en el repositorio
2. Descarga los **datos**
3. Consulta la **guía de ayuda** cuando la necesites
4. Pregunta tus dudas **aquí en los comentarios**

**¡Buena suerte! 💪**

---

**Repositorio**: https://github.com/TodoEconometria/ejercicios-bigdata
**Ejercicio 01**: Base de Datos Relacional - Tienda Informática
