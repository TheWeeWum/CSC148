from typing import Union, List, Optional


def nested_sum(obj: Union[int, List]) -> int:
    """
    >>> nested_list = [[0, -1, 0], -2, [[-3, [-5], -7]], 5, -5, [-7, -1]]
    >>> nested_sum(nested_list)
    -26
    """
    if isinstance(obj, int):
        return obj
    else:
        total = 0
        for thing in obj:
            total += nested_sum(thing)
        return total


def flatten(obj: Union[int, List]) -> List[int]:
    """
    >>> nested_list = [[0, -1, 0], -2, [[-3, [-5], -7]], 5, -5, [-7, -1]]
    >>> flatten(nested_list)
    [0, -1, 0, -2, -3, -5, -7, 5, -5, -7, -1]
    """
    if isinstance(obj, int):
        return [obj]
    else:
        return_list = []
        for thing in obj:
            return_list += flatten(thing)
        return return_list


def uniques(obj: Union[int, List]) -> List[int]:
    """
    >>> nested_list = [[0, -1, 0], -2, [[-3, [-5], -7]], 5, -5, [-7, -1]]
    >>> uniques(nested_list)
    [0, -1, -2, -3, -5, -7, 5]
    """
    if isinstance(obj, int):
        return [obj]
    else:
        s = []
        for thing in obj:
            lst = flatten(thing)
            for each in lst:
                if each not in s:
                    s += [each]
        return s


def longest_run(obj: Union[int, List]) -> int:
    """
    >>> nested_list = [[0, -1, 0], -2, [[-3, [-5], -7], 5, -5], [-7, -1]]
    >>> longest_run(nested_list)
    4
    >>> nested_list = [[0, -1, 0], -2, [-3, [-5], -7, 5, -5], [-7, -1]]
    >>> longest_run(nested_list)
    5
    """
    if isinstance(obj, int):
        return 1
    else:
        longest = len(obj)
        for thing in obj:
            long = longest_run(thing)
            if long > longest:
                longest = long
        return longest


def flatten_string(obj: Union[str, List]) -> str:
    """
    >>> string = ["he", "ll", "o", [[" "], "wo", "rl"], "d", [["!"]]]
    >>> flatten_string(string)
    'hello world!'
    """
    if isinstance(obj, str):
        return obj
    else:
        s = ""
        for thing in obj:
            s += flatten_string(thing)
        return s


def nested_list_contains(obj: Union[int, List], item: int) -> bool:
    """
    >>> nested_list_contains(5, 5)
    True
    >>> nested_list_contains(5, 4)
    False
    >>> nested_list_contains([5], 5)
    True
    >>> nested_list_contains([5], 4)
    False
    >>> nested_list_contains([5, 6, [9, 14, [4], 5, [[100]]], 90], 100)
    True
    >>> nested_list_contains([5, 6, [9, 14, [4], 5, [[100]]], 90], 85)
    False
    >>> nested_list_contains([], 10)
    False
    """
    if isinstance(obj, int):
        return obj == item
    else:
        for thing in obj:
            ans = nested_list_contains(thing, item)
            if ans:
                return True
        return False


def deepest(obj: Union[int, List]) -> int:
    """
    >>> deepest([])
    1
    >>> deepest(5)
    0
    >>> deepest([5, 43, [6, [4], [[4]]]])
    4
    >>> deepest([[[[[[[[[[]]]]]]]]]])
    10
    >>> deepest([[[[]]], [[[[[[[]]]]]]], []])
    8
    """

    if isinstance(obj, int):
        return 0
    else:
        deeper = 1
        for thing in obj:
            depth = deepest(thing) + 1
            if depth > deeper:
                deeper = depth
        return deeper


def first_at_depth(obj: Union[int, List], d: int) -> Optional[int]:
    """
    >>> first_at_depth(5, 0)
    5
    >>> first_at_depth([4], 1)
    4
    >>> first_at_depth([4, 5, [3, 3], [5, [10]]], 3)
    10
    >>> assert first_at_depth([], 1) is None
    >>> assert first_at_depth(5, 5) is None
    >>> assert first_at_depth([4, 5, [3, 3], [5, [10]]], 5) is None
    >>> first_at_depth([5, 6, [[5, 4, 2], [5, 2, 4]]], 2)
    >>> first_at_depth([5, 6, [[5, 4, 2], [5, 2, 4], 89]], 2)
    89
    >>> first_at_depth([1, 2, 3, 4], 1)
    1

    """
    if d == 0:
        if isinstance(obj, int):
            return obj
        else:
            return None
    elif isinstance(obj, int):
        return None
    else:
        for thing in obj:
            ans = first_at_depth(thing, d-1)
            if isinstance(ans, int):
                return ans
        return None


