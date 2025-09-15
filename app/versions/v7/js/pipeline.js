import { FASTAPI_URL } from "../../../js/config.js";

const runBtn = document.getElementById("runPipelineBtn");
const sourceSelect = document.getElementById("sourceSelect");
const datasetSelect = document.getElementById("datasetSelect");
const urlInput = document.getElementById("url");
const statusEl = document.getElementById("status");
const polarsPre = document.getElementById("polars-output");
const pysparkPre = document.getElementById("pyspark-output");

const polarsSummary = document.getElementById("polars-summary");
const polarsThead = document.getElementById("polars-thead");
const polarsTbody = document.getElementById("polars-tbody");

const pysparkPane = document.getElementById("pyspark-pane");
const pysparkHeader = document.getElementById("pyspark-header");
const polarsPane = document.getElementById("polars-pane");

async function runPipeline() {
    statusEl.textContent = "Running pipelines...";
    polarsPre.textContent = "Loading...";
    pysparkPre.textContent = "Loading...";
    polarsThead.innerHTML = "";
    polarsTbody.innerHTML = "";

    const source = sourceSelect.value;
    const dataset = datasetSelect.value;

    if (dataset === "custom") {
        const url = urlInput.value.trim();
        if (!url) {
            statusEl.textContent = "Please provide a CSV URL.";
            return;
        }
    }

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

    const params = new URLSearchParams({ source, url, file_type: source });

    try {
        const resp = await fetch(`${FASTAPI_URL}/etl/run?${params.toString()}`);
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

        const result = polarsData.result;
        polarsSummary.textContent = `Rows: ${result.summary.rows}`;

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

        statusEl.textContent = "Pipelines completed successfully.";
    } catch (err) {
        polarsPre.textContent = String(err);
        polarsSummary.textContent = "";
        polarsThead.innerHTML = "";
        polarsTbody.innerHTML = "";
        pysparkPre.textContent = String(err);
        statusEl.textContent = "Error running pipelines.";
        console.error(err);
    }
}

runBtn.addEventListener("click", runPipeline);

// Toggle custom URL field
datasetSelect.addEventListener("change", () => {
  if (datasetSelect.value === "custom") {
    urlInput.classList.remove("hidden");
    urlInput.focus();
  } else {
    urlInput.classList.add("hidden");
  }
});

const pysparkPane = document.getElementById("pyspark-pane");
const pysparkHeader = document.getElementById("pyspark-header");
const pysparkPre = document.getElementById("pyspark-output");

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
  },
  parquet: {
    nyc_taxi_yellow_jan_2023: "https://www.nyc.gov/assets/tlc/downloads/pdf/data_reports/2023_01_yellow_tripdata.parquet",
    nyc_taxi_green_jan_2023: "https://www.nyc.gov/assets/tlc/downloads/pdf/data_reports/2023_01_green_tripdata.parquet",
    nyc_taxi_for_hire_jan_2023: "https://www.nyc.gov/assets/tlc/downloads/pdf/data_reports/2023_01_for_hire_tripdata.parquet"
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
