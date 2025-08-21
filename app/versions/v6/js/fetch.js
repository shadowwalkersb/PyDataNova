fetch("http://localhost:8000/users/")
  .then(response => response.json())
  .then(data => {
    const container = document.getElementById('fastapi-users')
    container.innerHTML = data.map(user=> `<li>${user.id}: ${user.name}</li>`).join('')
  })
  .catch(error => console.error("Error fetching data:", error));
