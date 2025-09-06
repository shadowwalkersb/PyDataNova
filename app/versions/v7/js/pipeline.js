// Minimal config: override via window.FASTAPI_URL if needed
const API_BASE = window.FASTAPI_URL || "http://localhost:8000";

const runBtn = document.getElementById("runPipelineBtn");
const statusEl = document.getElementById("status");

const sourceSelect = document.getElementById("sourceSelect");
const datasetSelect = document.getElementById("datasetSelect");
const csvUrlInput = document.getElementById("csvUrl");

const polarsPre = document.getElementById("polars-output");
const pysparkPre = document.getElementById("pyspark-output");

// Show/hide custom URL input
datasetSelect.addEventListener("change", () => {
  if (datasetSelect.value === "custom") {
    csvUrlInput.classList.remove("hidden");
    csvUrlInput.focus();
  } else {
    csvUrlInput.classList.add("hidden");
  }
});

runBtn.addEventListener("click", async () => {
  statusEl.textContent = "Running pipeline…";
  polarsPre.textContent = "Loading…";
  pysparkPre.textContent = "Placeholder (inactive)";

  // Determine CSV URL
  let csv_url = "";
  const source = sourceSelect.value;

  if (datasetSelect.value === "custom") {
    csv_url = csvUrlInput.value.trim();
    if (!csv_url) {
      statusEl.textContent = "Please provide a CSV URL.";
      return;
    }
  } else if (datasetSelect.value === "nyc_taxi_sample") {
    csv_url = "https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv";
  } else {
    statusEl.textContent = "Unknown dataset selected.";
    return;
  }

  // Build query
  const params = new URLSearchParams({ source, csv_url });

  try {
    const resp = await fetch(`${API_BASE}/etl/polars?${params.toString()}`);
    if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
    const data = await resp.json();

    polarsPre.textContent = JSON.stringify(data.result ?? data, null, 2);
    statusEl.textContent = "Pipeline completed.";
  } catch (err) {
    console.error(err);
    statusEl.textContent = "Error running pipeline.";
    polarsPre.textContent = String(err);
  }
});
