class MaxNumber:
    @staticmethod
    def find_max_number(lst: list) -> int:
        if len(lst) == 0:
            raise Exception('No elements in list')
        else:
            max_number = lst[0]
            for i in range(1, len(lst)):
                if lst[i] > max_number:
                    max_number = lst[i]
            return max_number
