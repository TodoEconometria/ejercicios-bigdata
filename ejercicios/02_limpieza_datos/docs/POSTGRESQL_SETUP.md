# Instalación y Setup de PostgreSQL

Esta guía te ayudará a instalar y configurar PostgreSQL para el ejercicio.

---

## Windows

### Opción 1: Instalador Oficial (Recomendado)

1. **Descargar:**
   - https://www.postgresql.org/download/windows/
   - Elegir PostgreSQL 15 o 16

2. **Ejecutar instalador:**
   - Acepta configuración por defecto
   - **IMPORTANTE:** Anota la contraseña del usuario `postgres`
   - Puerto por defecto: `5432`

3. **Verificar instalación:**
   ```cmd
   # Abrir CMD o PowerShell
   psql --version
   # Debe mostrar: psql (PostgreSQL) 15.x
   ```

4. **Iniciar servicio:**
   ```cmd
   # Windows Services o:
   net start postgresql-x64-15
   ```

### Opción 2: Docker (Avanzado)

```cmd
docker pull postgres:15
docker run --name postgres-qog -e POSTGRES_PASSWORD=tu_password -p 5432:5432 -d postgres:15
```

---

## Mac

### Opción 1: Homebrew (Recomendado)

```bash
# 1. Instalar Homebrew si no lo tienes
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 2. Instalar PostgreSQL
brew install postgresql@15

# 3. Iniciar servicio
brew services start postgresql@15

# 4. Verificar
psql --version
```

### Opción 2: Postgres.app

1. Descargar: https://postgresapp.com/
2. Arrastrar a Applications
3. Abrir Postgres.app
4. Inicializar (clic en "Initialize")

---

## Linux (Ubuntu/Debian)

```bash
# 1. Actualizar repositorios
sudo apt update

# 2. Instalar PostgreSQL
sudo apt install postgresql postgresql-contrib

# 3. Verificar instalación
psql --version

# 4. Iniciar servicio
sudo systemctl start postgresql
sudo systemctl enable postgresql  # Auto-start en boot

# 5. Verificar servicio
sudo systemctl status postgresql
```

---

## Configuración Inicial

### 1. Conectar como superusuario

**Windows/Mac:**
```bash
psql -U postgres
# Pedirá password (el que pusiste en instalación)
```

**Linux:**
```bash
sudo -u postgres psql
```

### 2. Crear usuario para el proyecto

```sql
-- Crear usuario
CREATE USER tu_usuario WITH PASSWORD 'tu_password';

-- Dar permisos de crear bases de datos
ALTER USER tu_usuario CREATEDB;

-- Salir
\q
```

### 3. Crear base de datos del proyecto

**Desde terminal:**
```bash
psql -U tu_usuario -h localhost
```

**Desde psql:**
```sql
CREATE DATABASE qog_research;

-- Conectar a la BD
\c qog_research

-- Verificar
SELECT current_database();
```

### 4. Ejecutar esquema inicial

```bash
# Desde terminal (fuera de psql)
psql -U tu_usuario -d qog_research -f especificaciones/ESQUEMA_DB.sql

# O desde psql:
\i especificaciones/ESQUEMA_DB.sql
```

---

## Configuración de Conexión Python

### 1. Instalar driver

```bash
pip install psycopg2-binary
```

### 2. Crear archivo .env

```bash
# En la raíz del proyecto
cp .env.example .env
```

**Editar .env:**
```bash
DB_HOST=localhost
DB_PORT=5432
DB_NAME=qog_research
DB_USER=tu_usuario
DB_PASSWORD=tu_password
```

### 3. Test de conexión

```python
# test_connection.py
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

try:
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT'),
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD')
    )
    print("✅ Conexión exitosa!")

    cursor = conn.cursor()
    cursor.execute("SELECT version();")
    version = cursor.fetchone()[0]
    print(f"PostgreSQL: {version}")

    cursor.close()
    conn.close()

except Exception as e:
    print(f"❌ Error: {e}")
```

