# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KJjz61mmG7182Aw7HCNGqa-SYMIrkHtY
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr, mean, corr

spark=SparkSession.builder.appName("Media").getOrCreate()

spark

df=spark.read.csv("na.csv", header=True, inferSchema=True, sep=";")

df.show()

df_media=df.select(mean(col("Notas")).alias("Media"))

print(df_media.show())