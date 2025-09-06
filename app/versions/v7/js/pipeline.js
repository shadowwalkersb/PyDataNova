const API_BASE = window.FASTAPI_URL || "http://localhost:8000";

const runBtn = document.getElementById("runPipelineBtn");
const statusEl = document.getElementById("status");

const sourceSelect = document.getElementById("sourceSelect");
const datasetSelect = document.getElementById("datasetSelect");
const urlInput = document.getElementById("urlInput");

const polarsSummary = document.getElementById("polars-summary");
const polarsThead = document.getElementById("polars-thead");
const polarsTbody = document.getElementById("polars-tbody");

const pysparkPane = document.getElementById("pyspark-pane");
const pysparkHeader = document.getElementById("pyspark-header");
const pysparkPre = document.getElementById("pyspark-output");

// PySpark toggle
pysparkHeader.addEventListener("click", () => {
  if (pysparkPane.classList.contains("collapsed")) {
    pysparkPane.classList.remove("collapsed");
    pysparkPane.classList.add("expanded");
    pysparkHeader.innerHTML = "PySpark ETL &#9660;";
  } else {
    pysparkPane.classList.remove("expanded");
    pysparkPane.classList.add("collapsed");
    pysparkHeader.innerHTML = "PySpark ETL &#9654;";
  }
});

// Change datasets based on source
sourceSelect.addEventListener("change", () => {
  datasetSelect.innerHTML = "";
  urlInput.classList.add("hidden");

  if (sourceSelect.value === "csv") {
    datasetSelect.innerHTML = `
      <option value="airtravel_csv" selected>Air Travel Sample (CSV)</option>
      <option value="custom">Custom URL</option>`;
  } else if (sourceSelect.value === "json") {
    datasetSelect.innerHTML = `
      <option value="sample_json" selected>Sample JSON</option>
      <option value="custom">Custom URL</option>`;
  } else if (sourceSelect.value === "api") {
    datasetSelect.innerHTML = `
      <option value="sample_api" selected>Sample API</option>
      <option value="custom">Custom URL</option>`;
  }
});

datasetSelect.addEventListener("change", () => {
  if (datasetSelect.value === "custom") {
    urlInput.classList.remove("hidden");
    urlInput.focus();
  } else {
    urlInput.classList.add("hidden");
  }
});

// Run pipeline
runBtn.addEventListener("click", async () => {
  statusEl.textContent = "Running pipeline…";
  polarsSummary.textContent = "";
  polarsThead.innerHTML = "";
  polarsTbody.innerHTML = "";
  pysparkPre.textContent = "Placeholder (inactive)";

  const source = sourceSelect.value;
  let url = "";

  if (datasetSelect.value === "custom") {
    url = urlInput.value.trim();
    if (!url) {
      statusEl.textContent = "Please provide a dataset URL.";
      return;
    }
  } else {
    // Predefined datasets
    if (source === "csv") url = "https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv";
    else if (source === "json") url = "https://jsonplaceholder.typicode.com/posts";
    else if (source === "api") url = "https://jsonplaceholder.typicode.com/todos";
  }

  const params = new URLSearchParams({ source, url });

  try {
    const resp = await fetch(`${API_BASE}/etl/run?${params.toString()}`);
    if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
    const data = await resp.json();
    const result = data.result ?? data;

    if (result.summary) polarsSummary.textContent = `Rows: ${result.summary.rows}`;
    if (result.preview && result.preview.length > 0) {
      const columns = result.columns ?? Object.keys(result.preview[0]);
      polarsThead.innerHTML = "<tr>" + columns.map(c => `<th>${c}</th>`).join("") + "</tr>";
      polarsTbody.innerHTML = result.preview
        .map(row => "<tr>" + columns.map(c => `<td>${row[c] ?? ""}</td>`).join("") + "</tr>")
        .join("");
    }

    statusEl.textContent = "Pipeline completed.";
  } catch (err) {
    console.error(err);
    statusEl.textContent = "Error running pipeline.";
  }
});
