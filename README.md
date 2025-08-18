# PyDataNova

PyDataNova is an experimental, modular data pipeline and infrastructure project, designed to evolve from a simple 'Hello World' example into a full-featured template for modern backend, data engineering, and deployment workflows.

This repository will serve as:
- A **learning and reference** environment for backend + data tooling.
- A **progressive showcase** of alternative tech stacks (Python HTTP server → Nginx → FastAPI, etc.)
- A **potential cookiecutter template** for bootstrapping production-ready projects.

---

## Project Structure

```
PyDataNova/
├── app/                # Frontend
│   ├── versions/
│   │   ├── v1/         # Basic static HTML
│   │   ├── v2/         # Added CSS/JS interactivity
│   │   └── v3/         # Table display with mock data
│   └── index.html      # Main landing page
└── README.md
```

---
## Vision & Roadmap

### Phase 1 – Minimal Hello World
- Static frontend (HTML/CSS/JS)
- Basic backend service (Python HTTP server)
- GitHub Actions CI/CD
- Local development first; containerized deployment (Docker) later

### Phase 2 – Incremental Improvements
- Swap Python HTTP server for Nginx
- Replace Nginx with FastAPI backend
- Add Prometheus + Grafana monitoring
- Deploy to cloud using Terraform

### Phase 3 – Template Extraction
- Modularize code and configs into reusable cookiecutter template
- Showcase multiple alternative tech stacks for components
- Expand into backend + data engineering workflows

## Tech Stack (Planned)
---

- **Languages:** Python, JavaScript
- **Backend:** Python HTTP server → Nginx → FastAPI
- **Frontend:** Static HTML/CSS/JS → React (future)
- **Infrastructure:** Docker, Terraform
- **Monitoring:** Prometheus, Grafana
- **CI/CD:** GitHub Actions

---

## GitHub Pages Deployment
The static frontend in the `/app` folder is automatically deployed to GitHub Pages after each push to the `main` branch. You can view the live site here:

[🚀 View the Live App](https://shadowwalkersb.github.io/PyDataNova/)

---

## License
[MIT License](LICENSE) – see LICENSE file for details.
