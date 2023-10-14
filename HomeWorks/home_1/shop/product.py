class Product:

    def __init__(self, title: str, cost: int):
        self.title = title
        self.cost = cost

    def __str__(self):
        return f"{self.title} по цене {self.cost}$"

    def get_cost(self):
        return self.cost

    def set_cost(self, value: int):
        if isinstance(value, int) and value > 0:
            self.cost = value
        else:
            raise ValueError("Неверный тип данных")

    def get_title(self):
        return self.title

    def set_title(self, value: str):
        if isinstance(value, str) and len(value) > 0:
            self.title = value
        else:
            raise ValueError("Неверный тип данных")
