# У вас есть класс BookService, который использует интерфейс BookRepository для получения информации
# о книгах из базы данных. Ваша задача написать unit-тесты для BookService,
# используя Mockito для создания мок-объекта BookRepository.


from unittest import mock
import unittest
from book import Book
from book_repository import BookRepository


class TestBookService(unittest.TestCase):
    def setUp(self):
        self.book_1 = Book(1, "Война и мир", "Лев Толстой")
        self.book_2 = Book(2, "Полное собрание", "Александр Пушкин")
        self.book_3 = Book(3, "Мцыри", "Михаил Лермонтов")
        self.book_repository = BookRepository
        self.book_repository = unittest.MagicMock(name="BookRepository")

    # def test_find_by_id(self, id_num):
    #     with unittest.patch()


if __name__ == "__main__":
    unittest.main()
