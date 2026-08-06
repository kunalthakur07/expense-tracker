from collections import defaultdict
from src.utils.filehandler import FileHandler

class ReportGenerator:
    @staticmethod
    def total_income_expense():
        rows = FileHandler.load_transactions()
        total_income = 0.0
        total_expense = 0.0
        for r in rows:
            amt = float(r['amount'])
            if r['type'] == 'Income':
                total_income += amt
            else:
                total_expense += amt
        return total_income, total_expense

    @staticmethod
    def category_summary():
        rows = FileHandler.load_transactions()
        by_cat = defaultdict(float)
        for r in rows:
            if r['type'] == 'Expense':
                by_cat[r['category']] += float(r['amount'])
        return dict(by_cat)

    @staticmethod
    def monthly_summary():
        rows = FileHandler.load_transactions()
        by_month = defaultdict(lambda: {'income':0.0, 'expense':0.0})
        for r in rows:
            month = r['date'][:7]   # YYYY-MM
            amt = float(r['amount'])
            if r['type'] == 'Income':
                by_month[month]['income'] += amt
            else:
                by_month[month]['expense'] += amt
        return dict(by_month)
