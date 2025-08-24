import httpx
import pandas as pd
from io import StringIO
from prefect import flow, task

CSV_URL = "https://raw.githubusercontent.com/corgis-edu/corgis/master/website/datasets/csv/weather/weather.csv"
API_URL = "https://jsonplaceholder.typicode.com/posts"

@task
def extract_csv():
    resp = httpx.get(CSV_URL)
    resp.raise_for_status()
    df = pd.read_csv(StringIO(resp.text))
    return df

@task
def transform_weather(df):
    return df.groupby("Station.State")["Data.Temperature.Avg Temp"].mean().head(5).to_dict()

@task
def extract_api():
    resp = httpx.get(API_URL)
    resp.raise_for_status()
    return resp.json()

@task
def transform_api(data):
    return [{"id": post["id"], "userId": post["userId"], "title": post["title"]} for post in data[:5]]

@flow(name="v8_pipeline")
def run_pipeline():
    csv_df = extract_csv()
    csv_result = transform_weather(csv_df)

    api_data = extract_api()
    api_result = transform_api(api_data)

    return {"csv": csv_result, "api": api_result}
