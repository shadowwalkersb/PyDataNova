import httpx
import pandas as pd
from io import StringIO

CSV_URL = "https://raw.githubusercontent.com/corgis-edu/corgis/master/website/datasets/csv/weather/weather.csv"

def extract_csv(url: str) -> pd.DataFrame:
    """Download CSV from URL and return as DataFrame"""
    resp = httpx.get(url)
    resp.raise_for_status()
    return pd.read_csv(StringIO(resp.text))

def transform_weather(df: pd.DataFrame) -> dict:
    """Compute average temperature per state (top 5 states for demo)"""
    return df.groupby("Station.State")["Data.Temperature.Avg Temp"].mean().head(5).to_dict()

def run_pipeline() -> dict:
    """Run the ETL pipeline and return results"""
    df = extract_csv(CSV_URL)
    return {"weather": transform_weather(df)}
