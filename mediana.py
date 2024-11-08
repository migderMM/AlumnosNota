# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1oaLCd3I9sPd6JMwcUW8SeBXSZGpLuQyX
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr, mean, corr

spark=SparkSession.builder.appName("Promedio").getOrCreate()

df=spark.read.csv("na.csv", header=True, inferSchema=True, sep=";")

df.show()

median_expr="(percentile_approx({column},0.5))".format(column="Notas")
median=df.selectExpr(median_expr).first()[0]

print(f"Mediana: {median}")