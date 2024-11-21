__author__: str = "730715418"

"""Mutating functions."""

def manual_append(lst: list[int], value: int) -> None:
    lst.append(value)

def double(lst: list[int]) -> None:
    i: int = 0
    while i < len(lst):
        lst[i] *= 2
        i += 1
    
# Global variables
list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

# Call the double function
double(list_2)

# Print statements
print("list_1:", list_1)
print("list_2:", list_2)
