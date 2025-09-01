import { FASTAPI_URL, FLASK_URL } from "../../../js/config.js";
import { renderData } from "./helpers.js";

fetch(FASTAPI_URL + "/")
  .then(response => response.json())
  .then(data => {
    document.getElementById('fastapi-root').textContent = data.message;
  })
.catch(error => {
  console.error(error);
  document.getElementById('fastapi-root').textContent = "Failed to load root";
});

fetch(FASTAPI_URL + "/users/")
  .then(response => response.json())
  .then(data => {
    renderData('fastapi-users', data);
  })
.catch(error => {
  console.error(error);
  document.getElementById('fastapi-users').textContent = "Failed to load users";
});

fetch(FASTAPI_URL + "/items/")
  .then(response => response.json())
  .then(data => {
    renderData('fastapi-items', data);
  })
.catch(error => {
  console.error(error);
  document.getElementById('fastapi-items').textContent = "Failed to load items";
});

fetch(FLASK_URL + "/")
  .then(response => response.json())
  .then(data => {
    document.getElementById('flask-root').textContent = data.message;
  })
.catch(error => {
  console.error(error);
  document.getElementById('flask-root').textContent = "Failed to load root";
});

fetch(FLASK_URL + "/users/")
  .then(response => response.json())
  .then(data => {
    renderData('flask-users', data);
  })
.catch(error => {
  console.error(error);
  document.getElementById('flask-users').textContent = "Failed to load users";
});

fetch(FLASK_URL + "/items/")
  .then(response => response.json())
  .then(data => {
    renderData('flask-items', data);
  })
.catch(error => {
  console.error(error);
  document.getElementById('flask-items').textContent = "Failed to load items";
});
