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

// Dataset mapping
const DATASETS = {
  csv: {
    airtravel_csv: "https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv",
    nyc_taxi_sample: "https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv", // placeholder
    covid_csv: "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv"
  },
  json: {
    sample_json: "https://jsonplaceholder.typicode.com/posts",
    openweather_sample: "https://api.open-meteo.com/v1/forecast?latitude=35&longitude=139&hourly=temperature_2m",
    github_events: "https://api.github.com/events"
  },
  api: {
    sample_api: "https://jsonplaceholder.typicode.com/todos",
    spacex_launches: "https://api.spacexdata.com/v4/launches/latest",
    iss_now: "http://api.open-notify.org/iss-now.json"
  }
};

// Initialize datasets on load
function populateDatasets() {
  const src = sourceSelect.value;
  datasetSelect.innerHTML = "";
  for (const [key, _url] of Object.entries(DATASETS[src])) {
    datasetSelect.innerHTML += `<option value="${key}">${key}</option>`;
  }
  datasetSelect.innerHTML += `<option value="custom">Custom URL</option>`;
}

populateDatasets();

// Change datasets when source changes
sourceSelect.addEventListener("change", () => {
  populateDatasets();
  urlInput.classList.add("hidden");
});

// Show URL input if "custom"
datasetSelect.addEventListener("change", () => {
  if (datasetSelect.value === "custom") {
    urlInput.classList.remove("hidden");
    urlInput.focus();
  } else {
    urlInput.classList.add("hidden");
  }
});

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
    url = DATASETS[source][datasetSelect.value];
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
