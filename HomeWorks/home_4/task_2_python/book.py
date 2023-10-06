class Book:
    def __init__(self, id_num, title, author):
        self.id = id_num
        self.title = title
        self.author = author

    @property
    def id(self) -> int:
        """getter method"""
        return self.id

    @id.setter
    def id(self, value: int) -> None:
        """setter method"""
        self._id = value

    @property
    def title(self):
        return self.title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def author(self):
        return self.author

    @author.setter
    def author(self, value):
        self.author = value
