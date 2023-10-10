from controller import Controller


class Interface:

    @staticmethod
    def greeting() -> str:
        print("Добро пожаловать в калькулятор")
        print("Для выхода введите '0' или введите ваше выражение")
        task = input("Что считаем: ")
        return task

    @staticmethod
    def answer(task, answer) -> None:
        print(f"{task} = {answer}")
