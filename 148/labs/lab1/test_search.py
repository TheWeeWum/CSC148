"""CSC148 Lab 1

=== CSC148 Winter 2023 ===
Department of Computer Science,
University of Toronto

=== Module description ===
This module illustrates a simple unit test for our binary_search function.
"""
from search import binary_search


def test_search() -> None:
    """Simple test for binary_search."""
    assert binary_search([0, 5, 10, 15, 20, 25, 30, 35, 40], 5) == 1


def test_single() -> None:
    """Simple test for binary_search."""
    assert binary_search([1], 1) == 0


def test_single_false() -> None:
    """Simple test for binary_search."""
    assert binary_search([2], 3) == -1


def test_empty() -> None:
    """Simple test for binary_search."""
    assert binary_search([], 3) == -1


def test_out_of_bounds_left() -> None:
    """Simple test for binary_search."""
    assert binary_search([2, 3, 4, 5], 1) == -1


def test_middle_num() -> None:
    """Simple test for binary_search."""
    assert binary_search([2, 3, 4, 5, 6], 5) == 3


def test_last_num() -> None:
    """Simple test for binary_search."""
    assert binary_search([2, 3, 4, 5, 6], 5) == 3


def test_out_of_bounds_right() -> None:
    """Simple test for binary_search."""
    assert binary_search([2, 3, 4, 5], 6) == -1


def test_non_existent() -> None:
    """Simple test for binary_search."""
    assert binary_search([2, 3, 5, 6], 4) == -1


def test_multiple() -> None:
    """Simple test for binary_search."""
    assert binary_search([2, 2, 3, 4, 4, 5, 6, 7, 7, 7], 4) == 3 or 4

# BRUV why is this not allowed??? makes so much easier to test. ;-; T_T :(
# def test_all_in_list() -> None:
#     """Tests to make sure every index of the array is searched"""
#     lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#     for i in range(10):
#         assert binary_search(lst, i) == i


def test_last() -> None:
    """Tests last in list"""
    assert binary_search([2, 2, 3, 4, 4, 5, 6, 7, 7, 8], 8) == 9


def test_middle() -> None:
    """Tests middle of list"""
    assert binary_search([1, 2, 3], 2) == 1


def test_empty() -> None:
    assert binary_search([], 1) == -1

if __name__ == '__main__':
    import pytest
    pytest.main(['test_search.py'])
