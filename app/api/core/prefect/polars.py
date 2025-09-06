import polars as pl
import io
import requests

def run_polars_pipeline(file_url: str):
    try:
        resp = requests.get(file_url)
        resp.raise_for_status()
        df = pl.read_csv(io.BytesIO(resp.content))

        # Only do transformations if expected columns exist
        cols = df.columns
        if "pickup_datetime" in cols and "dropoff_datetime" in cols:
            df = df.with_columns([
                (pl.col("dropoff_datetime").str.strptime(pl.Datetime) -
                 pl.col("pickup_datetime").str.strptime(pl.Datetime))
                .dt.cast(pl.Int64)  # seconds
                .alias("trip_duration_sec")
            ])
        else:
            # Skip trip_duration calculation
            pass

        preview = df.head(10).to_dicts()
        summary = {"rows": df.height}

        return {"columns": df.columns, "preview": preview, "summary": summary}
    except Exception as e:
        return {"error": str(e)}
