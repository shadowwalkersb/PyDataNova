import { FASTAPI_URL } from "./config.js";

const outputEl = document.getElementById("output");

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
    outputEl.textContent = JSON.stringify(data, null, 2);
  } catch (err) {
    outputEl.textContent = `Error: ${err.message}`;
  }
}

// Fetch root on page load
document.addEventListener("DOMContentLoaded", () => {
  callAPI("/");
});

// Attach button clicks dynamically
document.querySelectorAll(".button-stack button").forEach(btn => {
  btn.addEventListener("click", () => {
    const endpoint = btn.getAttribute("data-endpoint");
    const method = btn.getAttribute("data-method");
    callAPI(endpoint, method);
  });
});
