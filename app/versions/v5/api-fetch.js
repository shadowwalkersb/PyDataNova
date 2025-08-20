// const fastapiUrl = "https://your-fastapi-render.app";
// const flaskUrl = "https://your-flask-render.app";
const fastapiUrl = "http://localhost:8000";
const flaskUrl = "http://localhost:5001";

// FastAPI buttons
document.getElementById("btn-fastapi-root").onclick = () => {
  fetch(`${fastapiUrl}/root`)
    .then(res => res.json())
    .then(data => document.getElementById("fastapi-output").textContent = JSON.stringify(data, null, 2));
};

document.getElementById("btn-fastapi-mock").onclick = () => {
  fetch(`${fastapiUrl}/mock-data`)
    .then(res => res.json())
    .then(data => document.getElementById("fastapi-output").textContent = JSON.stringify(data, null, 2));
};

// Flask buttons
document.getElementById("btn-flask-root").onclick = () => {
  fetch(`${flaskUrl}/root`)
    .then(res => res.json())
    .then(data => document.getElementById("flask-output").textContent = JSON.stringify(data, null, 2));
};

document.getElementById("btn-flask-mock").onclick = () => {
  fetch(`${flaskUrl}/mock-data`)
    .then(res => res.json())
    .then(data => document.getElementById("flask-output").textContent = JSON.stringify(data, null, 2));
};
