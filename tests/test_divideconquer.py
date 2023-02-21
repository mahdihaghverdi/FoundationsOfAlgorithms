import pathlib
import random
import string
import sys
from string import digits

sys.path.append(str(pathlib.Path(__file__).parent.parent))

from algorithms import binsearch, mergesort, quicksort  # noqa


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
    assert not binsearch(False, [True, True, True])


class TestSorts:
    @classmethod
    def setup_class(cls):
        cls.fracs = [random.randint(-1024, 1024) + random.random() for _ in range(2048)]
        cls.fracs_sorted = sorted(cls.fracs)  # noqa
        cls.ints = [random.randint(-764, 4573) for _ in range(2048)]
        cls.ints_sorted = sorted(cls.ints)  # noqa
        cls.strs = "".join(
            "".join(random.choices(string.ascii_letters, k=random.randint(3, 50)))
            for _ in range(2048)
        )
        cls.strs_sorted = sorted(cls.strs)  # noqa
        cls.bools = [random.choice([True, False]) for _ in range(2048)]
        cls.bools_sorted = sorted(cls.bools)  # noqa

    def test_mergesort(self):
        assert mergesort(self.fracs) == self.fracs_sorted
        assert mergesort(self.ints) == self.ints_sorted
        assert mergesort(self.strs) == self.strs_sorted
        assert mergesort(self.bools) == self.bools_sorted

    def test_quicksort(self):
        assert quicksort(self.fracs) == self.fracs_sorted
        assert quicksort(self.ints) == self.ints_sorted
        assert quicksort(self.strs) == self.strs_sorted
        assert quicksort(self.bools) == self.bools_sorted
