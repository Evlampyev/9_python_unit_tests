# Задание 1. ** В классе Calculator создайте метод calculateDiscount, который принимает сумму покупки и процент скидки
# и возвращает сумму с учетом скидки. Ваша задача - проверить этот метод с использованием библиотеки AssertJ.
# Если метод calculateDiscount получает недопустимые аргументы, он должен выбрасывать исключение ArithmeticException.
# Не забудьте написать тесты для проверки этого поведения.


class Calculator:

    @staticmethod
    def calculation(first_operand: int, second_operand: int, operator: str) -> float:
        match operator:
            case '+':
                return first_operand + second_operand
            case '-':
                return first_operand - second_operand
            case '*':
                return first_operand * second_operand
            case '/':
                if second_operand != 0:
                    return first_operand / second_operand
                else:
                    raise ArithmeticError("На нуль делить нельзя")
            case _:
                raise ValueError("Неизвестная операция: " + operator)

    @staticmethod
    def square_root_extraction(number: float) -> float:
        if number == 0:
            raise ArithmeticError("Невозможно извлечь корень из 0")
        elif number < 0:
            raise ArithmeticError("Невозможно извлечь корень из отрицательного числа в вещественных числах")
        else:
            square_root = number / 2
            t = 0
            while (t - square_root) != 0:
                t = square_root
                square_root = (t + (number / t)) / 2
            return square_root

    @staticmethod
    def calculating_discount(purchase_amount: float, discount_amount: int) -> float:
        """
        :param purchase_amount: сумма покупки
        :param discount_amount: размер скидки в %
        :return: возвращает сумму покупки с учетом скидки
        """
        if isinstance(purchase_amount, int) and isinstance(discount_amount, int):
            if discount_amount == 0:
                return purchase_amount
            elif discount_amount < 0:
                raise ValueError("Скидка не может быть отрицательной")
            else:
                return purchase_amount * (1 - discount_amount / 100)
        else:
            raise ValueError("Введенные данные не числа")
