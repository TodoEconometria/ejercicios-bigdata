# ⚡ Ejercicio 2: El Filtro de Ruido (Anti-Stopwords) 💀﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌​‌​‌‍​​‌‌​‌‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​‌‌​​​‌​‍​​‌‌‌​​‌‍​​‌‌​‌‌​‍​‌‌​​​​‌﻿

> **"You hear the guitar, it's a-clean and it's a-pure..." 🎸**﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌​‌​‌‍​​‌‌​‌‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​‌‌​​​‌​‍​​‌‌‌​​‌‍​​‌‌​‌‌​‍​‌‌​​​​‌﻿
> *Como pasar de una distorsión caótica a un solo cristalino, en este ejercicio filtraremos el ruido del lenguaje para que brille la esencia.*

---

## 🎯 El Desafío: Limpiar la Mezcla

En el ejercicio anterior vimos que las palabras más comunes son "basura semántica" (*stopwords*). Tu misión es eliminarlas para que las palabras con peso real salgan a la superficie.

1. **Stopword Filtering:** Activar el pedal de filtro para ignorar palabras como "el", "es", "y". ⛓️
2. **Impacto Visual:** Comparar el "Antes" y el "Después" para ver cómo emerge el verdadero significado. ⚡
3. **Análisis de Sentimiento Primitivo:** Al limpiar el ruido, palabras como "fantástico" o "terrible" toman el protagonismo. 🤘

---

## 🏗️ El Pedal de Filtro (Stopword Filter)

Imagina que cada palabra común es un acopio de estática. Nuestro algoritmo actúa como un pedal de *noise gate* que solo deja pasar las frecuencias de alto impacto.

![Filtro de Ruido Textual](stopword_filter.png)

### El Ritual de Limpieza

* **Input:** Un texto sucio lleno de artículos y preposiciones.
* **Filtro:** Una lista negra de palabras prohibidas (`stopwords_es`). ⚔️
* **Output:** Una señal pura donde cada palabra cuenta una historia.

---

## 🎸 Comparativa del Escenario (Python Data)

Al ejecutar `02_limpieza_texto.py`, verás el contraste brutal entre los dos mundos.

### El Antes vs El Después

Observa cómo en el gráfico izquierdo predominan las palabras vacías, mientras que en el derecho aparece el **sentimiento puro**.

<!-- Imagen pendiente: limpieza_stopwords_comparativa.png -->

---

## 🌑 Profecía para el Analista

* **El Silencio es Poder:** Al eliminar el 70% de las palabras que no sirven, el análisis se vuelve 100% más preciso. 🌌
* **Sultans of Data:** Ahora que has limpiado la pista, estamos listos para el siguiente nivel: el análisis de sentimiento y la similitud. 🤘

﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌​‌​‌‍​​‌‌​‌‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​‌‌​​​‌​‍​​‌‌‌​​‌‍​​‌‌​‌‌​‍​‌‌​​​​‌﻿---
**Hash de Certificación:** `4e8d9b1a5f6e7c3d2b1a0f9e8d7c6b5a4f3e2d1c0b9a8f7e6d5c4b3a2f1e0d9c`
**Master of Ceremonies:** Juan Marcelo Gutierrez Miranda (@TodoEconometria)
**Vibe:** Heavy Clean Sound 🎸⚡
