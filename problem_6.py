import random
import sys


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if ints is None or len(ints) == 0:
        return (None, None)
    min = sys.maxsize
    max = -1

    for num in ints:
        if num < min:
            min = num
        if num > max:
            max = num
    return (min, max)


# Example Test Case of Ten Integers

# l = [i for i in range(0, 10)]  # a list containing 0 - 9
# random.shuffle(l)

# print("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

# Edge case
print(get_min_max([]))      # Should return (None, None)
print(get_min_max([1]))     # Should return (1, 1)
