import polars as pl
import io
import pandas as pd
from typing import Optional, Dict

def run_polars_pipeline(file_bytes: Optional[bytes] = None, file_url: Optional[str] = None, file_type: str = "csv") -> Dict:
    """
    Minimal Polars ETL wrapper.
    file_bytes: CSV or JSON content as bytes
    file_url: alternative (not used if file_bytes provided)
    file_type: "csv" or "json"
    Returns preview (first 5 rows), summary (row count, columns)
    """
    if file_bytes:
        buffer = io.BytesIO(file_bytes)
    elif file_url:
        import requests
        resp = requests.get(file_url)
        resp.raise_for_status()
        buffer = io.BytesIO(resp.content)
    else:
        raise ValueError("No input provided for ETL")

    # Read data
    if file_type == "csv":
        df = pl.read_csv(buffer)
    elif file_type == "json":
        df = pl.read_json(buffer)
    else:
        raise ValueError(f"Unsupported file type: {file_type}")

    # Minimal ETL: here you could add transforms, cleaning, etc.
    preview = df.head(5).to_dicts()
    summary = {"rows": df.height, "columns": df.columns}

    return {"preview": preview, "summary": summary, "columns": df.columns}
