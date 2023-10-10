from unittest import main, TestCase
from calculate import Calculate  # файл почему-то ассоциируется с файлом из папки seminar_1, победить не смог
import sys
sys.path.insert(0, 'C:\GeekBrains\II четверть\09. Unit_tests\Lecture\Lecture_5')


class TestCalculate(TestCase):
    def setUp(self):
        self.a = 6
        self.b = 12

    def test_add(self):
        self.calc = Calculate(self.a, self.b, '+')
        self.assertEquals(self.calc.answer, 18)

    def test_sub(self):
        self.calc = Calculate(self.a, self.b, '-')
        self.assertEquals(self.calc.answer, -6)

    def test_mul(self):
        self.calc = Calculate(self.a, self.b, '*')
        self.assertEquals(self.calc.answer, 72)

    def test_div(self):
        self.calc = Calculate(self.a, self.b, '/')
        self.assertEquals(self.calc.answer, 0.5)


if __name__ == "__main__":
    main()
