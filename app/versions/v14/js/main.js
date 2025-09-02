import { FASTAPI_URL } from "./config.js";

const outputEl = document.getElementById("output");

function showResult(data) {
  outputEl.textContent = JSON.stringify(data, null, 2);
}

// generic fetch helper
async function callAPI(endpoint, method = "GET") {
  const url = `${FASTAPI_URL}${endpoint}`;
  let options = { method };

  if (method === "POST") {
    options.headers = { "Content-Type": "application/json" };
    options.body = JSON.stringify({ message: "Hello from frontend" });
  }

  try {
    const resp = await fetch(url, options);
    const data = await resp.json();
    showResult(data);
  } catch (err) {
    showResult({ error: err.message });
  }
}

// root fetch on page load
document.addEventListener("DOMContentLoaded", () => {
  callAPI("/");  // display root response

  // attach all button clicks
  document.querySelectorAll(".button-stack button").forEach(btn => {
    btn.addEventListener("click", () => {
      const endpoint = btn.getAttribute("data-endpoint");
      const method = btn.getAttribute("data-method");
      callAPI(endpoint, method);
    });
  });
});
