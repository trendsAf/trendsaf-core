# trendsaf-core

**Open-source data infrastructure for commodity, trade, and logistics insights in frontier markets.**

Trendsaf helps developers and analysts access structured, standardized data from multiple sources ports, customs, and trade corridors across Africa and beyond, enabling near-real-time visibility, research, and forecasting.

---

## 🚀 Features

- ⚡️ **Pluggable ingestion pipelines** for diverse data sources 
- 🧰 **Python SDK** and CLI for data collection, transformation, and local analysis  
- 🌐 **Lightweight API server** (Flask or FastAPI) for exposing data to apps or dashboards  
- 📦 Easy to install, extend, and deploy (self-host or integrate into your stack)

---

## 🔧 Getting Started

### 📦 Installation

```bash
git clone https://github.com/apercu-labs/trendsaf-open-core.git
cd trendsaf-open-core
poetry install

```


### ▶️ Run the CLI

```bash

poetry run trendsaf fetch-port-data --port mombasa

```


### 🌐 Start the API
```bash

poetry run python -m trendsaf.api
# or, if using FastAPI:
poetry run uvicorn trendsaf.api.main:app --reload

```

### 📚 Documentation
📖 Full docs: trendsaf.org/docs (placeholder)

📘 CLI reference

⚙️ Ingestion pipelines

✍️ How to add a connector

🧪 Testing and CI setup


### 🧩 Architecture Overview
``` css
┌──────────────┐
│  CLI / SDK   │◄──── Devs / Analysts
└──────┬───────┘
       │
┌──────▼───────┐
│ Ingestion    │◄──── Scrapers/Manual uploads via interface/Customs APIs
│ Pipelines    │
└──────┬───────┘
       │
┌──────▼───────┐
│ Internal DB  │ (PostgreSQL)
└──────┬───────┘
       │
┌──────▼───────┐
│ REST API     │ (Flask/FastAPI)
└──────────────┘

```

### 🧪 Running Tests

``` bash
poetry run pytest

```

### Linting and formatting:

``` bash

poetry run black trendsaf/
poetry run flake8 trendsaf/

```


### 👥 Contributing
We welcome your contributions — new connectors, bug fixes, or docs!

Fork the repo and create your branch: git checkout -b feature/your-feature

Write clear, testable code with docs

Submit a PR with context and usage

🔖 Good first issues: #good-first-issue



## 🔐 License

Trendsaf Core is licensed under the **Polyform Noncommercial License 1.0.0**, customized by Aperçu Holdings Limited:

- ✅ Free to use for **non-commercial production** (e.g., education, nonprofit, personal, government)
- ❌ Not allowed for **commercial use**, **resale**, or **SaaS** offerings
- ✅ Source-available, modifiable, and forkable
- ✅ Open for community contributions

Read the full [`LICENSE`](./LICENSE.txt) for detailed terms.

### 💼 Need a commercial license?

If you plan to:
- Use Trendsaf Core as part of a commercial product or service
- Deploy in production for a for-profit business
- Embed it in internal enterprise tools

👉 Contact **Aperçu Labs** at [support@trendsaf.co](mailto:support@trendsaf.co) to purchase a commercial license.


### 🏗 Maintained By
Aperçu Labs and Trendsaf Limited
Part of Aperçu Holdings Limited group — the digital economy research lab for frontier economies.
