import { FASTAPI_URL } from './config.js';

const fetchRootBtn = document.getElementById("btn-root");
const fetchUsersBtn = document.getElementById("btn-users");
const fetchItemsBtn = document.getElementById("btn-items");
const responseDiv = document.getElementById("response");

// Event listeners
fetchRootBtn.addEventListener("click", async () => {
    try {
        const response = await fetch(`${FASTAPI_URL}/`);
        const data = await response.json();
        renderMessage(data.message);
    } catch (err) {
        console.error(err);
        renderMessage("Error fetching root message");
    }
});

fetchUsersBtn.addEventListener('click', async () => {
    try {
        const response = await fetch(`${FASTAPI_URL}/users`);
        const data = await response.json();
        responseDiv.innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
    } catch (err) {
        console.error(err);
        renderMessage("Error fetching mock data");
    }
});

fetchItemsBtn.addEventListener('click', async () => {
    try {
        const response = await fetch(`${FASTAPI_URL}/items`);
        const data = await response.json();
        responseDiv.innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
    } catch (err) {
        console.error(err);
        renderMessage("Error fetching mock data");
    }
});

// Helper to clear previous table
function clearTable() {
    responseDiv.innerHTML = "";
}

// Render a single message as a table
function renderMessage(message) {
    clearTable();
    const table = document.createElement("table");
    const row = document.createElement("tr");
    const cell = document.createElement("td");
    cell.textContent = message;
    row.appendChild(cell);
    table.appendChild(row);
    responseDiv.appendChild(table);
}
