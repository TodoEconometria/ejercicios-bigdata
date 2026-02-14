# Exercise 03: Distributed Processing with Dask﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌​‌‌‌‍​​‌‌​​​​‍​​‌‌‌​​​‍​​‌‌​​‌​‍​‌‌​​​​‌‍​​‌‌​‌‌​‍​​‌‌​‌‌​‍​​‌‌​‌​​﻿

In this module you will learn to scale your computing capacity beyond your machine's RAM, using local clusters.﻿​‌​‌​‌​​‍​‌​​​‌​‌‍​​‌‌‌​‌​‍​​‌‌​‌​​‍​‌‌​​‌​‌‍​​‌‌‌​​​‍​‌‌​​‌​​‍​​‌‌‌​​‌‍​‌‌​​​‌​‍​​‌‌​​​‌‍​‌‌​​​​‌‍​​‌‌​‌​‌‍​‌‌​​‌‌​‍​​‌‌​‌‌​‍​‌‌​​‌​‌‍​​‌‌​‌‌‌‍​‌‌​​​‌‌‍​​‌‌​​‌‌‍​‌‌​​‌​​‍​​‌‌‌​‌​‍​​‌‌​​‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​‌‌​‍​​‌‌​​​​‍​​‌‌​​‌​‍​​‌‌​​​‌‍​​‌‌​​‌‌‍​​‌‌‌​‌​‍​​‌‌​‌‌‌‍​​‌‌​​​​‍​​‌‌‌​​​‍​​‌‌​​‌​‍​‌‌​​​​‌‍​​‌‌​‌‌​‍​​‌‌​‌‌​‍​​‌‌​‌​​﻿

![Distributed Data Ecosystems](../assets/slides/m1_ecosistemas_p01.jpg)

## Objectives
1. Set up a Local Cluster with Dask.
2. Read Parquet files in a partitioned manner.
3. Execute complex aggregations (GroupBy) in parallel.

### Hadoop: The Democratization of Processing

![Hadoop Framework: MapReduce, HDFS, Avro, Parquet](../assets/slides/m1_ecosistemas_p02.jpg)

## Instructions

The main script is located at `ejercicios/03_procesamiento_distribuido/esqueleto.py`. Your task is to complete the functions marked with `TODO` to build a functional pipeline.

### Programming Task
You must implement the `procesamiento_dask()` function so that it:
1. Starts a local client (`LocalCluster`).
2. Reads the QoG dataset processed in the previous exercise.
3. Calculates the annual average of the Democracy Index.
4. Compares execution time vs traditional Pandas.
