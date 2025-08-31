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
