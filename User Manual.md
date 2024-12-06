
  # Smart Expense Tracker
  ### By: Cornelius Acheampong
  ## User Manual


#### Table of Contents
1. [Dependencies](#dependencies)
2. [Getting Started](#start)
3. [Main Interface](#main)
4. [Adding Expenses](#add)
5. [Viewing and Analyzing Expenses](#view)
6. [Data Management](#data)
7. [Troubleshooting](#trouble)

-----------------------------------------------------------

<a id="dependencies"></a>
#### Dependencies
   * Python (>= 3.7)
   * Tkinter (comes with Python installation)
   * Pandas (for data manipulation, needs to be installed)
   * Matplotlib (for data visualization, needs to be installed)
   * Pillow (PIL) (for handling images, needs to be installed)
   * Openpyxl (for exporting to Excel, needs to be installed)

-------------------------------------------------------------
<a id="start"></a>
#### Getting Started
   
To launch the Smart Expense Tracker:
  1. Run the application
  2. You will see the Smart Expense Tracker logo
  3. Click the "Get Started" button to access the main interface

--------------------------------------------------------------
<a id="main"></a>
#### Main Interface
The main interface provides four primary functions:
- Add expense
- View expenses
- Export expense data
- Clear data
Each function is accessible via clearly labeled buttons on the main screen.

----------------------------------------------------------------
<a id="add"></a>
#### Adding Expenses
To add a new expense:
1. Click the "Add expense" button on the main interface
2. Fill in the required fields:
   - Date (Format: MM-DD-YYYY)
   - Expense amount (Must be a positive number)
   - Description (Optional)
   - Category (Required)
3. Click "Submit" to save the expense
4. A confirmation message will appear showing the entered details
5. Click "Close" to return to the main interface
Important Notes:
- The date must be entered in MM-DD-YYYY format (e.g., 12-25-2024)
- The expense amount must be a positive number
- Category cannot be left blank
- All entries are automatically saved to "expense data.csv"

----------------------------------------------------------
<a id="view"></a>
#### Viewing and Analyzing Expenses
To view your expenses:
1. Click "View expenses" on the main interface
2. The visualization window offers three viewing options:
   a. Pie Chart
   - Shows expenses broken down by category
   - Displays percentage distribution of expenses
   - Click "Show Pie Chart" to view
   b. Line Chart
   - Displays expenses over time
   - Shows spending trends
   - Click "Show Line Chart" to view
      c. Table View
   - Lists all expenses in chronological order
   - Shows complete details including date, amount, description, and category
   - Click "Show Table" to view
   - Use the scrollbar to navigate through entries

------------------------------------------------------------
<a id="data"></a>
#### Data Management
Exporting Data:
1. Click "Export expense data" on the main interface
2. The data will automatically export to an Excel file
3. The file will be saved in your Downloads folder
4. The filename will include the current date and time (e.g., "ExpensesAt2024-12-06 14-30-00.xlsx")
Clearing Data:
1. Click "Clear data" on the main interface
2. A confirmation dialog will appear
3. Click "Yes" to permanently delete all expense data
4. Click "No" to cancel
Warning: Clearing data cannot be undone. Make sure to export your data before clearing if you need to keep a backup.

-------------------------------------------------------------
<a id="data"></a>
#### Troubleshooting
Common Issues and Solutions:
1. Invalid Date Format Error
   - Ensure you're using MM-DD-YYYY format
   - Use leading zeros for single-digit months and days (e.g., 01-05-2024)
2. Invalid Amount Error
   - Enter only numbers for the expense amount
   - Do not include currency symbols
   - Use a decimal point for cents (e.g., 10.50)
3. Data Not Saving
   - Ensure you have write permissions in the application directory
   - Check that "expense data.csv" is not open in another program
   - Verify there's enough disk space
4. Visualization Not Loading
   - Make sure you have at least one expense entry
   - Check if "expense data.csv" exists and is not corrupted
   - Try clearing and re-entering data if issues persist
For any persistent issues, please check that all files are in the same directory and that you have the required Python libraries installed (tkinter, pandas, matplotlib, PIL).
