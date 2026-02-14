# Exercise 1: Text Anatomy and the Rhythm of Words﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​​‌‌‍​​‌‌​​​‌‍​​‌‌‌​​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​​‌‌​​‌‌‍​​‌‌​​‌‌‍​​‌‌‌​​​﻿

> **"Check out Guitar George, he knows-all the chords..."**﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​​‌‌‍​​‌‌​​​‌‍​​‌‌‌​​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​​‌‌​​‌‌‍​​‌‌​​‌‌‍​​‌‌‌​​​﻿
> *Wrapped in the rhythm of Sultans of Swing, we'll learn to dissect language to find its hidden melody.*

---

## The Opening Ritual (Objectives)

Turn a murmur of words into a symphony of data. In this first step of **NLP (Natural Language Processing)**, you will learn to:

1. **Expose the Structure:** Understand that text is not just letters, but an architecture that must be unified (Merge).
2. **Normalize the Frequency:** Force the text to lowercase so the algorithm doesn't get confused between "Solo" and "solo".
3. **Tokenize the Chaos:** Use regular expressions (`re.findall`) like a scalpel to separate each term (token) from ambient noise.
4. **Count the Pulse:** Use `Counter` to measure how strongly each word beats in the corpus.

---

## The Dissection Machine

Imagine a high-precision shredder that takes an ancient scroll and converts it into pure data blocks.

![Text Anatomy](text_anatomy.png)

### The Processing Purgatory

1. **Unification:** We join all phrases into a single block of textual steel.
2. **Normalization:** We apply `lower()` to standardize the signal.
3. **Tokenization:** We extract the tokens, removing punctuation that doesn't contribute to the main "riff".

---

## Live Results (Python Output)

When running `01_conteo_palabras.py`, you'll see the Top 10 words that dominate the stage emerge.

### The Truth Chart

This is where we visualize the frequency spectrum. See those giant bars? Those are the most repeated words.

<!-- Pending image: conteo_palabras_top10.png -->

---

## Backstage Reflection

* **Do you see the noise?** Articles like "the", "a", or "of" tend to dominate the chart. They're like amplifier feedback: they're there, but they're not the melody.
* **Sultans of Swing:** Just like in a great Knopfler solo, every word has its place, but some (the *stopwords*) appear too often and drown out the real message.

﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​​‌‌‍​​‌‌​​​‌‍​​‌‌‌​​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​​‌‌​​‌‌‍​​‌‌​​‌‌‍​​‌‌‌​​​﻿---
**Certification Hash:** `4e8d9b1a5f6e7c3d2b1a0f9e8d7c6b5a4f3e2d1c0b9a8f7e6d5c4b3a2f1e0d9c`
**Master of Ceremonies:** Juan Marcelo Gutierrez Miranda (@TodoEconometria)
**Vibe:** Rock & Data
