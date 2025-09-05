from prefect import flow, task
import polars as pl

@task
def extract():
    return pl.DataFrame({
        "id": [1, 2, 3],
        "value": ["A", "B", "C"]
    })

@task
def transform(df: pl.DataFrame):
    return df.with_columns((pl.col("id") * 10).alias("id_x10"))

@task
def load(df: pl.DataFrame):
    return df.to_dicts()

@flow(name="Polars ETL")
def polars():
    raw = extract()
    transformed = transform(raw)
    return load(transformed)
