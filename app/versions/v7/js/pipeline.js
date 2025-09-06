// Minimal config: override via window.FASTAPI_URL if you need a different host/port
const API_BASE = window.FASTAPI_URL || "http://localhost:8000";

const runBtn = document.getElementById("runPipelineBtn");
const statusEl = document.getElementById("status");

const sourceSelect = document.getElementById("sourceSelect");
const datasetSelect = document.getElementById("datasetSelect");
const csvUrlInput = document.getElementById("csvUrl");

const polarsPre = document.getElementById("polars-output");
const pysparkPre = document.getElementById("pyspark-output");

// Toggle custom URL field
datasetSelect.addEventListener("change", () => {
  if (datasetSelect.value === "custom") {
    csvUrlInput.classList.remove("hidden");
    csvUrlInput.focus();
  } else {
    csvUrlInput.classList.add("hidden");
  }
});

runBtn.addEventListener("click", async () => {
  statusEl.textContent = "Running pipeline...";
  polarsPre.textContent = "Loading…";

  // Build query params
  const source = sourceSelect.value; // currently only "csv"
  const dataset = datasetSelect.value;

  const params = new URLSearchParams({ source });
  if (dataset === "custom") {
    const url = csvUrlInput.value.trim();
    if (!url) {
      statusEl.textContent = "Please provide a CSV URL.";
      return;
    }
    params.set("csv_url", url);
  } else {
    params.set("dataset", dataset); // e.g., "nyc_taxi_sample"
  }

  try {
    const resp = await fetch(`${API_BASE}/etl/polars?${params.toString()}`);
    if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
    const data = await resp.json();

    polarsPre.textContent = JSON.stringify(data.result ?? data, null, 2);
    statusEl.textContent = "Pipeline completed.";
    // PySpark stays collapsed/inactive
    pysparkPre.textContent = "Placeholder (inactive)";
  } catch (err) {
    console.error(err);
    statusEl.textContent = "Error running pipeline.";
    polarsPre.textContent = String(err);
  }
});
