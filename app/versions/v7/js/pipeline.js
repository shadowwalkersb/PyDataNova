import { FASTAPI_URL } from "../../../js/config.js";

const runBtn = document.getElementById("runPipelineBtn");
const statusEl = document.getElementById("status");
const polarsPre = document.getElementById("polars-output");
const pysparkPre = document.getElementById("pyspark-output");

runBtn.addEventListener("click", async () => {
    statusEl.textContent = "Running pipelines...";
    polarsPre.textContent = "Loading...";
    pysparkPre.textContent = "Loading...";

    try {
        // Fetch Polars pipeline
        const polarsResp = await fetch(`${FASTAPI_URL}/etl/polars`);
        const polarsData = await polarsResp.json();
        polarsPre.textContent = JSON.stringify(polarsData.result, null, 2);

        // Fetch PySpark pipeline
        const pysparkResp = await fetch(`${FASTAPI_URL}/etl/pyspark`);
        const pysparkData = await pysparkResp.json();
        pysparkPre.textContent = JSON.stringify(pysparkData.result, null, 2);

        statusEl.textContent = "Pipelines completed successfully.";
    } catch (err) {
        statusEl.textContent = "Error running pipelines";
        console.error(err);
    }
});
