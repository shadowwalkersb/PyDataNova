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
const polarsPane = document.getElementById("polars-pane");

const MULTI_SOURCES = {
  taxi_csv: ["https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv", "csv"],
  users_json: ["https://raw.githubusercontent.com/veekun/titanic-parquet/main/titanic.json", "json"]
};

datasetSelect.addEventListener("change", () => {
  if (datasetSelect.value === "custom") {
    urlInput.classList.remove("hidden");
    urlInput.focus();
  } else {
    urlInput.classList.add("hidden");
  }
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
