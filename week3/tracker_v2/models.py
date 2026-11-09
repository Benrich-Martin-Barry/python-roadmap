from dataclasses import dataclass
import json

@dataclass
class Expense:
    amount: float
    category: str
    note: str = ""

    def to_dict(self):
        return {"amount": self.amount, "category": self.category, "note": self.note}
    @classmethod
    def from_dict(cls, data):
        return cls(data["amount"], data["category"], data["note"])
class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add(self, amount, category, note=""):
        self.expenses.append(Expense(amount, category, note))

    def total(self):
        result = 0
        for e in self.expenses:
            result = result + e.amount
        return result
    
    def total_by_category(self):
        result = {}
        for e in self.expenses:
            category = e.category
            amount = e.amount
            result[category] = result.get(category, 0) + amount
        return result
    def save(self, path):
        data = [e.to_dict() for e in self.expenses]
        with open(path, "w") as f:
            json.dump(data, f)

    def load(self, path):
        try:
            with open(path) as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []
        self.expenses = [Expense.from_dict(d) for d in data]

