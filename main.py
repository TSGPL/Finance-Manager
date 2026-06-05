from ui.app import FinanceDashboard

if __name__ == "__main__":
    app = FinanceDashboard()
    app.mainloop()




# To Do List:
# 1. Add/Delete Transactions (No Logic Yet, Just UI) - Done
# 2. Edit Transactions (No Logic Yet, Just UI) - Done
# 3. View Transaction History (Logic to read from JSON, UI to display in Transactions Page)
# 4. Add / Edit Categories (Logic to read/write categories, UI to manage categories in Seperate Page)
# 5. View Reports (Spending by Category, Monthly Summary)
# 6. Export Data (CSV, PDF)
# 7. Add Charts (Spending Over Time, Category Breakdown)