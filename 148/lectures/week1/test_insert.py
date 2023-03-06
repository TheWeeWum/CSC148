"""CSC148 Lab 1

=== CSC148 Winter 2023 ===
Department of Computer Science,
University of Toronto

=== Module description ===
This module illustrates a simple unit test for our binary_search function.
"""
from number_insert import insert_after


def test_not_in_list() -> None:
    """Simple test for binary_search."""
    assert insert_after([0, 1, 2], 4, 2) == [0, 1, 2]


def test_insert_at_front() -> None:
    """Simple test for binary_search."""
    assert insert_after([0, 1, 2], 0, 2) == [0, 2, 1, 2]


# def test_n1_same_as_n2() -> None:
#     """Simple test for binary_search."""
#     assert insert_after([0, 1, 2], 2, 2) == [0, 1, 2, 2]


if __name__ == '__main__':
    import pytest
    pytest.main(['test_search.py'])
