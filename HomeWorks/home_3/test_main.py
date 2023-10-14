import unittest
from number import Number
from random import randint


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.left = 25
        self.right = 100
        self.first = randint(self.left - 100, self.left - 1)  # Число левее диапазона
        self.second = randint(self.left, self.right)  # Число в диапазоне
        self.third = randint(self.right + 1, self.right + 100)  # Число правее диапазона

    def test_even_odd_number_0(self):
        """
        Тестирование исходного случайного числа из диапазона на четность
        :return:
        """
        temp_1 = Number.even_odd_number(self.second)
        if self.second % 2 == 0:
            self.assertEqual(temp_1, True)
        else:
            self.assertEqual(temp_1, False)

    def test_even_odd_number_1(self):
        """
        Тестирование числа на 1 больше исходного на четность
        :return:
        """
        temp_1 = Number.even_odd_number(self.second + 1)
        if (self.second + 1) % 2 == 0:
            self.assertEqual(temp_1, True)
        else:
            self.assertEqual(temp_1, False)

    def test_number_to_the_left_interval(self):
        """
        Проверка числа левее диапазона
        :return:
        """
        self.assertFalse(Number.number_in_interval(self.first))

    def test_number_in_interval(self):
        """
        Проверка числа в диапазоне
        :return:
        """
        self.assertTrue(Number.number_in_interval(self.second))

    def test_number_to_the_right_interval(self):
        """
        Проверка числа правее диапазона
        :return:
        """
        self.assertFalse(Number.number_in_interval(self.first))


if __name__ == "__main__":
    unittest.main()
