import sqlite3
import os


class DatabaseManager:
    """Class to manage database operation for Expense Tracker."""

    def __init__(self, db_name="expenses.db"):
        """Initialize the database manager and create table if not exists."""
        # store database name and path
        self.db_name = os.path.join(os.path.dirname(__file__), db_name)
        self.create_table()

    def connect(self):
        """Connect to SQLite database."""
        try:
            return sqlite3.connect(self.db_name)
        except sqlite3.Error as e:
            print("Database connection error:", e)

    def create_table(self):
        """Create the expenses table if it doesn't exist."""
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS expenses(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   amount REAL NOT NULL,
                   category TEXT NOT NULL,
                   date DATE NOT NULL,
                   description TEXT
                )
            """)
            conn.commit()  # Save changes to the database

    def insert_expense(self, amount, category, date, description):
        """Insert a new expense into the database."""
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO expenses(amount, category, date, description)
                VALUES(?, ?, ?, ?)
            """, (amount, category, date, description))
            conn.commit()

    def get_expenses(self):
        """Retrieve all expenses from the database."""
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM expenses ")
            return cursor.fetchall()  # Return list of all expense records

    def search_expenses_by_category(self, category):
        """Search for expenses by category."""
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM expenses
                WHERE LOWER(category) = ?
            """, (category.lower(),))   # Convert to lowercase for case-insensitive search
            result = cursor.fetchall()
            return result

    def delete_expense(self, expense_id):
        """Delete an expense by its ID."""
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM expenses WHERE id= ?", (expense_id,))
            conn.commit()

    def get_summary(self):
        """Get expense summary grouped by category."""
        with self.connect() as conn:
            cursor = conn.cursor()
            # Group by category in lowercase to avoid case-sensitivity issues
            cursor.execute("""
            SELECT LOWER(category), SUM(amount) 
            FROM expenses 
            GROUP BY LOWER(category)
            """)
            result = cursor.fetchall()
            return result
