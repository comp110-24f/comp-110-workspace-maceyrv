__author__ = "730715418"

"""visualizing the coordinate pairs"""


# Import the concat function from concatenation.py
from concatenation import concat

# Import the get_coords function from coordinates.py
from coordinates import get_coords

# Global variables
x = "123"
y = "abc"

# Call concat using x and y and print the result
print(concat(x, y))

# Call get_coords using x and y
get_coords(x, y)