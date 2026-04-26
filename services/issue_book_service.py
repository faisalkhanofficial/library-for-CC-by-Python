from datetime import datetime
from data.library_data import books, issued_books

def issue_book(book, student, days):
    book = book.lower()

    if book not in books:
        return "Book not found"

    if not books[book]["available"]:
        return "Book already issued"

    books[book]["available"] = False

    issued_books[book] = {
        "student": student,
        "issue_date": datetime.now(),
        "days": days
    }

    return "Book issued successfully"