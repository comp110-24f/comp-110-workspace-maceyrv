def get_first(input: list[str]) -> str:
    """Return first element"""
    return input[0]

# remove_first: takes a list[str] and removes first element
def remove_first(input: list[str]) -> None:
    """Remove first element"""
    input.pop(0) 

# get_and_remove_first: takes a list[str] as input and returns +removes
def get_and_remove_first(input: list[str]) -> str:
    """Remove AND return first element"""
    first_elem: str = input[0]
    input.pop(0) #remove first_elem
    return first_elem