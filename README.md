# 💰 Expense Tracker Pro

**A Python personal finance dashboard — from a command-line project to a cloud-hosted, multi-user web application.**

Record expenses, track monthly budgets, and explore spending through interactive charts. The project has two live versions:

| Version | Demo | Data storage |
| --- | --- | --- |
| **V2 — PostgreSQL + Google login** | [Launch V2](https://expense-tracker-pro-v2.streamlit.app/) | Persistent, per-user data in Neon PostgreSQL |
| **V1 — Public demo** | [Try V1](https://expense-tracker-pro-2026.streamlit.app/) | Temporary, session-specific data |

> **Current development branch:** `feature/postgresql` contains the V2 app (`db_app.py`). The original JSON and public-demo applications are retained in the repository.

## ✨ Features

### V2 — Multi-user expense tracker

- **Google sign-in and sign-out** using Streamlit's authentication support
- **User-specific data:** expenses and monthly budgets linked to each authenticated user
- **Persistent PostgreSQL storage** hosted with Neon
- **Expense management:** add, browse, and delete expenses with input validation
- **Monthly budgets:** save a budget and compare it with monthly spending
- **Interactive analytics:** spending by category, monthly history, and dashboard summaries
- **Dark-themed, wide-layout Streamlit dashboard**

### V1 — Original learning project

- Command-line expense tracker, later expanded into a Streamlit dashboard
- Local JSON persistence (`app.py`)
- Temporary session-based public demo (`demo_app.py`)
- Expense calculations, monthly summaries, and budget tracking
- Automated unit tests for core expense-tracking functionality

## 📸 Dashboard Preview

The screenshots below show the original dashboard (V1).

### Main dashboard

![Expense Tracker Pro dashboard](./screenshots/dashboard.png)

### Monthly spending history

![Monthly spending history](./screenshots/spending-history.png)

## 🛠️ Tech Stack

| Technology | Purpose |
| --- | --- |
| Python | Application and business logic |
| Streamlit | Interactive web interface and Google login integration |
| PostgreSQL | Persistent relational storage for V2 |
| Neon | Hosted PostgreSQL database |
| Psycopg 3 | Parameterized SQL and PostgreSQL connectivity |
| Plotly | Interactive spending visualizations |
| JSON | Local persistence in the original V1 application |
| `unittest` | Automated tests for core application logic |
| Git & GitHub | Version control |

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/AhmadBiko/expense-tracker-pro.git
cd expense-tracker-pro
```

To work with the V2 code, check out its branch:

```bash
git switch feature/postgresql
```

### 2. Install dependencies

```bash
python -m venv .venv
```

Activate the virtual environment:

**Windows PowerShell**

```powershell
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux**

```bash
source .venv/bin/activate
```

Then install:

```bash
python -m pip install -r requirements.txt
```

### 3. Run V1 locally

For the original JSON-based Streamlit app:

```bash
streamlit run app.py
```

For the session-based public demo:

```bash
streamlit run demo_app.py
```

For the command-line version:

```bash
python main.py
```

### 4. Run V2 locally

V2 requires a compatible PostgreSQL database with the `users`, `expenses`, and `budgets` tables, plus configured Google OAuth authentication.

Set the `DATABASE_URL` environment variable to your own PostgreSQL connection URL. For example, in **PowerShell**:

```powershell
$env:DATABASE_URL = Read-Host "PostgreSQL connection URL"
```

Configure Google OAuth credentials in your **local, Git-ignored** `.streamlit/secrets.toml` according to [Streamlit's authentication documentation](https://docs.streamlit.io/develop/concepts/connections/authentication). Register a redirect URI corresponding to your local Streamlit address (for example, `http://localhost:8502/oauth2callback` when using port 8502).

Start V2:

```powershell
streamlit run db_app.py --server.port 8502
```

Never commit database URLs, passwords, OAuth client secrets, or your local `.streamlit/secrets.toml`.

> The cloud-hosted V2 demo is the easiest way to try the application without setting up your own database or OAuth client.

## 🧪 Testing

The original application includes **21 automated unit tests** for expense calculations, validation, data manipulation, and persistence-related behavior.

Run them with:

```bash
python -m unittest -v
```

**Previously verified V1 result:** 21 tests passed.

**V2 manual smoke testing:** Google login/logout, creating and deleting an expense, updating dashboard totals and charts, saving budgets, and signing back in. Separate Google accounts were also tested for data isolation. These manual checks are not a substitute for automated end-to-end or security tests.

## 📁 Project Structure

```text
expense-tracker-pro/
├── app.py                  # V1: local JSON dashboard
├── demo_app.py             # V1: temporary session-based demo
├── db_app.py               # V2: authenticated PostgreSQL dashboard
├── database.py             # V2: PostgreSQL operations
├── main.py                 # Command-line app
├── expense_functions.py    # Shared expense calculations
├── test_expense_tracker.py # Core unit tests
├── requirements.txt
├── screenshots/
│   ├── dashboard.png
│   └── spending-history.png
├── .gitignore
└── README.md
```

## 🔐 Data Isolation & Security

V2 identifies users through Google authentication and associates stored expenses and budgets with an internal user ID. Database queries use parameterized SQL, and user-owned operations filter records by that user ID.

The application keeps credentials outside tracked source files. A Git history scan with Gitleaks reported no detected leaks at the time of the release review. This is not a guarantee against every possible security issue.

## 🗺️ Development Journey

- [x] Build a Python command-line expense tracker
- [x] Add JSON persistence and input validation
- [x] Implement unit tests
- [x] Build a Streamlit dashboard with Plotly charts
- [x] Add budgets, spending history, and dashboard screenshots
- [x] Deploy a temporary-data public demo (V1)
- [x] Integrate PostgreSQL via Psycopg 3 (V2)
- [x] Add Google authentication and per-user data separation (V2)
- [x] Deploy V2 with Neon and Streamlit Community Cloud
- [ ] Future improvement: connection pooling and dashboard performance
- [ ] Future improvement: expanded automated integration/security tests

## 📌 Project Status

**V1:** Released as an original JSON-based application and public session demo.

**V2:** Deployed and manually tested on the `feature/postgresql` branch. Future performance improvements and additional tests are planned.

- [V2 live application](https://expense-tracker-pro-v2.streamlit.app/)
- [V1 live demo](https://expense-tracker-pro-2026.streamlit.app/)
- [Repository releases](https://github.com/AhmadBiko/expense-tracker-pro/releases)

## 👨‍💻 Author

**Ahmad Biko**  
Computer Engineering Student — HTW Berlin

[GitHub profile](https://github.com/AhmadBiko)

---

*Built as a practical project to learn Python, databases, authentication, testing, and web application development.*
