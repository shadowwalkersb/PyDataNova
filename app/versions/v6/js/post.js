document.getElementById("fastapi-user-form").addEventListener("submit", async e => {
  e.preventDefault();
  const form = e.target;
  const data = {
    first: form.first.value,
    last: form.last.value
  };

  await fetch("http://localhost:8000/users/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  });

  form.reset(); // clear form fields
  // optional: you could refresh table manually later
});

document.getElementById("flask-user-form").addEventListener("submit", async e => {
  e.preventDefault();
  const form = e.target;
  const data = {
    first: form.first.value,
    last: form.last.value
  };

  await fetch("http://localhost:8001/users/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(data)
  });

  form.reset(); // clear form fields
  // optional: you could refresh table manually later
});
