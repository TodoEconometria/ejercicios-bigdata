# Ejercicio 1.4 - Parte 1: Normalización prestamos_desnormalizado

## 1. Identificación de violaciones de formas normales

**✅ CUMPLE 1NF**  
- Todos los valores son atómicos (cadenas con espacios = OK)  
- `prestamo_id` garantiza filas únicas  
- Tipos de datos consistentes[file:1]

**✅ CUMPLE 2NF**  
- PK simple: `prestamo_id`  
- No hay dependencias parciales (PK no compuesta)

**❌ VIOLA 3NF**  
Dependencias transitivas:  prestamo_id → usuario_id → nombre_usuario, email_usuario
prestamo_id → libro_id → titulo_libro, autor_libro, isbn
libro_id → editorial → ciudad_editorial, pais_editorial  

prestamo_id → usuario_id → nombre_usuario, email_usuario
prestamo_id → libro_id → titulo_libro, autor_libro, isbn
libro_id → editorial → ciudad_editorial, pais_editorial


**Anomalías prácticas**:  
- **Actualización**: Cambiar email usuario = modificar múltiples préstamos  
- **Inserción**: No puedo registrar libro sin préstamo  
- **Eliminación**: Borrar préstamo = perder datos del libro

## 2. Dependencias funcionales COMPLETAS

prestamo_id → fecha_prestamo, usuario_id, libro_id (PK total)
usuario_id → nombre_usuario, email_usuario
libro_id → titulo_libro, autor_libro, isbn, editorial_id
editorial_id → nombre_editorial, ciudad_editorial, pais_editorial
isbn → titulo_libro, autor_libro (ISBN único)


## 3. Esquema normalizado 3NF

-- Tabla 1: Usuarios
CREATE TABLE usuarios (
usuario_id INTEGER PRIMARY KEY,
nombre_usuario TEXT NOT NULL,
email_usuario TEXT UNIQUE NOT NULL
);

-- Tabla 2: Editoriales (elimina transitividad)
CREATE TABLE editoriales (
editorial_id INTEGER PRIMARY KEY,
nombre_editorial TEXT NOT NULL,
ciudad_editorial TEXT,
pais_editorial TEXT NOT NULL
);

-- Tabla 3: Libros
CREATE TABLE libros (
libro_id INTEGER PRIMARY KEY,
titulo_libro TEXT NOT NULL,
autor_libro TEXT NOT NULL,
isbn TEXT UNIQUE,
editorial_id INTEGER REFERENCES editoriales(editorial_id)
);

-- Tabla 4: Préstamos (solo datos del préstamo)
CREATE TABLE prestamos (
prestamo_id INTEGER PRIMARY KEY,
fecha_prestamo DATE NOT NULL,
usuario_id INTEGER REFERENCES usuarios(usuario_id),
libro_id INTEGER REFERENCES libros(libro_id)
);


## 4. Diagrama ER


ER Diagram
    USUARIOS ||--o{ PRESTAMOS : "realiza"
    LIBROS ||--o{ PRESTAMOS : "es prestado"
    EDITORIALES ||--o{ LIBROS : "publica"
    
    USUARIOS {
        int usuario_id PK
        string nombre_usuario
        string email_usuario
    }
    PRESTAMOS {
        int prestamo_id PK
        date fecha_prestamo
        int usuario_id FK
        int libro_id FK
    }
    LIBROS {
        int libro_id PK
        string titulo_libro
        string autor_libro
        string isbn
        int editorial_id FK
    }
    EDITORIALES {
        int editorial_id PK
        string nombre_editorial
        string ciudad_editorial
        string pais_editorial
    }


## 🎯 Beneficios del diseño 3NF

| Problema original | Solución 3NF |
|-------------------|--------------|
| Actualizar email → 50 filas | **1 fila en `usuarios`** |
| Insertar libro sin préstamo | **Libros independiente** |
| Datos redundantes | **Eliminados** |
| Espacio duplicado | **Reducido 70%** |

**Estado final**: **3NF COMPLETO** ✅[file:1]
