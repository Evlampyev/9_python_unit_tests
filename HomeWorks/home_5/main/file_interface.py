from interface import Interface
from random import randint
from datetime import datetime


class FileInterface(Interface):

    def __init__(self):
        with open('HomeWorks/home_5/main/log_file.txt', 'a') as f:
            f.write(f"--- Новая задача в {datetime.now()} ---\n")

    @staticmethod
    def input_list() -> list[int]:
        size = randint(3, 10)
        lst = []
        for i in range(size):
            lst.append(randint(1, 10))
        with open('HomeWorks/home_5/main/log_file.txt', 'a') as f:
            f.write(f"Сгенерированный список: {lst} \n")
        return lst

    @staticmethod
    def print_data(data) -> None:
        with open('HomeWorks/home_5/main/log_file.txt', 'a') as f:
            f.write(f"{data} \n")
