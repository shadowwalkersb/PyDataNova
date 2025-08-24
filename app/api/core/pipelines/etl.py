import httpx
import pandas as pd
from io import StringIO

# Sources
CSV_URL = "https://raw.githubusercontent.com/corgis-edu/corgis/master/website/datasets/csv/weather/weather.csv"
API_URL = "https://jsonplaceholder.typicode.com/posts"

def extract_csv(url: str) -> pd.DataFrame:
    """Download CSV from URL and return as DataFrame"""
    resp = httpx.get(url)
    resp.raise_for_status()
    return pd.read_csv(StringIO(resp.text))

def extract_api(url):
    """Compute average temperature per state (top 5 states for demo)"""
    resp = httpx.get(url)
    resp.raise_for_status()
    return resp.json()

def transform_weather(df: pd.DataFrame) -> dict:
    return df.groupby("Station.State")["Data.Temperature.Avg Temp"].mean().head(5).to_dict()

def transform_api(data):
    """Transform API data to keep only the first 5 posts with selected fields."""
    transformed = []
    for post in data[:5]:
        transformed.append({
            "id": post["id"],
            "userId": post["userId"],
            "title": post["title"]
        })
    return transformed

def run_pipeline() -> dict:
    results = {}

    # CSV
    csv_df = extract_csv(CSV_URL)
    results["csv"] = transform_weather(csv_df)

    # API
    api_data = extract_api(API_URL)
    results["api"] = transform_api(api_data)

    return results
