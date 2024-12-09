"""
Data Visualization Window

This module provides an interface for visualizing expense data. Users can view 
data as a pie chart, line chart, or in a table format. Data is read from a CSV file, 
and the module ensures proper handling of date parsing and error messages for issues.
"""

# import required libraries
import tkinter as tk  # GUI framework for Python
from tkinter import ttk, messagebox  # Widgets and dialogs for Tkinter
import pandas as pd  # Data manipulation and analysis
import matplotlib.pyplot as plt  # For creating plots
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # For embedding Matplotlib figures in Tkinter
from matplotlib.figure import Figure  # For creating Matplotlib figures

class DataVisualization:
    """
    Class for visualizing expense data with options to display a pie chart, 
    line chart, or table.
    """

    def __init__(self, master):
        """
        Initializes the Data Visualization window.
        :param master: The parent window or root window.
        """
        self.window = tk.Toplevel(master)  # Create a top-level window
        self.window.title("Data Visualization")  # Set the window title
        self.window.geometry("800x600")  # Set the window size
        
        # Read the CSV file with flexible date parsing
        try:
            self.df = pd.read_csv("Expense data.csv")  # Load expense data
            self.df['Date'] = pd.to_datetime(self.df['Date'], format='ISO8601')  # Parse dates
            print("Data loaded successfully:")
            print(self.df.head())  # Print first few rows for debugging
        except Exception as e:
            # Show error message and print detailed error for debugging
            messagebox.showerror("Error", f"Error reading CSV file: {str(e)}")
            print(f"Detailed error: {str(e)}")
            self.window.destroy()  # Close the window on error
            return

        # Create frames for chart and buttons
        self.chart_frame = ttk.Frame(self.window)  # Frame for displaying charts or tables
        self.chart_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        self.button_frame = ttk.Frame(self.window)  # Frame for action buttons
        self.button_frame.pack(fill=tk.X, padx=10, pady=5)

        # Create buttons for selecting visualizations
        self.line_btn = ttk.Button(self.button_frame, text="Show Line Chart", command=self.show_line_chart)
        self.line_btn.pack(side=tk.LEFT, padx=5)  # Line chart button

        self.pie_btn = ttk.Button(self.button_frame, text="Show Pie Chart", command=self.show_pie_chart)
        self.pie_btn.pack(side=tk.LEFT, padx=5)  # Pie chart button

        self.table_btn = ttk.Button(self.button_frame, text="Show Table", command=self.show_table)
        self.table_btn.pack(side=tk.LEFT, padx=5)  # Table view button

        # Initialize with pie chart
        self.current_widget = None  # Keep track of the currently displayed widget
        self.show_pie_chart()

    def clear_current_widget(self):
        """Clears the currently displayed widget from the chart frame."""
        if self.current_widget:
            for widget in self.chart_frame.winfo_children():
                widget.destroy()

    def show_pie_chart(self):
        """Displays a pie chart of expenses grouped by category."""
        self.clear_current_widget()
        
        # Calculate category totals
        category_totals = self.df.groupby('Category')['Amount'].sum()

        # Create a Matplotlib figure and pie chart
        fig = Figure(figsize=(8, 6))
        ax = fig.add_subplot(111)
        ax.pie(category_totals.values, labels=category_totals.index, autopct='%1.1f%%')
        ax.set_title('Expenses by Category')

        # Embed the figure in Tkinter
        canvas = FigureCanvasTkAgg(fig, self.chart_frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(fill=tk.BOTH, expand=True)
        canvas.draw()
        self.current_widget = canvas_widget

    def show_line_chart(self):
        """Displays a line chart of daily expenses over time."""
        self.clear_current_widget()
        
        # Sort data by date before plotting
        self.df = self.df.sort_values('Date')
        daily_expenses = self.df.groupby('Date')['Amount'].sum()  # Group data by date

        # Create a Matplotlib figure and line chart
        fig = Figure(figsize=(8, 6))
        ax = fig.add_subplot(111)
        ax.plot(daily_expenses.index, daily_expenses.values, marker='o')  # Plot daily expenses
        ax.set_xlim(daily_expenses.index.min(), daily_expenses.index.max())  # Set x-axis range

        # Format the plot
        ax.set_title('Expenses Over Time')
        ax.set_xlabel('Date')
        ax.set_ylabel('Expense Amount ($)')
        fig.autofmt_xdate()  # Rotate date labels for better readability
        ax.grid(True, linestyle='--', alpha=0.7)  # Add a grid

        # Embed the figure in Tkinter
        canvas = FigureCanvasTkAgg(fig, self.chart_frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(fill=tk.BOTH, expand=True)
        canvas.draw()
        self.current_widget = canvas_widget

    def show_table(self):
        """Displays the expense data in a tabular format."""
        self.clear_current_widget()
        
        # Create a frame for the table and scrollbar
        table_frame = ttk.Frame(self.chart_frame)
        table_frame.pack(fill=tk.BOTH, expand=True)

        # Create a Treeview widget to display data as a table
        columns = ('Date', 'Amount', 'Description', 'Category')
        tree = ttk.Treeview(table_frame, columns=columns, show='headings')

        # Define column headings and widths
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=150)

        # Add a scrollbar for the table
        scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)

        # Populate the table with data
        for _, row in self.df.iterrows():
            tree.insert('', 'end', values=(
                row['Date'].strftime('%Y-%m-%d'),  # Format the date
                f"${row['Amount']:.2f}",  # Format the amount
                row['Description'],  # Add the description
                row['Category']  # Add the category
            ))

        # Pack the table and scrollbar
        tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.current_widget = table_frame

# Create and run the application
def main():
    """Main function to run the Data Visualization application."""
    root = tk.Tk()
    app = DataVisualization(root)
    root.mainloop()

if __name__ == "__main__":
    main()
