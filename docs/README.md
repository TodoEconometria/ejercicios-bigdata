# Documentacion del Curso

Esta carpeta contiene toda la documentacion del curso generada con **MkDocs Material**.

## Construccion Local

Para ver la documentacion localmente:

```bash
# Instalar dependencias
pip install -r requirements-docs.txt

# Servir documentacion (con hot-reload)
mkdocs serve

# Abrir navegador en: http://localhost:8000
```

## Build para Produccion

```bash
# Generar sitio estatico
mkdocs build

# Los archivos se generan en: site/
```

## Deploy a GitHub Pages

```bash
# Deploy automatico a GitHub Pages
mkdocs gh-deploy
```

Esto publicara la documentacion en: `https://TU_USUARIO.github.io/ejercicios-bigdata/`

## Estructura

```
docs/
├── index.md                 # Home / Landing page
├── guia-inicio/            # Guias para empezar
│   ├── index.md
│   ├── instalacion.md
│   ├── primer-ejercicio.md
│   └── roadmap.md
├── git-github/             # Guias de Git y GitHub
│   ├── index.md
│   ├── fork-clone.md
│   ├── sincronizar-fork.md
│   ├── pull-requests.md
│   └── comandos-utiles.md
├── ejercicios/             # Ejercicios del curso
│   ├── index.md
│   └── 01-introduccion-sqlite.md
├── dashboards/             # Guia de dashboards
│   └── index.md
├── faq.md                  # Preguntas frecuentes
├── stylesheets/            # CSS personalizado
│   └── extra.css
└── javascripts/            # JS personalizado
    └── mathjax.js
```

## Tecnologias

- **MkDocs:** Framework de documentacion
- **Material for MkDocs:** Tema moderno y profesional
- **Mermaid:** Diagramas interactivos
- **Pygments:** Syntax highlighting
- **MathJax:** Formulas matematicas (si se necesitan)

## Recursos

- [MkDocs Documentation](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [Markdown Guide](https://www.markdownguide.org/)
 
