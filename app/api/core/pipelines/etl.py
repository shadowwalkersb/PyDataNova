import polars as pl

def extract():
    # Dummy CSV or mock data
    data = pl.DataFrame({
        "id": [1, 2, 3],
        "name": ["Alice", "Bob", "Charlie"],
        "value": [10, 20, 30]
    })
    return data

def transform(df: pl.DataFrame):
    # Simple transformation: double the value
    return df.with_columns((df["value"] * 2).alias("value_transformed"))

def load(df: pl.DataFrame):
    df_pd = df.to_pandas()
    return len(df)

def etl_flow():
    df = extract()
    df_transformed = transform(df)
    rows_inserted = load(df_transformed)
    return {"rows_inserted": rows_inserted}
