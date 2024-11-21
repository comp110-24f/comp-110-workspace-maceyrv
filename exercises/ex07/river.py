__author__: str = "730715418"

"""File to define River class."""

from fish import Fish
from bear import Bear


class River:

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Remove Fish older than 3 and Bears older than 5."""

        # Create new lists to store animals that are not too old
        self.fish = [fish for fish in self.fish if fish.age <= 3]
        self.bears = [bear for bear in self.bears if bear.age <= 5]

    def remove_fish(self, amount: int):
        """Remove certain amount of fish from the front of the river"""
        for _ in range(amount):
            if self.fish:
                self.fish.pop(0)

    def bears_eating(self):
        """Each bear will eat 3 fish if there are at least 5 fish in the river."""
        for bear in self.bears:
            if len(self.fish) >= 5:  # If there are at least 5 fish in the river
                self.remove_fish(3)  # Remove 3 fish from the river
                bear.eat(3)  # Bear eats 3 fish and increases hunger score

    def check_hunger(self):
        """Check the hunger_score of every Bear and remove them if they are starving."""
        # Create a new list for surviving bears
        self.bears = [bear for bear in self.bears if bear.hunger_score >= 0]

    def repopulate_fish(self):
        """Each pair of Fish will produce 4 offspring."""
        num_new_fish = len(self.fish) // 2
        for _ in range(num_new_fish * 4):
            self.fish.append(Fish())  # Add new fish to the river

    def repopulate_bears(self):
        """Each pair of Bears will produce 1 offspring."""
        num_new_bears = len(self.bears) // 2  # Each pair produces one new bear
        for _ in range(num_new_bears):
            self.bears.append(Bear())  # Add new bears to the river

    def view_river(self):
        """Print the current status of the river"""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulate one week (7 days) of life in the river"""
        for _ in range(7):
            self.one_river_day()
