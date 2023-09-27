import unittest
from calculate import Calculate


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Тестируем сумму целых чисел
        """
        data = [1, 2, 3]
        result = Calculate.summa(data)
        self.assertEqual(result, 6)

    def test_division_by_zero(self):
        nom, denom = 10, 0
        result = Calculate.division(nom, denom)
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
