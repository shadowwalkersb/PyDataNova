const fetchRootBtn = document.getElementById("btn-root");
const fetchMockBtn = document.getElementById("btn-mock");
const responseDiv = document.getElementById("response");
// const tableContainer = document.getElementById("table-container");

// API URL lives only in JS
// const API_BASE_URL = "https://pydatanova-api.onrender.com";
const API_BASE_URL = "http://127.0.0.1:8000";

// Event listeners
fetchRootBtn.addEventListener("click", async () => {
    try {
        const response = await fetch(`${API_BASE_URL}/`);
        const data = await response.json();
        // responseDiv.textContent = data.message;
        renderMessage(data.message);
    } catch (err) {
        console.error(err);
        renderMessage("Error fetching root message");
    }
});

fetchMockBtn.addEventListener('click', async () => {
    try {
        const response = await fetch(`${API_BASE_URL}/mock-data`);
        const data = await response.json();
        // responseDiv.textContent = JSON.stringify(data, null, 2);
        renderMockData(data);
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

// Render mock data as a table
function renderMockData(data) {
    clearTable();
    const table = document.createElement("table");

    // Table header
    const headerRow = document.createElement("tr");
    data.columns.forEach(col => {
        const th = document.createElement("th");
        th.textContent = col;
        headerRow.appendChild(th);
    });
    table.appendChild(headerRow);

    // Table rows
    data.rows.forEach(rowData => {
        const row = document.createElement("tr");
        rowData.forEach(cellData => {
            const td = document.createElement("td");
            td.textContent = cellData;
            row.appendChild(td);
        });
        table.appendChild(row);
    });

    responseDiv.appendChild(table);
}
