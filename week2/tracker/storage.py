import json

def load_expenses(data_file):
    try:
        with open(data_file) as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_expenses(data_file, expenses):
    with open(data_file, "w") as f:
        json.dump(expenses, f)

