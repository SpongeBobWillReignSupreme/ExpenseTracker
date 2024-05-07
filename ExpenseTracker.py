import csv

def addExpense(date, category, price):
    with open('expenses.csv', 'a', newline = '') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([date, category, price])

def getExpensesByCategory(category):
    total = 0
    with open('expenses.csv', newline = '') as csvfile:
        reader = csv.reader(csvfile)
        expenses = [row for row in reader if row[1].lower() == category.lower()]
        for expense in expenses:
            total += float(expense[2])
    return expenses, total

def main():
    print("Expense  Tracker")
    
    while True:
        print("\n1. Add Expense\n2. View Expenses by Category\n3. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            date = input("Enter the date: YYYY-MM-DD: ")
            category = input("Enter the category: ")
            price = input("Enter the price: ")
            addExpense(date, category, price)
            print("Expense added successfully.")
        elif choice == '2':
            category = input("Enter the category: ")
            expenses, total = getExpensesByCategory(category)
            print(f"\nExpenses under {category}:")
            for expense in expenses:
                print(f"Date: {expenses[0]}, Price: {expense[2]}")
            print(f"Total expenses under {category}: {total}")
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
