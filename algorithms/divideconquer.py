import random
import string
from collections.abc import Sequence
from typing import TypeVar, Iterable

T = TypeVar("T", str, int, bool)


def binsearch(what: T, iterable: Iterable[T]) -> bool:
    """Recursive binary search"""

    _iterable = list(iterable)

    def _binsearch(low: int, high: int) -> bool:
        if low > high:
            return False
        middle_index = (high + low) // 2

        try:
            middle_item = _iterable[middle_index]
        except IndexError:
            return False

        if what < middle_item:
            return _binsearch(low=low, high=middle_index - 1)
        if what > middle_item:
            return _binsearch(low=middle_index + 1, high=high)
        return what == middle_item

    return _binsearch(low=0, high=len(_iterable))


def mergesort(iterable: Iterable) -> list:
    """Mergesort a sequence"""

    _iterable = list(iterable)

    def merge():
        if len(left) == 0:
            return right

        if len(right) == 0:
            return left

        result = []
        index_left = index_right = 0
        while len(result) < len(left) + len(right):
            if left[index_left] <= right[index_right]:
                result.append(left[index_left])
                index_left += 1
            else:
                result.append(right[index_right])
                index_right += 1

            if index_right == len(right):
                result += left[index_left:]
                break
            if index_left == len(left):
                result += right[index_right:]
                break
        return result

    seq_len = len(_iterable)
    if seq_len < 2:
        return _iterable
    left, right = _iterable[: seq_len // 2], _iterable[seq_len // 2:]
    left = mergesort(left)
    right = mergesort(right)
    return merge()


# TODO: Write a parallel version of mergesort using multiprocessing


def quicksort(iterable: Iterable) -> list:
    iterable = list(iterable)
    if len(iterable) < 2:
        return iterable

    low, same, high = [], [], []
    pivot = iterable[random.randrange(0, len(iterable))]
    for item in iterable:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        else:
            high.append(item)

    return quicksort(low) + same + quicksort(high)


# TODO: Write a parallel version of mergesort using multiprocessing
