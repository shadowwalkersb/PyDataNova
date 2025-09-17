import polars as pl
import io
import requests

def pipeline(file_url):
    resp = requests.get(file_url)
    resp.raise_for_status()
    buffer = io.BytesIO(resp.content)

    df = pl.read_csv(buffer)

    preview = df.head(5).to_dicts()
    summary = {"rows": df.height, "columns": df.columns}

    return {"preview": preview, "summary": summary, "columns": df.columns}
