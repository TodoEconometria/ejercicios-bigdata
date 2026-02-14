# 🧶 Análisis de Similitud: El Mystery del Portal Web﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​​‌‌‍​‌‌​​‌​‌‍​​‌‌​​​‌‍​‌‌​​​‌​‍​​‌‌‌​​‌‍​​‌‌​‌​​‍​​‌‌‌​​‌‍​​‌‌​‌​‌﻿

> **"Un sistema de recomendación es como un bibliotecario que sabe exactamente qué revista te va a gustar sin haber leído el contenido completo, solo mirando las palabras que se repiten. 🤘"**﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​​‌‌‍​‌‌​​‌​‌‍​​‌‌​​​‌‍​‌‌​​​‌​‍​​‌‌‌​​‌‍​​‌‌​‌​​‍​​‌‌‌​​‌‍​​‌‌​‌​‌﻿

---

## 🎯 El Desafío del Portal

Imagina que gestionas un portal dinámico. Tu jefe te ha puesto un reto: **"Agrupa estos artículos automáticamente. No tengo tiempo para leerlos todos."**

![Estructura del Portal](portal_web.png)

Para resolverlo, usamos el **Índice de Jaccard**, una herramienta matemática que convierte el texto en "conjuntos" y mide cuánto se solapan. ⚡

![Diagrama Conceptual de Jaccard](jaccard_diagram.png)

---

## 🏗️ El Corazón del Algoritmo

La magia ocurre comparando lo que los documentos **comparten** frente a **todo lo que dicen**.

| Atributo | Explicación Visual |
| :--- | :--- |
| **Intersección** | Las palabras que aparecen en AMBOS textos. ⚔️ |
| **Unión** | Todas las palabras únicas de AMBOS textos. 🌌 |
| **Resultado** | Un número entre **0** (desconocidos) y **1** (almas gemelas). 🤘 |

![Lógica de Jaccard](comparacion_jaccard.png)

### La Fórmula Matemática

![Fórmula de Jaccard](formula_jaccard.png)

---

## 🎸 Resultados Reales (Generados por tu Script)

Aquí es donde la teoría se encuentra con la realidad. Al ejecutar `04_similitud_jaccard.py`, el sistema "ve" el portal así:

### 1. El Mapa de Calor del Saber

En esta matriz, los colores cálidos (rojos) indican alta similitud. Observa cómo se forman **cuadrados en la diagonal**. ¡Eso son tus categorías de Fútbol, Tecnología y Cocina detectadas automáticamente! ⚡

![Índice de Categorías del Corpus](indice_categorias.png)

![Matriz de Similitud Real](analisis_jaccard_completo.png)

### 2. La Prueba del Algoritmo (Clustermap)

¿Puede la inteligencia artificial agrupar los temas sin ayuda? El **Dendrograma** (el árbol lateral) nos dice que sí. Los artículos de la misma temática se "buscan" y se agrupan en ramas comunes. 💀

![Agrupamiento Jerárquico](clustermap_ejercicio.png)

### 3. Clustermap con Valores Numéricos

Otra vista del mismo agrupamiento, ahora con los valores exactos de similitud en cada celda:

![Clustermap Detallado](clustermap.png)

---

## ⚔️ Aplicaciones en el Mundo Real

No es solo un ejercicio académico. Esta técnica se usa cada segundo en:

- **🏴‍☠️ Detección de Plagio:** Comparar entregas de alumnos para ver si comparten "demasiado" vocabulario.
- **🛸 Recomendadores:** "Si leíste sobre el nuevo CPU, te recomiendo este artículo sobre memoria RAM".
- **⛓️ SEO y Buscadores:** Para entender si dos páginas hablan de lo mismo y evitar contenido duplicado.

![Aplicaciones Reales de Jaccard](aplicaciones_reales.png)

---

## 🌑 Reflexión Final para el Alumno

Mira las gráficas que se han guardado en tu carpeta:

1. ¿Ves algún punto rojo fuera de la diagonal? Eso indicaría que dos temas diferentes comparten palabras.
2. ¿Qué pasaría si el corpus fuera de 10,000 documentos? El mapa de calor se volvería ilegible, pero el **Clustermap** seguiría dándonos la estructura. 🤘

﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​​‌‌‍​‌‌​​‌​‌‍​​‌‌​​​‌‍​‌‌​​​‌​‍​​‌‌‌​​‌‍​​‌‌​‌​​‍​​‌‌‌​​‌‍​​‌‌​‌​‌﻿---
**Hash de Certificación:** `4e8d9b1a5f6e7c3d2b1a0f9e8d7c6b5a4f3e2d1c0b9a8f7e6d5c4b3a2f1e0d9c`
**Autor:** Juan Marcelo Gutierrez Miranda (@TodoEconometria)
