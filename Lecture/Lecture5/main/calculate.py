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
                assert IOError, 'Не известная операция'

    def add(self) -> float:
        return self.a + self.b

    def sub(self) -> float:
        return self.a - self.b

    def mul(self) -> float:
        return self.a * self.b

    def div(self) -> float:
        assert self.b != 0, 'На ноль делить нельзя'
        return self.a / self.b
