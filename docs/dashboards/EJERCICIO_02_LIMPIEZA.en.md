# Exercise 2: The Noise Filter (Anti-Stopwords)﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌‌​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​​​‍​‌‌​​​​‌﻿

> **"You hear the guitar, it's a-clean and it's a-pure..."**﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌‌​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​​​‍​‌‌​​​​‌﻿
> *Like going from chaotic distortion to a crystal-clear solo, in this exercise we'll filter out language noise so the essence shines through.*

---

## The Challenge: Cleaning the Mix

In the previous exercise we saw that the most common words are "semantic garbage" (*stopwords*). Your mission is to remove them so that the words with real weight rise to the surface.

1. **Stopword Filtering:** Engage the filter pedal to ignore words like "the", "is", "and".
2. **Visual Impact:** Compare the "Before" and "After" to see how the true meaning emerges.
3. **Primitive Sentiment Analysis:** By cleaning the noise, words like "fantastic" or "terrible" take center stage.

---

## The Filter Pedal (Stopword Filter)

Imagine that every common word is a burst of static. Our algorithm acts like a *noise gate* pedal that only lets through the high-impact frequencies.

![Textual Noise Filter](stopword_filter.png)

### The Cleaning Ritual

* **Input:** A dirty text full of articles and prepositions.
* **Filter:** A blacklist of forbidden words (`stopwords_es`).
* **Output:** A pure signal where every word tells a story.

---

## Stage Comparison (Python Data)

When running `02_limpieza_texto.py`, you'll see the brutal contrast between the two worlds.

### The Before vs The After

Observe how in the left chart empty words dominate, while on the right the **pure sentiment** appears.

<!-- Pending image: limpieza_stopwords_comparativa.png -->

---

## Prophecy for the Analyst

* **Silence is Power:** By removing 70% of useless words, the analysis becomes 100% more precise.
* **Sultans of Data:** Now that you've cleaned the track, we're ready for the next level: sentiment analysis and similarity.

﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌‌​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​​​‍​‌‌​​​​‌﻿---
**Certification Hash:** `4e8d9b1a5f6e7c3d2b1a0f9e8d7c6b5a4f3e2d1c0b9a8f7e6d5c4b3a2f1e0d9c`
**Master of Ceremonies:** Juan Marcelo Gutierrez Miranda (@TodoEconometria)
**Vibe:** Heavy Clean Sound
