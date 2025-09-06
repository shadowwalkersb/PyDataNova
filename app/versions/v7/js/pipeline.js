const API_BASE = window.FASTAPI_URL || "http://localhost:8000";

const runBtn = document.getElementById("runPipelineBtn");
const statusEl = document.getElementById("status");

const sourceSelect = document.getElementById("sourceSelect");
const datasetSelect = document.getElementById("datasetSelect");
const csvUrlInput = document.getElementById("csvUrl");

const polarsSummary = document.getElementById("polars-summary");
const polarsThead = document.getElementById("polars-thead");
const polarsTbody = document.getElementById("polars-tbody");
const pysparkPre = document.getElementById("pyspark-output");

// Toggle custom URL input
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
  polarsSummary.textContent = "";
  polarsThead.innerHTML = "";
  polarsTbody.innerHTML = "";
  pysparkPre.textContent = "Placeholder (inactive)";

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

  const params = new URLSearchParams({ source, csv_url });

  try {
    const resp = await fetch(`${API_BASE}/etl/polars?${params.toString()}`);
    if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
    const data = await resp.json();
    const result = data.result ?? data;

    // --- Summary ---
    if (result.summary) {
      polarsSummary.textContent = `Rows: ${result.summary.rows}`;
    }

    // --- Table ---
    if (result.preview && result.preview.length > 0) {
      const columns = result.columns ?? Object.keys(result.preview[0]);
      polarsThead.innerHTML =
        "<tr>" + columns.map(c => `<th>${c}</th>`).join("") + "</tr>";
      polarsTbody.innerHTML = result.preview
        .map(row =>
          "<tr>" + columns.map(c => `<td>${row[c] ?? ""}</td>`).join("") + "</tr>"
        )
        .join("");
    }

    statusEl.textContent = "Pipeline completed.";
  } catch (err) {
    console.error(err);
    statusEl.textContent = "Error running pipeline.";
    polarsSummary.textContent = "";
    polarsThead.innerHTML = "";
    polarsTbody.innerHTML = "";
    pysparkPre.textContent = String(err);
  }
});

const pysparkPane = document.getElementById("pyspark-pane");
const pysparkHeader = document.getElementById("pyspark-header");

pysparkHeader.addEventListener("click", () => {
  if (pysparkPane.classList.contains("collapsed")) {
    pysparkPane.classList.remove("collapsed");
    pysparkPane.classList.add("expanded");
    pysparkHeader.innerHTML = "PySpark ETL &#9660;"; // down arrow
  } else {
    pysparkPane.classList.remove("expanded");
    pysparkPane.classList.add("collapsed");
    pysparkHeader.innerHTML = "PySpark ETL &#9654;"; // right arrow
  }
});
