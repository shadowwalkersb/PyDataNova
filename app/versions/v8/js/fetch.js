const API_BASE = window.FASTAPI_URL || "http://localhost:8000";

const runBtn = document.getElementById("runPipelineBtn");
const statusEl = document.getElementById("status");
const polarsPane = document.getElementById("polars-pane");

const MULTI_SOURCES = {
  taxi_csv: ["https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv", "csv"],
  users_csv: ["https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv", "csv"]
};

runBtn.addEventListener("click", async () => {
  statusEl.textContent = "Status: Running orchestration…";
  polarsPane.querySelectorAll(".sub-pane").forEach(el => el.remove());

  try {
    const resp = await fetch(`${API_BASE}/etl/run`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(MULTI_SOURCES)
    });
    if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
    const data = await resp.json();

    for (const [source, result] of Object.entries(data.results)) {
      const subDiv = document.createElement("div");
      subDiv.classList.add("sub-pane");

      const header = document.createElement("div");
      header.classList.add("sub-pane-header");
      header.textContent = source;

      const pre = document.createElement("pre");
      pre.textContent = JSON.stringify(result, null, 2);

      header.addEventListener("click", () => {
        pre.style.display = pre.style.display === "none" ? "block" : "none";
      });

      subDiv.appendChild(header);
      subDiv.appendChild(pre);
      polarsPane.appendChild(subDiv);
    }

    statusEl.textContent = "Status: Orchestration completed.";
  } catch (err) {
    console.error(err);
    statusEl.textContent = "Status: Error running orchestration.";
  }
});
