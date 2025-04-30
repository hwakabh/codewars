from unittest import TestCase
from unittest import main

from .halving_sum import halving_sum


class TestHalvingSum(TestCase):
    def test_halving_sum(self):
        ptr = [
            (25, 47),
            (127, 247),
        ]
        for inp, exp in ptr:
            with self.subTest(inp=inp, exp=exp):
                self.assertEqual(halving_sum(n=inp), exp)


if __name__ == "__main__":
    main(verbosity=2)
