from unittest import TestCase
from unittest import main

from .sum_of_positive import positive_sum


class TestSumOfPositive(TestCase):
    def test_positive_sum(self):
        ptr = [
            ([1, 2, 3, 4, 5], 15),
            ([1, -2, 3, 4, 5], 13),
            ([-1, 2, 3, 4, -5], 9),
            ([], 0),
            ([-1, -2, -3, -4, -5], 0),
        ]
        for inp,  exp in ptr:
            with self.subTest(inp=inp, exp=exp):
                self.assertEqual(positive_sum(arr=inp), exp)


if __name__ == "__main__":
    main(verbosity=2)
