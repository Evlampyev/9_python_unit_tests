from unittest import TestCase, main
from random_number import RandomNumber
from max_element import MaxNumber


class TestMain(TestCase):
    def test_create_list(self):
        """Проверяем, что список чисел генерируется корректно"""
        size = 10
        lst = RandomNumber(size)

        lst.create_lst()
        self.assertEquals(size, len(lst.get_lst()))

    def test_negative_result(self):
        size = -1
        lst = RandomNumber(size)
        self.assertTrue(len(lst.lst) == 0)

    def test_find_max(self):
        size = 5
        lst = RandomNumber(size)
        lst.create_lst()
        result = MaxNumber.find_max_number(lst.lst)
        maximus = max(lst.lst)
        self.assertEquals(result, maximus)


if __name__ == "__main__":
    main()
