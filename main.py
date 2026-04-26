from data.library_data import books
from services.add_book_service import add_book
from services.issue_book_service import issue_book
from services.return_book_service import return_book
from utils.helper import get_days


def show_books():
    print("\n--- Books List ---")
    for book, info in books.items():
        status = "Available" if info["available"] else "Issued"
        print(f"{book} - {status}")


def library_menu():
    while True:
        print("\n====== LIBRARY MENU ======")
        print("1. Show Books")
        print("2. Add Book")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            show_books()

        elif choice == "2":
            book = input("Enter book name: ")
            print(add_book(book))

        elif choice == "3":
            book = input("Enter book name: ")
            student = input("Enter student name: ")
            days = get_days()

            if days is not None:
                print(issue_book(book, student, days))

        elif choice == "4":
            book = input("Enter book name: ")
            print(return_book(book))

        elif choice == "5":
            print("Exiting system...")
            break

        else:
            print("Invalid choice")


library_menu()