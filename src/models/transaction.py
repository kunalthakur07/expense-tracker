from abc import ABC, abstractmethod
from datetime import datetime

class Transaction(ABC):
    def __init__(self, date: str, amount: float, category: str, description: str = ""):
        # store date as YYYY-MM-DD
        self._date = date
        self._amount = amount
        self._category = category
        self._description = description

    def get_date(self):
        return self._date

    def get_amount(self):
        return self._amount

    def get_category(self):
        return self._category

    def get_description(self):
        return self._description

    @abstractmethod
    def type(self):
        pass
