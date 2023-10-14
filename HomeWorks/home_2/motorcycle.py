from vehicle import Vehicle


class MotorCycle(Vehicle):
    def __init__(self, company, model, year):
        self.company = company
        self.model = model
        self.year_release = year
        self.num_wheels = 2
        self.speed = 0

    def test_drive(self):
        self.speed = 75

    def park(self):
        self.speed = 0

    def get_company(self) -> str:
        return self.company

    def get_model(self) -> str:
        return self.model

    def get_year_release(self) -> int:
        return self.year_release

    def get_speed(self) -> int:
        return self.speed

    def __str__(self):
        return f"This motorcycle is a {self.year_release} make {self.model}"
