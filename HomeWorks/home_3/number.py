from random import randint


class Number:

    def __init__(self):
        self.number = randint(1, 150)
        print(f'{self.number} - четное: {self.even_odd_number(self.number)}')
        print(f'{self.number} - в интервале (25,100): {self.number_in_interval(self.number)}')

    @staticmethod
    def even_odd_number(n: int) -> bool:
        """
        Проверка числа на чётность
        :param n: число для проверки
        :return: True - четное, False - нечетное
        """
        if n % 2 == 0:
            return True
        else:
            return False

    @staticmethod
    def number_in_interval(n: int) -> bool:
        """
        Проверяет, попадает ли число в интервал (25;100)
        :param n: число для проверки
        :return: True - попадает, False - не попадает
        """
        if 25 < n < 100:
            return True
        else:
            return False
