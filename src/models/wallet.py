class Wallet:
    def __init__(self, user):
        self.user = user
        self.balance = 0.0

    def update_balance(self, amount):
        # positive to add, negative to subtract
        self.balance += amount

    def get_balance(self):  
        return self.balance
