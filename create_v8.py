import os

# Base path
BASE = "PyDataNova/app"

# Files with contents
files = {
    f"{BASE}/api/fastapi_service/main.py": """from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_service.routers.etl_orchestration import router as etl_router

app = FastAPI(title="PyDataNova FastAPI v8")

origins = [
    "https://shadowwalkersb.github.io",
    "http://localhost:5500",
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(etl_router)

@app.get("/")
async def root():
    return {"message": "PyDataNova FastAPI v8 running…"}
""",
    f"{BASE}/api/fastapi_service/routers/etl_orchestration.py": """from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.api.core.prefect.orchestrate import orchestrate_pipelines

router = APIRouter(prefix="/etl", tags=["ETL-Orchestration"])

@router.post("/run")
async def run_orchestration(sources: dict):
    try:
        results = orchestrate_pipelines(sources)
        return {"results": results}
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)
""",
    f"{BASE}/api/core/prefect/flows/polars.py": """from prefect import flow, task
import pandas as pd

@task
def extract_csv(url: str):
    df = pd.read_csv(url)
    return df

@task
def transform(df):
    return df.head(5)

@task
def load(df):
    return df.to_dict(orient="records")

@flow
def polars_pipeline(url: str):
    df = extract_csv(url)
    transformed = transform(df)
    result = load(transformed)
    return result
""",
    f"{BASE}/api/core/prefect/orchestrate.py": """from app.api.core.prefect.flows.polars import polars_pipeline

def orchestrate_pipelines(sources: dict):
    results = {}
    for name, info in sources.items():
        if info[1] == "csv":
            results[name] = polars_pipeline(info[0])
        else:
            results[name] = {"error": f"Unsupported type {info[1]}"}
    return results
""",
    f"{BASE}/versions/v8/index.html": """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>v8 – ETL Orchestration</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <div class="container">
    <h1>v8 – ETL Orchestration Dashboard</h1>
    <button id="runPipelineBtn">Run Orchestration</button>
    <p id="status">Status: idle</p>

    <h2>Polars Pipelines</h2>
    <div id="polars-pane"></div>
  </div>
  <script type="module" src="js/fetch.js"></script>
</body>
</html>
""",
    f"{BASE}/versions/v8/style.css": """body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

.container {
    display: flex;
    flex-direction: column;
    gap: 10px;
    padding: 10px;
    box-sizing: border-box;
    min-height: 100vh;
}

h1, h2 {
    margin-top: 0;
    text-align: center;
}

#runPipelineBtn {
    padding: 6px 12px;
    background-color: #28a745;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 1rem;
    transition: background-color 0.2s ease;
}

#runPipelineBtn:hover {
    background-color: #218838;
}

.sub-pane {
    border: 1px dashed #aaa;
    border-radius: 4px;
    margin: 10px 0;
    padding: 8px;
    background-color: #fff;
}

.sub-pane-header {
    font-weight: bold;
    background-color: #e2e2e2;
    padding: 4px 8px;
    border-radius: 3px;
    user-select: none;
    cursor: pointer;
}
""",
    f"{BASE}/versions/v8/js/fetch.js": """const API_BASE = window.FASTAPI_URL || "http://localhost:8000";

const runBtn = document.getElementById("runPipelineBtn");
const statusEl = document.getElementById("status");
const polarsPane = document.getElementById("polars-pane");

const MULTI_SOURCES = {
  taxi_csv: ["https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv", "csv"],
  users_csv: ["https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv", "csv"]
};

runBtn.addEventListener("click", async () => {
  statusEl.textContent = "Status: Running orchestration…";
  polarsPane.querySelectorAll(".sub-pane").forEach(el => el.remove());

  try {
    const resp = await fetch(`${API_BASE}/etl/run`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(MULTI_SOURCES)
    });
    if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
    const data = await resp.json();

    for (const [source, result] of Object.entries(data.results)) {
      const subDiv = document.createElement("div");
      subDiv.classList.add("sub-pane");

      const header = document.createElement("div");
      header.classList.add("sub-pane-header");
      header.textContent = source;

      const pre = document.createElement("pre");
      pre.textContent = JSON.stringify(result, null, 2);

      header.addEventListener("click", () => {
        pre.style.display = pre.style.display === "none" ? "block" : "none";
      });

      subDiv.appendChild(header);
      subDiv.appendChild(pre);
      polarsPane.appendChild(subDiv);
    }

    statusEl.textContent = "Status: Orchestration completed.";
  } catch (err) {
    console.error(err);
    statusEl.textContent = "Status: Error running orchestration.";
  }
});
"""
}

# Create folders and files
for path, content in files.items():
    dir_path = os.path.dirname(path)
    os.makedirs(dir_path, exist_ok=True)
    with open(path, "w") as f:
        f.write(content)

print("v8 folder structure and files created successfully!")
