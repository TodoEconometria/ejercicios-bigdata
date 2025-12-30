# Base de Datos Jardinería

Esta carpeta contiene los scripts SQL de la **base de datos de una empresa de jardinería**.

---

## Descripción

Base de datos de ejemplo que modela una empresa de venta de productos de jardinería y plantas.

**Contiene:**
- Tabla `clientes` - Clientes de la empresa
- Tabla `empleados` - Empleados y organización
- Tabla `oficinas` - Oficinas de la empresa
- Tabla `pedidos` - Pedidos realizados
- Tabla `detalle_pedidos` - Líneas de cada pedido
- Tabla `productos` - Catálogo de productos
- Tabla `gamas_producto` - Categorías de productos
- Tabla `pagos` - Pagos realizados por clientes

---

## Archivos

Los scripts SQL se añadirán aquí:

- `schema.sql` - Estructura de tablas (DDL)
- `data.sql` - Datos de ejemplo (DML)
- `constraints.sql` - Constraints y foreign keys

---

## Uso

### Para PostgreSQL (Ejercicio 2.2)

Scripts optimizados para PostgreSQL con tipos de datos nativos.

### Para Oracle (Ejercicio 3.2)

Se requiere adaptar:
- Tipos de datos (`VARCHAR` → `VARCHAR2`)
- Auto-increment (`SERIAL` → `SEQUENCE`)
- Sintaxis de `INSERT`

---

## Diagrama ER

```mermaid
erDiagram
    OFICINAS {
        string codigo_oficina PK
        string ciudad
        string pais
        string region
        string codigo_postal
        string telefono
        string linea_direccion1
        string linea_direccion2
    }

    EMPLEADOS {
        int codigo_empleado PK
        string nombre
        string apellido1
        string apellido2
        string extension
        string email
        string codigo_oficina FK
        int codigo_jefe FK
        string puesto
    }

    CLIENTES {
        int codigo_cliente PK
        string nombre_cliente
        string nombre_contacto
        string apellido_contacto
        string telefono
        string linea_direccion1
        string ciudad
        string pais
        string codigo_postal
        int codigo_empleado_rep_ventas FK
        decimal limite_credito
    }

    GAMAS_PRODUCTO {
        string gama PK
        string descripcion_texto
        string descripcion_html
        string imagen
    }

    PRODUCTOS {
        string codigo_producto PK
        string nombre
        string gama FK
        string dimensiones
        string proveedor
        string descripcion
        int cantidad_en_stock
        decimal precio_venta
        decimal precio_proveedor
    }

    PEDIDOS {
        int codigo_pedido PK
        date fecha_pedido
        date fecha_esperada
        date fecha_entrega
        string estado
        text comentarios
        int codigo_cliente FK
    }

    DETALLE_PEDIDOS {
        int codigo_pedido PK_FK
        string codigo_producto PK_FK
        int cantidad
        decimal precio_unidad
        int numero_linea
    }

    PAGOS {
        int codigo_cliente PK_FK
        string forma_pago PK
        string id_transaccion PK
        date fecha_pago
        decimal total
    }

    OFICINAS ||--o{ EMPLEADOS : trabaja_en
    EMPLEADOS ||--o| EMPLEADOS : jefe_de
    EMPLEADOS ||--o{ CLIENTES : atiende
    CLIENTES ||--o{ PEDIDOS : realiza
    CLIENTES ||--o{ PAGOS : hace
    GAMAS_PRODUCTO ||--o{ PRODUCTOS : tiene
    PEDIDOS ||--o{ DETALLE_PEDIDOS : contiene
    PRODUCTOS ||--o{ DETALLE_PEDIDOS : incluido_en
```

---

## Casos de Uso

Esta base de datos es excelente para practicar:

1. **Consultas complejas con múltiples JOINs**
   - Empleados → Clientes → Pedidos → Detalles → Productos

2. **Análisis de ventas**
   - Total de ventas por cliente
   - Productos más vendidos
   - Rendimiento por empleado

3. **Gestión de inventario**
   - Stock disponible
   - Productos con bajo stock
   - Análisis de rotación

4. **Análisis temporal**
   - Evolución de ventas por mes/año
   - Estacionalidad en pedidos
   - Análisis de pagos

---

## Recursos

- Scripts SQL disponibles en repositorios públicos de bases de datos educativas

---

**Última actualización:** 2025-12-17
