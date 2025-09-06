import polars as pl
import io
import pandas as pd
from typing import Optional, Dict
import json

def run_polars_pipeline(file_bytes: Optional[bytes] = None,
                        file_url: Optional[str] = None,
                        file_type: str = "csv") -> Dict:
    """
    Polars ETL wrapper supporting CSV, JSON arrays, and arbitrary JSON objects.
    Returns preview (first 5 rows), summary (rows, columns), and column names.
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

    if file_type == "csv":
        df = pl.read_csv(buffer)
    elif file_type == "json":
        try:
            # Try to read as array of objects
            df = pl.read_json(buffer)
        except Exception:
            # If JSON is a single object or nested, normalize to a table via pandas
            buffer.seek(0)
            raw = json.load(buffer)
            if isinstance(raw, dict):
                # single object -> wrap in a list
                raw = [raw]
            elif isinstance(raw, list):
                # already a list -> ok
                pass
            else:
                # unknown structure
                raise ValueError("Unsupported JSON structure")
            pdf = pd.json_normalize(raw)
            df = pl.from_pandas(pdf)
    else:
        raise ValueError(f"Unsupported file type: {file_type}")

    # Minimal ETL: preview first 5 rows
    preview = df.head(5).to_dicts()
    summary = {"rows": df.height, "columns": df.columns}

    return {"preview": preview, "summary": summary, "columns": df.columns}
