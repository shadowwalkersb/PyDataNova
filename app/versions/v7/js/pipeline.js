import { FASTAPI_URL } from "../../../js/config.js";

const runBtn = document.getElementById("runPipelineBtn");
const statusEl = document.getElementById("status");

runBtn.addEventListener("click", async () => {
    statusEl.textContent = "Running pipelines...";
});
