from unittest import main, TestCase
from Lecture.Lecture_5.main.calculate import Calculate


class TestCalculate(TestCase):
    def setUp(self):
        """Метод, который платформа тестирования будет автоматически вызывать для каждого выполняемого нами теста"""
        self.a = 6
        self.b = 12

    def test_add(self):
        calc = Calculate(self.a, self.b, '+')
        self.assertEquals(calc.answer, 18)

    def test_sub(self):
        calc = Calculate(self.a, self.b, '-')
        self.assertEquals(calc.answer, -6)

    def test_mul(self):
        calc = Calculate(self.a, self.b, '*')
        self.assertEquals(calc.answer, 72)

    def test_div(self):
        calc = Calculate(self.a, self.b, '/')
        self.assertEquals(calc.answer, 0.5)

    def test_div_by_zero(self):
        calc = Calculate(self.a, 0, '/')
        self.assertEquals(calc.answer, 'На ноль делить нельзя')


if __name__ == "__main__":
    main()
