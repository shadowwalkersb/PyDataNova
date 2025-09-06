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
  statusEl.textContent = "Status: Running pipeline...";
  polarsPre.textContent = "Loading…";
  pysparkPre.textContent = "Inactive";

  const source = sourceSelect.value;
  const dataset = datasetSelect.value;

  const params = new URLSearchParams({ source });
  if (dataset === "custom") {
    const url = csvUrlInput.value.trim();
    if (!url) {
      statusEl.textContent = "Status: Please provide a URL.";
      return;
    }
    params.set("url", url);
  } else {
    params.set("dataset", dataset);
  }

  try {
    const resp = await fetch(`${API_BASE}/etl/polars?${params.toString()}`);
    if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
    const data = await resp.json();
    polarsPre.textContent = JSON.stringify(data.result ?? data, null, 2);
    statusEl.textContent = "Status: Pipeline completed.";
  } catch (err) {
    console.error(err);
    polarsPre.textContent = String(err);
    statusEl.textContent = "Status: Error running pipeline.";
  }
});
