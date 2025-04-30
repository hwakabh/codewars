from unittest import TestCase
from unittest import main

from .find_the_first_non_consecutive_number import first_non_consecutive


class TestFindTheFirstNonConsecutiveNumber(TestCase):
    def test_first_non_consecutive(self):
        test_pattern = [
            ([1, 2, 3, 4, 6, 7, 8], 6),
            ([1, 2, 3, 4, 5, 6, 7, 8], None),
            ([4, 6, 7, 8, 9, 11], 6),
            ([4, 5, 6, 7, 8, 9, 11], 11),
            ([31, 32], None),
            ([-3, -2, 0, 1], 0),
            ([-5, -4, -3, -1], -1),
        ]
        for inp, exp in test_pattern:
            with self.subTest(inp=inp, exp=exp):
                self.assertEqual(first_non_consecutive(arr=inp), exp)


if __name__ == "__main__":
    main(verbosity=2)
