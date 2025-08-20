# PyDataNova

PyDataNova is an experimental, modular data pipeline and infrastructure project, designed to evolve from a simple static frontend into a full-featured, API-connected portfolio demonstrating backend, data engineering, and deployment workflows.

This repository serves as:

- A **learning and reference** environment for backend + data tooling.
- A **progressive showcase** of frontend and backend integration (static HTML/CSS/JS → FastAPI API).
- A **potential cookiecutter template** for bootstrapping production-ready projects.

---

## Project Structure

```
PyDataNova/
├── app/                # Frontend
│   ├── versions/
│   │   ├── v1/         # Basic static HTML
│   │   ├── v2/         # Added CSS/JS interactivity
│   │   ├── v3/         # Table display with mock data
│   │   └── v4/         # API-connected table, styled frontend
│   └── index.html      # Main landing page
├── api/                # FastAPI backend
│   ├── main.py         # API endpoints
│   └── requirements.txt
└── README.md
```

---

## Frontend (v4)

- Modular HTML, CSS, and separate JS (`api-fetch.js`)
- Fetches data from local FastAPI backend (`http://127.0.0.1:8000/mock-data`)
- Displays data in a **centered, styled table**

### Run locally

1. Start the FastAPI backend:

```bash
cd api
pip install -r requirements.txt
uvicorn main:app --reload
```

2. Serve the frontend (optional, any static server) or open directly in browser:

```bash
cd app/versions/v4
python -m http.server 5500
```

3. Update `api-fetch.js` fetch URL if needed:

```js
fetch('http://127.0.0.1:8000/mock-data')
  .then(res => res.json())
  .then(data => {
      // render table
  });
```

4. Open in browser: [http://127.0.0.1:5500/index.html](http://127.0.0.1:5500/index.html)

Now the table should populate with mock data from the running FastAPI backend.

---

## Backend (FastAPI)

- Endpoints:
  - `/` → hello message
  - `/mock-data` → mock table data

- Mock data format:

```json
{
  "columns": ["ID", "Value", "Category"],
  "rows": [
    [1, 42, "A"],
    [2, 17, "B"],
    [3, 33, "C"]
  ]
}
```

- Optionally, you can serve the frontend through FastAPI to simplify fetch URLs:

```python
from fastapi.staticfiles import StaticFiles
app.mount("/", StaticFiles(directory="../app/versions/v4", html=True), name="frontend")
```
Then browse `http://127.0.0.1:8000/` and the fetch works as `/mock-data`.

---

## Vision & Roadmap

### Phase 1 – Minimal Hello World
- Static frontend (HTML/CSS/JS)
- Basic backend service (Python HTTP server → FastAPI)
- GitHub Actions CI/CD
- Local development first; containerized deployment (Docker) later

### Phase 2 – Incremental Improvements
- Multiple backend endpoints with mock / real data
- API-connected frontend table
- Versioned frontend iterations (v1 → v4)
- Optional monitoring (Prometheus + Grafana)
- Cloud deployment via Terraform

### Phase 3 – Template Extraction
- Modularize code and configs into reusable cookiecutter template
- Showcase alternative tech stacks for components
- Expand into backend + data engineering workflows

---

## Tech Stack (Current & Planned)

- **Languages:** Python, JavaScript
- **Frontend:** HTML, CSS, Vanilla JS (v1–v4), React (future)
- **Backend:** FastAPI (v4), Python HTTP server (earlier)
- **Infrastructure:** Docker (future), Terraform (future)
- **Monitoring:** Prometheus, Grafana (future)
- **CI/CD:** GitHub Actions

---

## GitHub Pages Deployment
The static frontend in the `/app` folder is automatically deployed to GitHub Pages after each push to the `main` branch. You can view the live site here:

[🚀 View the Live App](https://shadowwalkersb.github.io/PyDataNova/)

> **Note:** The v4 frontend fetches data from the local FastAPI backend. Deployment to a live API backend will require updating the fetch URLs accordingly.

---

## License
[MIT License](LICENSE) – see LICENSE file for details.
