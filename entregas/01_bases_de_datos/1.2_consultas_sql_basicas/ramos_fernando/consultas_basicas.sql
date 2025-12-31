-- ═══════════════════════════════════════════════════════════════
-- Consulta 1.1: Listar todas las CPUs
-- ═══════════════════════════════════════════════════════════════
-- Objetivo: Practicar SELECT básico con múltiples columnas
-- Descripción: Muestra las CPUs más caras para identificar productos premium
-- Resultado esperado: Top 10 procesadores ordenados por precio descendente
-- ═══════════════════════════════════════════════════════════════

SELECT
    name,                       -- Nombre del procesador
    price,                      -- Precio en dólares
    core_count,                 -- Número de núcleos del procesador
    core_clock                  -- Velocidad base del procesador en GHz
FROM cpu                        -- Tabla de procesadores
ORDER BY price DESC             -- Ordenar de mayor a menor precio
LIMIT 10;                       -- Limitar resultados a los 10 más caros

-- ═══════════════════════════════════════════════════════════════
-- Consulta 1.2: CPUs de AMD baratas
-- ═══════════════════════════════════════════════════════════════
-- Objetivo: Practicar WHERE con operadores de comparación y LIKE
-- Descripción: Filtra CPUs de AMD con precio inferior a $200
-- Resultado esperado: CPUs AMD económicas ordenadas por precio ascendente
-- ═══════════════════════════════════════════════════════════════

SELECT
    name,           -- Nombre del procesador
    price,          -- Precio en dólares
    core_count,     -- Número de núcleos
    core_clock      -- Velocidad base del procesador
FROM cpu            -- Tabla de procesadores
WHERE name LIKE '%AMD%'     -- Filtrar solo procesadores AMD
  AND price < 200           -- Solo productos económicos (menos de $200)
ORDER BY price ASC;         -- Ordenar de menor a mayor precio

-- ═══════════════════════════════════════════════════════════════
-- Consulta 1.3: Motherboards por socket
-- ═══════════════════════════════════════════════════════════════
-- Objetivo: Filtrado por valores específicos usando IN
-- Descripción: Busca placas base compatibles con sockets modernos
-- Resultado esperado: Motherboards AM5 y LGA1700 agrupadas por socket
-- ═══════════════════════════════════════════════════════════════

SELECT
    name,                       -- Nombre de la placa base
    socket,                     -- Tipo de socket del procesador
    price,                      -- Precio en dólares
    form_factor                 -- Factor de forma (ATX, Micro-ATX, etc.)
FROM motherboard                -- Tabla de placas base
WHERE socket IN ('AM5', 'LGA1700')  -- Solo sockets AM5 o LGA1700
ORDER BY socket, price;         -- Ordenar por socket y luego por precio

-- ═══════════════════════════════════════════════════════════════
-- Consulta 1.4: Memoria RAM rápida
-- ═══════════════════════════════════════════════════════════════
-- Objetivo: Comparaciones numéricas y BETWEEN
-- Descripción: Busca RAM de alto rendimiento con buena relación precio/GB
-- Resultado esperado: RAM de 6000 MHz o superior en rango de precio medio
-- ═══════════════════════════════════════════════════════════════

SELECT
    name,                       -- Nombre del módulo RAM
    speed,                      -- Velocidad (frecuencia) de la RAM
    price,                      -- Precio en dólares
    price_per_gb                -- Precio por GB (métrica de eficiencia)
FROM memory                     -- Tabla de memoria RAM
WHERE speed LIKE '%6000%'       -- Velocidad contenga "6000" (6000 MHz o superior)
  AND price BETWEEN 80 AND 150  -- Rango de precio medio ($80-$150)
ORDER BY price_per_gb ASC;      -- Ordenar por mejor relación precio/GB

-- ═══════════════════════════════════════════════════════════════
-- Consulta 1.5: Tarjetas gráficas NVIDIA
-- ═══════════════════════════════════════════════════════════════
-- Objetivo: Practicar LIKE con múltiples patrones (OR)
-- Descripción: Busca tarjetas gráficas NVIDIA potentes (>=8GB VRAM)
-- Resultado esperado: GPUs NVIDIA ordenadas por memoria descendente
-- ═══════════════════════════════════════════════════════════════

SELECT
    name,                       -- Nombre de la tarjeta gráfica
    memory,                     -- Memoria VRAM en GB
    price                       -- Precio en dólares
