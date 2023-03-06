"""Lab 7: Recursion

=== CSC148 Winter 2022 ===
Department of Computer Science,
University of Toronto

=== Module Description ===
This module contains a few nested list functions for you to practice recursion.
"""
from typing import Union, List


def greater_than_all(obj: Union[int, List], n: int) -> bool:
    """Return True iff there is no int in <obj> that is larger than or
    equal to <n> (or, equivalently, <n> is greater than all ints in <obj>).

    >>> greater_than_all(10, 3)
    False
    >>> greater_than_all([1, 2, [1, 2], 4], 10)
    True
    >>> greater_than_all([], 0)
    True
    """
    if isinstance(obj, int):
        return obj < n
    else:
        for thing in obj:
            if not greater_than_all(thing, n):
                return False
        return True


def add_n(obj: Union[int, List], n: int) -> Union[int, List]:
    """Return a new nested list where <n> is added to every item in <obj>.

    >>> add_n(10, 3)
    13
    >>> add_n([1, 2, [1, 2], 4], 10)
    [11, 12, [11, 12], 14]
    >>> add_n([5, [4, [], [4, 2]], 6, [4]], 10)
    [15, [14, [], [14, 12]], 16, [14]]
    """
    """
    # should it be this /\ or this \/
    [15, [14, [10], [14, 12]], 16, [14]]
    """
    if isinstance(obj, int):
        return obj + n
    else:
        lst = []
        for i in range(len(obj)):
            if isinstance(obj[i], int):
                obj[i] += n
                lst += [obj[i]]
            else:
                lst.append(add_n(obj[i], n))
        return lst


def nested_list_equal(obj1: Union[int, List], obj2: Union[int, List]) -> bool:
    """Return whether two nested lists are equal, i.e., have the same value.

    Note: order matters.
    You should only use == in the base case. Do NOT use it to compare
    otherwise (as that defeats the purpose of this exercise)!

    >>> nested_list_equal(17, [1, 2, 3])
    False
    >>> nested_list_equal([1, 2, [1, 2], 4], [1, 2, [1, 2], 4])
    True
    >>> nested_list_equal([1, 2, [1, 2], 4], [4, 2, [2, 1], 3])
    False
    >>> nested_list_equal(16, 16)
    True
    """
    # HINT: You'll need to modify the basic pattern to loop over indexes,
    # so that you can iterate through both obj1 and obj2 in parallel.

    if isinstance(obj1, int) or isinstance(obj2, int):
        return obj1 == obj2
    elif len(obj1) != len(obj2):
        return False
    else:
        for i in range(len(obj1)):
            if not nested_list_equal(obj1[i], obj2[i]):
                return False
        return True


def duplicate(obj: Union[int, List]) -> Union[int, List]:
    """Return a new nested list with all numbers in <obj> duplicated.

    Each integer in <obj> should appear twice *consecutively* in the
    output nested list. The nesting structure is the same as the input,
    only with some new numbers added. See doctest examples for details.

    If <obj> is an int, return a list containing two copies of it.

    >>> duplicate(1)
    [1, 1]
    >>> duplicate([])
    []
    >>> duplicate([1, 2])
    [1, 1, 2, 2]
    >>> duplicate([1, [2, 3]])  # NOT [1, 1, [2, 2, 3, 3], [2, 2, 3, 3]]
    [1, 1, [2, 2, 3, 3]]
    >>> duplicate([5, 6, [5, [4], [3, 4], 5]])
    [5, 5, 6, 6, [5, 5, [4, 4], [3, 3, 4, 4], 5, 5]]
    """
    # HINT: in the recursive case, you'll need to distinguish between
    # a <sublist> that is an int and a <sublist> that is a list
    # (put an isinstance check inside the loop).

    if isinstance(obj, int):
        return [obj, obj]
    else:
        lst = []
        for i in range(len(obj)):
            if isinstance(obj[i], int):
                lst += [obj[i], obj[i]]
            else:
                lst.append(duplicate(obj[i]))
        return lst


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    # import python_ta
    # python_ta.check_all()
