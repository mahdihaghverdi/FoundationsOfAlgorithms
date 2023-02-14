from typing import Sequence


def binsearch(what, sequence: Sequence) -> bool:
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
