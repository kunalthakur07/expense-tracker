import tkinter as tk
from tkinter import ttk, messagebox
from src.utils.filehandler import FileHandler
from src.utils.datehandler import DateHandler

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Expense Tracker")
        self.geometry("500x350")
        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self, text="Date (YYYY-MM-DD)").pack()
        self.date_entry = ttk.Entry(self)
        self.date_entry.pack()
        self.date_entry.insert(0, DateHandler.today_str())

        ttk.Label(self, text="Category").pack()
        self.cat_entry = ttk.Entry(self)
        self.cat_entry.pack()

        ttk.Label(self, text="Description").pack()
        self.desc_entry = ttk.Entry(self)
        self.desc_entry.pack()

        ttk.Label(self, text="Amount").pack()
        self.amount_entry = ttk.Entry(self)
        self.amount_entry.pack()

        self.type_var = tk.StringVar(value="Expense")
        ttk.Radiobutton(self, text="Expense", variable=self.type_var, value="Expense").pack()
        ttk.Radiobutton(self, text="Income", variable=self.type_var, value="Income").pack()

        ttk.Button(self, text="Save", command=self.save).pack(pady=10)

    def save(self):
        date = self.date_entry.get()
        cat = self.cat_entry.get()
        desc = self.desc_entry.get()
        amt = float(self.amount_entry.get() or 0)
        ttype = self.type_var.get()
        FileHandler.save_transaction(date, cat, desc, amt, ttype)
        messagebox.showinfo("Saved", f"{ttype} saved.")
