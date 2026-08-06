from src.utils.datehandler import DateHandler
from src.utils.filehandler import FileHandler
from src.controllers.report_generator import ReportGenerator
from src.controllers.insight_engine import InsightEngine
from src.utils.visualizer import plot_category_spending


def print_menu():
    print("\nPersonal Expense Tracker")
    print("1. Add Expense")
    print("2. Add Income")
    print("3. Show Summary")
    print("4. Top Categories")
    print("5. Overspending Alert")
    print("6. Show Category Spending Chart")
    print("7. Show Savings Percentage")
    print("8. Exit")

def add_transaction(ttype):
    date = input("Date (YYYY-MM-DD) [leave empty for today]: ").strip()
    if date == "":
        date = DateHandler.today_str()
    category = input("Category: ").strip()
    description = input("Description: ").strip()
    amount = float(input("Amount: ").strip())
    FileHandler.save_transaction(date, category, description, amount, ttype)
    print(f"{ttype} saved.")

def run_console_app():
    FileHandler.init_file()
    while True:
        print_menu()
        choice = input("Choose: ").strip()
        if choice == '1':
            add_transaction("Expense")
        elif choice == '2':
            add_transaction("Income")
        elif choice == '3':
            inc, exp = ReportGenerator.total_income_expense()
            print(f"Total Income: {inc}")
            print(f"Total Expense: {exp}")
            print("Monthly Summary:")
            for m, vals in ReportGenerator.monthly_summary().items():
                print(m, vals)
        elif choice == '4':
            print("Top categories:", InsightEngine.top_categories())
        elif choice == '5':
            print(InsightEngine.overspending_alert())
        elif choice == '6':
            plot_category_spending()
        elif choice == '7':
            print(InsightEngine.savings_percentage())
        elif choice == '8':
            break
        else:
            print("Invalid choice.")
