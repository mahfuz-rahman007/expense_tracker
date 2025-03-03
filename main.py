import ExpenseTracker
import Transaction

def main():
    tracker = ExpenseTracker.ExpenseTracker()

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expense")
        print("3. Filter By Category")
        print("4. Exit")

        choice = input("Choose an Option: ")

        if choice == "1":
            amount = float(input("Enter Amount: "))
            category = input("Enter Category: ")
            date = input("Enter Date (YYYY-MM-DD): ")
            description = input("Enter Description (Optional): ")
            tracker.add_expense(Transaction.Transaction(amount, category, date, description))
            print("New Expense Added")

        elif choice == "2":
            tracker.view_expense()

        elif choice == "3":
            category = input("Enter Category To Filter: ")
            tracker.filter_expense(category)

        elif choice == "4":
            print("Exiting... Bye!!")
            break

        else:
            print("\nInvalid Choice Try Again!!!!!!!!!!!!!!!!!!!!!!!!!!")

main()