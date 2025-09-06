const API_BASE = window.FASTAPI_URL || "http://localhost:8000";

const runBtn = document.getElementById("runPipelineBtn");
const statusEl = document.getElementById("status");
const polarsPre = document.getElementById("polars-output");
const pysparkPre = document.getElementById("pyspark-output");

// Example multi-source payload
const MULTI_SOURCES = {
  taxi_csv: ["https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/iris/iris.csv", "csv"],
  users_json: ["https://raw.githubusercontent.com/veekun/titanic-parquet/main/titanic.json", "json"]
};

runBtn.addEventListener("click", async () => {
  statusEl.textContent = "Status: Running multiple pipelines…";
  polarsPre.textContent = "Loading…";
  pysparkPre.textContent = "Inactive";

  try {
    const resp = await fetch(`${API_BASE}/etl/polars/multi`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(MULTI_SOURCES)
    });
    if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
    const data = await resp.json();
    polarsPre.textContent = JSON.stringify(data.results, null, 2);
    statusEl.textContent = "Status: All pipelines completed.";
  } catch (err) {
    console.error(err);
    polarsPre.textContent = String(err);
    statusEl.textContent = "Status: Error running pipelines.";
  }
});
