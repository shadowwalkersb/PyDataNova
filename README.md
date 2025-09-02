# PyDataNova

PyDataNova is an experimental, modular data pipeline and infrastructure project, designed to evolve from a simple 'Hello World' example into a full-featured template for modern backend, data engineering, and deployment workflows.

This repository serves as:
- A **learning and reference** environment for backend + data tooling.
- A **progressive showcase** of alternative tech stacks across versions.
- A **potential cookiecutter template** for bootstrapping production-ready projects.

## Project Structure

```
PyDataNova/
├── app/                # Frontend
│   ├── js/             # Common JS for all versions
│   │   └── config.js
│   ├── versions/
│   │   ├── v1/         # Basic static HTML
│   │   ├── v2/         # Added CSS/JS interactivity
│   │   ├── v3/         # Table display with mock data
│   │   ├── v4/         # API inspector + buttons
│   │   ├── v5/         # Dual Backend demo
│   │   └── v6/         # Real DB + dynamic panes
│   └── index.html      # Main landing page
└── README.md
```

## Versions

### [v1 – Basic static HTML](#v1--basic-static-html)
- Minimal HTML landing page.
- "Hello World" style project start.
- Deployed via GitHub Pages.

### [v2 – CSS/JS Interactivity](#v2--cssjs-interactivity)
- Added CSS styling and basic JavaScript.
- Buttons trigger dynamic responses.
- First step toward interactive UI.

### [v3 – Table Display with Mock Data](#v3--table-display-with-mock-data)
- Added table to display mock data.
- Demonstrates rendering structured information.
- Foundation for real backend integration.

### [v4 – API Inspector + Buttons](#v4--api-inspector--buttons)
- Added API Inspector sidebar (fixed width).
- Buttons to fetch `/`, `/users`, `/items`.
- Dynamic response panel for live results.

### [v5 – Dual Backend](#v5--dual-backend)
- Introduces **two backend services**: FastAPI + Flask.
- Buttons in the UI fetch data from **both backends**.
- Displays responses in separate panels for comparison.
- Demonstrates **multi-backend integration** and modular fetch logic.

### [v6 – Real DB + Dynamic Panes](#v6--real-db--dynamic-panes)
- Integrated **real database** (Neon/PostgreSQL) for persistence.
- Dynamic backend panes created in the frontend for FastAPI and Flask.
- Forms to read and add users/items directly to the DB.
- Demonstrates **end-to-end full-stack interaction** with real data.
- CORS configured for local and GitHub Pages frontend.

## Roadmap
### v7+ (Future)
- ETL/data pipeline demos using Prefect.
- Modular ingestion, transformation, and storage.
- GraphQL API, optional Golang microservice, analytics with Polars/Dask.
- Infrastructure deployment (Docker/Kubernetes/Tilt/Terraform/AWS).
- Advanced orchestration, monitoring, and analytics.

## Tech Stack (Planned)
- **Languages:** Python, JavaScript
- **Backend:** FastAPI, Flask
- **Frontend:** Static HTML/CSS/JS → React (future)
- **Infrastructure:** Docker, Kubernetes, Terraform
- **Monitoring:** Prometheus, Grafana
- **CI/CD:** GitHub Actions

## GitHub Pages Deployment
The static frontend in the `/app` folder is automatically deployed to GitHub Pages after each push to the `main` branch. You can view the live site here:

[🚀 View the Live App](https://shadowwalkersb.github.io/PyDataNova/)

## License
[MIT License](LICENSE) – see LICENSE file for details.
