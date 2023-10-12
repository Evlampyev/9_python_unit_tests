from controller import Controller
from interface import Interface


def main():
    interface = Interface()
    while (task := interface.greeting()) != '0':
        control = Controller(task)
        interface.answer(task, control.answer[0])


if __name__ == "__main__":
    main()
