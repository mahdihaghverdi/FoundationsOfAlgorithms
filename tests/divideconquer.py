import random
import string
from string import digits

from algorithms import binsearch, mergesort


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


def test_mergesort():
    fracs = [random.random() for _ in range(2048)]
    ints = [random.randint(3, 4573) for _ in range(2048)]
    strs = "".join(
        "".join(random.choices(string.ascii_letters, k=random.randint(3, 50)))
        for _ in range(50)
    )
    assert mergesort(fracs) == sorted(fracs)
    assert mergesort(ints) == sorted(ints)
    assert mergesort(strs) == sorted(strs)
