# 💡 AYUDA - Ejercicio 01

## 🎯 Pistas y Consejos (Sin Spoilers)

Este archivo te da **pistas** para avanzar, pero **NO** resuelve el ejercicio por ti.

---

## 📊 Parte 1: Análisis Exploratorio

### Pista 1: Empezar Simple

```python
import pandas as pd
import os

# Lista todos los CSVs
ruta_datos = 'datos/csv_tienda_informatica'
archivos = os.listdir(ruta_datos)
print(f"Total de archivos: {len(archivos)}")
```

### Pista 2: Analizar Estructura

Para cada CSV, pregúntate:
- ¿Cuántas columnas tiene?
- ¿Qué tipos de datos?
- ¿Hay campos comunes entre archivos?
- ¿Hay datos faltantes?

```python
# Ejemplo básico
df = pd.read_csv('datos/csv_tienda_informatica/cpu.csv')

print("Columnas:", df.columns.tolist())
print("\nInfo del DataFrame:")
print(df.info())
print("\nDatos faltantes:")
print(df.isnull().sum())
```

### Pista 3: Identificar Patrones

Muchos productos tienen el fabricante en el nombre:
```python
# Ejemplo: "AMD Ryzen 7 7800X3D" → "AMD"
df['primer_palabra'] = df['name'].str.split().str[0]
print(df['primer_palabra'].value_counts())
```

---

## 🗂️ Parte 2: Diseño de Base de Datos

### Pista 4: Estructura Básica

**Pregunta clave**: ¿Creo UNA tabla para todos los productos o MUCHAS tablas?

**Opción A**: Tabla única `productos` (más simple)
- Todos los productos en una tabla
- Columnas comunes: id, nombre, precio, categoría
- Problema: ¿Cómo guardo specs técnicas diferentes?

**Opción B**: Tabla maestra + tablas específicas (más normalizado)
- `productos` (info común)
- `cpus`, `gpus`, `monitores`, etc. (specs específicas)
- Relación: 1 producto → 1 registro en tabla específica

### Pista 5: Normalización

**¿Qué puedes normalizar?**

1. **Categorías**: En lugar de texto "CPU" en cada fila, crea tabla `categorias`
2. **Fabricantes**: En lugar de "AMD" en el nombre, crea tabla `fabricantes`
3. **Marcas**: Similar a fabricantes
4. **Especificaciones comunes**: ¿Hay specs que se repiten?

**Ejemplo de normalización**:
```
Antes: 
productos(id, nombre="AMD Ryzen 7", precio, categoria="CPU")

Después:
productos(id, nombre="Ryzen 7", precio, id_categoria, id_fabricante)
categorias(id, nombre="CPU")
fabricantes(id, nombre="AMD")
```

### Pista 6: Relaciones

**Tipos de relaciones a considerar**:
- Producto → Categoría (N:1)
- Producto → Fabricante (N:1)
- Producto → Especificaciones (1:1)
- ¿Compatibilidad entre productos? (N:M) - Avanzado

### Pista 7: Claves Primarias

Cada tabla necesita una clave primaria:
```sql
-- Opción 1: ID autoincremental
CREATE TABLE productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- SQLite
    -- id SERIAL PRIMARY KEY,               -- PostgreSQL
    nombre TEXT
);

-- Opción 2: Código natural (si existe)
CREATE TABLE categorias (
    codigo VARCHAR(10) PRIMARY KEY,
    nombre VARCHAR(100)
);
```

### Pista 8: Claves Foráneas

Conecta tablas relacionadas:
```sql
CREATE TABLE productos (
    id INTEGER PRIMARY KEY,
    nombre TEXT,
    id_categoria INTEGER,
    FOREIGN KEY (id_categoria) REFERENCES categorias(id)
);
```

---

## 💻 Parte 3: Implementación

### Pista 9: Estrategia de Carga

**Orden recomendado**:
1. Crear TODAS las tablas primero (schema)
2. Cargar tablas de referencia (categorías, fabricantes)
3. Cargar productos principales
4. Cargar especificaciones técnicas

```python
# Pseudo-código
def cargar_datos():
    # 1. Crear schema
    crear_todas_las_tablas()
    
    # 2. Cargar referencias
    cargar_categorias()
    cargar_fabricantes()
    
    # 3. Cargar productos
    for csv_file in archivos_csv:
        df = pd.read_csv(csv_file)
        transformar_datos(df)
        insertar_en_bd(df)
```

