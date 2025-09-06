import polars as pl
import io
import requests


def run_polars_pipeline(file_path: str = None, file_url: str = None):
    """
    Simple ETL using Polars.
    - Load CSV (local path or remote URL)
    - Transform (basic ops for now)
    - Return preview
    """
    try:
        if file_url:
            resp = requests.get(file_url)
            resp.raise_for_status()
            df = pl.read_csv(io.BytesIO(resp.content))
        elif file_path:
            df = pl.read_csv(file_path)
        else:
            return {"error": "No CSV source provided"}

        # --- Transform step (basic example) ---
        preview = df.head(10).to_dicts()

        return {
            "rows": len(df),
            "columns": df.columns,
            "preview": preview,
        }
    except Exception as e:
        return {"error": str(e)}
