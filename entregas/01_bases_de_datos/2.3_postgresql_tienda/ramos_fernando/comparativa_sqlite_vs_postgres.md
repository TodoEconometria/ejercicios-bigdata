# Comparativa: SQLite vs PostgreSQL

**Autor:** Fernando Ramos Treviño  
**Fecha:** 01/01/2026  
**Ejercicio:** 2.3 - Migración SQLite → PostgreSQL

---

## 1. Introducción

Este documento analiza las diferencias observadas durante la migración de tres modelos de bases de datos de tienda informática desde SQLite a PostgreSQL.

### Bases de datos migradas:
- **Modelo A**: 25 tablas, 56,454 registros
- **Modelo B**: 12 tablas, 57,289 registros
- **Modelo C**: 14 tablas, 113,770 registros

---

## 2. Diferencias en Tipos de Datos

### Mapeo de tipos realizado:

| SQLite | PostgreSQL | Justificación |
|--------|-----------|---------------|
| INTEGER | INTEGER | Equivalente directo |
| TEXT | VARCHAR(255) | Mayor control de longitud |
| REAL | NUMERIC(10,2) | Precisión decimal para precios |
| BLOB | BYTEA | Datos binarios |
| DECIMAL | NUMERIC(10,2) | Precisión fija |

### Observaciones:
- SQLite usa tipado dinámico, PostgreSQL usa tipado estático estricto
- PostgreSQL ofrece mayor precisión para datos numéricos (precios, cantidades)
- VARCHAR(255) en PostgreSQL vs TEXT ilimitado en SQLite mejora la validación de datos

---

## 3. Manejo de Palabras Reservadas

### Problema detectado:
El **Modelo A** contiene tablas con nombres que son palabras reservadas SQL:
- `case` (carcasa)
- Otras tablas con guiones: `case-fan`, `cpu-cooler`, etc.

### Solución implementada:
Se escaparon todos los nombres de tablas y columnas con comillas dobles:
```sql
CREATE TABLE "case" (...)
INSERT INTO "case-fan" (...)

Lección aprendida:
PostgreSQL es más estricto con palabras reservadas que SQLite. Buena práctica: evitar nombres de tablas con palabras reservadas o caracteres especiales.

4. Constraints y Claves Primarias
SQLite:
Permite claves primarias INTEGER con AUTOINCREMENT

Constraints menos estrictos

Mayor flexibilidad en tipos de datos

PostgreSQL:
Claves primarias con tipo SERIAL (equivalente a AUTOINCREMENT)

Constraints más estrictos desde la creación

Validación de tipos en tiempo de inserción

Migración realizada:
Primary Keys migradas correctamente

NOT NULL constraints preservados

Foreign Keys no implementadas en el modelo original (podría añadirse en PostgreSQL)

5. Rendimiento
Modelo A (56,454 registros):
SQLite: Base de datos única en archivo .db

PostgreSQL: Base de datos cliente-servidor

Observación: PostgreSQL mejor preparado para consultas complejas con múltiples JOINS

Modelo B y C (57k-113k registros):
PostgreSQL ofrece ventajas en:

Consultas concurrentes

Índices más sofisticados

Optimización de queries complejas

Trade-offs:
SQLite: Ideal para aplicaciones embebidas, sin configuración

PostgreSQL: Ideal para aplicaciones multiusuario, alta concurrencia

6. Escalabilidad
Análisis por modelo:
Aspecto	SQLite	PostgreSQL
Tamaño máximo BD	~281 TB	Ilimitado
Usuarios concurrentes	1 escritor	Múltiples
Transacciones	Bloques completos	Row-level locking
Replicación	No nativa	Nativa
Conclusión:
Para el catálogo de productos de 56,454 items (Modelo A), PostgreSQL escala mejor ante:

Múltiples usuarios consultando simultáneamente

Operaciones de escritura concurrentes (órdenes, inventario)

Crecimiento futuro del catálogo

7. Características Avanzadas
Ventajas de PostgreSQL identificadas:
Full-Text Search: Búsqueda de productos por descripción

JSON/JSONB: Almacenar especificaciones técnicas variables

Window Functions: Análisis de ventas por categorías

CTEs y Recursive Queries: Jerarquías de categorías

Extensiones: PostGIS para tiendas físicas con geolocalización

No disponible en SQLite:
Stored Procedures

Triggers complejos

Vistas materializadas

Particionamiento de tablas

8. Mantenimiento y Administración
SQLite:
✅ Cero configuración

✅ Backup = copiar archivo

❌ Sin herramientas de monitoreo nativas

PostgreSQL:
✅ pgAdmin para administración visual

✅ Logs detallados de queries

✅ VACUUM, ANALYZE para optimización

❌ Requiere configuración inicial

9. Conclusiones
¿Cuándo usar SQLite?
Prototipos rápidos (como este ejercicio inicial)

Aplicaciones móviles

Aplicaciones de escritorio monousuario

Bases de datos embebidas

¿Cuándo usar PostgreSQL?
Aplicaciones web multiusuario

E-commerce (como esta tienda informática)

Datos críticos que requieren ACID completo

Necesidad de consultas complejas y optimizadas

Recomendación para este proyecto:
Para una tienda informática real con el catálogo migrado (56k+ productos), PostgreSQL es la mejor opción por:

Soporte de múltiples usuarios concurrentes

Integridad referencial estricta

Mejor rendimiento en queries complejas (búsquedas, filtros, ordenaciones)

Escalabilidad ante crecimiento

10. Script de Migración
El script desarrollado (migracion_desde_sqlite.py) implementa:

✅ Migración automática de esquemas

✅ Mapeo de tipos de datos

✅ Escape de palabras reservadas

✅ Migración de datos con validación

✅ Reporte de progreso

Mejoras futuras posibles:
Migración de índices

Migración de foreign keys

Validación de integridad referencial

Logs de errores detallados