class Shop:

    def __init__(self):
        self.products = []

    def get_products(self):
        return self.products

    def set_products(self, products):
        self.products = products

    def add_product(self, product):
        self.products.append(product)

    def get_sorted_list_products(self):
        """
        :return: отсортированный по возрастанию и цене список продуктов
        """

        self.products.sort(key=lambda k: k.cost)

    def get_most_expensive_product(self):
        """
        :return: самый дорогой продукт
        """
        self.get_sorted_list_products()
        result = self.products
        expensive_product = result[len(self.products) - 1]
        return f"{expensive_product}"

    def __str__(self):
        res = ''
        for product in self.products:
            res += f"{product} \n"
        return res
