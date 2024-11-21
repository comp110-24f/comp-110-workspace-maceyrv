__author__: str = "730715418"

import pytest
from utils import only_evens, sub, add_at_index


# only_evens
def test_only_evens_evenand_odd() -> None:
    """Test with evens and odds."""
    assert only_evens([1, 2, 3, 4]) == [2, 4]


def test_only_evens_only_odds() -> None:
    """Test with all odd numbers."""
    assert only_evens([1, 3, 5]) == []


def test_only_evens_empty() -> None:
    """Test with an empty list."""
    assert only_evens([]) == []


# sub
def test_sub_true_subset() -> None:
    """Test a typical use case for sub."""
    assert sub([10, 20, 30, 40], 1, 3) == [20, 30]


def test_sub_empty() -> None:
    """Test sub on an empty list."""
    assert sub([], 0, 3) == []


def test_sub_out_of_bounds() -> None:
    """Test sub with start and end indices out of bounds."""
    assert sub([10, 20, 30], -5, 5) == [10, 20, 30]


# add_at_index
def test_add_at_index_use_case() -> None:
    """Test typical case for add_at_index."""
    input = [1, 2, 3]
    add_at_index(input, 4, 2)
    assert input == [1, 2, 4, 3]


def test_add_at_index_empty() -> None:
    """Test adding to an empty list."""
    input = []
    add_at_index(input, 1, 0)
    assert input == [1]


def test_add_at_index_raises_indexerror() -> None:
    """Test add_at_index raises IndexError when index is out of bounds."""
    input = [1, 2, 3]
    with pytest.raises(IndexError):
        add_at_index(input, 4, 5)
