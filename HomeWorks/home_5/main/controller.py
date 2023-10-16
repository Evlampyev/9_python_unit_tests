from int_list import IntList
from teminal_interface import TerminalInterface as MyInterface
# from file_interface import FileInterface as MyInterface


# Реализована возможность переключения интерфейса:
# teminal_interface - терминал
# file_interface - в файл log_file

class Controller:
    """
    Организация работы приложения
    """
    def __init__(self, size):
        self.lists = []
        self.averages = []
        for _ in range(size):
            self.lists.append(IntList())
        self.my_interface = MyInterface()

    def entry(self):
        """
        Организация ввода списков
        :return:
        """
        for my_list in self.lists:
            my_list.setter_int_list(self.my_interface.input_list())

    def calculate_average(self):
        """
        Организация вычисления среднего значения списка
        :return:
        """
        for my_list in self.lists:
            my_list.average_value_of_list()
            self.averages.append(my_list.average_value)

    def print_calculating_average(self):
        """
        Организация вывода промежуточного результата
        :return: Для списка {} среднее значение равно {}
        """
        for i, my_list in enumerate(self.lists):
            text = f"Для списка {i + 1} среднее значение равно {my_list.average_value}"
            self.my_interface.print_data(text)

    def print_comparison_result(self):
        """
        Вычисление списка с большим средним значением и организация вывода конечного результата
        :return: Среднее значение списка(ов) {}, больше чем {}
        """
        size = len(self.averages)
        largest = max(self.averages)
        list_largest = []
        list_others = []
        for i, average in enumerate(self.averages):
            if average == largest:
                list_largest.append(i + 1)
            else:
                list_others.append(i + 1)
        if size == len(list_largest):
            text = "Средние значения списков равны"
        else:
            text = f"Среднее значение списка(ов) {list_largest}, больше чем {list_others}"
        MyInterface.print_data(text)
