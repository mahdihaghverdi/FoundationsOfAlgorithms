from collections.abc import Sequence
from typing import TypeVar

T = TypeVar("T", str, int, bool)


def binsearch(what: T, sequence: Sequence[T]) -> bool:
    """Recursive binary search"""

    def _binsearch(low: int, high: int) -> bool:
        if low > high:
            return False
        middle_index = (high + low) // 2

        try:
            middle_item = sequence[middle_index]
        except IndexError:
            return False

        if what < middle_item:
            return _binsearch(low=low, high=middle_index - 1)
        if what > middle_item:
            return _binsearch(low=middle_index + 1, high=high)
        return what == middle_item

    return _binsearch(low=0, high=len(sequence))


def mergesort(sequence: Sequence) -> list:
    """Mergesort a sequence"""

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

    seq_len = len(sequence)
    if seq_len < 2:
        return list(sequence)
    left, right = sequence[: seq_len // 2], sequence[seq_len // 2:]
    left = mergesort(left)
    right = mergesort(right)
    return merge()
