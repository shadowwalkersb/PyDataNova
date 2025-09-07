import { FASTAPI_URL } from "../../../js/config.js";

const runBtn = document.getElementById("runPipelineBtn");
const statusEl = document.getElementById("status");
const polarsPre = document.getElementById("polars-output");
const pysparkPre = document.getElementById("pyspark-output");

async function runPipeline() {
    statusEl.textContent = "Running pipelines...";
    polarsPre.textContent = "Loading...";
    pysparkPre.textContent = "Loading...";

    try {
        const polarsResp = await fetch(`${FASTAPI_URL}/etl/polars`);
        if (!polarsResp.ok) throw new Error(`Polars failed: ${polarsResp.status}`);
        const polarsData = await polarsResp.json();

        const pysparkResp = await fetch(`${FASTAPI_URL}/etl/pyspark`);
        if (!pysparkResp.ok) throw new Error(`PySpark failed: ${pysparkResp.status}`);
        const pysparkData = await pysparkResp.json();

        polarsPre.textContent = JSON.stringify(polarsData.result, null, 2);
        pysparkPre.textContent = JSON.stringify(pysparkData.result, null, 2);

        statusEl.textContent = "Pipelines completed successfully.";
    } catch (err) {
        polarsPre.textContent = String(err);
        pysparkPre.textContent = String(err);
        statusEl.textContent = "Error running pipelines.";
        console.error(err);
    }
}

runBtn.addEventListener("click", runPipeline);
