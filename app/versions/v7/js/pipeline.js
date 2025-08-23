const runBtn = document.getElementById("runPipelineBtn");
const statusEl = document.getElementById("status");
const tableHeader = document.getElementById("tableHeader");
const tableBody = document.getElementById("tableBody");

runBtn.addEventListener("click", async () => {
  statusEl.textContent = "Started...";
  tableHeader.innerHTML = "";
  tableBody.innerHTML = "";

});
