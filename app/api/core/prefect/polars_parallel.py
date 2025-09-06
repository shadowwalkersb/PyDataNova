import polars as pl
import requests
from io import BytesIO, StringIO
from prefect import flow, task

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
