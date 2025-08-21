import { renderData } from "./helpers.js";

fetch("http://localhost:8000/users/")
  .then(response => response.json())
  .then(data => {
    renderData('fastapi-users', data);
  })
  .catch(error => console.error("Error fetching data:", error));

fetch("http://localhost:8000/items/")
  .then(response => response.json())
  .then(data => {
    renderData('fastapi-items', data);
  })
  .catch(error => console.error("Error fetching data:", error));


fetch("http://localhost:8001/users/")
  .then(response => response.json())
  .then(data => {
    renderData('flask-users', data);
  })
  .catch(error => console.error("Error fetching data:", error));

fetch("http://localhost:8001/items/")
  .then(response => response.json())
  .then(data => {
    renderData('flask-items', data);
  })
  .catch(error => console.error("Error fetching data:", error));

import { FASTAPI_URL, FLASK_URL } from "./config.js";

// Helper: render table
export function renderTable(containerId, data) {
  const container = document.getElementById(containerId);
  container.innerHTML = "";
  if (!data.length) { container.innerText = "No data"; return; }

  const table = document.createElement("table");
  const headers = Object.keys(data[0]);

  const thead = document.createElement("thead");
  const trHead = document.createElement("tr");
  headers.forEach(h => { const th = document.createElement("th"); th.innerText = h; trHead.appendChild(th); });
  thead.appendChild(trHead);
  table.appendChild(thead);

  const tbody = document.createElement("tbody");
  data.forEach(row => {
    const tr = document.createElement("tr");
    headers.forEach(h => { const td = document.createElement("td"); td.innerText = row[h]; tr.appendChild(td); });
    tbody.appendChild(tr);
  });
  table.appendChild(tbody);

  container.appendChild(table);
}

// Fetch CRUD data
export async function fetchUsers(base, containerId, db="elephant") {
  const res = await fetch(`${base}/users?db=${db}`);
  const data = await res.json();
  renderTable(containerId, data);
}

export async function fetchItems(base, containerId, db="elephant") {
  const res = await fetch(`${base}/items?db=${db}`);
  const data = await res.json();
  renderTable(containerId, data);
}
