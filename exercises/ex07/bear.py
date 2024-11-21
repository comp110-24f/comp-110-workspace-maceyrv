__author__: str = "730715418"

"""File to define Bear class."""


class Bear:

    def __init__(self):
        self.age = 0
        self.hunger_score = 0  # The bear starts with a hunger score of 0

    def one_day(self):
        """Increase the bear's age and decrease hunger score by 1 every day."""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int):
        """Increase the bear's hunger score by num_fish."""
        self.hunger_score += num_fish
