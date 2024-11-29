import tkinter as tk
from tkinter import ttk, messagebox
import csv
import re
from datetime import datetime
import os

class AddExpenseWindow:
    def __init__(self, master):
        self.window = tk.Toplevel(master)
        self.window.title("Add Expenses")
        self.window.geometry("400x300")

        label = tk.Label(self.window, text="Add expenses")
        label.pack()

        self.expense_date = ttk.Label(self.window, text="Date (MM-DD-YYYY):")
        self.date_entry = ttk.Entry(self.window)
        self.expense_date.pack()
        self.date_entry.pack()

        self.expense = ttk.Label(self.window, text="Expense amount:")
        self.expense_entry = ttk.Entry(self.window)
        self.expense.pack()
        self.expense_entry.pack()

        self.desc = ttk.Label(self.window,text="Description:")
        self.desc_entry = ttk.Entry(self.window)
        self.desc.pack()
        self.desc_entry.pack()

        self.cat = ttk.Label(self.window, text="Category:")
        self.cat_entry = ttk.Entry(self.window)
        self.cat.pack()
        self.cat_entry.pack()

        submit_btn = ttk.Button(self.window, text="Submit", command=self.submit)
        submit_btn.pack()

        close_btn = tk.Button(self.window, text="Close", command=self.window.destroy)
        close_btn.pack()

    def submit(self):
        date_period = self.date_entry.get()
        amount = self.expense_entry.get()
        description = self.desc_entry.get()
        category = self.cat_entry.get()

        if not category or not date_period or not amount:
            messagebox.showerror("Error","Date, Expense Amount, and Category cannot be blank!")
            return
        
        try:
        # Convert the period input to a valid date format
            converted_date = datetime.strptime(date_period, "%m-%d-%Y").strftime("%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Invalid date format. Please use MM-DD-YYYY.")
            return
        # if not re.match(r"^(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])-\d{4}$", date_period):
        #     messagebox.showerror("Validation Error", "Date must be in MM-DD-YYYY format.")
        #     return
        
        try:
            expense_float = float(amount)
            if expense_float <= 0:
                messagebox.showerror("Validation Error", "Expense must be a positive number.")
                return
        except ValueError:
            messagebox.showerror("Validation Error", "Expense must be a numeric value.")
            return
        
        messagebox.showinfo("Expense Submitted", f"Date: {date_period}\nExpense: {amount}\nDescription: {description}\nCategory: {category}")

        self.window.destroy()

        self.save_to_csv(converted_date, amount, description, category)

    def save_to_csv(self, timeframe,amount, desc,cat):
        file_path = "expense data.csv"
        file_exists = os.path.exists(file_path)
        
        try:
            with open("expense data.csv", mode='a', newline="") as file:
                writer = csv.writer(file)
                if not file_exists or os.stat(file_path).st_size == 0:
                    writer.writerow(["Date", "Amount", "Description", "Category"])
                writer.writerow([timeframe, amount, desc,cat])
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save data: {e}")
        

        