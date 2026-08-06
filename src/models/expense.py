from .transaction import Transaction

class Expense(Transaction):
    def __init__(self, date, amount, category, description=""):
        super().__init__(date, amount, category, description)

    def type(self):
        return "Expense"
