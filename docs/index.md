# Big Data con Python - De Cero a Produccion

> **Aprende a procesar millones de registros sin que tu computadora explote**
>
> Repositorio educativo completo para dominar Big Data con Python, desde conceptos basicos hasta produccion.

[![GitHub stars](https://img.shields.io/github/stars/TodoEconometria/ejercicios-bigdata?style=social)](https://github.com/TodoEconometria/ejercicios-bigdata/stargazers)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Conectar-blue)](https://www.linkedin.com/in/juangutierrezconsultor/)
[![Web](https://img.shields.io/badge/Web-TodoEconometria-orange)](https://www.todoeconometria.com)

---

## Que es Esto y Por Que Existe?

### El Problema

Imagina esto: Tienes un archivo Excel con **5 anos de ventas** (500,000 filas). Excel se congela. Python con Pandas se queda sin memoria. Tu jefe necesita el analisis **manana**.

**Te suena familiar?**

Este es el problema que enfrentan miles de analistas, cientificos de datos y empresas diariamente. Los datos crecen exponencialmente, pero las herramientas tradicionales no escalan.

### La Solucion

Este repositorio te ensena a:

```python
# ❌ Antes: Excel y Pandas basico
df = pd.read_csv("ventas_5_anos.csv")  # 💥 MemoryError
df.groupby("region").sum()              # 🐌 20 minutos

# ✅ Despues: Big Data con Python
df = dd.read_csv("ventas_5_anos.csv")  # ⚡ Carga lazy
df.groupby("region").sum().compute()    # 🚀 2 segundos
```

**Resultado:** Procesas 100GB de datos en tu laptop como si fueran 10MB.

### Por Que Este Repositorio

Este material surge de **230 horas de curso presencial** donde enseno Big Data a profesionales. He destilado:

- :white_check_mark: **10+ anos de experiencia** en analisis de datos
- :white_check_mark: **Errores comunes** que cometen los principiantes (y como evitarlos)
- :white_check_mark: **Mejores practicas** de la industria
- :white_check_mark: **Proyectos reales** adaptados para aprender

**No es solo teoria.** Cada ejercicio esta disenado para enfrentarte a problemas del mundo real.

---

## Para Quien es Este Repositorio?

=== "Alumnos del Curso Presencial"

    Si estas inscrito en mi curso presencial:

    - :white_check_mark: Este repo es tu **material de apoyo** completo
    - :white_check_mark: Aqui encontraras **todos los ejercicios** del curso
    - :white_check_mark: Puedes practicar **antes, durante y despues** de las clases
    - :white_check_mark: Tienes **soporte directo** en las sesiones presenciales

    !!! success "Ventaja"
        Mientras otros solo tienen diapositivas, tu tienes un repositorio completo con codigo ejecutable.

=== "Autodidactas y Curiosos"

    Si encontraste este repositorio por tu cuenta:

    - :white_check_mark: **Todo el contenido es gratuito** y de codigo abierto
    - :white_check_mark: Puedes aprender **a tu ritmo** sin presion
    - :white_check_mark: Practica con **ejercicios reales** de Big Data
    - :warning: **No incluye soporte** (solo para alumnos presenciales)

    !!! tip "Ventaja"
        Material profesional de calidad sin costo, perfecto para tu portafolio.

=== "Empresas y Profesionales"

    Si buscas soluciones para tu empresa:

    - :white_check_mark: **Portfolio real** de capacidades en Big Data
    - :white_check_mark: Muestra como **entreno equipos** profesionales
    - :white_check_mark: **Consultoria y capacitacion** in-company disponible
    - :white_check_mark: Proyectos de **analisis de datos a medida**

    !!! info "Ventaja"
        Ve exactamente que nivel de calidad ofrezco antes de contratarme.

---

## Que Aprenderas?

### Tecnologias que Dominaras

| Tecnologia | Que Hace | Cuando Usarla |
|------------|----------|---------------|
| **Python** | Lenguaje base | Siempre |
| **Pandas** | Datos en memoria (< 5GB) | Analisis exploratorio |
| **Dask** | Datos > RAM (5-100GB) | Datasets grandes en 1 maquina |
| **PySpark** | Datos masivos (> 100GB) | Clusters, produccion |
| **SQLite** | Base de datos embebida | Prototipos, proyectos pequenos |
| **Parquet** | Formato columnar | Almacenar datos procesados |
| **Git/GitHub** | Control de versiones | Todo proyecto profesional |
| **Flask** | Web framework | Dashboards, APIs |

### Ejemplos de Que Podras Hacer

!!! example "Ejemplo 1: Analizar 10 Millones de Viajes de Taxi"

    ```python
    # Dataset: NYC Taxi (121 MB CSV, 10M+ registros)
    # Pregunta: Cual es el ingreso promedio por hora del dia?

    import dask.dataframe as dd

    # Cargar 121 MB como si fueran 10 MB ⚡
    df = dd.read_csv("yellow_tripdata_2021-01.csv")

    # Analisis que en Pandas tomaria 5 minutos, aqui: 10 segundos
    resultado = (df.groupby(df['tpep_pickup_datetime'].dt.hour)
                  ['total_amount']
                  .mean()
                  .compute())

    print(resultado)
    # Resultado: Hora 23 es la mas rentable ($18.50 promedio)
    ```

!!! example "Ejemplo 2: Dashboard en Tiempo Real"

    Crear un dashboard interactivo que muestra:

    - :bar_chart: Distribucion de viajes por hora
    - :world_map: Mapa de calor de zonas mas rentables
    - :money_with_wings: Ingresos totales por dia/semana/mes
    - :chart_with_upwards_trend: Tendencias temporales

!!! example "Ejemplo 3: Pipeline ETL de Produccion"

    ```
    CSV (100GB) → Limpiar → Transformar → Parquet → Dashboard
                  (Dask)    (PySpark)    (10GB)     (Flask)
    ```

---

## Como Empezar?

!!! tip "Primera Vez con Git y Python?"
    Empieza con nuestra [Guia de Instalacion](guia-inicio/instalacion.md) donde te explicamos paso a paso como instalar todas las herramientas necesarias.

!!! info "Ya tienes Git y Python?"
    Ve directo a [Tu Primer Ejercicio](guia-inicio/primer-ejercicio.md) para comenzar a trabajar.

!!! warning "Desarrollador Experimentado?"
    Revisa el [Roadmap del Curso](guia-inicio/roadmap.md) para ver todos los ejercicios disponibles y elegir por donde empezar.

---

## Estadisticas del Repositorio

![GitHub stars](https://img.shields.io/github/stars/TodoEconometria/ejercicios-bigdata?style=social)
![GitHub forks](https://img.shields.io/github/forks/TodoEconometria/ejercicios-bigdata?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/TodoEconometria/ejercicios-bigdata?style=social)

---

## Servicios Profesionales

### Consultoria en Big Data

Necesitas ayuda con un proyecto de datos en tu empresa?

**Ofrezco:**

- :white_check_mark: **Desarrollo de Pipelines ETL/ELT** con Python y Spark
- :white_check_mark: **Capacitacion Empresarial** (cursos personalizados para tu equipo)
- :white_check_mark: **Analisis de Datos** para insights accionables
- :white_check_mark: **Automatizacion de Procesos** de datos
- :white_check_mark: **Migracion a Big Data** (de Excel/SQL a Dask/Spark)

!!! example "Casos de Uso"

    **Empresa A:** "Tenemos 5 anos de ventas en Excel y toma 2 horas generar reportes"

    → Solucion: Pipeline automatizado con Dask + Dashboard en tiempo real
    → Resultado: Reportes en 30 segundos

    **Empresa B:** "Queremos capacitar a 15 analistas en Big Data"

    → Solucion: Curso in-company de 40 horas adaptado a su industria
    → Resultado: Equipo autonomo procesando TB de datos

    **Startup C:** "Necesitamos procesar logs de servidores (1TB/dia)"

    → Solucion: Pipeline PySpark en AWS EMR
    → Resultado: Analisis en tiempo real con costos optimizados

### Contacto

:email: **Email:** [cursos@todoeconometria.com](mailto:cursos@todoeconometria.com)
:briefcase: **LinkedIn:** [Juan Gutierrez](https://www.linkedin.com/in/juangutierrezconsultor/)
:globe_with_meridians: **Web:** [www.todoeconometria.com](https://www.todoeconometria.com)

---

## Contribuciones

Este repositorio esta en constante evolucion. Si encuentras:

- :bug: Errores o bugs
- :pencil: Mejoras en la documentacion
- :bulb: Ideas para nuevos ejercicios
- :art: Ejemplos de dashboards

!!! tip "Crea un Issue o Pull Request"
    1. Fork este repositorio
    2. Crea una rama (`git checkout -b feature/nueva-funcionalidad`)
    3. Commit tus cambios (`git commit -m 'Agregar nueva funcionalidad'`)
    4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
    5. Abre un Pull Request

---

## Licencia

Este proyecto esta bajo la Licencia MIT - ver el archivo [LICENSE](https://github.com/TodoEconometria/ejercicios-bigdata/blob/main/LICENSE) para detalles.

**En resumen:** Puedes usar este material para aprender, ensenar, o modificar, siempre que des credito.

---

## Listo para Empezar?

```bash
# 1. Haz fork de este repositorio (boton arriba a la derecha)

# 2. Clona TU fork
git clone https://github.com/TU_USUARIO/ejercicios-bigdata.git

# 3. Instala dependencias
cd ejercicios-bigdata
pip install -r requirements.txt

# 4. Empieza con el Ejercicio 01
cd ejercicios
python 01_cargar_sqlite.py

# 5. Aprende, practica, crece!
```

---

<p align="center">
  <b>Tu carrera en Big Data empieza aqui.</b><br>
  Preguntas? Abre un <a href="https://github.com/TodoEconometria/ejercicios-bigdata/issues">Issue</a> o contactame en <a href="https://www.linkedin.com/in/juangutierrezconsultor/">LinkedIn</a>
</p>

<p align="center">
  Hecho con ❤️ por <a href="https://www.todoeconometria.com">TodoEconometria</a>
</p>
