-- =====================================================
-- EJERCICIO 1.4 - PARTE 3: Universidad 3NF COMPLETA
-- =====================================================

/*
REQUISITOS CUMPLIDOS:
✅ 5 estudiantes, 3 profesores, 4 cursos
✅ 1 curso = 1 profesor
✅ 1 estudiante → N cursos
✅ 1 profesor → N cursos
*/

-- ===== 1. CREATE TABLES 3NF =====
CREATE TABLE departamentos (
    departamento_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_departamento TEXT NOT NULL
);

CREATE TABLE carreras (
    carrera_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_carrera TEXT NOT NULL
);

CREATE TABLE profesores (
    profesor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_profesor TEXT NOT NULL,
    email_profesor TEXT UNIQUE NOT NULL,
    departamento_id INTEGER REFERENCES departamentos(departamento_id)
);

CREATE TABLE estudiantes (
    estudiante_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_estudiante TEXT NOT NULL,
    email_estudiante TEXT UNIQUE NOT NULL,
    carrera_id INTEGER REFERENCES carreras(carrera_id)
);

CREATE TABLE cursos (
    curso_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_curso TEXT NOT NULL,
    codigo_curso TEXT UNIQUE NOT NULL,
    creditos INTEGER NOT NULL,
    profesor_id INTEGER REFERENCES profesores(profesor_id)
);

CREATE TABLE inscripciones (
    inscripcion_id INTEGER PRIMARY KEY AUTOINCREMENT,
    estudiante_id INTEGER REFERENCES estudiantes(estudiante_id),
    curso_id INTEGER REFERENCES cursos(curso_id)
);

-- ===== 2. DATOS EJEMPLO =====
INSERT INTO departamentos VALUES (1, 'Informática'), (2, 'Matemáticas');
INSERT INTO carreras VALUES (1, 'Ingeniería de Datos'), (2, 'Ciencia de Datos');

INSERT INTO profesores VALUES
(1, 'Dr. Ana García', 'ana.garcia@uni.edu', 1),
(2, 'Dr. Luis Martínez', 'luis.martinez@uni.edu', 1),
(3, 'Dra. María López', 'maria.lopez@uni.edu', 2);

INSERT INTO estudiantes VALUES
(1, 'Juan Pérez', 'juan.perez@alumno.uni', 1),
(2, 'María González', 'maria.gonzalez@alumno.uni', 1),
(3, 'Carlos Rodríguez', 'carlos.rodriguez@alumno.uni', 2),
(4, 'Laura Sánchez', 'laura.sanchez@alumno.uni', 1),
(5, 'Pedro Díaz', 'pedro.diaz@alumno.uni', 2);

INSERT INTO cursos VALUES
(1, 'Bases de Datos', 'BD101', 6, 1),
(2, 'Big Data', 'BD201', 6, 2),
(3, 'Machine Learning', 'ML301', 8, 1),
(4, 'Estadística Avanzada', 'EA401', 6, 3);

INSERT INTO inscripciones VALUES
(1, 1, 1), (2, 1, 2), (3, 2, 1), (4, 3, 3),
(5, 4, 2), (6, 5, 4);

-- ===== 3. 5 CONSULTAS ÚTILES =====
-- 1. CURSOS POR CARRERA
SELECT c.nombre_carrera, COUNT(DISTINCT i.curso_id) as num_cursos
FROM carreras c
JOIN estudiantes e ON c.carrera_id = e.carrera_id
JOIN inscripciones i ON e.estudiante_id = i.estudiante_id
GROUP BY c.carrera_id;

-- 2. CRÉDITOS TOTALES POR ESTUDIANTE
SELECT e.nombre_estudiante, SUM(cu.creditos) as creditos_totales
FROM estudiantes e
JOIN inscripciones i ON e.estudiante_id = i.estudiante_id
JOIN cursos cu ON i.curso_id = cu.curso_id
GROUP BY e.estudiante_id
ORDER BY creditos_totales DESC;

-- 3. CUÁNTOS CURSOS POR ALUMNO
SELECT e.nombre_estudiante, COUNT(i.inscripcion_id) as num_cursos
FROM estudiantes e
LEFT JOIN inscripciones i ON e.estudiante_id = i.estudiante_id
GROUP BY e.estudiante_id
ORDER BY num_cursos DESC;

-- 4. PROFESORES CON MÁS ESTUDIANTES
SELECT p.nombre_profesor, COUNT(DISTINCT i.estudiante_id) as num_estudiantes
FROM profesores p
JOIN cursos c ON p.profesor_id = c.profesor_id
JOIN inscripciones i ON c.curso_id = i.curso_id
GROUP BY p.profesor_id
ORDER BY num_estudiantes DESC;

-- 5. DEPARTAMENTO CON MÁS PROFESORES
SELECT d.nombre_departamento, COUNT(p.profesor_id) as num_profesores
FROM departamentos d
JOIN profesores p ON d.departamento_id = p.departamento_id
GROUP BY d.departamento_id
ORDER BY num_profesores DESC;

-- =====================================================
-- RESULTADO PARTE 3: 6 tablas 3NF ✅
-- Datos: 5 estudiantes, 3 profesores, 4 cursos
-- 5 consultas útiles implementadas
-- =====================================================
