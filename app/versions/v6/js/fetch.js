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
