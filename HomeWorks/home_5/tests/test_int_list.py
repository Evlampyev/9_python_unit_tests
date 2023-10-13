from unittest import TestCase, main
from int_list import IntList


class TestIntList(TestCase):
    def test_getter_int_list(self):
        lst = IntList()
        lst.int_list = [1, 2, 3]
        self.assertEquals([1, 2, 3], lst.getter_int_list())

    def test_setter_int_list(self):
        lst = IntList()
        lst.setter_int_list([1, 2, 3, 4])
        self.assertEquals([1, 2, 3, 4], lst.int_list)

    def test_average_value_of_list(self):
        lst = IntList()
        lst.int_list = [1, 2, 3, 4, 5]
        lst.average_value_of_list()
        self.assertTrue(lst.average_value == 3)


if __name__ == "__main__":
    main()
