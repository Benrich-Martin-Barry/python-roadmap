from dataclasses import dataclass


@dataclass
class Expense:
    amount: float
    category: str = "other"
    note: str = ""

    def is_big(self):
        return self.amount > 1000


a = Expense(250.0)
b = Expense(5000.0, "rent", "october")
print(a)
print(b.is_big())