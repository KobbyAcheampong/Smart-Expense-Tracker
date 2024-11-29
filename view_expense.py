import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class DataVisualization:
    def __init__(self, master):
        self.window = tk.Toplevel(master)
        self.window.title("Data Visualization")
        self.window.geometry("800x600")
        
        # Read the CSV file with more flexible date parsing
        try:
            self.df = pd.read_csv("Expense data.csv")
            # Try parsing dates with dayfirst=True to handle different date formats
            self.df['Date'] = pd.to_datetime(self.df['Date'], format='ISO8601')
            print("Data loaded successfully:")
            print(self.df.head())  # This will help us see the data structure
        except Exception as e:
            messagebox.showerror("Error", f"Error reading CSV file: {str(e)}")
            print(f"Detailed error: {str(e)}")  # Print detailed error for debugging
            self.window.destroy()
            return

        # Create frames for chart and buttons
        self.chart_frame = ttk.Frame(self.window)
        self.chart_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        self.button_frame = ttk.Frame(self.window)
        self.button_frame.pack(fill=tk.X, padx=10, pady=5)

        # Create buttons
        self.line_btn = ttk.Button(
            self.button_frame, 
            text="Show Line Chart", 
            command=self.show_line_chart
        )
        self.line_btn.pack(side=tk.LEFT, padx=5)

        self.pie_btn = ttk.Button(
            self.button_frame, 
            text="Show Pie Chart", 
            command=self.show_pie_chart
        )
        self.pie_btn.pack(side=tk.LEFT, padx=5)

        self.table_btn = ttk.Button(
            self.button_frame, 
            text="Show Table", 
            command=self.show_table
        )
        self.table_btn.pack(side=tk.LEFT, padx=5)

        # Initialize with pie chart
        self.current_widget = None
        self.show_pie_chart()

    def clear_current_widget(self):
        if self.current_widget:
            for widget in self.chart_frame.winfo_children():
                widget.destroy()

    def show_pie_chart(self):
        self.clear_current_widget()
        
        # Calculate category totals
        category_totals = self.df.groupby('Category')['Amount'].sum()

        # Create figure and plot
        fig = Figure(figsize=(8, 6))
        ax = fig.add_subplot(111)
        ax.pie(category_totals.values, labels=category_totals.index, autopct='%1.1f%%')
        ax.set_title('Expenses by Category')

        # Create canvas and display
        canvas = FigureCanvasTkAgg(fig, self.chart_frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(fill=tk.BOTH, expand=True)
        canvas.draw()
        self.current_widget = canvas_widget

    def show_line_chart(self):
        self.clear_current_widget()
        
        # Create figure and plot
        fig = Figure(figsize=(8, 6))
        ax = fig.add_subplot(111)
        
        # Sort data by date before plotting
        self.df = self.df.sort_values('Date')
        
        # Group by date and plot
        daily_expenses = self.df.groupby('Date')['Amount'].sum()
        
        # Plot with actual date range
        ax.plot(daily_expenses.index, daily_expenses.values, marker='o')
        
        # Set the x-axis limits to the actual data range
        ax.set_xlim(daily_expenses.index.min(), daily_expenses.index.max())
        
        # Format the plot
        ax.set_title('Expenses Over Time')
        ax.set_xlabel('Date')
        ax.set_ylabel('Expense Amount ($)')
        fig.autofmt_xdate()  # Rotate date labels
        
        # Add grid for better readability
        ax.grid(True, linestyle='--', alpha=0.7)
        
        # Create canvas and display
        canvas = FigureCanvasTkAgg(fig, self.chart_frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(fill=tk.BOTH, expand=True)
        canvas.draw()
        self.current_widget = canvas_widget

    def show_table(self):
        self.clear_current_widget()
        
        # Create frame for table and scrollbar
        table_frame = ttk.Frame(self.chart_frame)
        table_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create Treeview
        columns = ('Date', 'Amount', 'Description', 'Category')
        tree = ttk.Treeview(table_frame, columns=columns, show='headings')
        
        # Define columns
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=150)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        
        # Add data to table
        for _, row in self.df.iterrows():
            tree.insert('', 'end', values=(
                row['Date'].strftime('%Y-%m-%d'), 
                f"${row['Amount']:.2f}", 
                row['Description'], 
                row['Category']
            ))
        
        # Pack widgets
        tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.current_widget = table_frame

# Create and run the application
def main():
    root = tk.Tk()
    app = DataVisualization(root)
    root.mainloop()

if __name__ == "__main__":
    main()