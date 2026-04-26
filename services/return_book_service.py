from datetime import datetime
from data.library_data import books, issued_books
from services.fine_service import calculate_fine

def return_book(book):
    book = book.lower()

    if book not in issued_books:
        return "Invalid return"

    record = issued_books.pop(book)
    books[book]["available"] = True

    used_days = (datetime.now() - record["issue_date"]).days
    extra_days = used_days - record["days"]

    fine = calculate_fine(extra_days)

    return f"Book returned. Fine: Rs {fine}"