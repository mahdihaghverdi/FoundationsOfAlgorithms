from string import digits

from algorithms import binsearch


def test_binsearch():
    # int
    numbers = list(range(1, 1025))
    assert binsearch(1, numbers)
    assert binsearch(1024, numbers)
    assert not binsearch(2000, numbers)

    # str
    assert binsearch("1", digits)
    assert binsearch("8", digits)
    assert not binsearch("10", digits)

    # bool
    assert binsearch(True, sorted([True, True, False, True]))
    assert not binsearch(False, sorted([True, True, True]))
