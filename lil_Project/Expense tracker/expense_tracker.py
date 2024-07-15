import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt
import uuid

# Constants
FILE_NAME = 'expenses.csv'
FIELDS = ['ID', 'Date', 'Amount', 'Category', 'Description']

# Ensure the CSV file exists
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(FIELDS)

def add_expense():
    try:
        date_str = input("Enter date (YYYY-MM-DD): ")
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print(" Invalid date format. Please enter the date in YYYY-MM-DD Format. ")
        return
    
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print(" Invalid amount. Please enter a numeric value. ")
        return
    
    category = input("Enter category: ")
    description = input("Enter description: ")
    expense_id = str(uuid.uuid4())
    
    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([expense_id, date, amount, category, description])
    
    print("Expense added successfully!")

def view_expenses():
    print("Expenses:")
    with open(FILE_NAME, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)

def delete_expense():
    expense_id = input(" Enter ID of the expense to delete. ")
    temp_file = 'temp.csv'
    deleted = False
    
    with open(FILE_NAME, mode='r') as file, open(temp_file, mode='w', newline='') as temp:
        reader = csv.DictReader(file)
        writer = csv.DictWriter(temp, fieldnames=FIELDS)
        writer.writeheader()
        deleted = False
        
        for row in reader:
            if row['ID'] == expense_id and not deleted:
                deleted = True
                continue
            writer.writerow(row)
    
    os.replace(temp_file, FILE_NAME)
    print("Expense deleted successfully!" if deleted else "Expense not found.")

def expense_summary():
    summary = {}
    with open(FILE_NAME, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            category = row['Category']
            amount = float(row['Amount'])
            if category in summary:
                summary[category] += amount
            else:
                summary[category] = amount
    
    # Display summary
    for category, total in summary.items():
        print(f"{category}: ${total:.2f}")
    
    # Plot pie chart
    plt.pie(summary.values(), labels=summary.keys(), autopct='%1.1f%%')
    plt.title('Expense Summary by Category')
    plt.show()

def main():
    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Expense Summary")
        print("5. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            delete_expense()
        elif choice == '4':
            expense_summary()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
