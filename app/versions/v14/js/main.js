import { FASTAPI_URL } from "./config.js";

const v14OutputEl = document.getElementById("v14-output");

async function callV14Pipeline() {
  v14OutputEl.textContent = "Running pipeline...";
  try {
    const res = await fetch(`${FASTAPI_URL}/pipeline/run`, { method: "POST" });
    const data = await res.json();
    v14OutputEl.textContent = JSON.stringify(data, null, 2);
  } catch (err) {
    v14OutputEl.textContent = "Error: " + err;
  }
}

window.callV14Pipeline = callV14Pipeline;