FROM video_card                 -- Tabla de tarjetas gráficas
WHERE (name LIKE '%NVIDIA%'     -- Nombre contiene "NVIDIA"
   OR name LIKE '%GeForce%')    -- O nombre contiene "GeForce"
  AND memory >= 8               -- Solo tarjetas con 8GB VRAM o más
ORDER BY memory DESC, price;    -- Ordenar por memoria (desc) y luego precio

-- ═══════════════════════════════════════════════════════════════
-- Consulta 1.6: Monitores grandes
-- ═══════════════════════════════════════════════════════════════
-- Objetivo: Operadores de comparación y manejo de NULL
-- Descripción: Busca monitores gaming de alta frecuencia y gran tamaño
-- Resultado esperado: Monitores >=27" con >=144Hz excluyendo precios nulos
-- ═══════════════════════════════════════════════════════════════

SELECT
    name,                       -- Nombre del monitor
    screen_size,                -- Tamaño de pantalla en pulgadas
    refresh_rate,               -- Frecuencia de actualización en Hz
    price                       -- Precio en dólares
FROM monitor                    -- Tabla de monitores
WHERE screen_size >= 27         -- Pantalla de 27 pulgadas o más
  AND refresh_rate >= 144       -- Frecuencia de 144 Hz o superior (gaming)
  AND price IS NOT NULL         -- Excluir monitores sin precio definido
ORDER BY screen_size DESC;      -- Ordenar por tamaño descendente

-- ═══════════════════════════════════════════════════════════════
-- Consulta 1.7: Rangos de precio
-- ═══════════════════════════════════════════════════════════════
-- Objetivo: Practicar operador BETWEEN (inclusivo)
-- Descripción: Busca teclados de gama media
-- Resultado esperado: Teclados entre $50 y $150 ordenados por precio
-- ═══════════════════════════════════════════════════════════════

SELECT
    name,                       -- Nombre del teclado
    price,                      -- Precio en dólares
    style,                      -- Estilo del teclado (mechanical, membrane, etc.)
    switches                    -- Tipo de switches (si aplica)
FROM keyboard                   -- Tabla de teclados
WHERE price BETWEEN 50 AND 150  -- Rango de precio $50-$150 (ambos inclusivos)
ORDER BY price;                 -- Ordenar de menor a mayor precio

-- ═══════════════════════════════════════════════════════════════
-- Consulta 1.8: Productos sin especificar
-- ═══════════════════════════════════════════════════════════════
-- Objetivo: Practicar IS NULL (no usar = NULL)
-- Descripción: Busca CPUs sin gráficos integrados (típicamente de alto rendimiento)
-- Resultado esperado: CPUs sin GPU integrada ordenadas por precio (desc)
-- ═══════════════════════════════════════════════════════════════

SELECT
    name,                       -- Nombre del procesador
    price,                      -- Precio en dólares
    core_count                  -- Número de núcleos
FROM cpu                        -- Tabla de procesadores
WHERE graphics IS NULL          -- Solo CPUs sin gráficos integrados (campo NULL)
ORDER BY price DESC;            -- Ordenar de mayor a menor precio


-- ═══════════════════════════════════════════════════════════════
-- PARTE 2: MODELO B (tienda_modelo_b.db)
-- ═══════════════════════════════════════════════════════════════

-- ═══════════════════════════════════════════════════════════════
-- Consulta 2.1: Productos por fabricante
-- ═══════════════════════════════════════════════════════════════
-- Objetivo: SELECT simple en tabla normalizada con filtro por FK
-- Descripción: Lista productos de un fabricante específico (id=1)
-- Resultado esperado: Top 15 productos más caros de ese fabricante
-- ═══════════════════════════════════════════════════════════════

SELECT
    nombre,             -- Nombre del producto
    precio,             -- Precio en dólares
    categoria_id        -- ID de la categoría del producto
FROM productos          -- Tabla de productos normalizada
WHERE fabricante_id = 1 -- Solo productos del fabricante con ID 1
ORDER BY precio DESC    -- Ordenar de mayor a menor precio
LIMIT 15;               -- Limitar a 15 resultados

-- ═══════════════════════════════════════════════════════════════
-- Consulta 2.2: Productos de una categoría específica
-- ═══════════════════════════════════════════════════════════════
-- Objetivo: Filtrar por Foreign Key usando subconsulta o conociendo el ID
-- Descripción: Busca CPUs de gama media-alta (precio > $100)
-- Resultado esperado: CPUs ordenadas por precio descendente
-- Nota: Primero buscar el ID de la categoría "CPU" en tabla categorias
-- ═══════════════════════════════════════════════════════════════

