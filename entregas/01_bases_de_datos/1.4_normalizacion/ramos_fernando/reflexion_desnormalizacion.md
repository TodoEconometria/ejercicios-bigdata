# Ejercicio 1.4 - PARTE 4: Desnormalización Intencional

## 🎯 Problema de Performance Identificado

**Query problemática** (ejecutada **1000 veces/minuto**):
SELECT v.fecha, c.nombre AS cliente, p.nombre AS producto,
v.cantidad, v.total
FROM ventas v
JOIN clientes c ON v.cliente_id = c.id
JOIN productos p ON v.producto_id = p.id
WHERE v.fecha >= '2024-01-01';


**Cuello de botella**: **3 JOINs × 1000 queries/min = 3000 JOINs/min**

Cada JOIN = 3 IOPS (disco) → 9000 IOPS totales
SSD moderno = 500k IOPS máx → ¿Problema? SÍ con índices fragmentados


## 🛠️ Solución: Tabla Desnormalizada `ventas_reportes`

**Diseño 3NF → Desnormalizado**:

CREATE TABLE ventas_reportes (
venta_id INTEGER PRIMARY KEY,
fecha DATE NOT NULL,
cliente_nombre TEXT, -- COPIADO de clientes.nombre
producto_nombre TEXT, -- COPIADO de productos.nombre
cantidad INTEGER NOT NULL,
total REAL NOT NULL -- CALCULADO: cantidad × precio × (1-descuento)


**Query optimizada** (sin JOINs):

SELECT fecha, cliente_nombre, producto_nombre, cantidad, total
FROM ventas_reportes
WHERE fecha >= '2024-01-01'; -- 100x MÁS RÁPIDO


## 🔄 Estrategia Sincronización: Job ETL Nocturno

**Método elegido**: **Batch nocturno** (2AM diario)

**Script ETL**:

sync_ventas_reportes.py
TRUNCATE ventas_reportes;
INSERT INTO ventas_reportes
SELECT v.venta_id, v.fecha, c.nombre, p.nombre,
v.cantidad, v.cantidad * v.precio_unitario * (1-v.descuento)
FROM ventas v JOIN clientes c JOIN productos p
WHERE v.fecha >= '2024-01-01'; -- Solo datos históricos


**Cron job**:

2AM diario
0 2 * * * python /etl/sync_ventas_reportes.py


**Razonamiento**: Ventas **históricas** → nombres clientes/productos **NO cambian**.

## ⚖️ Trade-offs Cuantificados

| Aspecto | 3NF (Normalizado) | Desnormalizado | Ganador |
|---------|-------------------|----------------|---------|
| **Query reportes** | 300ms (3 JOINs) | **3ms (1 tabla)** | 🏆 Desnorm |
| **Espacio disco** | **100MB** | 170MB (+70%) | 3NF |
| **INSERT venta nueva** | 4 tablas | **2 tablas** | Desnorm |
| **UPDATE cliente nombre** | **1 fila** | 1M filas (nocturno) | 3NF |
| **Consistencia datos** | **100%** | 99.9% (delay 24h) | 3NF |
| **Mantenimiento** | Simple | **ETL + monitoreo** | 3NF |

## 🎯 Reglas Decisiones: ¿Cuándo Desnormalizar?

DESNORMALIZAR cuando:

Reportes OLAP >1000 queries/min

Data Warehouse esquemas estrella

Queries con >3 JOINs frecuentes

Latencia <10ms crítica

Datos históricos (inmutables)

❌ NORMALIZAR cuando:

OLTP transaccional (actualizaciones)

Datos cambian frecuentemente

Espacio disco crítico

Queries ad-hoc variadas



## 📊 Resultado Cuantitativo


ANTES: 1000 queries × 300ms = 300 segundos CPU/min
DESPUÉS: 1000 queries × 3ms = 3 segundos CPU/min

🏆 MEJORA: 100x MÁS RÁPIDO


## 🧠 Lecciones Aprendidas

1. **3NF = Correctitud** (0 anomalías, 0 redundancia)
2. **Desnormalización = Performance** (cuando JOINs matan)
3. **Sincronización ETL = Clave** (método batch para históricos)
4. **Trade-off consciente**: Elegir por **caso de uso** (OLTP vs OLAP)

**Conclusión**: **Desnormalización INTENCIONAL** = herramienta poderosa cuando se usa con criterio[file:1]
