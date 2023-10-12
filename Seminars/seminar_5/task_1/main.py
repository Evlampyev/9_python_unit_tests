def main(lst: list):
    if isinstance(lst, list):
        return sum(lst) / len(lst)
    else:
        raise TypeError


if __name__ == "__main__":
    lst = [1, 12, 3, 5, 6, 7, 8, 9]
    main(lst)
