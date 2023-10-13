from abc import ABC


class Interface(ABC):
    def input_list(self) -> list[int]:
        """
        Получение списка целых чисел
        :return: list[int]
        """
        pass

    def print_list(self, lst) -> None:
        """Вывод списка"""
        pass

    def print_compare_two_list(self, result):
        pass
