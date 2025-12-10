"""
PLANTILLA BÁSICA - Ejercicio 01
================================
Este archivo contiene ejemplos BÁSICOS de conexión a bases de datos.
NO es el código completo - tú debes escribir tu propia solución.

Autor: TodoEconometria
"""

# ============================================
# OPCIÓN A: SQLite (Recomendado)
# ============================================

def ejemplo_sqlite():
    """Ejemplo básico de conexión a SQLite."""
    import sqlite3
    
    # Crear/conectar a base de datos
    conn = sqlite3.connect('mi_base_datos.db')
    cursor = conn.cursor()
    
    # Ejemplo: Crear una tabla
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ejemplo (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            precio REAL
        )
    ''')
    
    # Ejemplo: Insertar datos
    cursor.execute('''
        INSERT INTO ejemplo (nombre, precio) 
        VALUES (?, ?)
    ''', ('Producto 1', 99.99))
    
    # Guardar cambios
    conn.commit()
    
    # Ejemplo: Consultar datos
    cursor.execute('SELECT * FROM ejemplo')
    resultados = cursor.fetchall()
    print(resultados)
    
    # Cerrar conexión
    conn.close()


# ============================================
# OPCIÓN B: PostgreSQL (Avanzado)
# ============================================

def ejemplo_postgresql():
    """Ejemplo básico de conexión a PostgreSQL."""
    import psycopg2
    
    # Conectar a PostgreSQL
    conn = psycopg2.connect(
        host="localhost",
        database="mi_base_datos",
        user="mi_usuario",
        password="mi_password"
    )
    cursor = conn.cursor()
    
    # Ejemplo: Crear una tabla
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ejemplo (
            id SERIAL PRIMARY KEY,
            nombre VARCHAR(255) NOT NULL,
            precio DECIMAL(10,2)
        )
    ''')
    
    # Ejemplo: Insertar datos
    cursor.execute('''
        INSERT INTO ejemplo (nombre, precio) 
        VALUES (%s, %s)
    ''', ('Producto 1', 99.99))
    
    conn.commit()
    cursor.close()
    conn.close()


# ============================================
# OPCIÓN C: SQLAlchemy (ORM)
# ============================================

def ejemplo_sqlalchemy():
    """Ejemplo con SQLAlchemy - más moderno y flexible."""
    from sqlalchemy import create_engine, Column, Integer, String, Float
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker
    
    # Crear motor de BD (SQLite en este ejemplo)
    engine = create_engine('sqlite:///mi_base_datos.db')
    
    # Base para modelos
    Base = declarative_base()
    
    # Definir un modelo (tabla)
    class Producto(Base):
        __tablename__ = 'productos'
        
        id = Column(Integer, primary_key=True)
        nombre = Column(String(255), nullable=False)
        precio = Column(Float)
    
    # Crear tablas
    Base.metadata.create_all(engine)
    
    # Crear sesión
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Insertar datos
    nuevo_producto = Producto(nombre='Producto 1', precio=99.99)
    session.add(nuevo_producto)
    session.commit()
    
    # Consultar datos
    productos = session.query(Producto).all()
    for p in productos:
        print(f"{p.id}: {p.nombre} - ${p.precio}")
    
    session.close()


# ============================================
# LEER CSV CON PANDAS
# ============================================

def ejemplo_leer_csv():
    """Ejemplo de cómo leer un CSV con pandas."""
    import pandas as pd
    
    # Leer CSV
    df = pd.read_csv('datos/csv_tienda_informatica/cpu.csv')
    
    # Ver información básica
    print("Columnas:", df.columns.tolist())
    print("Filas:", len(df))
    print("\nPrimeras filas:")
    print(df.head())
    
    # Ver tipos de datos
    print("\nTipos de datos:")
    print(df.dtypes)
    
    # Ver datos faltantes
    print("\nDatos faltantes:")
    print(df.isnull().sum())
    
    # Ejemplo: Extraer fabricante del nombre
    df['fabricante'] = df['name'].str.split().str[0]
    print("\nFabricantes únicos:")
    print(df['fabricante'].value_counts())


# ============================================
# INSERTAR DATAFRAME EN BD
# ============================================

def ejemplo_dataframe_a_bd():
    """Ejemplo de cómo insertar un DataFrame en la BD."""
    import pandas as pd
    import sqlite3
    
    # Leer CSV
    df = pd.read_csv('datos/csv_tienda_informatica/cpu.csv')
    
    # Conectar a BD
    conn = sqlite3.connect('mi_base_datos.db')
    
    # Opción 1: Insertar todo el DataFrame
    # ¡CUIDADO! Esto NO aplica normalización
    df.to_sql('cpus_raw', conn, if_exists='replace', index=False)
    
    # Opción 2: Insertar fila por fila con control
    for index, row in df.iterrows():
        # Aquí puedes transformar los datos antes de insertar
        # Por ejemplo, separar fabricante, normalizar, etc.
        pass
    
    conn.close()


# ============================================
# TRANSACCIONES (Importante para consistencia)
# ============================================

def ejemplo_transacciones():
    """Ejemplo de uso de transacciones."""
    import sqlite3
    
    conn = sqlite3.connect('mi_base_datos.db')
    cursor = conn.cursor()
    
    try:
        # Iniciar transacción (implícita)
        cursor.execute('INSERT INTO tabla1 VALUES (?)', (1,))
        cursor.execute('INSERT INTO tabla2 VALUES (?)', (2,))
        
        # Si todo va bien, confirmar
        conn.commit()
        print("Transacción exitosa")
        
    except Exception as e:
        # Si algo falla, revertir TODO
        conn.rollback()
        print(f"Error: {e}")
        print("Transacción revertida")
    
    finally:
        conn.close()


# ============================================
# NOTAS IMPORTANTES
# ============================================

"""
ESTE ARCHIVO SOLO MUESTRA EJEMPLOS BÁSICOS.

TÚ DEBES:
1. Analizar los CSVs
2. Diseñar tu esquema relacional
3. Escribir el código de transformación y carga
4. Implementar claves foráneas y constraints
5. Crear consultas significativas

NO copies este código directamente - ¡úsalo solo como referencia!

Consulta la documentación oficial:
- SQLite: https://docs.python.org/3/library/sqlite3.html
- PostgreSQL: https://www.psycopg.org/docs/
- SQLAlchemy: https://docs.sqlalchemy.org/
- Pandas: https://pandas.pydata.org/docs/
"""

# ============================================
# MAIN (para probar los ejemplos)
# ============================================

if __name__ == "__main__":
    print("=" * 50)
    print("PLANTILLA BÁSICA - Ejercicio 01")
    print("=" * 50)
    print("\nEste archivo contiene ejemplos de referencia.")
    print("NO es el código completo del ejercicio.")
    print("\nLee ENUNCIADO_EJERCICIO.md para las instrucciones completas.")
    print("=" * 50)
