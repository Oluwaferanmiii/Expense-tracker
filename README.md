# Console-Based Expense Tracker Application

## 📚 Description
The **Expense Tracker Application** is a console-based Python project that allows users to:
- **Add, View, Search, and Delete Expenses**: Record and manage expenses with details like amount, category, date, and description.
- **Summary & Statistics**: View total expenses, highest and lowest expenses, and group expenses by category.
- **Data Persistence**: Expenses are saved in a SQLite database (`expenses.db`), ensuring data is saved even after restarting the application.
- **Export and Import**: Export expenses to a JSON file and import them back for easy backup and restoration.

This project demonstrates key Python concepts including:
- **Object-Oriented Programming (OOP)**
- **Modules and Imports**
- **Exception Handling**
- **SQLite Database Integration**
- **JSON Export/Import**
- **Python Standard Library** (`os`, `json`, `datetime`, etc.)

---

## 🚀 Features
- **Add Expense**: Record expenses with amount, category, date, and description.
- **View Expenses**: Display all expenses or filter by category.
- **Search Expenses**: Search for expenses by category.
- **Delete Expenses**: Remove expenses by ID.
- **Summary & Statistics**:
  - Total expenses grouped by category.
  - Highest and lowest expense.
  - Average expense.
- **Export and Import**:
  - Export expenses to a `JSON` file.
  - Import expenses from a JSON file.
- **User-Friendly Console Menu**: Easy navigation with text-based menu options.
- **Error Handling**: Handles invalid inputs, database connection errors, and JSON decode errors.
- **Colorful Terminal Output**: Using `colorama` for better UI experience.

---

## 🛠️ Technologies Used
- **Python 3.x**
- **SQLite3**: For database management.
- **JSON**: For data export and import.
- **Colorama**: For colorful console output.
- **Modules Used**:
  - `sqlite3` - Database operations
  - `json` - JSON import/export
  - `datetime` - Date validation and formatting
  - `os` - File operations

---

## 📁 Project Structure

```mermaid
graph TD;
    A[expense-tracker] --> B[database.py <br> Manages SQLite database operations]
    A --> C[expense_tracker.py <br> Business logic for expense tracker]
    A --> D[main.py <br> Entry point (User Interface)]
    A --> E[expenses.db <br> SQLite database file (auto-created)]
    A --> F[expenses.json <br> JSON file for export/import (optional)]
```

---

## 🚦 Prerequisites
Ensure you have **Python 3.x** installed. You can check by running:
```sh
python --version 
```
You also need to install the required module:
```sh
pip install colorama
```

---

## 📥 Installation
Clone the Repository:
```sh
git clone https://github.com/Oluwaferanmiii/expense-tracker.git
cd expense-tracker
```
Install Dependencies:
```sh
pip install colorama
```
Run the Application:
```sh
python main.py
```

---

## 📊 Usage
### Main Menu:
```sh
=== Expense Tracker ===
1. Add Expense
2. View Expenses
3. Search Expenses
4. Delete Expense
5. Summary & Statistics
6. Export to JSON
7. Import from JSON
8. Exit
```
### Add Expense:
* Input amount, category, date (YYYY-MM-DD), and description.
* Amount should be greater than zero.
* Date is validated using the datetime module.
* Description is optional but recommended.

### View Expense: 
* Lists all expenses sorted by date.
* Displays expense ID, amount, category, date, and description.

### Search Expenses: 
* Search by category (case insensitive).

### Delete Expense:
* Delete an expense by its unique ID

### Summary & Statistics:
* Displays total expenses grouped by category.
* Shows highest and lowest expenses.

### Export to JSON:
* Exports all expenses to a expenses.json file.

### Import from JSON:
* Imports expenses from a JSON file.
* Checks for duplicate entries before importing.

---

## 💾 Data Persistence
* All expenses are saved in an SQLite database (expenses.db).
* Expenses are automatically saved and loaded on each run.
* Data can be exported to JSON for backup and imported from JSON for restoration.

---

## 🎨 Colorful Console Output
* This application uses colorama for colorful terminal output.
* Install it using:
```sh
pip install colorama
```

---

## 🛠️ Example Commands
```sh
python main.py      # Launches the application
```

---

## 🔍 JSON Example
```sh
[
    {
        "id": 1,
        "amount": 50.0,
        "category": "food",
        "date": "2025-02-28",
        "description": "Lunch at restaurant"
    },
    {
        "id": 2,
        "amount": 100.0,
        "category": "transport",
        "date": "2025-02-27",
        "description": "Taxi fare"
    }
]
```

---

## ✅ Future Enhancements
* Update Expense: Allow users to update existing expenses.
* Advanced Search: Search by date range, amount range, or description keywords.
* Summary Visualizations: Use matplotlib to visualize expense distribution by category.
* Multi-Currency Support: Support for multiple currencies with exchange rates.
* Recurring Expenses: Automatically add recurring expenses (e.g., rent, subscriptions).

---

## 🐞 Troubleshooting
* If you encounter a ModuleNotFoundError, ensure dependencies are installed:
```sh
pip install colorama
```
If the application crashes, check for:
* Invalid input types (e.g., letters in amount fields)
* Incorrect date format (should be YYYY-MM-DD)
* Missing expenses.db file (it will auto-create on the first run)

---

## 📜 License
This project is licensed under the MIT License.

---

## 🤝 Contributing
Contributions are welcome! If you have ideas for improvements or find any bugs, feel free to:
* Open an issue
* Submit a pull request

---

## 👨‍💻 Author
Feranmi - https://github.com/Oluwaferanmiii

---

## 📢 Feedback
If you encounter any issues or have suggestions, feel free to open an issue or contact me through GitHub.

---

## 📌 Note
This is a console-based application and requires a terminal or command prompt to run. A future version may include a graphical user interface (GUI).

