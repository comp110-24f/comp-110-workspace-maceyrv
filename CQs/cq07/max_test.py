__author__: str = "730715418"

from find_max import find_and_remove_max


def test_find_and_remove_max_return_norm() -> None:
    input: list[int] = [5, 3, 9, 1, 9]
    result = find_and_remove_max(input)
    assert result == 9
    assert input == [5, 3, 1]


def test_find_and_remove_empty() -> None:
    input: list[int] = []
    result = find_and_remove_max(input)
    assert result == -1
    assert input == []


def test_edge_case_unconventional() -> None:
    lst: list[int] = [5, 5, 5, 5]
    result = find_and_remove_max(lst)
    assert result == 5
    assert lst == []
