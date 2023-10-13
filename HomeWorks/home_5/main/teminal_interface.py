from interface import Interface


class TerminalInterface(Interface):

    @staticmethod
    def input_list() -> list[int]:
        lst = list(map(int, input("Введите список целых чисел через пробел: ").split()))
        return lst

    @staticmethod
    def print_data(data) -> None:
        print(data)
