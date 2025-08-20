// config.js or at top of your main JS
const API_BASE = window.location.hostname.includes('github.io')
  ? 'https://pydata-api.onrender.com'   // live Render API
  : 'http://localhost:8000';           // local API for dev

// Usage:
fetch(`${API_BASE}/mock-data`)
  .then(res => res.json())
  .then(data => console.log(data));
