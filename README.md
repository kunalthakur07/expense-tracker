# 💸 Expense Tracker

A simple, clean personal finance tracker built with Python. Log your income and expenses, view reports, plan budgets, and get spending insights — all from a lightweight desktop app or the command line.

---

## 🤔 What Does It Do?

Managing money is hard enough — tracking it shouldn't be. This app lets you:

- **Log transactions** — record income or expenses with a date, category, amount, and description
- **View reports** — get a summary of where your money is going
- **Plan budgets** — set limits per category so you don't overspend
- **Get insights** — the insight engine flags unusual spending and highlights trends
- **Switch UIs** — use the Tkinter desktop window or the console, whichever you prefer

---

## 📁 Project Structure

```
ExpenseTracker/
│
├── src/
│   ├── main.py                  # Entry point — launches the app
│   │
│   ├── models/                  # Data models (plain Python classes)
│   │   ├── transaction.py       # Base transaction model
│   │   ├── expense.py           # Expense subtype
│   │   ├── income.py            # Income subtype
│   │   ├── wallet.py            # Wallet / balance tracking
│   │   ├── users.py             # User model
│   │   └── category.py          # Spending category
│   │
│   ├── controllers/             # Business logic
│   │   ├── auth_manager.py      # Simple username-based login & registration
│   │   ├── budget_planner.py    # Budget setting and checking
│   │   ├── insight_engine.py    # Spending insights & anomaly detection
│   │   └── report_generator.py  # Summary and report creation
│   │
│   ├── ui/                      # User interfaces
│   │   ├── tk_ui.py             # Desktop GUI (Tkinter)
│   │   └── console_ui.py        # Terminal / CLI interface
│   │
│   └── utils/                   # Helper utilities
│       ├── filehandler.py       # CSV read/write for persistence
│       ├── datehandler.py       # Date formatting helpers
│       └── visualizer.py        # Basic chart/visualization helpers
│
└── data/                        # Stored data (CSV files, gitignored secrets)
```

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/ExpenseTracker.git
cd ExpenseTracker
```

### 2. Create & activate a virtual environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

> **Note:** The core app uses only Python's standard library (`tkinter`, `csv`, `datetime`). No heavy dependencies required.

### 4. Run the app

```bash
python -m src.main
```

This launches the **Tkinter desktop GUI** by default. To switch to the console interface, open `src/main.py` and swap the commented lines.

---

## 🖥️ Using the Desktop UI

When you launch the app, you'll see a simple form:

| Field | What to enter |
|---|---|
| **Date** | Auto-filled with today's date (`YYYY-MM-DD`) |
| **Category** | e.g. `Food`, `Rent`, `Salary` |
| **Description** | A short note about the transaction |
| **Amount** | The monetary value (numbers only) |
| **Type** | Select **Expense** or **Income** |

Hit **Save** and the transaction is written to your data folder as a CSV.

---

## 🗺️ UML Diagram

The diagram below shows how the models, controllers, utilities, and UI layers interact with each other.

![Expense Tracker UML Diagram](uml/Expense_Tracker_UML.drawio.png)

---

## 🧠 How It Works (Under the Hood)

1. **Models** are plain Python dataclasses/classes — no database required.
2. **FileHandler** reads and writes everything to CSV files inside `data/`, making your data portable and human-readable.
3. **Controllers** sit between the UI and the models. They handle auth, budgets, reports, and insights.
4. **UI layer** is completely swappable — both `tk_ui.py` and `console_ui.py` call the same controllers.

---

## 📊 Features at a Glance

| Feature | Status |
|---|---|
| Add income / expense | ✅ |
| Category tagging | ✅ |
| CSV-based persistence | ✅ |
| Budget planning | ✅ |
| Spending insights | ✅ |
| Report generation | ✅ |
| Desktop GUI (Tkinter) | ✅ |
| Console / CLI mode | ✅ |
| User login & registration | ✅ |

---

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **GUI:** Tkinter (built-in)
- **Storage:** CSV files
- **Architecture:** MVC-inspired (Models → Controllers → UI)

---

## 🤝 Contributing

Pull requests are welcome! If you find a bug or have a feature idea, open an issue first so we can discuss it.

1. Fork the repo
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m "Add my feature"`
4. Push and open a PR

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).
