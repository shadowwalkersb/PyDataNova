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
        // Run Polars ETL
        const polarsResp = await fetch(`${FASTAPI_URL}/etl/polars`);
        if (!polarsResp.ok) throw new Error(`Polars failed: ${polarsResp.status}`);
        const polarsData = await polarsResp.json();

        // Run PySpark ETL
        const sparkResp = await fetch(`${FASTAPI_URL}/etl/pyspark`);
        if (!sparkResp.ok) throw new Error(`PySpark failed: ${sparkResp.status}`);
        const sparkData = await sparkResp.json();

        // Update UI
        statusEl.textContent = "Pipelines completed successfully.";

        polarsPre.textContent = JSON.stringify(polarsData.result, null, 2);
        pysparkPre.textContent = JSON.stringify(sparkData.result, null, 2);

    } catch (err) {
        statusEl.textContent = "Error running pipelines.";
        console.error(err);
    }
}

runBtn.addEventListener("click", runPipeline);
