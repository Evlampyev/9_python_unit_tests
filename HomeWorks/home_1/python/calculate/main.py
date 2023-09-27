from calculate import Calculator


def main():
    calc = Calculator
    op_1 = 18
    op_2 = 9
    print(f"{op_1} + {op_2} = {calc.calculation(op_1, op_2, '+')}")
    print(f"{op_1} - {op_2} = {calc.calculation(op_1, op_2, '-')}")
    print(f"{op_1} * {op_2} = {calc.calculation(op_1, op_2, '*')}")
    print(f"{op_1} / {op_2} = {calc.calculation(op_1, op_2, '/')}")
    # print(f"{op_1} / {0} = {calc.calculation(op_1, 0, '/')}")
    print(f"Корень квадратный из {op_2} = {calc.square_root_extraction(op_2)}")
    price = 1000
    discount = 15
    print(f"При начальной стоимости {price}$ и скидке в {discount}% итоговая сумма будет "
          f"{calc.calculating_discount(price, discount)}$")


if __name__ == '__main__':
    main()
