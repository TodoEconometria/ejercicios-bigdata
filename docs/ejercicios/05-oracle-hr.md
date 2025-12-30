# Ejercicio 3.1: Oracle con Base de Datos HR

> **Estado:** En construcción

---

## Descripción General

Trabajarás con **Oracle Database** usando la base de datos HR en su entorno nativo original.

**Duración estimada:** 5-7 horas
**Nivel:** Avanzado
**Prerequisitos:** Ejercicio 2.1 (PostgreSQL HR)

---

## Objetivos de Aprendizaje

Al completar este ejercicio serás capaz de:

- ✅ Instalar y configurar Oracle Database Express Edition (XE)
- ✅ Usar SQL Developer o SQL*Plus
- ✅ Trabajar con sintaxis específica de Oracle
- ✅ Crear secuencias y triggers
- ✅ Escribir procedimientos almacenados en PL/SQL
- ✅ Comparar Oracle con PostgreSQL
- ✅ Entender características enterprise de Oracle

---

## Oracle Database

Oracle es el motor de bases de datos relacional líder en el mercado enterprise.

**Características:**
- PL/SQL (lenguaje procedural)
- Particionamiento avanzado
- Replicación y alta disponibilidad
- Seguridad enterprise
- Optimizador de consultas muy potente

---

## Diferencias Oracle vs PostgreSQL

### Sintaxis

| Aspecto | Oracle | PostgreSQL |
|---------|--------|------------|
| Auto-increment | SEQUENCE | SERIAL |
| String concat | `\|\|` o `CONCAT()` | `\|\|` |
| Tipos VARCHAR | `VARCHAR2` | `VARCHAR` |
| LIMIT | `ROWNUM` o `FETCH FIRST` | `LIMIT` |
| Outer Join | `(+)` (legacy) | `LEFT/RIGHT JOIN` |

### Funcionalidad

- **PL/SQL vs PL/pgSQL**: Oracle tiene PL/SQL más maduro
- **Packages**: Oracle soporta packages (agrupación de procedimientos)
- **Triggers**: Sintaxis diferente
- **Performance**: Oracle optimizado para cargas enterprise

---

## Contenido del Ejercicio

El ejercicio completo está en:

```
ejercicios/01_bases_de_datos/3.1_oracle_hr/
```

### Datos

Scripts SQL originales de Oracle están en: `datos/oracle_hr/`

---

## Temas Cubiertos

### 1. Instalación y Configuración
- Instalar Oracle XE 21c
- Configurar listener
- Crear usuarios y permisos
- Conectar con SQL Developer

### 2. Sintaxis Oracle
- Tipos de datos específicos
- Funciones built-in de Oracle
- ROWNUM y paginación
- Hints del optimizador

### 3. PL/SQL Básico
- Bloques anónimos
- Variables y tipos
- Estructuras de control
- Manejo de excepciones

### 4. Objetos de Base de Datos
- Secuencias
- Triggers
- Vistas
- Sinónimos

### 5. Procedimientos y Funciones
- Crear procedimientos almacenados
- Parámetros IN/OUT/IN OUT
- Funciones que retornan valores

---

## Requisitos Técnicos

### Software Necesario

1. **Oracle Database 21c Express Edition (XE)** - Gratuito
   - [Descargar Oracle XE](https://www.oracle.com/database/technologies/xe-downloads.html)
   - Requiere cuenta Oracle (gratuita)
   - Limitaciones XE: 12GB RAM, 2 CPUs, 12GB datos de usuario

2. **SQL Developer** - Cliente gráfico oficial de Oracle
   - [Descargar SQL Developer](https://www.oracle.com/database/sqldeveloper/technologies/download/)
   - Alternativa: DBeaver con driver Oracle

3. **Oracle Instant Client** (opcional para conexiones remotas)

### Sistema Operativo

- **Windows:** Instalación directa
- **Mac/Linux:** Usar Docker
  ```bash
  docker pull container-registry.oracle.com/database/express:21.3.0-xe
  ```

---

## Entregas

Consulta las [instrucciones de entrega](../../entregas/01_bases_de_datos/) para saber qué archivos debes subir.

**Carpeta de entrega:**
```
entregas/01_bases_de_datos/tu_apellido_nombre/3.1_oracle_hr/
```

---

## Recursos de Apoyo

### Documentación Oficial
- [Oracle Database Documentation](https://docs.oracle.com/en/database/)
- [PL/SQL Language Reference](https://docs.oracle.com/en/database/oracle/oracle-database/21/lnpls/)

### Tutoriales
- [Oracle Live SQL](https://livesql.oracle.com/) - Práctica online gratuita
- [PL/SQL Tutorial](https://www.oracletutorial.com/plsql-tutorial/)

### Comparativas
- [Oracle vs PostgreSQL](https://www.postgresql.org/about/featurematrix/)
- [Migración Oracle → PostgreSQL](https://wiki.postgresql.org/wiki/Oracle_to_Postgres_Conversion)

---

## Próximos Pasos

Después de completar este ejercicio:

1. **Ejercicio 3.2** - Oracle Jardinería (más práctica con Oracle)
2. **Ejercicio 4.1** - SQL Server (otro motor enterprise)

---

**Fecha de publicación:** Por definir
**Última actualización:** 2025-12-17
