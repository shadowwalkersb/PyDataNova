from prefect import flow, task
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("PyDataNova-v7").getOrCreate()

@task
def extract():
    data = [(1, "X"), (2, "Y"), (3, "Z")]
    return spark.createDataFrame(data, ["id", "value"])

@task
def transform(df):
    return df.withColumn("id_x10", col("id") * 10)

@task
def load(df):
    return [row.asDict() for row in df.collect()]

@flow(name="PySpark ETL")
def pyspark():
    raw = extract()
    transformed = transform(raw)
    return load(transformed)
