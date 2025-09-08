import { FASTAPI_URL } from "../../../js/config.js";

const runBtn = document.getElementById("runPipelineBtn");
const sourceSelect = document.getElementById("sourceSelect");
const datasetSelect = document.getElementById("datasetSelect");
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

    try {
        const polarsResp = await fetch(`${FASTAPI_URL}/etl/polars`);
        if (!polarsResp.ok) throw new Error(`Polars failed: ${polarsResp.status}`);
        const polarsData = await polarsResp.json();

        const pysparkResp = await fetch(`${FASTAPI_URL}/etl/pyspark`);
        if (!pysparkResp.ok) throw new Error(`PySpark failed: ${pysparkResp.status}`);
        const pysparkData = await pysparkResp.json();

        polarsPre.textContent = JSON.stringify(polarsData.result ?? polarsData, null, 2);
        pysparkPre.textContent = JSON.stringify(pysparkData.result ?? pysparkData, null, 2);

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
  }
});
