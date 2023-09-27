from product import Product
from shop import Shop


def main():
    magnit = Shop()
    milk = Product('Молоко', 50)
    water = Product('Вода', 15)
    bread = Product('Хлеб', 42)
    cake = Product("Торт", 200)
    magnit.add_product(cake)
    magnit.add_product(milk)
    magnit.add_product(water)
    magnit.add_product(bread)

    print("Все продукты:")
    print(magnit)
    print("Отсортированы по цене")
    magnit.get_sorted_list_products()
    print(magnit)
    print("Самый дорогой товар: ")
    print(magnit.get_most_expensive_product())


if __name__ == '__main__':
    main()
