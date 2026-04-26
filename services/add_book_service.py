from data.library_data import books

def add_book(book_name):
    book = book_name.lower()

    if book in books:
        return "Book already exists"

    books[book] = {"available": True}
    return "Book added successfully"