```bash
python test_connection.py
```

---

## Clientes GUI (Opcional)

### pgAdmin (Oficial PostgreSQL)

**Instalación:**
- Incluido con instalador PostgreSQL Windows
- Mac/Linux: https://www.pgadmin.org/download/

**Configuración:**
1. Abrir pgAdmin
2. Crear nuevo servidor:
   - Name: QoG Local
   - Host: localhost
   - Port: 5432
   - Database: qog_research
   - User: tu_usuario
   - Password: tu_password

### DBeaver (Universal)

**Instalación:**
- https://dbeaver.io/download/

**Ventajas:**
- Más ligero que pgAdmin
- Soporta múltiples BDs
- Interfaz más moderna

---

## Comandos Útiles PostgreSQL

### Comandos psql

```sql
-- Listar bases de datos
\l

-- Conectar a BD
\c qog_research

-- Listar tablas
\dt

-- Describir tabla
\d qog_data

-- Listar schemas
\dn

-- Ver vistas
\dv

-- Salir
\q
```

### Queries útiles

```sql
-- Ver tamaño de BD
SELECT pg_size_pretty(pg_database_size('qog_research'));

-- Ver tablas y tamaños
SELECT
    schemaname,
    tablename,
    pg_size_pretty(pg_total_relation_size(schemaname||'.'||tablename)) AS size
FROM pg_tables
WHERE schemaname = 'qog'
ORDER BY pg_total_relation_size(schemaname||'.'||tablename) DESC;

-- Contar filas en tabla
SELECT COUNT(*) FROM qog.qog_data;

-- Ver últimas filas insertadas
SELECT * FROM qog.qog_data
ORDER BY created_at DESC
LIMIT 10;
```

---

## Troubleshooting

### Error: "psql: command not found"

**Windows:**
Agregar a PATH:
```
C:\Program Files\PostgreSQL\15\bin
```

**Mac:**
```bash
echo 'export PATH="/opt/homebrew/opt/postgresql@15/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

### Error: "FATAL: password authentication failed"

1. Verificar password en .env
2. Resetear password:
```bash
# Como superusuario postgres
psql -U postgres
ALTER USER tu_usuario WITH PASSWORD 'nueva_password';
```

### Error: "could not connect to server"

**Verificar servicio corriendo:**

Windows:
```cmd
sc query postgresql-x64-15
```

Mac:
```bash
brew services list | grep postgres
```

Linux:
```bash
sudo systemctl status postgresql
```

**Iniciar si está parado:**
```bash
# Windows
net start postgresql-x64-15

# Mac
brew services start postgresql@15

# Linux
sudo systemctl start postgresql
```

### Error: "port 5432 already in use"

Algo está usando el puerto. Opciones:

1. Cambiar puerto PostgreSQL en `postgresql.conf`
2. Identificar qué lo usa:
```bash
# Windows
netstat -ano | findstr :5432

# Mac/Linux
lsof -i :5432
```

### Error: "permission denied for schema"

```sql
-- Dar permisos completos al usuario
GRANT ALL PRIVILEGES ON SCHEMA qog TO tu_usuario;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA qog TO tu_usuario;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA qog TO tu_usuario;
```

---

## Recursos Adicionales

### Documentación
- **PostgreSQL Docs:** https://www.postgresql.org/docs/
- **Tutorial oficial:** https://www.postgresql.org/docs/current/tutorial.html
- **psycopg2 docs:** https://www.psycopg.org/docs/

### Tutoriales
- **PostgreSQL Tutorial:** https://www.postgresqltutorial.com/
- **SQLBolt:** https://sqlbolt.com/

### Videos
- Buscar en YouTube: "PostgreSQL beginner tutorial"

---

**¿Problemas?** Pregunta en el foro del curso.

**Última actualización:** 2025-12-17
