import unittest
from calculate import Calculator


class TestCalculate(unittest.TestCase):
    def setUp(self) -> None:
        self.op_1 = 6
        self.op_2 = 3
        self.calc = Calculator()

    def test_calculation_sum(self):
        """
        Тестируем сумму чисел
        """
        result = Calculator.calculation(self.op_1, self.op_2, '+')
        self.assertEqual(result, 9)

    def test_calculation_sub(self):
        """
        Тестируем разность чисел
        :return:
        """
        result = Calculator.calculation(self.op_1, self.op_2, '-')
        self.assertEqual(result, 3)

    def test_calculation_mul(self):
        result = Calculator.calculation(self.op_1, self.op_2, '*')
        self.assertEqual(result, 18)

    def test_calculation_div(self):
        """
        Тестируем деление
        :return:
        """
        result = Calculator.calculation(self.op_1, self.op_2, '/')
        self.assertEqual(result, 2)

    def test_calculation_div_by_zero(self):
        """
        Тестируем вывод ошибки о делении на нуль
        :return:
        """
        with self.assertRaises(ArithmeticError):
            Calculator.calculation(self.op_1, 0, '/')

    def test_calculating_discount(self):
        """
        Тестирование расчета скидки
        :return:
        """
        pr = 100
        dis = 35
        result = self.calc.calculating_discount(pr, dis)
        self.assertEqual(result, 65)

    def test_calculating_discount_0(self):
        """
        Тестирование скидки, если её нет
        :return:
        """
        pr = 100
        dis = 0
        result = self.calc.calculating_discount(pr, dis)
        self.assertEqual(result, pr)

    def test_calculating_discount_value_error(self):
        """
        Тестирование на ошибку ввода данных
        :return:
        """
        pr = 100
        dis = '15'
        with self.assertRaises(ValueError):
            self.calc.calculating_discount(pr, dis)

    def test_calculating_discount_value_error_2(self):
        """
        Тестирование на ошибку ввода данных
        :return:
        """
        pr = '100'
        dis = 15
        with self.assertRaises(ValueError):
            self.calc.calculating_discount(pr, dis)


if __name__ == "__main__":
    unittest.main()
