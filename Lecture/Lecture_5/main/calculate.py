from typing import Any


class Calculate:

    def __init__(self, a, b, operator: str):
        self.answer = None
        self.a = a
        self.b = b
        self.operator = operator
        self.calculate()

    def calculate(self):
        match self.operator:
            case '+':
                self.answer = self.add()
            case '-':
                self.answer = self.sub()
            case '*':
                self.answer = self.mul()
            case '/':
                self.answer = self.div()
            case _:
                self.answer = 'Не известная операция'

    def add(self) -> float:
        return self.a + self.b

    def sub(self) -> float:
        return self.a - self.b

    def mul(self) -> float:
        return self.a * self.b

    def div(self) -> str | Any:
        try:
            return self.a / self.b
        except ZeroDivisionError as er:
            return f'На ноль делить нельзя'
