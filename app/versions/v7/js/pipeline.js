import { FASTAPI_URL } from "./config.js";

const runBtn = document.getElementById("runPipelineBtn");
const statusEl = document.getElementById("status");
const tableHeader = document.getElementById("tableHeader");
const tableBody = document.getElementById("tableBody");

runBtn.addEventListener("click", async () => {
  statusEl.textContent = "Started...";
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
    })
    .catch(err => {
        statusEl.textContent = "Error running pipeline";
        console.error(err);
    });
});
