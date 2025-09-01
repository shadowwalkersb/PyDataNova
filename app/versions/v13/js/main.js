import { FASTAPI_URL, FLASK_URL } from "./config.js";

async function callRest(endpoint) {
  try {
    const res = await fetch(`${FASTAPI_URL}${endpoint}`);
    const data = await res.json();
    document.getElementById("rest-output").textContent = JSON.stringify(data, null, 2);
  } catch (err) {
    document.getElementById("rest-output").textContent = "Error: " + err;
  }
}

async function callGraphQL(query) {
  try {
    const res = await fetch(`${FASTAPI_URL}/graphql`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query })
    });
    const data = await res.json();
    document.getElementById("graphql-output").textContent = JSON.stringify(data, null, 2);
  } catch (err) {
    document.getElementById("graphql-output").textContent = "Error: " + err;
  }
}

async function callFlask(endpoint) {
  try {
    const res = await fetch(`${FLASK_URL}${endpoint}`);
    const data = await res.json();
    document.getElementById("flask-output").textContent = JSON.stringify(data, null, 2);
  } catch (err) {
    document.getElementById("flask-output").textContent = "Error: " + err;
  }
}

// Dynamically insert API links into HTML
function setApiLinks() {
  document.getElementById('fastapi-link').innerHTML =
    `<a href="${FASTAPI_URL}" target="_blank">${FASTAPI_URL}</a>`;

  document.getElementById('graphql-link').innerHTML =
    `<a href="${FASTAPI_URL}/graphql" target="_blank">${FASTAPI_URL}/graphql</a>`;

  document.getElementById('flask-link').innerHTML =
    `<a href="${FLASK_URL}" target="_blank">${FLASK_URL}</a>`;
}

window.callRest = callRest;
window.callGraphQL = callGraphQL;
window.callFlask = callFlask;

// Initialize dynamic links on page load
setApiLinks();
