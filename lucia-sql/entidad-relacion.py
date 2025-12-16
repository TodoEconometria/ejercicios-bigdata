
import pandas as pd
import os
from collections import defaultdict


class TiendaInformaticaER:
    def __init__(self, carpeta_csv="csv_tienda_informatica"):
        self.carpeta_csv = carpeta_csv
        self.productos = []  # Lista unificada de productos
        self.categorias = {}  # {nombre: id}
        self.fabricantes = {}  # {nombre: id}
        self.colores = {}  # {nombre: id}
        self.memoria = []

    def procesar_csvs(self):
        """Procesa todos los CSVs y construye las tablas"""
        print("=" * 80)
        print("🏪 PROCESANDO TIENDA DE INFORMÁTICA")
        print("=" * 80)

        if not os.path.exists(self.carpeta_csv):
            print(f"❌ Crea la carpeta '{self.carpeta_csv}' y coloca los CSVs")
            return False

        archivos = [f for f in os.listdir(self.carpeta_csv) if f.endswith('.csv')]

        if not archivos:
            print(f"❌ No hay archivos CSV en '{self.carpeta_csv}'")
            return False

        print(f"\n📦 Procesando {len(archivos)} categorías de productos...\n")

        id_producto = 1
        id_categoria = 1
        id_fabricante = 1
        id_color = 1
        id_memoria = 1

        for archivo in archivos:
            nombre_categoria = archivo.replace('.csv', '').upper()
            ruta = os.path.join(self.carpeta_csv, archivo)

            try:
                df = pd.read_csv(ruta)
                print(f"   📁 {archivo:45s} → {len(df):4d} productos")

                # Registrar categoría
                if nombre_categoria not in self.categorias:
                    self.categorias[nombre_categoria] = id_categoria
                    id_categoria += 1

                cat_id = self.categorias[nombre_categoria]

                # Procesar cada producto del CSV
                for idx, row in df.iterrows():
                    # Detectar columnas de nombre y precio
                    nombre = self._extraer_nombre(row, df.columns)
                    precio = self._extraer_precio(row, df.columns)
                    color = self._extraer_color(row, df.columns)

                    if not nombre or not precio:
                        continue

                    # Extraer fabricante (primera palabra del nombre)
                    fabricante = self._extraer_fabricante(nombre)

                    # Registrar fabricante
                    if fabricante not in self.fabricantes:
                        self.fabricantes[fabricante] = id_fabricante
                        id_fabricante += 1

                    # Registrar color
                    if color and color not in self.colores:
                        self.colores[color] = id_color
                        id_color += 1

                    # Crear producto
                    producto = {
                        'id_producto': id_producto,
                        'name': nombre,
                        'price': precio,
                        'color': color,
                        'tipo': nombre_categoria,
                        'id_categoria': cat_id,
                        'id_fabricante': self.fabricantes[fabricante],
                        'id_color': self.colores.get(color, None),
                        'id_memoria': id_memoria
                    }

                    self.productos.append(producto)

                    # ➤ Extraer memoria
                    mem_valor = self._extraer_memoria(row, df.columns)
                    if mem_valor is not None:
                        memoria = {
                            'id_memoria': id_memoria,
                            'valor': mem_valor,
                            'id_producto': id_producto  # Relación 1:1
                        }
                        self.memoria.append(memoria)
                        id_memoria += 1

                    id_producto += 1

            except Exception as e:
                print(f"   ⚠️  Error en {archivo}: {e}")

        print(f"\n✅ Procesamiento completado:")
        print(f"   • Productos: {len(self.productos)}")
        print(f"   • Categorías: {len(self.categorias)}")
        print(f"   • Fabricantes: {len(self.fabricantes)}")
        print(f"   • Colores: {len(self.colores)}")

        return True

    def _extraer_nombre(self, row, columnas):
        """Extrae el nombre del producto"""
        # Buscar columnas comunes de nombre
        nombres_posibles = ['name', 'nombre', 'product', 'producto', 'title', 'titulo', 'model', 'modelo']

        for col in columnas:
            if any(n in col.lower() for n in nombres_posibles):
                valor = str(row[col])
                if valor and valor != 'nan' and len(valor) > 3:
                    return valor

        # Si no encuentra, usar la primera columna de texto
        for col in columnas:
            valor = str(row[col])
            if valor and valor != 'nan' and len(valor) > 10:
                return valor

        return None

    def _extraer_precio(self, row, columnas):
        """Extrae el precio del producto"""
        # Buscar columnas de precio
        precios_posibles = ['price', 'precio', 'cost', 'costo', 'value', 'valor', 'pvp']

        for col in columnas:
            if any(p in col.lower() for p in precios_posibles):
                try:
                    valor = str(row[col])
                    # Limpiar: remover símbolos de moneda y comas
                    valor_limpio = valor.replace('$', '').replace('€', '').replace(',', '').replace(' ', '')
                    precio = float(valor_limpio)
                    if precio > 0:
                        return precio
                except:
                    continue

        # Buscar cualquier columna numérica que parezca precio
        for col in columnas:
            try:
                valor = float(row[col])
                if 10 <= valor <= 100000:  # Rango razonable de precios
                    return valor
            except:
                continue

        return None

    def _extraer_color(self, row, columnas):
        """Extrae el color del producto"""
        colores_posibles = ['color', 'colour', 'col']

        for col in columnas:
            if any(c in col.lower() for c in colores_posibles):
                valor = str(row[col])
                if valor and valor != 'nan':
                    return valor.upper()

        return None

    def _extraer_fabricante(self, nombre):
        """Extrae el fabricante (primera palabra del nombre)"""
        if not nombre:
            return "DESCONOCIDO"

        # Obtener primera palabra
        palabras = nombre.split()
        if not palabras:
            return "DESCONOCIDO"

        primera_palabra = palabras[0]

        # Limpiar caracteres especiales pero mantener guiones y números
        fabricante = ''.join(c for c in primera_palabra if c.isalnum() or c in ['-', '_'])

        # Mapeo de fabricantes conocidos para unificar variaciones
        mapeo_fabricantes = {
            'AMD': ['AMD', 'RYZEN'],
            'INTEL': ['INTEL', 'CORE'],
            'NVIDIA': ['NVIDIA', 'GEFORCE', 'RTX', 'GTX'],
            'ASUS': ['ASUS', 'ROG', 'TUF'],
            'MSI': ['MSI'],
            'GIGABYTE': ['GIGABYTE', 'AORUS'],
            'CORSAIR': ['CORSAIR'],
            'KINGSTON': ['KINGSTON', 'HYPERX'],
            'SAMSUNG': ['SAMSUNG'],
            'WESTERN': ['WESTERN', 'WD'],
            'SEAGATE': ['SEAGATE'],
            'CRUCIAL': ['CRUCIAL'],
            'GSKILL': ['G.SKILL', 'GSKILL'],
            'COOLERMASTER': ['COOLER', 'COOLERMASTER'],
            'NZXT': ['NZXT'],
            'THERMALTAKE': ['THERMALTAKE'],
            'EVGA': ['EVGA'],
            'ASROCK': ['ASROCK']
        }

        fabricante_upper = fabricante.upper()

        # Buscar en el mapeo
        for fab_principal, variaciones in mapeo_fabricantes.items():
            if any(var in fabricante_upper for var in variaciones):
                return fab_principal

        return fabricante_upper if fabricante else "DESCONOCIDO"

    def _extraer_memoria(self, row, columnas):
        for col in columnas:
            if "memory" in col.lower() or "capacity" in col.lower():
                valor = row[col]
                if pd.notna(valor):  # Evitar NaN
                    return valor
        return None

    def generar_tablas_sql(self, archivo="tienda_informatica.sql"):
        """Genera el script SQL completo"""
        print("\n" + "=" * 80)
        print("📝 GENERANDO SCRIPT SQL...")
        print("=" * 80)

        sql = "-- =====================================================\n"
        sql += "-- BASE DE DATOS: TIENDA DE INFORMÁTICA\n"
        sql += "-- Generado automáticamente\n"
        sql += "-- =====================================================\n\n"

        # DROP TABLES
        sql += "-- Eliminar tablas si existen\n"
        sql += "DROP TABLE IF EXISTS PRODUCTO;\n"
        sql += "DROP TABLE IF EXISTS CATEGORIA;\n"
        sql += "DROP TABLE IF EXISTS FABRICANTE;\n"
        sql += "DROP TABLE IF EXISTS COLOR;\n\n"

        # TABLA CATEGORIAS
        sql += "-- =====================================================\n"
        sql += "-- TABLA: CATEGORIA\n"
        sql += "-- =====================================================\n"
        sql += "CREATE TABLE CATEGORIA (\n"
        sql += "    id_categoria INT PRIMARY KEY,\n"
        sql += "    nombre_categoria VARCHAR(100) NOT NULL\n"
        sql += ");\n\n"

        # TABLA FABRICANTES
        sql += "-- =====================================================\n"
        sql += "-- TABLA: FABRICANTE\n"
        sql += "-- =====================================================\n"
        sql += "CREATE TABLE FABRICANTE (\n"
        sql += "    id_fabricante INT PRIMARY KEY,\n"
        sql += "    nombre_fabricante VARCHAR(100) NOT NULL\n"
        sql += ");\n\n"

        # TABLA COLORES
        sql += "-- =====================================================\n"
        sql += "-- TABLA: COLOR\n"
        sql += "-- =====================================================\n"
        sql += "CREATE TABLE COLOR (\n"
        sql += "    id_color INT PRIMARY KEY,\n"
        sql += "    nombre_color VARCHAR(50) NOT NULL\n"
        sql += ");\n\n"

        # TABLA MEMORIA
        sql += "-- =====================================================\n"
        sql += "-- TABLA: MEMORIA\n"
        sql += "-- =====================================================\n"
        sql += "CREATE TABLE MEMORIA (\n"
        sql += "    id_memoria INT PRIMARY KEY,\n"
        sql += "    valor VARCHAR(100),\n"
        sql += "    id_producto INT UNIQUE,\n"
        sql += "    FOREIGN KEY (id_producto) REFERENCES PRODUCTO(id_producto)\n"
        sql += ");\n\n"

        # TABLA PRODUCTO (CENTRAL)
        sql += "-- =====================================================\n"
        sql += "-- TABLA: PRODUCTO (TABLA CENTRAL)\n"
        sql += "-- =====================================================\n"
        sql += "CREATE TABLE PRODUCTO (\n"
        sql += "    id_producto INT PRIMARY KEY,\n"
        sql += "    name VARCHAR(255) NOT NULL,\n"
        sql += "    price DECIMAL(10,2) NOT NULL,\n"
        sql += "    color VARCHAR(50),\n"
        sql += "    tipo VARCHAR(100),\n"
        sql += "    id_categoria INT NOT NULL,\n"
        sql += "    id_fabricante INT NOT NULL,\n"
        sql += "    id_color INT,\n"
        sql += "    FOREIGN KEY (id_categoria) REFERENCES CATEGORIA(id_categoria),\n"
        sql += "    FOREIGN KEY (id_fabricante) REFERENCES FABRICANTE(id_fabricante),\n"
        sql += "    FOREIGN KEY (id_color) REFERENCES COLOR(id_color)\n"
        sql += "    FOREIGN KEY (id_memoria) REFERENCES MEMORIA(id_memoria)\n"
        sql += ");\n\n"

        # INSERTS - CATEGORIAS
        sql += "-- =====================================================\n"
        sql += "-- INSERTAR CATEGORIAS\n"
        sql += "-- =====================================================\n"
        for nombre, id_cat in sorted(self.categorias.items(), key=lambda x: x[1]):
            sql += f"INSERT INTO CATEGORIA VALUES ({id_cat}, '{nombre}');\n"
        sql += "\n"

        # INSERTS - FABRICANTES
        sql += "-- =====================================================\n"
        sql += "-- INSERTAR FABRICANTES\n"
        sql += "-- =====================================================\n"
        for nombre, id_fab in sorted(self.fabricantes.items(), key=lambda x: x[1]):
            sql += f"INSERT INTO FABRICANTE VALUES ({id_fab}, '{nombre}');\n"
        sql += "\n"

        # INSERTS - COLORES
        sql += "-- =====================================================\n"
        sql += "-- INSERTAR COLORES\n"
        sql += "-- =====================================================\n"
        for nombre, id_col in sorted(self.colores.items(), key=lambda x: x[1]):
            sql += f"INSERT INTO COLOR VALUES ({id_col}, '{nombre}');\n"
        sql += "\n"

        # INSERTS - MEMORIAS
        sql += "-- =====================================================\n"
        sql += "-- INSERTAR MEMORIAS\n"
        sql += "-- =====================================================\n"
        for mem in self.memorias:
            valor_limpio = str(mem['valor']).replace("'", "''")
            sql += f"INSERT INTO MEMORIA VALUES ({mem['id_memoria']}, '{valor_limpio}', {mem['id_producto']});\n"
        sql += "\n"

        # INSERTS - PRODUCTOS (primeros 100 para no saturar)
        sql += "-- =====================================================\n"
        sql += f"-- INSERTAR PRODUCTOS (mostrando primeros 100 de {len(self.productos)})\n"
        sql += "-- =====================================================\n"

        for producto in self.productos[:100]:
            nombre_limpio = producto['name'].replace("'", "''")  # Escapar comillas
            color_valor = f"'{producto['color']}'" if producto['color'] else "NULL"
            id_color_valor = producto['id_color'] if producto['id_color'] else "NULL"

            sql += f"INSERT INTO PRODUCTO VALUES ("
            sql += f"{producto['id_producto']}, "
            sql += f"'{nombre_limpio}', "
            sql += f"{producto['price']:.2f}, "
            sql += f"{color_valor}, "
            sql += f"'{producto['tipo']}', "
            sql += f"{producto['id_categoria']}, "
            sql += f"{producto['id_fabricante']}, "
            sql += f"{id_color_valor}"
            sql += ");\n"


        if len(self.productos) > 100:
            sql += f"\n-- ... y {len(self.productos) - 100} productos más\n"

        # Guardar
        with open(archivo, 'w', encoding='utf-8') as f:
            f.write(sql)

        print(f"✅ Script SQL generado: {archivo}")
        print(f"   • {len(self.categorias)} categorías")
        print(f"   • {len(self.fabricantes)} fabricantes")
        print(f"   • {len(self.colores)} colores")
        print(f"   • {len(self.productos)} productos")

    def generar_diagrama_ascii(self):
        """Genera diagrama ER en texto"""
        print("\n" + "=" * 80)
        print("📐 DIAGRAMA ENTIDAD-RELACIÓN")
        print("=" * 80)
        print()
        print("                         ┌─────────────────────┐")
        print("                    ┌────│     CATEGORIA       │")
        print("                    │    │  id_categoria (PK)  │")
        print("                    │    │  nombre_categoria   │")
        print("                    │    └─────────────────────┘")
        print("                    │             ▲")
        print("                    │             │ 1")
        print("                    │             │")
        print("                    │    N        │")
        print("┌───────────────────┴─────────────┴───────────────────┐")
        print("│              PRODUCTO (TABLA CENTRAL)               │")
        print("│  ┌───────────────────────────────────────────────┐  │")
        print("│  │ id_producto (PK)                              │  │")
        print("│  │ name                                          │  │")
        print("│  │ price                                         │  │")
        print("│  │ color                                         │  │")
        print("│  │ tipo                                          │  │")
        print("│  │ id_categoria (FK) ────────────────────────┐   │  │")
        print("│  │ id_fabricante (FK) ─────────────┐         │   │  │")
        print("│  │ id_color (FK) ───────┐          │         │   │  │")
        print("│  └──────────────────────┼──────────┼─────────┼───┘  │")
        print("└─────────────────────────┼──────────┼─────────┼──────┘")
        print("                          │          │         │")
        print("                          │ 0..1     │ N       │ N")
        print("                          │          │         │")
        print("                          ▼          ▼         ▼")
        print("              ┌───────────────┐  ┌──────────────┐")
        print("              │    COLOR      │  │  FABRICANTE  │")
        print("              │ id_color (PK) │  │ id_fab (PK)  │")
        print("              │ nombre_color  │  │ nombre_fab   │")
        print("              └───────────────┘  └──────────────┘")
        print()
        print("CARDINALIDADES:")
        print("  • PRODUCTO N:1 CATEGORIA    (Un producto pertenece a UNA categoría)")
        print("  • PRODUCTO N:1 FABRICANTE   (Un producto tiene UN fabricante)")
        print("  • PRODUCTO N:1 COLOR        (Un producto puede tener UN color)")
        print()

    def generar_informe(self, archivo="informe_tienda.txt"):
        """Genera informe detallado"""
        with open(archivo, 'w', encoding='utf-8') as f:
            f.write("=" * 80 + "\n")
            f.write("INFORME DE ANÁLISIS - TIENDA DE INFORMÁTICA\n")
            f.write("=" * 80 + "\n\n")

            # Resumen
            f.write("RESUMEN GENERAL:\n")
            f.write("-" * 80 + "\n")
            f.write(f"Total de productos: {len(self.productos)}\n")
            f.write(f"Total de categorías: {len(self.categorias)}\n")
            f.write(f"Total de fabricantes: {len(self.fabricantes)}\n")
            f.write(f"Total de colores: {len(self.colores)}\n\n")

            # Categorías
            f.write("CATEGORÍAS:\n")
            f.write("-" * 80 + "\n")
            for nombre, id_cat in sorted(self.categorias.items(), key=lambda x: x[1]):
                productos_cat = len([p for p in self.productos if p['id_categoria'] == id_cat])
                f.write(f"  [{id_cat:2d}] {nombre:30s} → {productos_cat:4d} productos\n")
            f.write("\n")

            ## Fabricantes TOP 20
            f.write("TOP 20 FABRICANTES (por cantidad de productos):\n")
            f.write("-" * 80 + "\n")
            fab_count = defaultdict(int)
            fab_precios = defaultdict(list)
            for p in self.productos:
                fab_count[p['id_fabricante']] += 1
                fab_precios[p['id_fabricante']].append(p['price'])

            fab_ordenados = sorted(fab_count.items(), key=lambda x: x[1], reverse=True)[:20]
            for id_fab, count in fab_ordenados:
                nombre_fab = [n for n, i in self.fabricantes.items() if i == id_fab][0]
                precio_medio = sum(fab_precios[id_fab]) / len(fab_precios[id_fab]) if fab_precios[id_fab] else 0
                f.write(f"  {nombre_fab:20s} → {count:4d} productos (precio medio: ${precio_medio:.2f})\n")
            f.write("\n")

            # Colores
            if self.colores:
                f.write("COLORES DISPONIBLES:\n")
                f.write("-" * 80 + "\n")
                for nombre, id_col in sorted(self.colores.items(), key=lambda x: x[1]):
                    productos_col = len([p for p in self.productos if p.get('id_color') == id_col])
                    f.write(f"  [{id_col:2d}] {nombre:20s} → {productos_col:4d} productos\n")
                f.write("\n")

            # Muestra de productos
            f.write("MUESTRA DE PRODUCTOS (primeros 20):\n")
            f.write("-" * 80 + "\n")
            for p in self.productos[:20]:
                f.write(f"ID: {p['id_producto']:5d} | ")
                f.write(f"{p['name'][:50]:50s} | ")
                f.write(f"${p['price']:8.2f} | ")
                f.write(f"{p['tipo']}\n")

        print(f"📄 Informe generado: {archivo}")

    def exportar_csvs_normalizados(self):
        """Exporta las tablas normalizadas a CSV"""
        print("\n" + "=" * 80)
        print("💾 EXPORTANDO TABLAS NORMALIZADAS A CSV...")
        print("=" * 80)

        # PRODUCTOS
        df_productos = pd.DataFrame(self.productos)
        df_productos.to_csv('PRODUCTO.csv', index=False, encoding='utf-8')
        print(f"   ✓ PRODUCTO.csv → {len(df_productos)} registros")

        # CATEGORIAS
        df_categorias = pd.DataFrame([
            {'id_categoria': id_cat, 'nombre_categoria': nombre}
            for nombre, id_cat in self.categorias.items()
        ])
        df_categorias.to_csv('CATEGORIA.csv', index=False, encoding='utf-8')
        print(f"   ✓ CATEGORIA.csv → {len(df_categorias)} registros")

        # FABRICANTES
        df_fabricantes = pd.DataFrame([
            {'id_fabricante': id_fab, 'nombre_fabricante': nombre}
            for nombre, id_fab in self.fabricantes.items()
        ])
        df_fabricantes.to_csv('FABRICANTE.csv', index=False, encoding='utf-8')
        print(f"   ✓ FABRICANTE.csv → {len(df_fabricantes)} registros")

        # COLORES
        if self.colores:
            df_colores = pd.DataFrame([
                {'id_color': id_col, 'nombre_color': nombre}
                for nombre, id_col in self.colores.items()
            ])
            df_colores.to_csv('COLOR.csv', index=False, encoding='utf-8')
            print(f"   ✓ COLOR.csv → {len(df_colores)} registros")

        print("\n✅ Exportación completada")

    def ejecutar_todo(self):
        """Ejecuta el proceso completo"""
        print("\n" + "*" * 80)
        print("*" + " GENERADOR ER - TIENDA DE INFORMÁTICA ".center(78) + "*")
        print("*" * 80)

        if not self.procesar_csvs():
            return

        self.generar_diagrama_ascii()
        self.generar_tablas_sql()
        self.generar_informe()
        self.exportar_csvs_normalizados()

        print("\n" + "=" * 80)
        print("✅ PROCESO COMPLETADO")
        print("=" * 80)
        print("\n📂 Archivos generados:")
        print("   • tienda_informatica.sql   (Script SQL completo)")
        print("   • informe_tienda.txt       (Informe detallado)")
        print("   • PRODUCTO.csv             (Tabla normalizada)")
        print("   • CATEGORIA.csv            (Tabla normalizada)")
        print("   • FABRICANTE.csv           (Tabla normalizada)")
        print("   • COLOR.csv                (Tabla normalizada)")
        print()


# =====================================================
# MAIN
# =====================================================

def main():
    tienda = TiendaInformaticaER("csv_tienda_informatica")
    tienda.ejecutar_todo()


if __name__ == "__main__":
    main()