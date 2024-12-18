"""Repository is an architectural pattern that is used to abstract data access. The repository
acts as a layer between the business logic of the application and the data source
(for example, a database). It provides a unified interface for performing operations with data,
hiding from the rest of the system the details of how this data is stored and retrieved.

It is used:
* When it is necessary to isolate the logic of working with a database or other data source
    from business logic;
* When it is necessary to provide the possibility of easily replacing the data source
    (for example, using a file or API instead of a database).
* When it is necessary to simplify the testing of business logic by eliminating
    dependence on a specific data source.

"""


# Data store model.
class Book:
    def __init__(self, id_, title, author):
        self.id = id_
        self.title = title
        self.author = author

    def __repr__(self):
        return f"Book(id={self.id}, title='{self.title}', author='{self.author}')"


# Repository.
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
