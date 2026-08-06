class BudgetPlanner:
    def __init__(self):
        self.budgets = {}  # category->amount

    def set_budget(self, category, amount):
        self.budgets[category] = amount

    def get_budget(self, category):
        return self.budgets.get(category, None)

    def compare_with_actual(self, actual_by_cat):
        # actual_by_cat: dict {cat: amt}
        report = {}
        for cat, budget in self.budgets.items():
            actual = actual_by_cat.get(cat, 0.0)
            report[cat] = {'budget': budget, 'actual': actual, 'diff': actual - budget}
        return report
