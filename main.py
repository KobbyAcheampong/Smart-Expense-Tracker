import tkinter as tk
from tkinter import ttk, messagebox, Label
from PIL import Image, ImageTk
from add_expense_window import AddExpenseWindow
from view_expense import DataVisualization
import pandas as pd
from datetime import datetime
import os
from pathlib import Path

def show_main_interface():
    # for widget in main_frame.winfo_children():
    #     widget.destroy()
    get_started.destroy()

    def add_expenses():
        AddExpenseWindow(main_frame)

    def data_viz():
        DataVisualization(main_frame)

    def export_to_excel():
        try:
            df = pd.read_csv("expense data.csv")

            current_date = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
            downloads_path = str(Path.home()/"Downloads")
            filename = f'ExpensesAt{current_date}.xlsx'
            filepath = os.path.join(downloads_path,filename)

            df.to_excel(filepath, index=False)

            messagebox.showinfo("Success", f"Data exported successfully to {filepath}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occured: {str(e)}")

    def clear_expenses():
        confirm = messagebox.askyesno(
            "Confirm clear",
            "Are you sure you want to clear all expense data? This action cannot be undone."
        )

        if confirm:
            try:
                df=pd.read_csv('expense data.csv')
                headers=df.columns.to_list()

                empty_df = pd.DataFrame(columns=headers)

                empty_df.to_csv('expense data.csv', index=False)

                messagebox.showinfo("Success", 'All expense data has been cleared!')
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while clearing data!")


    add_expense_btn = tk.Button(main_frame, text="Add expense", width=25, command=add_expenses)
    add_expense_btn.pack()

    view_expense_btn = tk.Button(main_frame, text="View expenses", width=25, command=data_viz)
    view_expense_btn.pack()

    export_expense_btn = tk.Button(main_frame, text="Export expense data", width=25, command=export_to_excel)
    export_expense_btn.pack()

    clear_expense = tk.Button(main_frame,text="Clear data", width=25, command=clear_expenses)
    clear_expense.pack()

root = tk.Tk()
root.geometry("600x600")
root.title("Smart Expense Tracker")

main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)

image= Image.open('Smart Expense Tracker Logo.jpg')
image = image.resize((400,400))
photo = ImageTk.PhotoImage(image)
image_present = True

logo=tk.Label(main_frame, image=photo, text="Smart Expense Tracker logo")
logo.image=photo
logo.pack()

get_started = ttk.Button(main_frame, text="Get Started", command=show_main_interface)
get_started.pack()



root.mainloop()