# 👨‍🎓 Guía Completa para Alumnos

Esta guía contiene todo lo que necesitas saber para trabajar en este repositorio.

---

## 📋 Índice

1. [Preparación Inicial](#1-preparación-inicial-solo-una-vez)
2. [Flujo de Trabajo Diario](#2-flujo-de-trabajo-diario)
3. [Crear y Entregar tu Dashboard](#3-crear-y-entregar-tu-dashboard)
4. [Requisitos del Dashboard](#4-requisitos-del-dashboard)
5. [Errores Comunes](#5-errores-comunes)
6. [FAQ](#6-preguntas-frecuentes)

---

## 1. Preparación Inicial (Solo una vez)

### 1.1 Fork del Repositorio

1. Ve a: https://github.com/TodoEconometria/ejercicios-bigdata
2. Haz clic en **Fork** (arriba a la derecha)
3. Esto crea una copia en TU cuenta de GitHub

### 1.2 Clonar en PyCharm

**Opción A: Desde PyCharm (Recomendado)**

1. Abre PyCharm
2. En la pantalla de bienvenida: **Get from VCS**
   - Si ya tienes un proyecto abierto: `Git` > `Clone...`
3. Selecciona **GitHub** en la barra lateral
4. Busca tu fork: `tu-usuario/ejercicios-bigdata`
5. Clic en **Clone**

**Opción B: Desde la terminal**

```bash
git clone https://github.com/TU-USUARIO/ejercicios-bigdata.git
cd ejercicios-bigdata
```

### 1.3 Conectar con el Repositorio del Profesor (Upstream)

Esto te permite recibir actualizaciones del profesor.

**En PyCharm:**

1. `Git` > `Manage Remotes...`
2. Clic en **+** para agregar
3. **Name:** `upstream`
4. **URL:** `https://github.com/TodoEconometria/ejercicios-bigdata.git`
5. **OK**

**En terminal:**

```bash
git remote add upstream https://github.com/TodoEconometria/ejercicios-bigdata.git
git remote -v  # Verificar que se agregó
```

### 1.4 Configurar Entorno Python

```bash
# Crear entorno virtual
python -m venv .venv

# Activar (Windows)
.venv\Scripts\activate

# Activar (Linux/Mac)
source .venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

### 1.5 Descargar los Datos

```bash
cd datos
python descargar_datos.py
cd ..
```

✅ **Ya estás listo para trabajar!**

---

## 2. Flujo de Trabajo Diario

Cada vez que vayas a trabajar en una nueva tarea:

### Paso 1: Actualizar tu Fork

Obtén los últimos cambios del profesor.

**En PyCharm:**

1. `Git` > `Fetch` (descarga información)
2. `Git` > `Merge...`
3. Selecciona `upstream/main`
4. Clic en **Merge**

**En terminal:**

```bash
git fetch upstream
git checkout main
git merge upstream/main
git push origin main  # Actualiza tu fork en GitHub
```

### Paso 2: Crear una Rama Nueva

**⚠️ IMPORTANTE:** NUNCA trabajes en `main` directamente.

**Nombre de la rama:** `tu-nombre-tarea` (ej: `juan-dashboard-eda`)

**En PyCharm:**

1. `Git` > `New Branch...`
2. Nombre: `tu-nombre-dashboard-eda`
3. **Create**

**En terminal:**

```bash
git checkout -b tu-nombre-dashboard-eda
```

### Paso 3: Trabajar en tu Código

1. Crea tu carpeta en `dashboards/tu-nombre-dashboard/`
2. Desarrolla tu dashboard
3. Prueba que funcione localmente

### Paso 4: Hacer Commit

**En PyCharm:**

1. Pestaña **Commit** (icono ✔️ a la izquierda)
2. Selecciona los archivos modificados
3. Mensaje: `Agregar dashboard EDA - [Tu Nombre]`
4. Clic en **Commit**

**En terminal:**

```bash
git add dashboards/tu-nombre-dashboard/
git commit -m "Agregar dashboard EDA - [Tu Nombre]"
```

### Paso 5: Push a GitHub

**En PyCharm:**

1. `Git` > `Push...`
2. Verifica la rama destino
3. **Push**

**En terminal:**

```bash
git push -u origin tu-nombre-dashboard-eda
```

### Paso 6: Crear Pull Request

**Opción A: Desde PyCharm**
- Después del push, verás una notificación con link al PR
- Haz clic y se abre el navegador

**Opción B: Desde GitHub**

1. Ve a tu fork en GitHub
2. Verás un banner: **"Compare & pull request"**
3. Clic en el botón
4. Verifica:
   - **Base:** `TodoEconometria/ejercicios-bigdata` - `main`
   - **Head:** `tu-usuario/ejercicios-bigdata` - `tu-rama`
5. Completa título y descripción
6. **Create pull request**

---

## 3. Crear y Entregar tu Dashboard

### 3.1 Estructura del Dashboard

Crea esta estructura en `dashboards/tu-nombre-dashboard/`:

```
tu-nombre-dashboard/
├── app.py              # Aplicación Flask
├── templates/          # Templates HTML
│   └── index.html
├── static/             # (Opcional) CSS, JS, imágenes
│   ├── css/
│   ├── js/
│   └── img/
└── README.md           # Documentación
```

### 3.2 Ejemplo de app.py Básico

```python
"""
Dashboard EDA - NYC Taxi
Autor: Tu Nombre
"""

from flask import Flask, render_template, jsonify
import pandas as pd
import os

app = Flask(__name__)

# Ruta relativa a los datos
DATA_PATH = os.path.join('..', '..', 'datos', 'nyc_taxi.csv')

def cargar_datos():
    """Carga el dataset de NYC Taxi"""
    if not os.path.exists(DATA_PATH):
        return None
    return pd.read_csv(DATA_PATH)

@app.route('/')
def index():
    """Página principal"""
    return render_template('index.html')

@app.route('/api/estadisticas')
def estadisticas():
    """API: Estadísticas básicas"""
    df = cargar_datos()
    if df is None:
        return jsonify({'error': 'No se encontró el archivo de datos'})

    stats = {
        'total_viajes': int(df.shape[0]),
        'distancia_promedio': float(df['trip_distance'].mean()),
        'tarifa_promedio': float(df['fare_amount'].mean()),
        'pasajeros_promedio': float(df['passenger_count'].mean())
    }
    return jsonify(stats)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

### 3.3 Template de README.md para tu Dashboard

```markdown
# Dashboard [Nombre] - NYC Taxi EDA

**Autor:** Tu Nombre
**Fecha:** Diciembre 2025

## Descripción

[1-2 párrafos explicando qué hace tu dashboard]

## Características

- ✅ Visualización 1: [Descripción]
- ✅ Visualización 2: [Descripción]
- ✅ Visualización 3: [Descripción]
- ✅ Estadísticas descriptivas
- ✅ Análisis de calidad de datos

## Tecnologías Utilizadas

- Flask
- Pandas
- Chart.js (o Plotly, etc.)
- HTML/CSS/JavaScript

## Cómo Ejecutar

\```bash
cd dashboards/tu-nombre-dashboard
python app.py
\```

Luego abre: http://localhost:5000

## Conclusiones

1. [Conclusión 1 del análisis]
2. [Conclusión 2 del análisis]
3. [Conclusión 3 del análisis]

## Capturas de Pantalla

[Opcional: Agrega capturas de tu dashboard]
```

---

## 4. Requisitos del Dashboard

Tu dashboard **DEBE** incluir:

### ✅ Requisitos Obligatorios

1. **Mínimo 3 visualizaciones diferentes**
   - Gráficos de barras, líneas, dispersión, dona, etc.
   - Pueden usar Chart.js, Plotly, Matplotlib, etc.

2. **Estadísticas descriptivas (mínimo 5)**
   - Total de registros
   - Promedios (distancia, tarifa, pasajeros)
   - Valores min/max
   - Desviación estándar
   - Conteo de valores nulos

3. **Análisis de calidad de datos**
   - Identificar valores nulos
   - Detectar outliers
   - Validar tipos de datos

4. **README.md en tu carpeta**
   - Descripción del dashboard
   - Cómo ejecutarlo
   - Tecnologías usadas
   - 3-5 conclusiones del análisis

5. **Código limpio**
   - Comentarios explicativos
   - Nombres de variables descriptivos
   - Funciones bien estructuradas

### 🌟 Puntos Extra (Opcionales)

- +5 pts: Más de 5 visualizaciones
- +5 pts: Filtros interactivos
- +5 pts: Diseño responsive y profesional
- +5 pts: Análisis estadístico avanzado (correlaciones, regresiones, etc.)
- +5 pts: Tests unitarios

---

## 5. Errores Comunes

### Error: "No such file or directory: datos/nyc_taxi.csv"

**Causa:** Ruta incorrecta al archivo de datos

**Solución:**

```python
# ✅ Correcto - Ruta relativa desde tu dashboard
import os
DATA_PATH = os.path.join('..', '..', 'datos', 'nyc_taxi.csv')

# ❌ Incorrecto - Ruta absoluta
DATA_PATH = 'C:\\Users\\tu-usuario\\...'
```

### Error: "Port 5000 is already in use"

**Causa:** Ya hay otro proceso usando el puerto 5000

**Solución:**

```python
# Cambia el puerto en app.py
app.run(debug=True, host='0.0.0.0', port=5001)
```

O cierra el proceso anterior:

```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID [número] /F

# Linux/Mac
lsof -i :5000
kill -9 [PID]
```

### Error: "ModuleNotFoundError: No module named 'flask'"

**Causa:** Dependencias no instaladas

**Solución:**

```bash
# Asegúrate de tener el entorno virtual activado
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac

# Instala dependencias
pip install -r requirements.txt
```

### Mi gráfico no se muestra

**Soluciones:**

1. Abre la consola del navegador (F12)
2. Revisa errores de JavaScript
3. Verifica que los datos lleguen desde el backend
4. Comprueba que los IDs de HTML coincidan con el JavaScript

### El PR fue rechazado

**Revisa:**

1. Lee los comentarios del profesor
2. Haz los cambios solicitados
3. Commit y push a la misma rama
4. El PR se actualiza automáticamente

---

## 6. Preguntas Frecuentes

### ¿Puedo usar librerías adicionales?

Sí, pero:
1. Agrégalas a un archivo `requirements.txt` en tu carpeta de dashboard
2. Menciónalas en tu README.md
3. Documenta por qué las necesitas

### ¿Puedo trabajar en equipo?

Consulta con el profesor. Si es permitido:
- Ambos deben figurar en el README
- Ambos deben hacer commits
- Un solo PR con ambos como autores

### ¿Qué pasa si encuentro errores en los datos?

¡Excelente!
1. Documéntalo en tu README
2. Explica cómo lo manejaste
3. Incluye análisis de calidad de datos

### ¿Puedo usar otro framework en lugar de Flask?

Consulta con el profesor primero. Flask es el estándar para este curso.

### ¿Debo incluir los datos en mi PR?

**NO.** Los datos ya están en la carpeta `datos/`. Solo sube tu código.

### ¿Cuándo recibiré feedback?

El profesor revisa los PRs regularmente. Recibirás:
- Comentarios en el código
- Calificación (si aplica)
- Aprobación o solicitud de cambios

### ¿Puedo hacer múltiples dashboards?

Sí, pero:
- Crea un PR separado para cada dashboard
- Usa ramas diferentes
- No mezcles trabajos en un solo PR

### ¿Cómo veo el dashboard de ejemplo?

```bash
cd dashboards/nyc_taxi_eda
python app.py
# Abre http://localhost:5000
```

**IMPORTANTE:** Úsalo como referencia, NO copies el código.

---

## 📞 ¿Necesitas Ayuda?

### Ayuda del Curso (Gratis)

1. **Lee la documentación:**
   - [FAQ completo](docs/FAQ.md)
   - [Troubleshooting](docs/TROUBLESHOOTING.md)
   - [Arquitectura del proyecto](ARQUITECTURA.md)

2. **Busca en Issues:**
   - Revisa [Issues cerrados](../../issues?q=is%3Aissue+is%3Aclosed)
   - Alguien pudo tener el mismo problema

3. **Crea un Issue:**
   - [Nuevo Issue](../../issues/new)
   - Label: `question`
   - Describe tu problema claramente

### Tutoriales Recomendados

- **Flask:** https://flask.palletsprojects.com/
- **Pandas:** https://pandas.pydata.org/docs/
- **Chart.js:** https://www.chartjs.org/docs/
- **Git/GitHub:** https://docs.github.com/

---

## ✅ Checklist Final Antes de Entregar

Antes de crear tu PR, verifica:

- [ ] Creé una rama nueva (no estoy en `main`)
- [ ] Mi carpeta está en `dashboards/mi-nombre-dashboard/`
- [ ] Incluí `app.py` funcional
- [ ] Incluí al menos `templates/index.html`
- [ ] Incluí `README.md` completo
- [ ] Mi dashboard tiene mínimo 3 visualizaciones
- [ ] Mi dashboard muestra estadísticas descriptivas
- [ ] Probé mi dashboard localmente y funciona
- [ ] Mi código está comentado
- [ ] No incluí datos en el PR (están en `.gitignore`)
- [ ] Hice commit con mensaje descriptivo
- [ ] Hice push a mi fork
- [ ] Creé el Pull Request con descripción completa
- [ ] Incluí conclusiones del análisis en el README

---

## 🎯 Criterios de Evaluación

Tu dashboard será evaluado en:

| Criterio | Peso | Qué se evalúa |
|----------|------|---------------|
| **Funcionalidad** | 40% | Funciona sin errores, visualizaciones se muestran, datos se procesan |
| **Análisis** | 30% | Estadísticas relevantes, visualizaciones apropiadas, conclusiones fundamentadas |
| **Código** | 20% | Limpio, comentado, buenas prácticas, estructura organizada |
| **Documentación** | 10% | README completo, instrucciones claras, descripción del PR |

---

## 🎓 Ejemplo de Referencia

Dashboard de ejemplo del profesor:

```
dashboards/nyc_taxi_eda/
```

**Incluye:**
- Estructura básica de Flask
- 3 tipos de visualizaciones
- API endpoints
- Diseño responsive
- Código comentado

**⚠️ NO COPIES el código.** Úsalo para entender la estructura y crear tu propia implementación.

---

## 🚀 ¡Éxito en tu Proyecto!

Recuerda:
- ⭐ La práctica hace al maestro
- 💡 Experimenta y aprende
- 🤝 Ayuda a tus compañeros
- 📚 Consulta la documentación

**¡Mucha suerte con tu dashboard!** 🎉

---

<p align="center">
  <a href="README.md">← Volver al README principal</a>
</p>
