# 🧶 Ejercicio 1: Anatomía del Texto y el Ritmo de las Palabras 🎸﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​‌​‌‍​‌‌​​​‌​‍​‌‌​​‌​​‍​​‌‌​​‌​‍​‌‌​​‌‌​‍​​‌‌​‌​‌‍​​‌‌‌​​‌‍​​‌‌​​​‌﻿

> **"Check out Guitar George, he knows-all the chords... 🤘"**﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​‌​‌‍​‌‌​​​‌​‍​‌‌​​‌​​‍​​‌‌​​‌​‍​‌‌​​‌‌​‍​​‌‌​‌​‌‍​​‌‌‌​​‌‍​​‌‌​​​‌﻿
> *Envolviéndote en el ritmo de los Sultans of Swing, aprenderemos a diseccionar el lenguaje para encontrar su melodía oculta.*

---

## 🎯 El Ritual de Inicio (Objetivos)

Convertir un murmullo de palabras en una sinfonía de datos. En este primer paso del **NLP (Procesamiento de Lenguaje Natural)**, aprenderás a:

1. **Exponer la Estructura:** Entender que el texto no es solo letras, sino una arquitectura que debe ser unificada (Merge). ⛓️
2. **Normalizar la Frecuencia:** Doblegar el texto a minúsculas para que el algoritmo no se confunda entre "🎸 Solo" y "solo". ⚡
3. **Tokenizar el Caos:** Usar expresiones regulares (`re.findall`) como un bisturí para separar cada término (token) del ruido ambiental. ⚔️
4. **Contar el Pulso:** Usar `Counter` para medir qué tan fuerte late cada palabra en el corpus. 🌌

---

## 🏗️ La Máquina de Disección

Imagina una trituradora de alta precisión que toma un pergamino antiguo y lo convierte en bloques de datos puros.

![Anatomía del Texto](text_anatomy.png)

### El Purgatorio del Procesamiento

1. **Unificación:** Juntamos todas las frases en un solo bloque de acero textual.
2. **Normalización:** Aplicamos `lower()` para estandarizar la señal. ⚡
3. **Tokenización:** Extraemos los tokens, eliminando la puntuación que no aporta al "riff" principal.

---

## 🎸 Resultados del Directo (Python Output)

Al ejecutar `01_conteo_palabras.py`, verás surgir el Top 10 de palabras que dominan el escenario.

### El Gráfico de la Verdad

Aquí es donde visualizamos el espectro de frecuencias. ¿Ves esas barras gigantes? Son las palabras que más se repiten.

<!-- Imagen pendiente: conteo_palabras_top10.png -->

---

## ⚔️ Reflexión de Backstage

* **¿Ves el ruido?** Artículos como "el", "la" o "de" suelen dominar el gráfico. Son como los acoples de un amplificador: están ahí, pero no son la melodía. 🏁
* **Sultans of Swing:** Al igual que en un buen solo de Knopfler, cada palabra tiene su lugar, pero algunas (las *stopwords*) aparecen demasiado y tapan el verdadero mensaje. 🎸

﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​‌​‌‍​‌‌​​​‌​‍​‌‌​​‌​​‍​​‌‌​​‌​‍​‌‌​​‌‌​‍​​‌‌​‌​‌‍​​‌‌‌​​‌‍​​‌‌​​​‌﻿---
**Hash de Certificación:** `4e8d9b1a5f6e7c3d2b1a0f9e8d7c6b5a4f3e2d1c0b9a8f7e6d5c4b3a2f1e0d9c`
**Master of Ceremonies:** Juan Marcelo Gutierrez Miranda (@TodoEconometria)
**Vibe:** Rock & Data 🤘⚡
