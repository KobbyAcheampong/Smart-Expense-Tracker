"""
Smart Expense Tracker Application

This application allows users to add expenses, view expense data, export data to an Excel file, 
and clear all expense data. It uses Tkinter for the GUI, pandas for data manipulation, 
and PIL for image handling.
"""
# import required libraries
import tkinter as tk  # GUI framework for Python
from tkinter import ttk, messagebox, Label  # Widgets and dialogs for Tkinter
from PIL import Image, ImageTk  # For image handling and display
from add_expense_window import AddExpenseWindow  # Submodule for adding expenses
from view_expense import DataVisualization  # Submodule for visualizing expense data
import pandas as pd  # For handling data manipulation and export
from datetime import datetime  # For timestamping exported files
import os  # For interacting with the operating system
from pathlib import Path  # For managing file paths

#  Main function to display the application's primary interface after clicking "Get Started"
def show_main_interface():
    """
    Displays the main interface after the 'Get Started' button is clicked.
    Provides options to add expenses, view expenses, export data, and clear data.
    """
    # Destroy the 'Get Started' button to display the main interface
    get_started.destroy()
    
    # Helper function to handle adding new expenses
    def add_expenses():
        """Opens the Add Expense window."""
        AddExpenseWindow(main_frame)
    
    # Helper function to display expense visualizations
    def data_viz():
        """Opens the Data Visualization window to view expenses."""
        DataVisualization(main_frame)
    
     # Helper function to export expense data to Excel
    def export_to_excel():
        """
        Exports the expense data from a CSV file to an Excel file.
        The file is saved in the user's Downloads folder with a timestamped filename.
        """
        try:
            df = pd.read_csv("expense data.csv")  # Read expense data from CSV
            current_date = datetime.now().strftime("%Y-%m-%d %H-%M-%S")  # Get the current timestamp
            downloads_path = str(Path.home() / "Downloads")  # Path to the Downloads folder
            filename = f'ExpensesAt{current_date}.xlsx'  # Generate filename
            filepath = os.path.join(downloads_path, filename)  # Create full file path
            df.to_excel(filepath, index=False)  # Export data to Excel
            messagebox.showinfo("Success", f"Data exported successfully to {filepath}")  # Show success message
        except Exception as e:
            # Show error message in case of an exception
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    # Helper function to clear all expense data
    def clear_expenses():
        """
        Clears all expense data from the CSV file after user confirmation.
        Maintains column headers while removing all data rows.
        """
        confirm = messagebox.askyesno(
            "Confirm clear",
            "Are you sure you want to clear all expense data? This action cannot be undone."
        )  # Prompt user for confirmation
        if confirm:
            try:
                df = pd.read_csv('expense data.csv')  # Read existing expense data
                headers = df.columns.to_list()  # Get column headers
                empty_df = pd.DataFrame(columns=headers)  # Create an empty DataFrame with same headers
                empty_df.to_csv('expense data.csv', index=False)  # Write the empty DataFrame to the CSV file
                messagebox.showinfo("Success", 'All expense data has been cleared!')  # Show success message
            except Exception as e:
                # Show error message in case of an exception
                messagebox.showerror("Error", f"An error occurred while clearing data!")

    # Add Expense button
    add_expense_btn = tk.Button(main_frame, text="Add expense", width=25, command=add_expenses)
    add_expense_btn.pack()  # Display the button

    # View Expenses button
    view_expense_btn = tk.Button(main_frame, text="View expenses", width=25, command=data_viz)
    view_expense_btn.pack()  # Display the button

    # Export Expenses button
    export_expense_btn = tk.Button(main_frame, text="Export expense data", width=25, command=export_to_excel)
    export_expense_btn.pack()  # Display the button

    # Clear Expenses button
    clear_expense = tk.Button(main_frame, text="Clear data", width=25, command=clear_expenses)
    clear_expense.pack()  # Display the button

# Main application window setup
root = tk.Tk()  # Create the root window
root.geometry("600x600")  # Set window size
root.title("Smart Expense Tracker")  # Set window title

main_frame = tk.Frame(root)  # Create the main frame for the application
main_frame.pack(fill=tk.BOTH, expand=True)  # Configure the frame to fill the window

# Load and display the application logo
image = Image.open('Smart Expense Tracker Logo.jpg')  # Open the logo image
image = image.resize((400, 400))  # Resize the image
photo = ImageTk.PhotoImage(image)  # Convert the image for Tkinter
image_present = True  # Flag indicating the image is loaded
logo = tk.Label(main_frame, image=photo, text="Smart Expense Tracker logo")  # Create a label for the image
logo.image = photo  # Attach the image to prevent garbage collection
logo.pack()  # Display the logo

# 'Get Started' button to show the main interface
get_started = ttk.Button(main_frame, text="Get Started", command=show_main_interface)
get_started.pack()  # Display the button

# Run the main event loop
root.mainloop()
