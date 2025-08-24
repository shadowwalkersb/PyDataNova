import httpx
import pandas as pd
from io import StringIO
from prefect import flow, task, get_run_logger

# Sources
CSV_URL = "https://raw.githubusercontent.com/corgis-edu/corgis/master/website/datasets/csv/weather/weather.csv"
API_URL = "https://jsonplaceholder.typicode.com/posts"

# -------------------
# Extraction Tasks
# -------------------
@task
def extract_csv():
    logger = get_run_logger()
    logger.info("Starting CSV extraction")
    resp = httpx.get(CSV_URL)
    resp.raise_for_status()
    df = pd.read_csv(StringIO(resp.text))
    logger.info("CSV extraction finished")
    return df

@task
def extract_api():
    logger = get_run_logger()
    logger.info("Starting API extraction")
    resp = httpx.get(API_URL)
    resp.raise_for_status()
    data = resp.json()
    logger.info("API extraction finished")
    return data

# -------------------
# Transform Tasks
# -------------------
@task
def transform_weather(df):
    logger = get_run_logger()
    logger.info("Transforming CSV data")
    result = df.groupby("Station.State")["Data.Temperature.Avg Temp"].mean().head(5).to_dict()
    logger.info("CSV transform finished")
    return result

@task
def transform_api(data):
    logger = get_run_logger()
    logger.info("Transforming API data")
    result = [{"id": p["id"], "userId": p["userId"], "title": p["title"]} for p in data[:5]]
    logger.info("API transform finished")
    return result

# -------------------
# Pipeline Flow
# -------------------
@flow
def run_pipeline():
    """Run all ETL tasks in parallel and return results with progress"""
    results = {}

    # Run extraction in parallel
    csv_df_future = extract_csv.submit()
    api_data_future = extract_api.submit()

    # Transform after extraction
    results["csv"] = transform_weather.submit(csv_df_future)
    results["api"] = transform_api.submit(api_data_future)

    # Wait for all tasks to complete and gather results
    final_results = {k: v.result() for k, v in results.items()}
    return final_results
