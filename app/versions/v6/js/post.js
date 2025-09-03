import { FASTAPI_URL, FLASK_URL } from "../../../js/config.js";
import { fetchAndDisplay } from "./helpers.js";

// Add user
export function addUser(url, id, form) {
  const data = {
    first: form.first.value,
    last: form.last.value,
  };

  fetch(`${url}/users/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  })
    .then(res => res.json())
    .then(() => fetchAndDisplay(url, id))
    .catch(err => console.error("Error adding user:", err));
}

// Add item
export function addItem(url, id, form) {
  const data = {
    name: form.name.value,
    category: form.category.value,
    price: parseFloat(form.price.value),
    owner_id: parseInt(form.owner_id.value),
  };

  fetch(`${url}/items/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data),
  })
    .then(res => res.json())
    .then(() => fetchAndDisplay(url, id))
    .catch(err => console.error("Error adding item:", err));
}

const backends = [
  { id: "fastapi", url: FASTAPI_URL },
  { id: "flask", url: FLASK_URL }
];

backends.forEach(({ id, url }) => {

  // User form
  const userForm = document.getElementById(`${id}-user-form`);
  userForm.addEventListener("submit", async e => {
    e.preventDefault();
    addUser(url, `${id}-users`, userForm);
    userForm.reset();
  });

  // Item form
  const itemForm = document.getElementById(`${id}-item-form`);
  itemForm.addEventListener("submit", async e => {
    e.preventDefault();
    addItem(url, `${id}-items`, itemForm);
    itemForm.reset();
  });
});
