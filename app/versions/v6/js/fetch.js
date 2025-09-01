import { FASTAPI_URL, FLASK_URL } from "../../../js/config.js";
import { fetchAndDisplay } from "./helpers.js";

const endpoints = [
  { url: `${FASTAPI_URL}/`, id: "fastapi-root" },
  { url: `${FASTAPI_URL}/users-mock/`, id: "fastapi-users" },
  { url: `${FASTAPI_URL}/items-mock/`, id: "fastapi-items" },
  { url: `${FLASK_URL}/`, id: "flask-root" },
  { url: `${FLASK_URL}/users-mock/`, id: "flask-users" },
  { url: `${FLASK_URL}/items-mock/`, id: "flask-items" }
];

endpoints.forEach(({url, id}) => {
  fetchAndDisplay(url, id);
});

// Disable non-functional POST buttons in v6
document.querySelectorAll(".post-btn").forEach(btn => {
  btn.disabled = true;
  btn.title = "CRUD support coming in v7";
});