### Pista 10: Extraer Fabricante

```python
def extraer_fabricante(nombre):
    """
    Extrae el fabricante del nombre del producto.
    Ejemplo: "AMD Ryzen 7" → "AMD"
    """
    primera_palabra = nombre.split()[0]
    
    # Lista de fabricantes conocidos
    fabricantes_conocidos = ['AMD', 'Intel', 'NVIDIA', 'Corsair', 'ASUS', ...]
    
    if primera_palabra in fabricantes_conocidos:
        return primera_palabra
    return 'Desconocido'
```

### Pista 11: Inserción con Validación

```python
def insertar_producto(cursor, producto):
    """Inserta un producto validando primero."""
    
    # Validar precio
    if producto['precio'] <= 0:
        print(f"⚠️  Precio inválido: {producto['nombre']}")
        return
    
    # Validar nombre no vacío
    if not producto['nombre']:
        print("⚠️  Nombre vacío")
        return
    
    # Insertar
    try:
        cursor.execute('''
            INSERT INTO productos (nombre, precio) 
            VALUES (?, ?)
        ''', (producto['nombre'], producto['precio']))
    except Exception as e:
        print(f"❌ Error: {e}")
```

### Pista 12: Transacciones

```python
def cargar_csv_seguro(conn, csv_file):
    """Carga un CSV usando transacciones."""
    cursor = conn.cursor()
    
    try:
        df = pd.read_csv(csv_file)
        
        for _, row in df.iterrows():
            cursor.execute('INSERT INTO ...', (...))
        
        conn.commit()  # Todo OK → confirmar
        print(f"✅ {csv_file} cargado")
        
    except Exception as e:
        conn.rollback()  # Error → revertir TODO
        print(f"❌ Error en {csv_file}: {e}")
```

### Pista 13: Manejo de Datos Faltantes

```python
# Opción 1: Reemplazar con valor por defecto
df['price'].fillna(0, inplace=True)

# Opción 2: Eliminar filas incompletas
df = df.dropna(subset=['price', 'name'])

# Opción 3: Dejar como NULL (None en Python)
# No hagas nada, Python maneja None → NULL en SQL
```

---

## 🔍 Parte 4: Consultas SQL

### Pista 14: JOINs Básicos

```sql
-- Productos con su categoría
SELECT p.nombre, p.precio, c.nombre as categoria
FROM productos p
JOIN categorias c ON p.id_categoria = c.id;

-- Productos con fabricante
SELECT p.nombre, f.nombre as fabricante, p.precio
FROM productos p
JOIN fabricantes f ON p.id_fabricante = f.id;
```

### Pista 15: Agregaciones Útiles

```sql
-- Precio promedio por categoría
SELECT c.nombre, AVG(p.precio) as precio_medio
FROM productos p
JOIN categorias c ON p.id_categoria = c.id
GROUP BY c.nombre;

-- Top 5 fabricantes con más productos
SELECT f.nombre, COUNT(*) as total_productos
FROM productos p
JOIN fabricantes f ON p.id_fabricante = f.id
GROUP BY f.nombre
ORDER BY total_productos DESC
LIMIT 5;
```

### Pista 16: Subconsultas

```sql
-- Productos más caros que el promedio de su categoría
SELECT p.nombre, p.precio, c.nombre as categoria
FROM productos p
JOIN categorias c ON p.id_categoria = c.id
WHERE p.precio > (
    SELECT AVG(precio) 
    FROM productos 
    WHERE id_categoria = p.id_categoria
);
```

### Pista 17: Consultas de Negocio

Piensa en preguntas que el negocio querría responder:
- ¿Qué productos tienen mejor margen?
- ¿Qué categoría genera más ingresos?
- ¿Qué fabricante domina cada categoría?
- ¿Qué productos están por debajo/encima del precio promedio?
- ¿Qué combinaciones de productos compran juntos? (avanzado)

---

## 🚨 Errores Comunes

### Error 1: "FOREIGN KEY constraint failed"

**Causa**: Intentas insertar un `id_categoria` que no existe en la tabla `categorias`.

**Solución**: Inserta PRIMERO las categorías, LUEGO los productos.

