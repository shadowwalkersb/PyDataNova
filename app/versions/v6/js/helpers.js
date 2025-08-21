// Render an array of objects as a table
function renderTable(container, data) {
  if (!data.length) {
    container.textContent = "No data available";
    return;
  }

  const columns = Object.keys(data[0]);
  const table = document.createElement("table");

  const thead = document.createElement("thead");
  const headerRow = document.createElement("tr");
  columns.forEach(col => {
    const th = document.createElement("th");
    th.textContent = col;
    headerRow.appendChild(th);
  });
  thead.appendChild(headerRow);
  table.appendChild(thead);

  const tbody = document.createElement("tbody");
  data.forEach(row => {
    const tr = document.createElement("tr");
    columns.forEach(col => {
      const td = document.createElement("td");
      td.textContent = row[col];
      tr.appendChild(td);
    });
    tbody.appendChild(tr);
  });
  table.appendChild(tbody);

  container.appendChild(table);
}

// Render a simple array as a list
function renderList(container, data) {
  if (!data.length) {
    container.textContent = "No data available";
    return;
  }

  const ul = document.createElement("ul");
  data.forEach(item => {
    const li = document.createElement("li");
    li.textContent = item;
    ul.appendChild(li);
  });
  container.appendChild(ul);
}

// Generic function: decide list vs table
export function renderData(containerId, data) {
  const container = document.getElementById(containerId);
  container.innerHTML = ""; // clear old content

  if (!Array.isArray(data)) {
    container.textContent = "Invalid data";
    return;
  }

  if (data.length === 0) {
    container.textContent = "No data available";
    return;
  }

  // Choose table if array of objects, list if array of primitives
  if (typeof data[0] === "object" && data[0] !== null) {
    renderTable(container, data);
  } else {
    renderList(container, data);
  }
}
