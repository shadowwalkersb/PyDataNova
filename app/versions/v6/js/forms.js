// app/versions/v6/js/forms.js
import { FASTAPI_URL, FLASK_URL } from "./config.js";
import { fetchUsers, fetchItems } from "./fetch.js";

// Generic form handler
function handleFormSubmit(formId, base, type, containerId) {
  const form = document.getElementById(formId);
  form.addEventListener("submit", async e => {
    e.preventDefault();
    const formData = new FormData(form);
    const payload = Object.fromEntries(formData.entries());

    // Convert owner_id to number if exists
    if (payload.owner_id) payload.owner_id = Number(payload.owner_id);

    const db = payload.db || "elephant";
    delete payload.db;

    const url = `${base}/${type}?db=${db}`;
    await fetch(url, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });

    // Refresh table
    if (type === "users") fetchUsers(base, containerId, db);
    else fetchItems(base, containerId, db);

    form.reset();
  });
}

// Attach all forms
function attachForms() {
  handleFormSubmit("fastapi-user-form", FASTAPI_URL, "users", "fastapi-users");
  handleFormSubmit("fastapi-item-form", FASTAPI_URL, "items", "fastapi-items");
  handleFormSubmit("flask-user-form", FLASK_URL, "users", "flask-users");
  handleFormSubmit("flask-item-form", FLASK_URL, "items", "flask-items");
}

// Initialize
document.addEventListener("DOMContentLoaded", attachForms);
