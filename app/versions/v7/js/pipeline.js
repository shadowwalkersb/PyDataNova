const API_BASE = window.FASTAPI_URL || "http://localhost:8000";

const runBtn = document.getElementById("runPipelineBtn");
const statusEl = document.getElementById("status");
const polarsPane = document.getElementById("polars-pane");
const pysparkPre = document.getElementById("pyspark-output");

// Working public sources
const MULTI_SOURCES = {
  taxi_csv: ["https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv", "csv"],
  users_json: ["https://raw.githubusercontent.com/veekun/titanic-parquet/main/titanic.json", "json"]
};

runBtn.addEventListener("click", async () => {
  statusEl.textContent = "Status: Running multiple pipelines…";

  // Clear old sub-panels
  polarsPane.querySelectorAll(".sub-pane").forEach(el => el.remove());
  pysparkPre.textContent = "Inactive";

  try {
    const resp = await fetch(`${API_BASE}/etl/polars/multi`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(MULTI_SOURCES)
    });
    if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
    const data = await resp.json();

    // Inject sub-panels
    for (const [source, result] of Object.entries(data.results)) {
      const subDiv = document.createElement("div");
      subDiv.classList.add("sub-pane");

      const h3 = document.createElement("h3");
      h3.textContent = source;
      subDiv.appendChild(h3);

      const pre = document.createElement("pre");
      pre.textContent = JSON.stringify(result, null, 2);
      subDiv.appendChild(pre);

      polarsPane.appendChild(subDiv);
    }

    statusEl.textContent = "Status: All pipelines completed.";
  } catch (err) {
    console.error(err);
    statusEl.textContent = "Status: Error running pipelines.";
  }
});
