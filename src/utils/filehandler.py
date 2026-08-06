import csv
import os

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), '..', 'data')
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

EXPENSES_FILE = os.path.join(DATA_DIR, 'transactions.csv')

class FileHandler:
    @staticmethod
    def init_file():
        if not os.path.exists(EXPENSES_FILE):
            with open(EXPENSES_FILE, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['date', 'category', 'description', 'amount', 'type'])

    @staticmethod
    def save_transaction(date, category, description, amount, ttype):
        FileHandler.init_file()
        with open(EXPENSES_FILE, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([date, category, description, amount, ttype])

    @staticmethod
    def load_transactions():
        FileHandler.init_file()
        transactions = []
        with open(EXPENSES_FILE, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # rows: date, category, description, amount, type
                transactions.append(row)
        return transactions
