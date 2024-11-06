# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BiTzl-57BP379y7GtCQYOyf3LxdRv_6-
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr, mean, corr

spark=SparkSession.builder.appName("Correlacion").getOrCreate()

df=spark.read.csv("na.csv", header=True, inferSchema=True, sep=";")

df.show()

correlacion=df.select(corr("Notas","Notas").alias("Correlacion"))

correlacion.show()