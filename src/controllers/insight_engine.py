from src.controllers.report_generator import ReportGenerator

class InsightEngine:
    @staticmethod
    def overspending_alert(threshold_ratio=0.7):
        income, expense = ReportGenerator.total_income_expense()
        if income == 0:
            return None
        if expense > income * threshold_ratio:
            return f"Alert: Expenses are {expense/income:.2f}× of income. Consider reviewing budgets."
        return "No overspending detected."

    @staticmethod
    def top_categories(n=3):
        cat = ReportGenerator.category_summary()
        sorted_cat = sorted(cat.items(), key=lambda x: x[1], reverse=True)
        return sorted_cat[:n]
    
    @staticmethod
    def savings_percentage():
        income, expense = ReportGenerator.total_income_expense()
        if income == 0:
            return "No income recorded."
        savings = ((income - expense) / income) * 100
        return f"You saved {savings:.2f}% of your income this month."

