import { FASTAPI_URL } from '../../../js/config.js';

const fetchRootBtn = document.getElementById("btn-root");
const fetchUsersBtn = document.getElementById("btn-users");
const fetchItemsBtn = document.getElementById("btn-items");
const responseDiv = document.getElementById("response");

// Event listeners
fetchRootBtn.addEventListener("click", async () => {
    try {
        const response = await fetch(`${FASTAPI_URL}/`);
        const data = await response.json();
        renderMessage(data.message ?? JSON.stringify(data));
    } catch (err) {
        console.error(err);
        renderMessage("❌ Error fetching root message");
    }
});

fetchUsersBtn.addEventListener("click", async () => {
    try {
        const response = await fetch(`${FASTAPI_URL}/users`);
        const data = await response.json();
        renderFlexibleTable(data);
    } catch (err) {
        console.error(err);
        renderMessage("❌ Error fetching users");
    }
});

fetchItemsBtn.addEventListener("click", async () => {
    try {
        const response = await fetch(`${FASTAPI_URL}/items`);
        const data = await response.json();
        renderFlexibleTable(data);
    } catch (err) {
        console.error(err);
        renderMessage("❌ Error fetching items");
    }
});

// ---- Helpers ----
function clearTable() {
    responseDiv.innerHTML = "";
}

// Render a single message
function renderMessage(message) {
    clearTable();
    const p = document.createElement("p");
    p.textContent = message;
    responseDiv.appendChild(p);
}

// Render data as table (works for both {columns, rows} and plain arrays/objects)
function renderFlexibleTable(data) {
    clearTable();
    const table = document.createElement("table");

    if (data.columns && data.rows) {
        // Backend provided structured table data
        const headerRow = document.createElement("tr");
        data.columns.forEach(col => {
            const th = document.createElement("th");
            th.textContent = col;
            headerRow.appendChild(th);
        });
        table.appendChild(headerRow);

        data.rows.forEach(rowData => {
            const row = document.createElement("tr");
            rowData.forEach(cellData => {
                const td = document.createElement("td");
                td.textContent = cellData;
                row.appendChild(td);
            });
            table.appendChild(row);
        });
    } else if (Array.isArray(data)) {
        // Array of objects → convert keys as columns
        if (data.length > 0 && typeof data[0] === "object") {
            const cols = Object.keys(data[0]);
            const headerRow = document.createElement("tr");
            cols.forEach(col => {
                const th = document.createElement("th");
                th.textContent = col;
                headerRow.appendChild(th);
            });
            table.appendChild(headerRow);

            data.forEach(item => {
                const row = document.createElement("tr");
                cols.forEach(col => {
                    const td = document.createElement("td");
                    td.textContent = item[col];
                    row.appendChild(td);
                });
                table.appendChild(row);
            });
        } else {
            // Array of primitives
            data.forEach(val => {
                const row = document.createElement("tr");
                const td = document.createElement("td");
                td.textContent = val;
                row.appendChild(td);
                table.appendChild(row);
            });
        }
    } else if (typeof data === "object") {
        // Object → key-value pairs
        Object.entries(data).forEach(([key, value]) => {
            const row = document.createElement("tr");
            const keyCell = document.createElement("th");
            keyCell.textContent = key;
            const valCell = document.createElement("td");
            valCell.textContent = JSON.stringify(value);
            row.appendChild(keyCell);
            row.appendChild(valCell);
            table.appendChild(row);
        });
    } else {
        // Fallback
        const row = document.createElement("tr");
        const cell = document.createElement("td");
        cell.textContent = String(data);
        row.appendChild(cell);
        table.appendChild(row);
    }

    responseDiv.appendChild(table);
}
