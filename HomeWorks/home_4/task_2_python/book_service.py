from book import Book
from book_repository import BookRepository


class BookService:

    def __init__(self):
        self.book_repository = BookRepository()

    def find_book_by_id(self, id_num) -> Book:
        return self.book_repository.find_by_id(id_num)

    def find_all_books(self) -> list[Book]:
        return self.book_repository.find_all()
