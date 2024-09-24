"""The goal of this program is to practice breaking down and solving a big problem with multiple smaller functions. This program will help plan a tea party. """

__author__: str = "730715418"


# This is the big function callng each individual small function to accomplish the goal of this program
def main_planner(guests: int) -> None:
    """
    Calculates and prints the number of tea bags, treats, and the total cost based on the number of guests attending the tea party.

    """
    # printed statements for each of our calculated values
    print("A cozy tea party for " + str(guests) + " people")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )

    return None  # Nothing is returned because the results are printed


def tea_bags(people: int) -> int:
    """
    The purpose of this function is to calculate the number of tea bags needed for the tea party.

    We plan for each guest to drink 2 cups of tea so we need 2 tea bags per person

    """
    return people * 2  # Each person drinks two teas, requiring two tea bags.


def treats(people: int) -> int:
    """
    Calculate the number of treats based on how many expected cups of tea the guests will drink

    Each guest will get 1.5 treats per tea
    """

    return int(
        tea_bags(people=people) * 1.5
    )  # Multiplying the number of teas needed by 1.5 treats to get the number of treats needed


def cost(tea_count: int, treat_count: int) -> float:
    """
    Calculate the total cost of tea bags and treats for the tea party.
    Each tea bag costs $0.50 and each treat costs $0.75
    """

    return (tea_count * 0.50) + (treat_count * 0.75)  # Equation for the total cost


# Making the program runnable

if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
