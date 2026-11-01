from logic import add_expense, total, total_by_category
from storage import load_expenses, save_expenses

FILE = "expenses.json"

expenses = load_expenses(FILE)

while True:
    print("\n1. Add expense  2. View all  3. Total  4. Total by category  5. Quit")
    choice = input("Choose: ")

    if choice == "1":
        amount = float(input("Amount: "))
        category = input("Category: ")
        note = input("Note: ")
        add_expense(expenses, amount, category, note)
        save_expenses(FILE, expenses)
        print("Saved")
    elif choice == "2":
        for e in expenses:
            print(e["amount"], e["category"], e["note"])
    elif choice == "3":
        print("Total:", total(expenses))
    elif choice == "4":
        for category, amount in total_by_category(expenses).items():
            print(category, amount)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")