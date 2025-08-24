import { FASTAPI_URL } from "./config.js";

const runBtn = document.getElementById("runPipelineBtn");
const statusEl = document.getElementById("status");
const dataPre = document.getElementById("dataPre");

const tasks = ["csv", "api"];
let runId = null;

runBtn.addEventListener("click", async () => {
    // Reset UI
    statusEl.textContent = "Pipeline started...";
    dataPre.textContent = "";
    tasks.forEach(t => {
        const el = document.getElementById(`${t}Status`);
        if (el) el.textContent = "Pending";
    });

    try {
        const resp = await fetch(`${FASTAPI_URL}/pipeline/run`, { method: "POST" });
        const data = await resp.json();
        runId = data.run_id;

        const interval = setInterval(async () => {
            const statusResp = await fetch(`${FASTAPI_URL}/pipeline/status/${runId}`);
            const statusData = await statusResp.json();

            tasks.forEach(t => {
                const el = document.getElementById(`${t}Status`);
                if (el) el.textContent = statusData.tasks[t];
            });

            let output = "";
            for (const [source, val] of Object.entries(statusData.results)) {
                output += `--- ${source.toUpperCase()} ---\n`;
                output += JSON.stringify(val, null, 2) + "\n\n";
            }
            dataPre.textContent = output;

            if (Object.values(statusData.tasks).every(s => s === "Finished")) {
                clearInterval(interval);
                statusEl.textContent = "Pipeline completed";
            }
        }, 1000);

    } catch (err) {
        statusEl.textContent = "Error starting pipeline";
        console.error(err);
    }
});
