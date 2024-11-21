__author__ = "730715418"

"""print formatted pairs of characters from two strings"""


# Define the get_coords function
def get_coords(xs: str, ys: str) -> None:
    i = 0
    while i < len(xs):
        j = 0
        while j < len(ys):
            # Print the formatted coordinate pair
            print(xs[i], ys[j])
            j += 1
        i += 1

