import { FASTAPI_URL, FLASK_URL } from "../../../js/config.js";
import { fetchAndDisplay } from "./helpers.js";

fetchAndDisplay(FASTAPI_URL + "/", 'fastapi-root');
fetchAndDisplay(FASTAPI_URL + "/users/", 'fastapi-users');
fetchAndDisplay(FASTAPI_URL + "/items/", 'fastapi-items');
fetchAndDisplay(FLASK_URL + "/", 'flask-root');
fetchAndDisplay(FLASK_URL + "/users/", 'fastapi-users');
fetchAndDisplay(FLASK_URL + "/items/", 'fastapi-items');
