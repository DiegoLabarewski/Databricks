# Databricks notebook source
df = spark.read.csv("file:/Workspace/Users/user-ufpvolullmkq@oreilly-cloudlabs.com/Databricks/circuits.csv", header=True, inferSchema=True)
display(df)

# COMMAND ----------

print('s')
