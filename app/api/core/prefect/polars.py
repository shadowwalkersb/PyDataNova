import polars as pl
import io
import requests
from io import BytesIO, StringIO
from prefect import flow, task

def pipeline(file_path: str = None, file_url: str = None):
    try:
        if file_url:
            resp = requests.get(file_url)
            resp.raise_for_status()
            df = pl.read_csv(io.BytesIO(resp.content))
        elif file_path:
            df = pl.read_csv(file_path)
        else:
            return {"error": "No CSV source provided"}

        preview = df.head(10).to_dicts()

        return {
            "rows": len(df),
            "columns": df.columns,
            "preview": preview,
        }
    except Exception as e:
        return {"error": str(e)}

@task
def process_source(name: str, url: str, fmt: str):
    """
    Fetch CSV or JSON from URL, run Polars ETL, return preview.
    """
    resp = requests.get(url)
    resp.raise_for_status()
    content_type = resp.headers.get("Content-Type", "")

    if "json" in content_type or fmt.lower() == "json":
        df = pl.read_json(BytesIO(resp.content))
    else:  # default CSV
        df = pl.read_csv(StringIO(resp.text))

    # return first 20 rows as dict
    return {name: df.head(20).to_dicts()}

@flow
def polars_parallel(sources: dict):
    """
    Run multiple Polars ETL tasks in parallel.
    sources = {
        "taxi_csv": ["https://example.com/taxi.csv", "csv"],
        "users_json": ["https://example.com/users.json", "json"]
    }
    """
    futures = [process_source.submit(name, url, fmt) for name, (url, fmt) in sources.items()]
    results = {}
    for f in futures:
        results.update(f.result())
    return results
