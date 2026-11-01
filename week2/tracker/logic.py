def total(expenses):
    result = 0
    for e in expenses:
        result = result + e["amount"]
    return result
def add_expense(expenses, amount, category, note):
    e = {"amount": amount, "category": category, "note": note}
    expenses.append(e)
def total_by_category(expenses):
    result = {}
    for e in expenses:
        category = e["category"]
        amount = e["amount"]
        result[category] = result.get(category, 0) + amount
    return result


