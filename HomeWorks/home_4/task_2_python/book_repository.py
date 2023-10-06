from book import Book


class BookRepository:
    """Интерфейс для работы с БД"""

    def find_by_id(self, id_num: int) -> Book:
        pass

    def find_all(self) -> list[Book]:
        pass
