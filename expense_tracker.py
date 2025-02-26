from database import DatabaseManager
from datetime import datetime
import json
from colorama import Fore, Style    # For colored terminal output


class ExpenseTracker:
    """Expense Tracker class to manage expenses."""

    def __init__(self):
        """Initialize the ExpenseTracker with a DatabaseManager instance."""
        self.db = DatabaseManager()

    def add_expense(self):
        """Add a new expense with amount, category, date, and description."""
        # Get and validate amount
        try:
            amount = float(input("Enter amount: "))
            if amount <= 0:
                print("Amount must be greater than zero.")
                return
        except ValueError:
            print("Invalid amount. Please enter a number")
            return

        # Get category and convert to lowercase
        category = input(
            "Enter category (e.g, food, transport, bills): ").lower()

        # Get and validate date
        date_input = input("Enter date (YYYY-MM-DD): ")
        try:
            date = datetime.strptime(date_input, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format! Please enter in the YYYY-MM-DD format.")
            return

        # Get description and convert to lowercase
        description = input("Enter description: ").lower()

        # Insert expense into the database
        self.db.insert_expense(amount, category, date, description)
        print(Fore.GREEN + "Expense added successfully!" + Style.RESET_ALL)

    def view_expenses(self):
        """View all expenses."""
        expenses = self.db.get_expenses()

        print(Fore.GREEN + "\n--- Expenses ---" + Style.RESET_ALL)
        # Display each expense record
        for row in expenses:
            print(
                f"ID: {row[0]}, Amount: {row[1]}, Category: {row[2]}, Date: {row[3]}, Description: {row[4]}")

    def search_expenses(self):
        """Search for expenses by category."""
        category = input(
            Fore.BLUE + "Enter the category to search for: " + Style.RESET_ALL).lower()
        expenses = self.db.search_expenses_by_category(category)

        print(Fore.GREEN + "\n--- Search Result ---" + Style.RESET_ALL)
        # Check if any expenses were found
        if not expenses:
            print(Fore.RED + "No expense found for this category" + Style.RESET_ALL)
        else:
            for row in expenses:
                print(
                    f"ID: {row[0]}, Amount: {row[1]}, Category: {row[2]}, Date: {row[3]}, Description: {row[4]}")

    def delete_expense(self):
        """Delete an expense by its ID."""
        expense_id = int(
            input(Fore.BLUE + "Enter the ID of the expense to delete: " + Style.RESET_ALL))

        self.db.delete_expense(expense_id)
        print(Fore.RED + "Expense deleted successfully!" + Style.RESET_ALL)

    def summary_statistics(self):
        """Display expense summary grouped by category."""
        summary = self.db.get_summary()

        print(Fore.GREEN + "\n--- Expense Summary ---" + Style.RESET_ALL)
        # Display summary statistics by category
        if not summary:
            print(Fore.RED + "No expenses found." + Style.RESET_ALL)
        else:
            for row in summary:
                print(f"Category: {row[0]}, Total: {row[1]}")

    def export_to_json(self):
        """Export expenses to a JSON file."""
        expenses = self.db.get_expenses()
        data = [
            {
                "id": expense[0],
                "amount": expense[1],
                "category": expense[2],
                "date": expense[3],
                "description": expense[4]
            }
            for expense in expenses
        ]

        with open("expenses.json", "w") as json_file:
            json.dump(data, json_file, indent=4)

        print(Fore.GREEN + "Data successfully exported to expenses.json" + Style.RESET_ALL)

    def import_to_json(self, json_file_name="expenses.json"):
        """Import expenses from a JSON file."""
        try:
            with open(json_file_name, "r") as json_file:
                data = json.load(json_file)

            imported_count = 0

            # Check for duplicate expenses before importing
            for expense in data:
                existing_expenses = self.db.get_expenses()

                if not any(
                    exp[1] == expense["amount"] and
                    exp[2] == expense["category"] and
                    exp[3] == expense["date"] and
                    exp[4] == expense["description"]
                    for exp in existing_expenses
                ):
                    self.db.insert_expense(
                        expense["amount"],
                        expense["category"],
                        expense["date"],
                        expense["description"]
                    )
                    imported_count += 1

            print(
                Fore.GREEN + f"{imported_count} new expense(s) imported from expenses.json" + Style.RESET_ALL)

        except FileNotFoundError:
            print(Fore.RED + "No expenses.json file found." + Style.RESET_ALL)
        except json.JSONDecodeError:
            print(Fore.RED + "Error decoding JSON file." + Style.RESET_ALL)
