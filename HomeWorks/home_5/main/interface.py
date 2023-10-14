from abc import ABC


class Interface(ABC):
    """
    Абстрактный интерфейс для реализации вывода - ввода данных
    """

    @staticmethod
    def input_list() -> list[int]:
        """
        Получение списка целых чисел
        :return: list[int]
        """
        pass

    @staticmethod
    def print_data(data) -> None:
        """Вывод данных"""
        pass
