# Paso 4: Resultados y Analisis

**Alumno:** [Nombre Apellido]
**Pregunta de investigacion:** [Tu pregunta]

---

## 3.1 Grafico 1: [Titulo descriptivo]

![Grafico 1](capturas/grafico1.png)

### Interpretacion

[Escribe un parrafo respondiendo estas preguntas:
- Que patron o tendencia se observa en el grafico?
- Hay diferencias entre los paises? Cuales?
- Hay algun punto de inflexion o cambio notable? En que anio?
- Como se relaciona esto con tu pregunta de investigacion?]

### Prompt que usaste para generar este grafico

**Herramienta:** [ChatGPT / Claude / Copilot / otra / ninguna]

**Tu prompt exacto:**
```
[PEGA AQUI el prompt que usaste para escribir el codigo de este grafico.
Si lo escribiste tu sin IA, escribe "Codigo propio" y explica que
referencia usaste (documentacion de matplotlib, ejemplo de clase, etc.)]
```

**Que tuviste que ajustar:**
[Que cambiaste de lo que te genero la IA para que funcionara o se viera bien]

---

## 3.2 Grafico 2: [Titulo descriptivo]

![Grafico 2](capturas/grafico2.png)

### Interpretacion

[Mismo formato que el Grafico 1. Explica que muestra y que significa.]

### Prompt que usaste para generar este grafico

**Herramienta:** [ChatGPT / Claude / Copilot / otra / ninguna]

**Tu prompt exacto:**
```
[PEGA AQUI]
```

**Que tuviste que ajustar:**
[Tu respuesta]

---

## 3.3 Respuesta a mi pregunta de investigacion

[Basandote en tus graficos y datos, responde tu pregunta de investigacion
en 2-3 parrafos. Usa evidencia de tus graficos para respaldar tu respuesta.

Ejemplo: "Los datos muestran que la calidad institucional en el Cono Sur
mejoro consistentemente entre 2000-2015, especialmente en Uruguay (vdem_polyarchy
paso de 0.82 a 0.91). En contraste, el Sudeste Asiatico muestra trayectorias
divergentes: Tailandia sufrio un retroceso en 2014 (golpe de estado) mientras
que Indonesia mantuvo una mejora gradual..."]

---

## 3.4 Limitaciones

[Menciona al menos 1 limitacion de tu analisis. Ejemplo:
- "QoG no tiene datos completos para todos los anios en algunas variables"
- "5 paises no son suficientes para generalizar a toda una region"
- "El clustering con pocas variables puede no capturar toda la complejidad"]

---

## 3.5 Dashboard interactivo (opcional pero recomendado)

Si generaste un dashboard HTML interactivo (con Plotly, Bokeh, etc.), guardalo en tu carpeta
para que aparezca automaticamente en el ranking del curso.

**Donde ponerlo:**

```
tu_carpeta/
├── outputs/
│   └── dashboard/
│       └── index.html      <-- Aqui (opcion recomendada)
├── dashboard.html           <-- O aqui (en la raiz de tu carpeta)
├── pipeline.py
└── ...
```

**Como generarlo con Plotly (ejemplo):**

```python
import plotly.graph_objects as go
from plotly.subplots import make_subplots

fig = make_subplots(rows=2, cols=1, subplot_titles=["Grafico 1", "Grafico 2"])
# ... tus graficos ...
fig.write_html("outputs/dashboard/index.html", include_plotlyjs=True)
```

El sistema detecta automaticamente archivos `.html` en tu entrega y los muestra
en el ranking con un boton "Dashboard" para que cualquiera pueda ver tus resultados
interactivos sin descargar nada.

**Consejos para que tu dashboard se visualice correctamente:**

- Usa `include_plotlyjs=True` en `write_html()` para embeber Plotly (mas fiable que CDN)
- Si usas archivos externos (CSS, JS, datos), ponlos en una carpeta `assets/` junto al HTML
- Evita rutas absolutas locales (`C:\Users\...`) - usa rutas relativas (`assets/datos.js`)