def add_one(obj: Union[int, List]) -> None:
    """
    >>> lst = [4]
    >>> add_one(lst)
    >>> lst == [5]
    True
    >>> lst = []
    >>> add_one(lst)
    >>> lst == []
    True
    >>> lst = 5
    >>> add_one(lst)
    >>> lst == 5
    True
    >>> lst = [5, 23, 4, [5, 2, [5], 4], [3, 4], 1]
    >>> add_one(lst)
    >>> lst == [6, 24, 5, [6, 3, [6], 5], [4, 5], 2]
    True
    """
    if isinstance(obj, int):
        return None
    else:
        for i in range(len(obj)):
            if isinstance(obj[i], int):
                obj[i] += 1
            else:
                add_one(obj[i])


def factorial(num: int) -> int:
    """
    >>> factorial(5)
    120
    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(2)
    2
    """
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)


def fibonacci(num: int) -> int:
    """
    # [0, 1, 1, 2, 3, 5, 8, 13]
    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(3)
    2
    >>> fibonacci(6)
    8
    """
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


def sum_series(num: int) -> int:
    """
    >>> sum_series(0)
    0
    >>> sum_series(2)
    2
    >>> sum_series(6)
    12
    >>> sum_series(7)
    15
    """
    if num <= 0:
        return num
    else:
        return num + sum_series(num - 2)


def sum_harmonic(num):
    """
    >>> assert sum_harmonic(5) == 11/6 + 1/4 + 1/5
    >>> assert sum_harmonic(3) == 11/6
    >>> sum_harmonic(1)
    1
    """
    if num == 1:
        return 1
    else:
        return 1/num + sum_harmonic(num-1)


def power(a, b):
    """
    >>> power(1, 100)
    1
    >>> power(5, 3)
    125
    >>> power(100, 0)
    1
    >>> power(2, 6)
    64
    """
    if b == 0:
        return 1
    else:
        return a * power(a, b-1)


def greatest_common_divisor(a, b):
    """
    >>> greatest_common_divisor(5, 6)
    1
    >>> greatest_common_divisor(100, 20)
    20
    >>> greatest_common_divisor(60, 18)
    6
    """
    large = max(a, b)
    small = min(a, b)
    if a % b == 0:
        return small
    else:
        return greatest_common_divisor(small, large-small)


def proper_gcd(a, b):
    """
    >>> greatest_common_divisor(5, 6)
    1
    >>> greatest_common_divisor(100, 20)
    20
    >>> greatest_common_divisor(60, 18)
    6
    """
    low = min(a, b)
    high = max(a, b)

    if low == 0:
        return high
    elif low == 1:
        return 1
    else:
        return proper_gcd(low, high % low)


def buyable(n: int) -> List[int]:
    """
    25, 6, 4
    >>> buyable(5)
    []
    >>> buyable(25)
    [25]
    >>> buyable(10)
    [6, 4]
    >>> buyable(156)
    [25, 25, 25, 25, 25, 25, 6]
    >>> buyable(35)
    [25, 6, 4]
    """
    if n == 25 or n == 6 or n == 4:
        return [n]
    elif n < 4:
        return []
    else:
        if n > 25:
            return [25] + buyable(n - 25)
        elif n > 6:
            return [6] + buyable(n - 6)
        elif n < 4:
            return [4] + buyable(n - 4)
        else:
            return []


def get_ith_item(obj: Union[int, List], i: int) -> Union[str, int]:
    """
    >>> get_ith_item('5', 0)
    '5'
    >>> get_ith_item(['5'], 0)
    '5'
    >>> get_ith_item([[], '4', [[], '4']], 0)
    '4'
    >>> get_ith_item([[], [[], '4']], 0)
    '4'
    >>> get_ith_item(['5', '6', [['4']]], 2)
    '4'
    >>> get_ith_item(['5', '6', [['4']]], 3)
    3
    >>> get_ith_item(['5', [['5'], '4'], '2'], 3)
    '2'
    >>> get_ith_item(['5', '24', '5', '2', [['5', '3'], '4', '5'], '2'], 5)
    '3'
    """
    if i == 0:
        if isinstance(obj, str):
            return obj
        else:
            for thing in obj:
                ans = get_ith_item(thing, 0)
                if isinstance(ans, str):
                    return ans
            return 0
    else:
        index = i
        counter = 0
        for thing in obj:
            if isinstance(thing, str):
                counter += 1
                if index == 0:
                    return thing
                index -= 1
            else:
                temp = get_ith_item(thing, index)
                if isinstance(temp, int):
                    index = temp
                else:
                    return temp

    return index


def sum_nested(obj: Union[int, List]):
    """
    >>> sum_nested([5, 2, 5, 6,])
    18
    >>> sum_nested(5)
    5
    >>> sum_nested([1, 4, [5, [4], [5, 1]], 4])
    24
    """
    if isinstance(obj, int):
        return obj
    else:
        return sum([sum_nested(nested_sum(obj))])


def flatten_comp(obj: Union[int, List]):
    """
    >>> nested_list = [[0, -1, 0], -2, [[-3, [-5], -7]], 5, -5, [-7, -1]]
    >>> flatten_comp(nested_list)
    [0, -1, 0, -2, -3, -5, -7, 5, -5, -7, -1]
    """
    if isinstance(obj, int):
        return [obj]

    else:
        return sum(obj, [])