SELECT
    nombre,                 -- Nombre del producto
    precio,                 -- Precio en dólares
    fabricante_id           -- ID del fabricante
FROM productos              -- Tabla de productos
WHERE categoria_id = (      -- Subconsulta para obtener ID de categoría CPU
    SELECT id FROM categorias WHERE nombre = 'CPU'
)
  AND precio > 100          -- Solo productos de gama media-alta
ORDER BY precio DESC;       -- Ordenar de mayor a menor precio

-- ═══════════════════════════════════════════════════════════════
-- Consulta 2.3: Productos con color específico
-- ═══════════════════════════════════════════════════════════════
-- Objetivo: Trabajar con tabla de relación N:M (muchos a muchos)
-- Descripción: Encuentra productos disponibles en color negro
-- Resultado esperado: Primeros 20 productos con color Black
-- Nota: Requiere JOIN entre productos_colores y colores
-- ═══════════════════════════════════════════════════════════════

SELECT
    pc.producto_id          -- ID del producto
FROM productos_colores pc   -- Tabla intermedia de relación N:M
WHERE pc.color_id = (       -- Subconsulta para obtener ID del color Black
    SELECT id FROM colores WHERE nombre = 'Black'
)
LIMIT 20;                   -- Limitar a 20 resultados

-- ═══════════════════════════════════════════════════════════════
-- Consulta 2.4: Fabricantes con productos
-- ═══════════════════════════════════════════════════════════════
-- Objetivo: SELECT simple en tabla maestra
-- Descripción: Lista completa de fabricantes en orden alfabético
-- Resultado esperado: Todos los fabricantes ordenados por nombre
-- ═══════════════════════════════════════════════════════════════

SELECT
    id,                     -- ID del fabricante
    nombre                  -- Nombre del fabricante
FROM fabricantes            -- Tabla de fabricantes
ORDER BY nombre ASC;        -- Ordenar alfabéticamente

-- ═══════════════════════════════════════════════════════════════
-- Consulta 2.5: Productos caros
-- ═══════════════════════════════════════════════════════════════
-- Objetivo: Filtrado simple por precio con límite
-- Descripción: Encuentra los 10 productos más caros del catálogo
-- Resultado esperado: Top 10 productos premium ordenados por precio
-- ═══════════════════════════════════════════════════════════════

SELECT
    nombre,                 -- Nombre del producto
    precio,                 -- Precio en dólares
    categoria_id            -- ID de la categoría
FROM productos              -- Tabla de productos
WHERE precio > 500          -- Solo productos premium (más de $500)
ORDER BY precio DESC        -- Ordenar de mayor a menor precio
LIMIT 10;                   -- Top 10 más caros

-- ═══════════════════════════════════════════════════════════════
-- Consulta 2.6: Búsqueda por nombre
-- ═══════════════════════════════════════════════════════════════
-- Objetivo: Practicar LIKE en modelo normalizado
-- Descripción: Busca productos con iluminación RGB
-- Resultado esperado: Productos con "RGB" en el nombre ordenados por precio
-- ═══════════════════════════════════════════════════════════════

SELECT
    nombre,                 -- Nombre del producto
    precio                  -- Precio en dólares
FROM productos              -- Tabla de productos
WHERE nombre LIKE '%RGB%'   -- Buscar "RGB" en cualquier parte del nombre (case-insensitive)
ORDER BY precio ASC;        -- Ordenar de menor a mayor precio

-- ═══════════════════════════════════════════════════════════════
-- Consulta 2.7: Productos sin fabricante
-- ═══════════════════════════════════════════════════════════════
-- Objetivo: Practicar IS NULL con Foreign Keys
-- Descripción: Cuenta productos huérfanos (sin fabricante asignado)
-- Resultado esperado: Número total de productos sin fabricante
-- ═══════════════════════════════════════════════════════════════

SELECT
    COUNT(*) AS total_sin_fabricante    -- Contar productos sin fabricante
FROM productos                          -- Tabla de productos
WHERE fabricante_id IS NULL;            -- Solo productos donde fabricante_id es NULL

