import polars as pl
import io
import pandas as pd
from typing import Optional, Dict
import json

def run_polars_pipeline(file_bytes: Optional[bytes] = None,
                        file_url: Optional[str] = None,
                        file_type: str = "csv") -> Dict:
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
    elif file_type == "parquet":
        df = pl.read_parquet(buffer)
    elif file_type == "json" or file_type == "api":
        try:
            df = pl.read_json(buffer)
        except Exception:
            buffer.seek(0)
            raw = json.load(buffer)
            if isinstance(raw, dict):
                raw = [raw]
            elif isinstance(raw, list):
                pass
            else:
                raise ValueError("Unsupported JSON structure")
            pdf = pd.json_normalize(raw)
            df = pl.from_pandas(pdf)
    else:
        raise ValueError(f"Unsupported file type: {file_type}")

    preview = df.head(5).to_dicts()
    summary = {"rows": df.height, "columns": df.columns}
    return {"preview": preview, "summary": summary, "columns": df.columns}
