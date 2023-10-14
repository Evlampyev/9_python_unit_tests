from shop import Shop
from product import Product
import unittest


class TestShop(unittest.TestCase):
    def setUp(self) -> None:
        self.first = Product('First', 100)
        self.second = Product('Second', 500)
        self.third = Product('Third', 300)
        self.fourth = Product('Fourth', 250)
        self.shop = Shop()
        self.shop.add_product(self.first)
        self.shop.add_product(self.second)
        self.shop.add_product(self.third)
        self.shop.add_product(self.fourth)

    def test_sorting(self):
        """
        :return: отсортированы ли продукты
        """
        result = True
        self.shop.get_sorted_list_products()
        lst = self.shop.products
        for i in range(len(lst) - 1):
            if lst[i].cost > lst[i + 1].cost:
                result = False
        self.assertTrue(result, "Сортировка проведена не верно")

    def test_expensive_product(self):
        most_expensive = self.second
        self.assertEqual(f"{most_expensive}", self.shop.get_most_expensive_product())


if __name__ == '__main__':
    unittest.main()
