from interface import Interface


class TerminalInterface(Interface):

    def input_list(self) -> list[int]:
        lst = map(int, input("Введите список целых чисел через пробел").split())
        return lst

    def print_list(self, lst) -> None:
        print(lst)


