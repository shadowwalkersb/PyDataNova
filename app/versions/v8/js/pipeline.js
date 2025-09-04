import { FASTAPI_URL } from "./config.js";

const runBtn = document.getElementById("runPipelineBtn");
const statusEl = document.getElementById("status");
const dataPre = document.getElementById("dataPre");

// Task names for progress
const tasks = ["csv", "api"];

runBtn.addEventListener("click", async () => {
    // Reset UI
    statusEl.textContent = "Pipeline started...";
    dataPre.textContent = "";
    tasks.forEach(task => {
        const taskEl = document.getElementById(`${task}Status`);
        if (taskEl) taskEl.textContent = "Pending...";
    });

    try {
        // Trigger ETL
        const response = await fetch(`${FASTAPI_URL}/pipeline/run`, { method: "POST" });
        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        const data = await response.json();

        // Mark all tasks as finished
        tasks.forEach(task => {
            const taskEl = document.getElementById(`${task}Status`);
            if (taskEl) taskEl.textContent = "Finished";
        });

        statusEl.textContent = data.message;

        // Display results in <pre>
        const results = data.results;
        let output = "";
        for (const [source, value] of Object.entries(results)) {
            output += `--- ${source.toUpperCase()} ---\n`;
            output += JSON.stringify(value, null, 2) + "\n\n";
        }
        dataPre.textContent = output;

    } catch (err) {
        statusEl.textContent = "Error running pipeline";
        console.error(err);
    }
});
