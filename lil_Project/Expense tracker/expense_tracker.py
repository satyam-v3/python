import csv
import os
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import matplotlib.pyplot as plt
import random
import string

# Constants
FILE_NAME = 'expenses.csv'
FIELDS = ['ID', 'Date', 'Amount', 'Category', 'Description']

# Ensure the CSV file exists
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(FIELDS)

def generate_short_id(length=8):
    """Generate a short unique identifier."""
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))

def add_expense(date, amount, category, description):
    try:
        date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        messagebox.showerror("Error", "Invalid date format. Please enter the date in YYYY-MM-DD format.")
        return
    
    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Error", "Invalid amount. Please enter a numeric value.")
        return
    
    expense_id = generate_short_id()
    
    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([expense_id, date, amount, category, description])
    
    messagebox.showinfo("Success", "Expense added successfully!")

def view_expenses():
    expenses_window = tk.Toplevel(root)
    expenses_window.title("View Expenses")
    with open(FILE_NAME, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            expense_str = f"ID: {row['ID']}, Date: {row['Date']}, Amount: {row['Amount']}, Category: {row['Category']}, Description: {row['Description']}"
            tk.Label(expenses_window, text=expense_str).pack()

def delete_expense(expense_id):
    temp_file = 'temp.csv'
    deleted = False
    
    with open(FILE_NAME, mode='r') as file, open(temp_file, mode='w', newline='') as temp:
        reader = csv.DictReader(file)
        writer = csv.DictWriter(temp, fieldnames=FIELDS)
        writer.writeheader()
        
        for row in reader:
            if row['ID'] == expense_id and not deleted:
                deleted = True
                continue
            writer.writerow(row)
    
    os.replace(temp_file, FILE_NAME)
    if deleted:
        messagebox.showinfo("Success", "Expense deleted successfully!")
    else:
        messagebox.showerror("Error", "Expense not found.")

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
    summary_window = tk.Toplevel(root)
    summary_window.title("Expense Summary")
    for category, total in summary.items():
        tk.Label(summary_window, text=f"{category}: ${total:.2f}").pack()

    # Plot pie chart
    plt.pie(summary.values(), labels=summary.keys(), autopct='%1.1f%%')
    plt.title('Expense Summary by Category')
    plt.show()

# Create the main window
root = tk.Tk()
root.title("Personal Expense Tracker")

# Add Expense Frame
add_frame = tk.Frame(root)
add_frame.pack(pady=10)

tk.Label(add_frame, text="Date (YYYY-MM-DD)").grid(row=0, column=0)
tk.Label(add_frame, text="Amount").grid(row=1, column=0)
tk.Label(add_frame, text="Category").grid(row=2, column=0)
tk.Label(add_frame, text="Description").grid(row=3, column=0)

date_entry = tk.Entry(add_frame)
amount_entry = tk.Entry(add_frame)
category_entry = tk.Entry(add_frame)
description_entry = tk.Entry(add_frame)

date_entry.grid(row=0, column=1)
amount_entry.grid(row=1, column=1)
category_entry.grid(row=2, column=1)
description_entry.grid(row=3, column=1)

tk.Button(add_frame, text="Add Expense", command=lambda: add_expense(date_entry.get(), amount_entry.get(), category_entry.get(), description_entry.get())).grid(row=4, columnspan=2, pady=10)

# View Expenses Button
tk.Button(root, text="View Expenses", command=view_expenses).pack(pady=10)

# Delete Expense Frame
delete_frame = tk.Frame(root)
delete_frame.pack(pady=10)

tk.Label(delete_frame, text="Expense ID to Delete").grid(row=0, column=0)
delete_entry = tk.Entry(delete_frame)
delete_entry.grid(row=0, column=1)

tk.Button(delete_frame, text="Delete Expense", command=lambda: delete_expense(delete_entry.get())).grid(row=1, columnspan=2, pady=10)

# Expense Summary Button
tk.Button(root, text="Expense Summary", command=expense_summary).pack(pady=10)

# Run the main loop
root.mainloop()
