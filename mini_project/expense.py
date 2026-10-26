# ==========================================
#       PERSONAL EXPENSE TRACKER
# ==========================================

expenses = []


# Add Expense
def add_expense():

    print("\n========== ADD EXPENSE ==========")

    date = input("Enter date: ")
    description = input("Enter description: ")
    category = input("Enter category: ")

    try:
        amount = float(input("Enter amount: ₹"))

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

    except:
        print("Please enter a valid amount.")
        return

    expense = {
        "date": date,
        "description": description,
        "category": category,
        "amount": amount
    }

    expenses.append(expense)

    print("\nExpense added successfully!")


# View Expenses
def view_expenses():

    print("\n========== ALL EXPENSES ==========")

    if len(expenses) == 0:
        print("No expenses available.")
        return

    for i, expense in enumerate(expenses, 1):

        print("\nExpense", i)
        print("Date        :", expense["date"])
        print("Description :", expense["description"])
        print("Category    :", expense["category"])
        print("Amount      : ₹", expense["amount"])


# Total Expense
def total_expense():

    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    print("\n========== TOTAL EXPENSE ==========")
    print("Total Spending: ₹", total)


# Category Summary
def category_summary():

    print("\n========== CATEGORY SUMMARY ==========")

    if len(expenses) == 0:
        print("No expenses available.")
        return

    categories = {}

    for expense in expenses:

        category = expense["category"]
        amount = expense["amount"]

        if category in categories:
            categories[category] = categories[category] + amount
        else:
            categories[category] = amount

    for category in categories:
        print(category, ": ₹", categories[category])


# Search Expense
def search_expense():

    print("\n========== SEARCH EXPENSE ==========")

    keyword = input("Enter category or description: ").lower()

    found = False

    for expense in expenses:

        if (keyword in expense["description"].lower()
                or keyword in expense["category"].lower()):

            print("\nDate        :", expense["date"])
            print("Description :", expense["description"])
            print("Category    :", expense["category"])
            print("Amount      : ₹", expense["amount"])

            found = True

    if found == False:
        print("No matching expense found.")


# Delete Expense
def delete_expense():

    print("\n========== DELETE EXPENSE ==========")

    if len(expenses) == 0:
        print("No expenses available.")
        return

    view_expenses()

    try:

        number = int(input("\nEnter expense number to delete: "))

        if number < 1 or number > len(expenses):
            print("Invalid expense number.")
            return

        deleted = expenses.pop(number - 1)

        print("\nExpense deleted successfully!")
        print("Deleted:", deleted["description"])

    except:
        print("Please enter a valid number.")


# Dashboard
def dashboard():

    print("\n========== EXPENSE DASHBOARD ==========")

    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    print("Number of Expenses :", len(expenses))
    print("Total Spending     : ₹", total)

    if len(expenses) > 0:

        highest = expenses[0]

        for expense in expenses:

            if expense["amount"] > highest["amount"]:
                highest = expense

        average = total / len(expenses)

        print("Highest Expense    : ₹", highest["amount"])
        print("Average Expense    : ₹", round(average, 2))

    else:

        print("Highest Expense    : ₹ 0")
        print("Average Expense    : ₹ 0")


# ==========================================
# MAIN PROGRAM
# ==========================================

while True:

    print("\n")
    print("==========================================")
    print("       PERSONAL EXPENSE TRACKER")
    print("==========================================")

    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Total Expense")
    print("4. Category Summary")
    print("5. Search Expense")
    print("6. Delete Expense")
    print("7. Dashboard")
    print("8. Exit")

    print("==========================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expense()

    elif choice == "4":
        category_summary()

    elif choice == "5":
        search_expense()

    elif choice == "6":
        delete_expense()

    elif choice == "7":
        dashboard()

    elif choice == "8":
        print("\nThank you for using Expense Tracker!")
        break

    else:
        print("\nInvalid choice! Please enter 1-8.")