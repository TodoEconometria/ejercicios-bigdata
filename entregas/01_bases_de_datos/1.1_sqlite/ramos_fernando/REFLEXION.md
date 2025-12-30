# 💭 Reflexión sobre los Modelos de Datos

**Nombre del alumno:** _____________________

**Fecha:** _____________________

---

## Instrucciones

Responde las siguientes preguntas con tus propias palabras. No hay respuestas "correctas" absolutas, lo importante es que **justifiques** tu razonamiento.

**Requisitos:**
- Responde en párrafos completos (mínimo 3-4 líneas por pregunta)
- Usa ejemplos específicos de los ejercicios que hiciste
- Sé honesto sobre lo que encontraste difícil o fácil

---

## Pregunta 1: Facilidad de Implementación

**¿Cuál modelo fue más fácil de implementar? ¿Por qué?**

**Tu respuesta:**

```
[Escribe aquí tu respuesta]




```

**Pista:** Considera:
- ¿Cuántas líneas de código escribiste?
- ¿Tuviste que pensar mucho en el diseño?
- ¿Tuviste errores al crear las tablas?

---

## Pregunta 2: Ventajas del Modelo A

**¿Qué ventajas encontraste en el Modelo A (desnormalizado)?**

**Tu respuesta:**

```
[Escribe aquí tu respuesta]




```

**Pista:** Piensa en:
- Velocidad de carga de datos
- Simplicidad de las consultas
- ¿Cuándo sería útil este modelo?

---

## Pregunta 3: Desventajas del Modelo A

**¿Qué desventajas encontraste en el Modelo A?**

**Tu respuesta:**

```
[Escribe aquí tu respuesta]




```

**Pista:** Considera:
- Duplicación de datos (¿viste nombres de fabricantes repetidos?)
- ¿Qué pasaría si quisieras cambiar el nombre de un fabricante?
- Espacio en disco

---

## Pregunta 4: Cuándo Usar Modelo B

**¿En qué situación usarías el Modelo B sobre el A? Justifica.**

**Tu respuesta:**

```
[Escribe aquí tu respuesta]




```

**Pista:** Piensa en:
- Tipo de aplicación (lectura vs escritura)
- Importancia de la consistencia de datos
- Múltiples usuarios modificando datos

---

## Pregunta 5: Necesidad del Modelo C

**¿El Modelo C es necesario para todos los casos? Justifica.**

**Tu respuesta:**

```
[Escribe aquí tu respuesta]




```

**Pista:** Considera:
- ¿Todos los negocios necesitan gestionar pedidos y carritos?
- Complejidad vs beneficio
- Casos donde Modelo B es suficiente

---

## Pregunta 6: Impacto de Cambios

**¿Qué pasaría si quisieras agregar una nueva columna "descuento" a todos los productos?**

### a) En Modelo A: ¿Cuántas tablas modificarías?

**Tu respuesta:**

```
[Escribe aquí tu respuesta]


```

### b) En Modelo B: ¿Cuántas tablas modificarías?

**Tu respuesta:**

```
[Escribe aquí tu respuesta]


```

### c) ¿Qué modelo hace más fácil este tipo de cambios? ¿Por qué?

**Tu respuesta:**

```
[Escribe aquí tu respuesta]




```

---

## Pregunta 7: Consultas SQL

**¿Qué tipo de consultas fueron más fáciles en cada modelo?**

### Modelo A:

**Tu respuesta:**

```
[Escribe aquí tu respuesta]


```

### Modelo B:

**Tu respuesta:**

```
[Escribe aquí tu respuesta]


```

### Modelo C:

**Tu respuesta:**

```
[Escribe aquí tu respuesta]


```

---

## Pregunta 8: Caso Real

**Imagina que te contratan para hacer una aplicación. Describe qué modelo usarías en cada caso y POR QUÉ:**

### a) Dashboard de análisis de datos (solo lectura, sin usuarios modificando)

**Modelo elegido:** ___________

**Justificación:**

```
[Escribe aquí tu respuesta]



```

---

### b) Sistema de gestión interna de inventario (CRUD, 5 usuarios simultáneos)

**Modelo elegido:** ___________

**Justificación:**

```
[Escribe aquí tu respuesta]



```

---

### c) Tienda online con miles de clientes comprando

**Modelo elegido:** ___________

**Justificación:**

```
[Escribe aquí tu respuesta]



```

---

## Pregunta 9: Reflexión Personal

**¿Qué fue lo más difícil de este ejercicio? ¿Qué aprendiste?**

**Tu respuesta:**

```
[Escribe aquí tu respuesta]




```

---

## Pregunta 10: Trade-offs

**En tus propias palabras, explica el concepto de "trade-off" en el diseño de bases de datos.**

**Tu respuesta:**

```
[Escribe aquí tu respuesta]




```

**Ejemplo esperado:** "Un trade-off es cuando ganas algo pero pierdes otra cosa. Por ejemplo, en Modelo A ganas velocidad pero pierdes..."

---

## Autoevaluación

**Evalúa tu comprensión de cada modelo (1-5, siendo 5 "lo domino completamente"):**

| Modelo | Puntuación (1-5) | ¿Por qué esta puntuación? |
|--------|------------------|---------------------------|
| Modelo A | ___/5 | |
| Modelo B | ___/5 | |
| Modelo C | ___/5 | |

---

## Pregunta Bonus (Opcional)

**Si tuvieras que explicarle a alguien sin conocimientos técnicos cuándo usar cada modelo, ¿qué analogía usarías?**

**Tu respuesta:**

```
[Escribe aquí tu respuesta]




```

**Ejemplo de analogía:** "Modelo A es como tener todo en un solo cuaderno desordenado. Modelo B es como tener carpetas organizadas por tema..."

---

## Firma

**Declaro que estas respuestas son de mi autoría y reflejan mi comprensión personal del ejercicio.**

**Nombre:** _____________________

**Fecha:** _____________________

---

**Nota para el profesor:** Este documento es parte de la evaluación del Ejercicio 1.1. La calidad de las reflexiones cuenta un 10% de la nota final.
