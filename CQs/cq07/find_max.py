__author__: str = "730715418"


def find_and_remove_max(input: list[int]) -> int:
    if not input:
        return -1

    max_val: int = max(input)

    while max_val in input:
        input.remove(max_val)

    return max_val
