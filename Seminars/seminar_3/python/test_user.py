import unittest
from user import User


class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.user = User('Temp_Name', 'temp_password')

    def test_authenticate(self):
        self.user.authenticate('Temp_Name', 'temp_password')
        self.assertTrue(self.user.is_authenticate)

    def test_not_authenticate(self):
        self.user.authenticate('Temp_Name', 'not_temp_password')
        self.assertFalse(self.user.is_authenticate)


if __name__ == "__main__":
    unittest.main()
