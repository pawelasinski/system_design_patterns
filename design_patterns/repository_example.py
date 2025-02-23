"""Repository

The `Repository` pattern is an architectural pattern that abstracts data access,
acting as a bridge between business logic and the underlying data source
(e.g., a database, API, or file system). It provides a unified interface
for managing data operations while encapsulating storage details.

Why use it?
* Separation of concerns (keeps business logic independent of data storage details).
* Flexibility (easily swap data sources (e.g., database, API, or in-memory storage).
* Improved testability (enables unit testing without relying on a specific database).

"""


# Data store model
class Book:
    def __init__(self, id_, title, author):
        self.id = id_
        self.title = title
        self.author = author

    def __repr__(self):
        return f"Book(id={self.id}, title='{self.title}', author='{self.author}')"


# Repository
class BookRepository:
    def __init__(self):
        self._books = {}

    def add_book(self, book):
        self._books[book.id] = book

    def get_book_by_id(self, book_id):
        return self._books.get(book_id)

    def get_all_books(self):
        return list(self._books.values())

    def remove_book_by_id(self, book_id):
        if book_id in self._books:
            del self._books[book_id]


if __name__ == "__main__":
    repository = BookRepository()

    repository.add_book(Book(1, "1984", "George Orwell"))
    repository.add_book(Book(2, "Brave New World", "Aldous Huxley"))
    repository.add_book(Book(3, "Fahrenheit 451", "Ray Bradbury"))

    print(repository.get_all_books())

    print(repository.get_book_by_id(1))

    repository.remove_book_by_id(2)
    print(repository.get_all_books())
