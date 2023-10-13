from controller import Controller


def main():
    controller = Controller(3)  # в скобках - количество списков
    controller.entry()
    controller.calculate_average()
    controller.print_calculating_average()
    controller.print_comparison_result()


if __name__ == "__main__":
    main()
