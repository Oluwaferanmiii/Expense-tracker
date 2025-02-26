from expense_tracker import ExpenseTracker
from colorama import Fore, Style


def main():
    """Main menu loop for the Expense Tracker application."""
    tracker = ExpenseTracker()

    while True:
        # Display main menu options
        print("\n==== Expense Tracker ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search Expenses")
        print("4. Delete Expense")
        print("5. Summary & Statistics")
        print("6. Export to JSON")
        print("7. Import from JSON")
        print("8. Exit")

        # Get user choice
        try:
            print("=========================")
            choice = int(
                input(Fore.YELLOW + "Enter your choice: " + Style.RESET_ALL))
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a number." + Style.RESET_ALL)
            continue
        except EOFError:
            print(
                Fore.RED + "\nUnexpected input detected. Please input a valid number" + Style.RESET_ALL)
            continue

        # Perform action based on user's choice
        if choice == 1:
            tracker.add_expense()
        elif choice == 2:
            tracker.view_expenses()
        elif choice == 3:
            tracker.search_expenses()
        elif choice == 4:
            tracker.delete_expense()
        elif choice == 5:
            tracker.summary_statistics()
        elif choice == 6:
            tracker.export_to_json()
        elif choice == 7:
            tracker.import_to_json()
        elif choice == 8:
            # Confirm before exiting
            confirm = input(
                Fore.RED + "Are you sure you want to exit? (y/n): " + Style.RESET_ALL).lower()
            if confirm == "y":
                print(Fore.RED + "Exiting..." + Style.RESET_ALL)
                break
            else:
                continue
        else:
            print(Fore.RED + "Invalid choice. Please select again." + Style.RESET_ALL)


if __name__ == "__main__":
    main()
