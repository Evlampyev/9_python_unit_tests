class IntList:

    def __init__(self):
        self.average_value = None
        self.int_list = []

    def getter_int_list(self):
        return self.int_list

    def setter_int_list(self, value):
        self.int_list = value

    def average_value_of_list(self):
        amount = sum(self.int_list)
        length = len(self.int_list)
        self.average_value = round(amount / length, 3)

    def __str__(self):
        return " ".join(map(str, self.int_list))
