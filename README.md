# Credit Risk Analytics Platform
### Data Engineering & Continuous Auditing Interface

An interactive financial data engineering application built to process large historical credit distributions, optimize backend analytics, and execute continuous automated data auditing.

## 🚀 Key Features & Architectural Highlights
* **Interactive Frontend Dashboard:** Architected using **Streamlit** and **Pandas** to ingest financial datasets, allowing real-time portfolio risk monitoring and interactive risk-grade filtering.
* **Optimized Database Backend:** Structured data storage using a local **SQLite database**, executing optimized analytics queries to clean, isolate, and validate historical data.
* **Automated Data-Validation Pipeline:** Formulated continuous-auditing scripts in Python that dynamically intercept incoming data streams, automatically catching and dropping sequence format errors and duplicate structural entries.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Database Engine:** SQLite / SQL
* **Core Libraries:** Pandas, Plotly Express
* **UI Framework:** Streamlit

## 📂 Project Repository Structure
```text
credit-risk-analytics/
│
├── data/                   # Historical source datasets (e.g., loan.csv)
├── database/               # SQL script schemas, analytic queries, and .db files
├── src/
│   ├── app.py              # Main interactive Streamlit application dashboard
│   ├── data_validation.py  # Python continuous auditing and validation engine
│   └── initialize_db.py    # Database loading and parsing script
├── requirements.txt        # Managed project package dependencies
└── README.md               # Detailed architectural documentation
