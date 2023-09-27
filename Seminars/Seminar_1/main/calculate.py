class Calculate:

    @staticmethod
    def summa(args) -> int:
        """
        Возвращает сумму элементов
        :param args:
        :return:
        """
        result = 0
        for el in args:
            result += el
        return result

    @staticmethod
    def division(numerator, denomintor) -> float:
        assert denomintor != 0, "Деление на ноль"
        return numerator / denomintor
