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
│   │   └── v4/         # API-connected table, buttons, styled frontend
│   │       ├── index.html
│   │       ├── style.css
│   │       └── api-fetch.js
├── api/                # FastAPI backend
│   ├── main.py         # API endpoints
│   └── requirements.txt
└── README.md
```

---

## Frontend (v4)

- Modular HTML, CSS, and separate JS (`api-fetch.js`)
- Two buttons:
  - **Fetch Root Message** → fetches `/` endpoint on the API
  - **Fetch Mock Data** → fetches `/mock-data` endpoint and renders table
- Displays data in a **centered, styled table**
- Buttons allow interactive testing of backend endpoints

### Run locally

1. Start the FastAPI backend:

```bash
cd api
pip install fastapi uvicorn
uvicorn main:app --reload
```

2. Open frontend v4 locally:

- Open `app/versions/v4/index.html` in your browser directly
- Click **Fetch Root Message** or **Fetch Mock Data** to interact with backend

> **Note:** Backend CORS is enabled to allow local frontend fetches.

- Once deployed, update fetch URLs to point to the Render API URL.

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

- CORS middleware is enabled for local frontend testing:

```python
from fastapi.middleware.cors import CORSMiddleware
```

---

## Vision & Roadmap

### Phase 1 – Minimal Hello World
- Static frontend (HTML/CSS/JS)
- FastAPI backend service
- GitHub Actions CI/CD
- Local development first; containerized deployment (Docker) later

### Phase 2 – Incremental Improvements
- Multiple backend endpoints with mock / real data
- API-connected frontend table with buttons
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

> **Note:** The v4 frontend fetches data from the local FastAPI backend. Update the fetch URLs to point to your Render API deployment when live.

---

## License
[MIT License](LICENSE) – see LICENSE file for details.
