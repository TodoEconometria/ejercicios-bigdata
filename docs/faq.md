# Preguntas Frecuentes (FAQ)

Respuestas a las preguntas mas comunes sobre el curso.

---

## General

### Necesito experiencia previa en Big Data?

**No.** El curso empieza desde cero. Solo necesitas:

- Conocimientos basicos de Python
- Saber usar la terminal/consola
- Ganas de aprender

!!! tip "No tienes Python?"
    Ve a la [Guia de Instalacion](guia-inicio/instalacion.md) donde te explicamos como instalar todo desde cero.

---

### Cuanto tiempo toma completar los ejercicios?

**Depende de tu nivel:**

| Nivel | Tiempo Total | Horas/Semana | Duracion |
|-------|--------------|--------------|----------|
| Principiante | 120-140 horas | 10-15h | 10-12 semanas |
| Intermedio | 60-80 horas | 8-10h | 6-8 semanas |
| Avanzado | 40-50 horas | 5-8h | 4-5 semanas |

**No hay prisa.** Aprende a tu ritmo. Lo importante es entender bien cada concepto.

---

### Los datos son reales o sinteticos?

**Reales.** Usamos datasets publicos reales:

- NYC Taxi & Limousine Commission (TLC)
- Weather data de NOAA
- Otros datasets publicos de Kaggle

Esto te da experiencia con datos del mundo real (sucios, incompletos, grandes).

---

### Puedo usar esto en mi portafolio?

**Si!** De hecho, te lo recomendamos.

Muchos alumnos han conseguido trabajo mostrando:

- Sus soluciones de los ejercicios
- El dashboard que crearon
- Su fork de GitHub con commits profesionales

!!! tip "Consejo"
    Haz tu fork publico y agrega un README personalizado explicando tu aprendizaje.

---

### Hay certificado al terminar?

**Para alumnos del curso presencial:** Si, certificado de 230 horas.

**Para autodidactas:** No hay certificado oficial, pero tu GitHub es tu certificado. Los empleadores valoran mas ver tu codigo que un PDF.

!!! success "Tu GitHub es tu Certificado"
    - Commits profesionales
    - Codigo bien documentado
    - Proyectos completos
    - Contribuciones activas

---

## Tecnico

### Que computadora necesito?

**Minimo:**

- 8GB RAM
- 20GB espacio en disco
- Procesador i5 o equivalente
- Windows 10+, macOS 10.14+, o Linux (Ubuntu 20.04+)

**Recomendado:**

- 16GB RAM
- 50GB espacio en disco SSD
- Procesador i7 o equivalente

!!! info "No tienes buenos recursos?"
    Puedes usar Google Colab o GitHub Codespaces (gratis) para trabajar en la nube.

---

### Funciona en Windows/Mac/Linux?

**Si.** El curso es compatible con los tres sistemas operativos.

- **Windows:** Preferiblemente Windows 10 o superior
- **macOS:** macOS 10.14 (Mojave) o superior
- **Linux:** Ubuntu 20.04+, Fedora, Arch, etc.

La [Guia de Instalacion](guia-inicio/instalacion.md) tiene instrucciones especificas para cada sistema.

---

### Puedo usar otro IDE en lugar de PyCharm?

**Si.** PyCharm es recomendado pero no obligatorio.

Alternativas:

- **Visual Studio Code** - Ligero y muy popular
- **Jupyter Lab** - Excelente para notebooks
- **Sublime Text** - Editor de texto avanzado
- **Vim/Emacs** - Si eres usuario avanzado

Lo importante es que te sientas comodo con tu herramienta.

---

### Como descargo los datos?

Los datos se descargan automaticamente con un script:

```bash
# Ir a la carpeta de datos
cd datos

# Ejecutar script de descarga
python descargar_datos.py
```

El script descarga y descomprime automaticamente todos los datasets necesarios.

!!! warning "Espacio en disco"
    Los datasets completos ocupan ~5GB. Asegurate de tener suficiente espacio.

---

## Git y GitHub

### Nunca he usado Git. Es muy dificil?

**No es dificil**, pero requiere practica.

Tenemos guias completas paso a paso:

1. [Fork y Clone](git-github/fork-clone.md) - Lo mas basico
2. [Tu Primer Ejercicio](guia-inicio/primer-ejercicio.md) - Workflow completo
3. [Comandos Utiles](git-github/comandos-utiles.md) - Referencia rapida

!!! tip "Aprende haciendo"
    La mejor forma de aprender Git es usandolo. Los primeros commits seran raros, pero mejoras rapido.

---

### Que es un Fork? Por que necesito uno?

**Fork** = Tu copia personal del repositorio en GitHub.

Lo necesitas porque:

- :lock: No puedes modificar el repositorio del profesor directamente
- :pencil2: El fork es TU espacio para trabajar
- :arrows_counterclockwise: Puedes sincronizarlo con el original
- :outbox_tray: Desde tu fork creas Pull Requests

Ver guia completa: [Fork y Clone](git-github/fork-clone.md)

---

### Como mantengo mi Fork actualizado?

