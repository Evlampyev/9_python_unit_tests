from random import randint


class RandomNumber:

    def __init__(self, size):
        self.lst = []
        self.size = size

    def create_lst(self):
        if self.size > 0:
            self.lst = [randint(1, 100) for i in range(self.size)]

    def get_lst(self):
        return self.lst


