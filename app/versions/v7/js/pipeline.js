import { FASTAPI_URL } from "./config.js";

const runBtn = document.getElementById("runPipelineBtn");
const statusEl = document.getElementById("status");
const tableHeader = document.getElementById("tableHeader");
const tableBody = document.getElementById("tableBody");
const dataPre = document.getElementById("dataPre");

runBtn.addEventListener("click", async () => {
    statusEl.textContent = "Running pipeline...";
    tableHeader.innerHTML = "";
    tableBody.innerHTML = "";

    // Trigger ETL
    fetch(`${FASTAPI_URL}/pipeline/run`, { method: "POST" })
    .then(response => {
        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        return response.json();
    })
    .then(data => {
        statusEl.textContent = data.message;
        dataPre.textContent = JSON.stringify(data.results, null, 2);

    })
    .catch(err => {
        statusEl.textContent = "Error running pipeline";
        console.error(err);
    });
});