Cuando el profesor agregue ejercicios nuevos, debes sincronizar tu fork.

**Metodo facil (GitHub Web):**

1. Ve a tu fork en GitHub
2. Click "Sync fork" → "Update branch"
3. En tu PC: `git pull origin main`

**Metodo completo (Terminal):**

```bash
git checkout main
git fetch upstream
git merge upstream/main
git push origin main
```

Ver guia completa: [Sincronizar Fork](git-github/sincronizar-fork.md)

---

### Hice un commit mal. Como lo deshago?

**Antes de hacer push:**

```bash
# Deshacer ultimo commit (mantiene cambios)
git reset --soft HEAD~1

# Deshacer ultimo commit (descarta cambios)
git reset --hard HEAD~1
```

**Despues de hacer push:**

```bash
# Crear nuevo commit que revierte el anterior
git revert HEAD
git push origin tu-rama
```

!!! danger "Evita force push"
    Nunca uses `git push --force` en ramas compartidas o Pull Requests abiertos.

---

## Ejercicios

### No puedo completar un ejercicio. Que hago?

**Paso 1:** Lee el error cuidadosamente

La mayoria de las veces el error te dice exactamente que esta mal.

**Paso 2:** Busca en Google

Copia el mensaje de error y buscalo. Probablemente alguien mas ya lo tuvo.

**Paso 3:** Revisa la documentacion

