"""
Add Expense Window

This module implements a pop-up window for adding new expense entries. Users can input 
the date, amount, description, and category of an expense, which is validated and 
saved to a CSV file for later use.
"""
# import required libraries
import tkinter as tk  # GUI framework for Python
from tkinter import ttk, messagebox  # Widgets and dialogs for Tkinter
import csv  # Module for CSV file handling
import re  # Regular expression operations for input validation
from datetime import datetime  # For date and time operations
import os  # Module for interacting with the file system


class AddExpenseWindow:
    """
    Creates a window for adding expense data with fields for date, amount, description, and category.
    """

    def __init__(self, master):
        """
        Initializes the Add Expense window.
        master: The parent window or root window.
        """
        self.window = tk.Toplevel(master)  # Create a top-level window as a child of the master window
        self.window.title("Add Expenses")  # Set the title of the window
        self.window.geometry("400x300")  # Set the size of the window

        # Label for window title
        label = tk.Label(self.window, text="Add expenses")
        label.pack()  # Display the label

        # Label and entry for the date field
        self.expense_date = ttk.Label(self.window, text="Date (MM-DD-YYYY):")  # Date label
        self.date_entry = ttk.Entry(self.window)  # Date entry box
        self.expense_date.pack()  # Display the date label
        self.date_entry.pack()  # Display the date entry box

        # Label and entry for the expense amount field
        self.expense = ttk.Label(self.window, text="Expense amount:")  # Expense label
        self.expense_entry = ttk.Entry(self.window)  # Expense entry box
        self.expense.pack()  # Display the expense label
        self.expense_entry.pack()  # Display the expense entry box

        # Label and entry for the description field
        self.desc = ttk.Label(self.window, text="Description:")  # Description label
        self.desc_entry = ttk.Entry(self.window)  # Description entry box
        self.desc.pack()  # Display the description label
        self.desc_entry.pack()  # Display the description entry box

        # Label and entry for the category field
        self.cat = ttk.Label(self.window, text="Category:")  # Category label
        self.cat_entry = ttk.Entry(self.window)  # Category entry box
        self.cat.pack()  # Display the category label
        self.cat_entry.pack()  # Display the category entry box

        # Submit button for submitting the form
        submit_btn = ttk.Button(self.window, text="Submit", command=self.submit)
        submit_btn.pack()  # Display the submit button

        # Close button to close the window
        close_btn = tk.Button(self.window, text="Close", command=self.window.destroy)
        close_btn.pack()  # Display the close button

    def submit(self):
        """
        Validates input data and saves it to a CSV file if valid.
        Displays messages for successful submission or validation errors.
        """
        # Retrieve user inputs
        date_period = self.date_entry.get()  # Get the date input
        amount = self.expense_entry.get()  # Get the expense amount input
        description = self.desc_entry.get()  # Get the description input
        category = self.cat_entry.get()  # Get the category input

        # Check for missing required fields
        if not category or not date_period or not amount:
            messagebox.showerror("Error", "Date, Expense Amount, and Category cannot be blank!")
            return
        
        try:
            # Validate and convert the date format
            converted_date = datetime.strptime(date_period, "%m-%d-%Y").strftime("%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Invalid date format. Please use MM-DD-YYYY.")
            return

        try:
            # Validate and convert the expense amount
            expense_float = float(amount)
            if expense_float <= 0:  # Check for non-positive amounts
                messagebox.showerror("Validation Error", "Expense must be a positive number.")
                return
        except ValueError:
            messagebox.showerror("Validation Error", "Expense must be a numeric value.")
            return
        
        # Show a confirmation message with the submitted data
        messagebox.showinfo(
            "Expense Submitted",
            f"Date: {date_period}\nExpense: {amount}\nDescription: {description}\nCategory: {category}"
        )

        # Close the current window
        self.window.destroy()

        # Save the data to the CSV file
        self.save_to_csv(converted_date, amount, description, category)

    def save_to_csv(self, timeframe, amount, desc, cat):
        """
        Saves the provided expense data to a CSV file.
        If the file does not exist, it creates one and adds headers.
        :param timeframe: The expense date in YYYY-MM-DD format.
        :param amount: The expense amount.
        :param desc: The description of the expense.
        :param cat: The category of the expense.
        """
        file_path = "expense data.csv"  # Define the file path for storing expense data
        file_exists = os.path.exists(file_path)  # Check if the file already exists

        try:
            with open(file_path, mode='a', newline="") as file:  # Open the file in append mode
                writer = csv.writer(file)  # Create a CSV writer object
                if not file_exists or os.stat(file_path).st_size == 0:  # Check if the file is new or empty
                    writer.writerow(["Date", "Amount", "Description", "Category"])  # Write the header row
                writer.writerow([timeframe, amount, desc, cat])  # Write the expense data
        except Exception as e:
            # Show error message in case of an exception
            messagebox.showerror("Error", f"Failed to save data: {e}")
        
