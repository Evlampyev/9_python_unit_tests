import unittest
from car import Car
from vehicle import Vehicle
from motorcycle import MotorCycle


class TestVehicle(unittest.TestCase):
    def setUp(self) -> None:
        """Исходные данные для подготовки к тестированию"""
        self.car = Car('Moskvich', '412', 1980)
        self.motorcycle = MotorCycle('Java', '250', 1946)

    def test_car_vehicle(self):
        """
        Проверка наследования
        :return:
        """
        self.assertTrue(isinstance(self.car, Vehicle))

    def test_car_num(self):
        """Проверка наличия 4 калес у автомобиля"""
        self.assertEqual(self.car.num_wheels, 4)

    def test_motorcycle_num(self):
        """Проверка наличия 2 колёс у мотоцикла"""
        self.assertEqual(self.motorcycle.num_wheels, 2)

    def test_car_speed(self):
        """Проверка скорости при движении автомобиля"""
        self.car.test_drive()
        self.assertEqual(self.car.speed, 60)

    def test_motorcycle_speed(self):
        """Проверка скорости при движении мотоцикла"""
        self.motorcycle.test_drive()
        self.assertEqual(self.motorcycle.speed, 75)

    def test_car_park(self):
        """Проверка скорости автомобиля на парковке"""
        self.car.test_drive()
        self.car.park()
        self.assertEqual(self.car.speed, 0)

    def test_motorcycle_park(self):
        """Проверка скорости мотоцикла на парковке"""
        self.motorcycle.test_drive()
        self.motorcycle.park()
        self.assertEqual(self.motorcycle.speed, 0)


if __name__ == "__main__":
    unittest.main()
