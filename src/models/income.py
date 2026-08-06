from .transaction import Transaction

class Income(Transaction):
    def __init__(self, date, amount, category, description=""):
        super().__init__(date, amount, category, description)

    def type(self):
        return "Income"
