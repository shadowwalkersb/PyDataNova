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
