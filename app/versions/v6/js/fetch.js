import { renderData } from "./helpers.js";

fetch("http://localhost:8000/users/")
  .then(response => response.json())
  .then(data => {
    renderData('fastapi-users', data);
  })
.catch(error => {
  console.error(error);
  document.getElementById('fastapi-users').textContent = "Failed to load users";
});

fetch("http://localhost:8000/items/")
  .then(response => response.json())
  .then(data => {
    renderData('fastapi-items', data);
  })
.catch(error => {
  console.error(error);
  document.getElementById('fastapi-users').textContent = "Failed to load users";
});


fetch("http://localhost:8001/users/")
  .then(response => response.json())
  .then(data => {
    renderData('flask-users', data);
  })
.catch(error => {
  console.error(error);
  document.getElementById('fastapi-users').textContent = "Failed to load users";
});

fetch("http://localhost:8001/items/")
  .then(response => response.json())
  .then(data => {
    renderData('flask-items', data);
  })
.catch(error => {
  console.error(error);
  document.getElementById('fastapi-users').textContent = "Failed to load users";
});
