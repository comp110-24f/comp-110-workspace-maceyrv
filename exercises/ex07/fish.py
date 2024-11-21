__author__: str = "730715418"

"""File to define Fish class."""


class Fish:

    def __init__(self):
        self.age = 0

    def one_day(self):
        """Increase the age of the fish by 1 each day."""
        self.age += 1
