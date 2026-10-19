# 💰 Expense Tracker Pro

A personal expense tracking application built with **Python, Streamlit, and Plotly**.

Expense Tracker Pro helps users record expenses, visualize spending habits, manage a monthly budget, and explore their spending history through an interactive dashboard.

The project started as a Python command-line application and has evolved into a web-based dashboard. It was developed as a hands-on learning project to practice Python programming, data handling, testing, and web application development.

## 📸 Dashboard Preview

### Main Dashboard
![Expense Tracker Pro Dashboard](./screenshots/dashboard.png)

### Monthly Spending History
![Monthly Spending History](./screenshots/spending-history.png)

## ✨ Features

### Interactive Dashboard
- Dark-themed Streamlit interface
- Total spending and expense summary metrics
- Spending breakdown by category using a donut chart
- Monthly spending history using an interactive bar chart
- Expense table with newest transactions displayed first

### Expense Management
- Add expenses with a category, amount, and description
- Automatically record the expense date
- Delete existing expenses
- Validate user input
- Save and load expenses locally using JSON

### Monthly Budget
- Set and save a monthly spending budget
- Track spending for the current month
- Visualize budget usage with a progress indicator
- Compare monthly spending against the selected budget

### Data Analysis
- Calculate total spending
- Calculate spending by category
- Identify the most expensive expense
- Group expenses by month
- Handle older expense records without dates

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application logic and data processing |
| Streamlit | Interactive web dashboard |
| Plotly | Spending charts and visualizations |
| JSON | Local data persistence |
| unittest | Automated testing |
| Git & GitHub | Version control |

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/AhmadBiko/expense-tracker-pro.git
cd expense-tracker-pro
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Or on macOS/Linux:

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install streamlit plotly
```

### 4. Run the Web Application

```bash
streamlit run app.py
```

Streamlit will display a local URL, typically:

`http://localhost:8501`

### 5. Run the Command-Line Version (Optional)

```bash
python main.py
```

## 🧪 Automated Testing

The project includes **21 automated unit tests** covering expense calculations, validation, data manipulation, and persistence-related functionality.

Run all tests with:

```bash
python -m unittest -v
```

Latest local test result:

**21 tests passed.**

## 📁 Project Structure

```text
expense-tracker-pro/
├── app.py
├── main.py
├── expense_functions.py
├── test_expense_tracker.py
├── .gitignore
└── README.md
```

- `app.py` — Streamlit dashboard
- `main.py` — Command-line interface
- `expense_functions.py` — Core expense and budget functions
- `test_expense_tracker.py` — Automated unit tests

The application stores expense and budget data in local JSON files. These files are excluded from Git tracking to avoid accidentally publishing personal financial information.

## 🗺️ Development Roadmap

- [x] Build a command-line expense tracker
- [x] Implement JSON data persistence
- [x] Add input validation and error handling
- [x] Implement automated unit tests
- [x] Build a Streamlit dashboard
- [x] Create spending charts with Plotly
- [x] Add monthly budget tracking
- [x] Add monthly spending history
- [x] Add dates and chronological expense sorting
- [x] Add dashboard screenshots
- [ ] Test installation in a clean environment
- [ ] Explore SQLite database integration
- [ ] Deploy the web application

## 📌 Project Status

**Web dashboard implemented — preparing v1.0 release.**

The application is functional locally and has passed its current automated test suite. Final installation verification and release documentation are the next steps.

## 👨‍💻 Author

**Ahmad Biko**

Computer Engineering Student — HTW Berlin

[GitHub Profile](https://github.com/AhmadBiko)

---

*Built as a practical Python development and software engineering learning project.*
