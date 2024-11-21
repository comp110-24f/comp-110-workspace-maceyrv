__author__: str = "730715418"


def only_evens(input: list[int]) -> list[int]:
    """Return a list of even numbers from the input list."""
    result = []
    for num in input:
        if num % 2 == 0:
            result.append(num)
    return result


def sub(input: list[int], start: int, end: int) -> list[int]:
    """Return a sublist from start index to end index (not inclusive)."""
    result = []

    if len(input) == 0 or start >= len(input) or end <= 0:
        return result

    if start < 0:
        start = 0
    if end > len(input):
        end = len(input)

    for i in range(start, end):
        result.append(input[i])

    return result


def add_at_index(input: list[int], element: int, index: int) -> None:
    """Insert an element at the specified index in the list."""
    if index < 0 or index > len(input):
        raise IndexError("Index is out of bounds for the input list")

    input.append(0)  # Add space at the end of the list.

    for i in range(len(input) - 1, index, -1):
        input[i] = input[i - 1]  # Shift elements to the right.

    input[index] = element
