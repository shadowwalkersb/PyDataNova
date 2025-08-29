import { FASTAPI_URL } from "./config.js";

const v14OutputEl = document.getElementById("v14-output");
const v14Btn = document.getElementById("v14-run-btn");

async function runV14Pipeline() {
  // Disable button and show running status
  v14Btn.disabled = true;
  const originalText = v14Btn.textContent;
  v14Btn.textContent = "Running…";

  v14OutputEl.textContent = "";

  try {
    const res = await fetch(`${FASTAPI_URL}/pipeline/run`, { method: "POST" });
    const data = await res.json();
    v14OutputEl.textContent = JSON.stringify(data, null, 2);
  } catch (err) {
    v14OutputEl.textContent = "Error: " + err;
  } finally {
    // Restore button state
    v14Btn.disabled = false;
    v14Btn.textContent = originalText;
  }
}

v14Btn.addEventListener("click", runV14Pipeline);