### Error 2: "Duplicate entry for PRIMARY KEY"

**Causa**: Intentas insertar un ID que ya existe.

**Solución**: Usa `AUTOINCREMENT` (SQLite) o `SERIAL` (PostgreSQL).

### Error 3: Base de datos no se crea

**Causa**: Permisos o ruta incorrecta.

**Solución**:
```python
import os
# Crear en la carpeta actual
db_path = os.path.join(os.getcwd(), 'mi_bd.db')
conn = sqlite3.connect(db_path)
```

### Error 4: Datos no se insertan

**Causa**: Olvidaste hacer `commit()`.

**Solución**:
```python
cursor.execute('INSERT ...')
conn.commit()  # ← ¡Importante!
```

---

## 📚 Estrategias de Debugging

### Estrategia 1: Empezar Pequeño

```python
# NO hagas esto primero:
# cargar_todos_los_csv()  # 25 archivos, 15k productos

# SÍ haz esto:
df_prueba = pd.read_csv('cpu.csv').head(10)  # Solo 10 filas
# Prueba con esto primero, cuando funcione → escala
```

### Estrategia 2: Logging

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def insertar_producto(producto):
    logger.info(f"Insertando: {producto['nombre']}")
    try:
        # ... código ...
        logger.info("✅ Éxito")
    except Exception as e:
        logger.error(f"❌ Error: {e}")
```

### Estrategia 3: Validación Incremental

```python
# Después de cada paso, verifica
conn = sqlite3.connect('bd.db')

# ¿Se crearon las tablas?
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
print("Tablas:", cursor.fetchall())

# ¿Se insertaron datos?
cursor.execute("SELECT COUNT(*) FROM productos")
print("Total productos:", cursor.fetchone()[0])
```

---

## 💡 Consejos Finales

### 1. Diseña en Papel Primero

No empieces a codificar sin un diseño claro:
- Dibuja el diagrama ER
- Lista todas las tablas
- Define las relaciones
- Solo entonces: codifica

### 2. Itera y Mejora

**Primera versión**: Simple, funcional
- Tablas básicas
- Datos cargados sin mucha normalización

**Segunda versión**: Normalizada
- Extrae fabricantes, categorías
- Añade claves foráneas

**Tercera versión**: Optimizada
- Índices
- Consultas eficientes
- Manejo robusto de errores

### 3. Documenta Mientras Haces

No dejes la documentación para el final:
```python
# MAL: Solo código
def f(x):
    return x.split()[0]

# BIEN: Con documentación
def extraer_fabricante(nombre_producto):
    """
    Extrae el fabricante del nombre del producto.
    
    Args:
        nombre_producto (str): Nombre completo del producto
        
    Returns:
        str: Nombre del fabricante
        
    Ejemplo:
        >>> extraer_fabricante("AMD Ryzen 7 7800X3D")
        "AMD"
    """
    return nombre_producto.split()[0]
```

### 4. Usa Control de Versiones

```bash
git init
git add .
git commit -m "Diseño inicial del esquema"

# Cada vez que logres algo:
git commit -m "Implementada carga de categorías"
git commit -m "Añadidas claves foráneas"
```

---

## 🆘 ¿Todavía Atascado?

### Checklist de Verificación

- [ ] ¿Leíste TODA la documentación?
- [ ] ¿Exploraste al menos 5 CSVs diferentes?
- [ ] ¿Dibujaste tu diagrama ER?
- [ ] ¿Probaste el código con datos pequeños primero?
- [ ] ¿Revisaste los ejemplos en `plantilla_base.py`?
- [ ] ¿Buscaste en la documentación oficial?
- [ ] ¿Consultaste recursos externos (tutoriales, foros)?

Si marcaste todo ✅ y sigues atascado:
1. Explica tu problema específico al profesor
2. Muestra lo que has intentado
3. Indica dónde exactamente te trabas

---

## 🎯 Recuerda

- **NO hay UNA solución correcta** - hay múltiples diseños válidos
- **El proceso importa tanto como el resultado**
- **Documenta tus decisiones y justifícalas**
- **Está bien equivocarse** - itera y mejora

---

**¡Tú puedes hacerlo! 💪**

Si has llegado hasta aquí, ya tienes suficientes pistas para empezar.

**Ahora: ¡cierra este archivo y empieza a diseñar!** ✏️
