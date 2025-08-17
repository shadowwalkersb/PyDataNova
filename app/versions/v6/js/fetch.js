import { FASTAPI_URL, FLASK_URL } from "../../../js/config.js";
import { fetchAndDisplay } from "./helpers.js";

const endpoints = [
  { url: `${FASTAPI_URL}/`, id: "fastapi-root" },
  { url: `${FASTAPI_URL}/users/`, id: "fastapi-users" },
  { url: `${FASTAPI_URL}/items/`, id: "fastapi-items" },
  { url: `${FLASK_URL}/`, id: "flask-root" },
  { url: `${FLASK_URL}/users/`, id: "flask-users" },
  { url: `${FLASK_URL}/items/`, id: "flask-items" }
];

endpoints.forEach(({url, id}) => {
  fetchAndDisplay(url, id);
});