- [Pandas Docs](https://pandas.pydata.org/docs/)
- [SQLite Tutorial](https://www.sqlitetutorial.net/)
- [Python Docs](https://docs.python.org/3/)

**Paso 4:** Pide ayuda

- **Alumnos presenciales:** Consulta en clase
- **Autodidactas:** Crea un Issue en GitHub explicando tu problema

!!! tip "Como pedir ayuda"
    Incluye:

    - Que intentaste hacer
    - Que error obtuviste (mensaje completo)
    - Que ya probaste
    - Tu codigo relevante

---

### Puedo hacer los ejercicios en desorden?

**No recomendado.** Los ejercicios estan disenados para:

- Construir sobre conocimientos previos
- Aumentar dificultad gradualmente
- Introducir conceptos en orden logico

!!! warning "Excepcion"
    Si ya tienes experiencia con Python y Pandas, puedes empezar en el NIVEL 2 (Ejercicio 03).

---

### Cuantas veces puedo intentar un ejercicio?

**Las que necesites.** No hay limite de intentos.

El objetivo es **aprender**, no aprobar rapidamente.

- Puedes actualizar tu Pull Request cuantas veces quieras
- El profesor te dara feedback iterativo
- Aprendes mas de los errores que de los aciertos

---

### Puedo usar librerias adicionales?

**Si**, pero:

1. Justifica por que las necesitas
2. Agregalas a `requirements.txt`
3. Documenta como instalarlas
4. Menciona en el PR que librerias usaste

!!! example "Ejemplo"
    Si usas `seaborn` para visualizaciones:

    ```python
    # requirements.txt
    pandas==2.0.0
    seaborn==0.12.0  # Para visualizaciones avanzadas
    ```

    Y en el PR explica: "Use seaborn para crear graficos mas profesionales"

---

## Soporte

### Ofrecen soporte si me atoro?

**Para alumnos del curso presencial:**

- :white_check_mark: Soporte completo en las sesiones
- :white_check_mark: Consultas por email
- :white_check_mark: Revision detallada de PRs

**Para autodidactas:**

- :x: No hay soporte directo
- :white_check_mark: Puedes crear Issues en GitHub
- :white_check_mark: Comunidad puede ayudarte
- :white_check_mark: Documentacion completa disponible

---

### Como contacto al instructor?

**Para consultas del curso:**

- GitHub Issues: [Crear Issue](https://github.com/TodoEconometria/ejercicios-bigdata/issues)
- Email: cursos@todoeconometria.com

**Para consultoria empresarial:**

- Email: cursos@todoeconometria.com
- LinkedIn: [Juan Gutierrez](https://www.linkedin.com/in/juangutierrezconsultor/)
- Web: [TodoEconometria](https://www.todoeconometria.com)

!!! warning "Tiempo de respuesta"
    - Alumnos presenciales: 24-48 horas
    - Autodidactas via Issues: Cuando este disponible
    - Empresas: 24 horas

---

## Problemas Tecnicos

### Python no se reconoce como comando

**Windows:**

1. Reinstala Python
2. Marca "Add Python to PATH"
3. Reinicia la terminal

**macOS/Linux:**

Usa `python3` en lugar de `python`:

```bash
python3 --version
pip3 install pandas
```

---

### Error: ModuleNotFoundError

**Causa:** No instalaste las dependencias.

**Solucion:**

```bash
# Activa el entorno virtual
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate      # Windows

# Instala dependencias
pip install -r requirements.txt
```

---

### Git dice "fatal: not a git repository"

**Causa:** No estas en la carpeta del proyecto.

**Solucion:**

```bash
# Navega a la carpeta correcta
cd path/to/ejercicios-bigdata

# Verifica
git status  # Deberia funcionar
```

---

### No puedo hacer push: "Permission denied"

**Causa:** Problemas de autenticacion con GitHub.

**Solucion rapida (HTTPS):**

```bash
# Cambiar a HTTPS
git remote set-url origin https://github.com/TU_USUARIO/ejercicios-bigdata.git

# Intentar push de nuevo
git push origin tu-rama
```

**Solucion permanente (SSH):**

Configura SSH keys: [GitHub SSH Guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)

---

### El dashboard no carga los datos

**Verificar:**

1. La base de datos existe?
   ```bash
   ls datos/taxi.db
   ```

2. Flask esta corriendo?
   ```bash
   python app.py
   ```

3. Puerto correcto? (default: 5000)
   ```
   http://localhost:5000
   ```

4. Revisar consola de errores del navegador (F12)

---

## Carrera y Empleo

### Este curso me ayudara a conseguir trabajo?

**Puede ayudar mucho**, especialmente si:

- Completas todos los ejercicios con calidad
- Creas un dashboard profesional
- Documentas bien tu codigo
- Mantienes un GitHub activo

!!! success "Que valoran los empleadores"
    1. **Portfolio de proyectos** (tu GitHub)
    2. **Codigo limpio y documentado**
    3. **Experiencia con datos reales**
    4. **Capacidad de resolver problemas**

Un repositorio bien trabajado vale mas que 10 certificados.

---

### Que trabajos puedo conseguir con estas habilidades?

Con las habilidades del curso puedes aplicar a:

- **Data Analyst** - Analisis de datos con Python/SQL
- **Junior Data Scientist** - Modelado y analisis avanzado
- **Data Engineer** - Pipelines ETL, procesamiento de datos
- **Business Intelligence Developer** - Dashboards y reportes
- **Python Developer** - Desarrollo backend con datos

---

### Necesito un titulo universitario?

**Depende del empleador.**

- **Empresas tech:** Valoran mas el portfolio que el titulo
- **Empresas tradicionales:** Pueden requerir titulo
- **Startups:** Portfolio > Titulo
- **Freelance:** Solo importa tu trabajo

!!! tip "Compensar falta de titulo"
    - Portfolio solido en GitHub
    - Certificaciones relevantes
    - Proyectos personales impresionantes
    - Contribuciones open source

---

## Otros

### Puedo compartir mi solucion publicamente?

**Si**, pero considera:

- **Despues de completar:** Compartir despues de que el profesor revise tu PR
- **Con creditos:** Menciona que es del curso de TodoEconometria
- **No spoilers:** No compartas soluciones para ayudar a hacer trampa

!!! success "Compartir es bueno"
    Compartir tu codigo ayuda a:

    - Otros a aprender
    - Construir tu marca personal
    - Demostrar habilidades a empleadores

---

### El curso se actualiza?

**Si.** El repositorio se actualiza regularmente con:

- Nuevos ejercicios
- Mejoras en los existentes
- Actualizaciones de librerias
- Nuevos datasets
- Correcciones de bugs

Mantén tu fork sincronizado para obtener actualizaciones: [Sincronizar Fork](git-github/sincronizar-fork.md)

---

### Puedo contribuir al curso?

**Si!** Las contribuciones son bienvenidas.

Puedes contribuir:

- :bug: Reportando bugs via Issues
- :pencil: Mejorando documentacion
- :bulb: Sugiriendo nuevos ejercicios
- :art: Compartiendo tu dashboard en la galeria

Ver seccion de [Contribuciones](index.md#contribuciones)

---

### Donde puedo aprender mas?

**Recursos recomendados:**

- [Python for Data Analysis](https://wesmckinney.com/book/) - Libro de Wes McKinney
- [SQL Tutorial](https://mode.com/sql-tutorial/) - SQL interactivo
- [Dask Tutorial](https://tutorial.dask.org/) - Tutorial oficial de Dask
- [r/datascience](https://www.reddit.com/r/datascience/) - Comunidad en Reddit

**Cursos complementarios:**

- [Python for Data Science (Coursera)](https://www.coursera.org/specializations/python)
- [SQL for Data Science (DataCamp)](https://www.datacamp.com/courses/intro-to-sql-for-data-science)
- [Apache Spark (Udacity)](https://www.udacity.com/course/learn-spark-at-udacity--ud2002)

---

## Preguntas no Resueltas?

!!! question "No encontraste tu respuesta?"

    **Alumnos presenciales:** Consulta en la proxima sesion o envia un email

    **Autodidactas:** Crea un Issue en GitHub:

    [Crear Issue](https://github.com/TodoEconometria/ejercicios-bigdata/issues/new){ .md-button .md-button--primary }

    Incluye:
    - Titulo descriptivo
    - Descripcion detallada de tu pregunta
    - Contexto (que ejercicio, que intentaste, etc.)

---

## Recursos Adicionales

- [Guia de Inicio](guia-inicio/index.md) - Empezar desde cero
- [Git y GitHub](git-github/index.md) - Guias de Git
- [Ejercicios](ejercicios/index.md) - Lista de ejercicios
- [Roadmap](guia-inicio/roadmap.md) - Plan de estudio
