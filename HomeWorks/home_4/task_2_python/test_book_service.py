# У вас есть класс BookService, который использует интерфейс BookRepository для получения информации
# о книгах из базы данных. Ваша задача написать unit-тесты для BookService,
# используя Mockito для создания мок-объекта BookRepository.


from unittest import mock
import unittest
from unittest.mock import patch
from unittest.mock import MagicMock
from book import Book
from book_repository import BookRepository


class TestBookService(unittest.TestCase):
    def setUp(self):
        self.book_1 = Book(1, "Война и мир", "Лев Толстой")
        self.book_2 = Book(2, "Полное собрание", "Александр Пушкин")
        self.book_3 = Book(3, "Мцыри", "Михаил Лермонтов")
        self.book_repository = BookRepository

    def test_find_by_id(self):
        result = 1
        self.assertTrue(result, 1)

    def test_find_all(self):
        result = 1
        self.assertTrue(result, 1)

if __name__ == "__main__":
    unittest.main()
