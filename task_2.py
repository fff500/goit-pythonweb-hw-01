from abc import ABC, abstractmethod
import logging


logging.basicConfig(level=logging.INFO)


class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def __getitem__(self, key: str) -> str:
        if key in ("title", "author", "year"):
            return getattr(self, key)
        raise KeyError(f"{key} is not a valid attribute")

    def __str__(self):
        return f"{self.title} by {self.author}, {self.year}"


class LibraryInterface(ABC):
    @abstractmethod
    def add_book() -> None:
        pass

    @abstractmethod
    def remove_book() -> None:
        pass

    @abstractmethod
    def show_books() -> None:
        pass


class Library(LibraryInterface):
    def __init__(self):
        self.books = []

    def add_book(self, title: str, author: str, year: int):
        book = Book(title, author, year)
        self.books.append(book)

    def remove_book(self, title: str):
        for book in self.books:
            if book["title"] == title:
                self.books.remove(book)
                break

    def show_books(self):
        for book in self.books:
            logging.info(book)


class LibraryManager:
    def __init__(self, library: LibraryInterface):
        self.library = library


def main():
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                manager.library.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.library.remove_book(title)
            case "show":
                manager.library.show_books()
            case "exit":
                break
            case _:
                logging.info("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
