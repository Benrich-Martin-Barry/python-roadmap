from models import ExpenseTracker

FILE = "expenses_v2.json"

tracker = ExpenseTracker()
tracker.load(FILE)

while True:
    print("\n1. Add expense  2. View all  3. Total  4. Total by category  5. Quit")
    choice = input("Choose: ")

    if choice == "1":
        amount = float(input("Amount: "))
        category = input("Category: ")
        note = input("Note: ")
        tracker.add(amount, category, note)
        tracker.save(FILE)
        print("Saved")
    elif choice == "2":
        for e in tracker.expenses:
            print(e.amount, e.category, e.note)
    elif choice == "3":
        print("Total:", tracker.total())
    elif choice == "4":
        for category, amount in tracker.total_by_category().items():
            print(category, amount)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")