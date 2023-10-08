class Book:
    def __init__(self, id_num, title, author):
        self.id = id_num
        self.title = title
        self.author = author

    def get_id(self) -> int:
        """getter method"""
        return self.id

    def set_id(self, value: int) -> None:
        """setter method"""
        self.id = value

    def get_title(self):
        return self.title

    def set_title(self, value):
        self.title = value

    def egt_author(self):
        return self.author

    def set_author(self, value):
        self.author = value
