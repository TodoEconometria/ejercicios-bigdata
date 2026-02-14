# Ejercicio 03: Procesamiento Distribuido con Dask﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​​‌‌‍​​‌‌‌​​​‍​‌‌​​‌‌​‍​​‌‌​​​‌‍​​‌‌‌​​‌‍​​‌‌​​‌​‍​‌‌​​​‌‌‍​‌‌​​​​‌﻿

En este módulo aprenderás a escalar tu capacidad de cómputo más allá de la memoria RAM de tu máquina, utilizando clusters locales.﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​‌‌​​​‌‌‍​​‌‌‌​​​‍​‌‌​​‌‌​‍​​‌‌​​​‌‍​​‌‌‌​​‌‍​​‌‌​​‌​‍​‌‌​​​‌‌‍​‌‌​​​​‌﻿

![Ecosistemas de Datos Distribuidos](../assets/slides/m1_ecosistemas_p01.jpg)

## Objetivos
1. Configurar un Cluster Local con Dask.
2. Leer archivos Parquet de forma particionada.
3. Ejecutar agregaciones complejas (GroupBy) en paralelo.

### Hadoop: La Democratizacion del Procesamiento

![Hadoop Framework: MapReduce, HDFS, Avro, Parquet](../assets/slides/m1_ecosistemas_p02.jpg)

## Instrucciones

El script principal se encuentra en `ejercicios/03_procesamiento_distribuido/esqueleto.py`. Tu tarea es completar las funciones marcadas con `TODO` para construir un pipeline funcional.

### Tarea de Programación
Debes implementar la función `procesamiento_dask()` para que:
1. Inicie un cliente local (`LocalCluster`).
2. Lea el dataset de QoG procesado en el ejercicio anterior.
3. Calcule el promedio anual del Índice de Democracia.
4. Compare el tiempo de ejecución vs Pandas tradicional.
