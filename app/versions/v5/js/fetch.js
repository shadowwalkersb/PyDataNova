import { FASTAPI_URL, FLASK_URL } from '../../../js/config.js';

const endpoints = [
  { btnId: "btn-fastapi-root", url: `${FASTAPI_URL}/`, outputId: "fastapi-output" },
  { btnId: "btn-fastapi-users", url: `${FASTAPI_URL}/users-mock/`, outputId: "fastapi-output" },
  { btnId: "btn-fastapi-items", url: `${FASTAPI_URL}/items-mock/`, outputId: "fastapi-output" },
  { btnId: "btn-flask-root", url: `${FLASK_URL}/`, outputId: "flask-output" },
  { btnId: "btn-flask-users", url: `${FLASK_URL}/users-mock/`, outputId: "flask-output" },
  { btnId: "btn-flask-items", url: `${FLASK_URL}/items-mock/`, outputId: "flask-output" }
];

// Helper to fetch and display response
async function fetchAndDisplay(url, outputId) {
    const outputEl = document.getElementById(outputId);
    try {
        const response = await fetch(url);
        const data = await response.json();
        outputEl.textContent = JSON.stringify(data, null, 2);
    } catch (err) {
        outputEl.textContent = `Error: ${err.message}`;
    }
}

endpoints.forEach(({btnId, url, outputId}) => {
    const btn = document.getElementById(btnId);
    if (btn) {
        btn.addEventListener("click", () => fetchAndDisplay(url, outputId));
    }
});