-- ═══════════════════════════════════════════════════════════════
-- Consulta 2.8: Rango de precios por categoría
-- ═══════════════════════════════════════════════════════════════
-- Objetivo: Filtrado combinado (categoría + rango de precio)
-- Descripción: Busca memoria RAM de gama media ($40-$120)
-- Resultado esperado: Top 20 módulos RAM en ese rango de precio
-- Nota: Primero buscar ID de categoría "Memory" en tabla categorias
-- ═══════════════════════════════════════════════════════════════

SELECT
    nombre,                     -- Nombre del producto
    precio                      -- Precio en dólares
FROM productos                  -- Tabla de productos
WHERE categoria_id = (          -- Subconsulta para obtener ID categoría Memory
    SELECT id FROM categorias WHERE nombre = 'Memory'
)
  AND precio BETWEEN 40 AND 120 -- Rango de precio gama media
ORDER BY precio ASC             -- Ordenar de menor a mayor precio
LIMIT 20;                       -- Limitar a 20 resultados


-- ═══════════════════════════════════════════════════════════════
-- PARTE 3: MODELO C (tienda_modelo_c.db)
-- ═══════════════════════════════════════════════════════════════

-- ═══════════════════════════════════════════════════════════════
-- Consulta 3.1: Clientes registrados
-- ═══════════════════════════════════════════════════════════════
-- Objetivo: SELECT simple en tabla de clientes
-- Descripción: Lista todos los clientes mostrando clientes más recientes primero
-- Resultado esperado: Clientes ordenados por fecha de registro descendente
-- ═══════════════════════════════════════════════════════════════

SELECT
    nombre,                     -- Nombre del cliente
    apellido,                   -- Apellido del cliente
    email,                      -- Correo electrónico
    fecha_registro              -- Fecha de registro en la plataforma
FROM clientes                   -- Tabla de clientes
ORDER BY fecha_registro DESC;   -- Ordenar por más recientes primero

-- ═══════════════════════════════════════════════════════════════
-- Consulta 3.2: Pedidos pendientes
-- ═══════════════════════════════════════════════════════════════
-- Objetivo: Filtrar por valores múltiples en columna de estado
-- Descripción: Busca pedidos que aún no han sido enviados
-- Resultado esperado: Pedidos con estado 'pendiente' o 'procesando'
-- ═══════════════════════════════════════════════════════════════

SELECT
    id,                         -- ID del pedido
    cliente_id,                 -- ID del cliente que realizó el pedido
    fecha,                      -- Fecha del pedido
    estado,                     -- Estado actual del pedido
    total                       -- Monto total del pedido
FROM pedidos                    -- Tabla de pedidos
WHERE estado IN ('pendiente', 'procesando')  -- Solo pedidos no enviados aún
ORDER BY fecha DESC;            -- Ordenar por fecha descendente (más recientes primero)

-- ═══════════════════════════════════════════════════════════════
-- Consulta 3.3: Productos con poco stock
-- ═══════════════════════════════════════════════════════════════
-- Objetivo: Comparar columnas entre sí (no con valores fijos)
-- Descripción: Identifica productos que necesitan reposición urgente
-- Resultado esperado: Productos donde stock actual < stock mínimo
-- ═══════════════════════════════════════════════════════════════

SELECT
    producto_id,                -- ID del producto
    cantidad_stock,             -- Cantidad actual en inventario
    stock_minimo,               -- Cantidad mínima recomendada
    ubicacion                   -- Ubicación en almacén
FROM inventario                 -- Tabla de inventario
WHERE cantidad_stock < stock_minimo  -- Productos por debajo del stock mínimo
ORDER BY cantidad_stock ASC;    -- Ordenar por los más críticos primero (menor stock)

-- ═══════════════════════════════════════════════════════════════
-- Consulta 3.4: Carritos activos
-- ═══════════════════════════════════════════════════════════════
-- Objetivo: Filtrar por boolean (campo activo = 1)
-- Descripción: Busca carritos de compra activos (sesiones en curso)
-- Resultado esperado: Carritos activos ordenados por última modificación
-- ═══════════════════════════════════════════════════════════════

SELECT
    id,                         -- ID del carrito
    cliente_id,                 -- ID del cliente dueño del carrito
    fecha_creacion,             -- Fecha de creación del carrito
    ultima_modificacion         -- Última vez que se modificó el carrito
FROM carritos                   -- Tabla de carritos de compra
WHERE activo = 1                -- Solo carritos activos (valor booleano)
ORDER BY ultima_modificacion DESC;  -- Ordenar por actividad más reciente
