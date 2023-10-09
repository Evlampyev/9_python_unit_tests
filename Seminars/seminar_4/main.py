from random_number import RandomNumber
from max_element import MaxNumber


def main():
    new_lst = RandomNumber(10)
    new_lst.create_lst()
    print(new_lst.lst)
    maximus = MaxNumber().find_max_number(new_lst.lst)
    print(f"Максимальный элемент списка - {maximus}")



if __name__ == "__main__":
    main()
