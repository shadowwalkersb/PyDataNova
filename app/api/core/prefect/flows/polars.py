from prefect import flow, task
import pandas as pd

@task
def extract_csv(url: str):
    df = pd.read_csv(url)
    return df

@task
def transform(df):
    return df.head(5)

@task
def load(df):
    return df.to_dict(orient="records")

@flow
def polars_pipeline(url: str):
    df = extract_csv(url)
    transformed = transform(df)
    result = load(transformed)
    return result
