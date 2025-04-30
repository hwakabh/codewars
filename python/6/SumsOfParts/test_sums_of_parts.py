from unittest import TestCase
from unittest import main

from .sums_of_parts import parts_sums


class TestSumsOfParts(TestCase):
    def test_parts_sums(self):
        test_patterns = [
            ([], [0]),
            ([0, 1, 3, 6, 10], [20, 20, 19, 16, 10, 0]),
            ([1, 2, 3, 4, 5, 6], [21, 20, 18, 15, 11, 6, 0]),
            ([744125, 935, 407, 454, 430, 90, 144, 6710213, 889, 810, 2579358], [10037855, 9293730, 9292795, 9292388, 9291934, 9291504, 9291414, 9291270, 2581057, 2580168, 2579358, 0]),
        ]
        for inp, exp in test_patterns:
            with self.subTest(inp=inp, exp=exp):
                self.assertEqual(parts_sums(ls=inp), exp)


if __name__ == "__main__":
    main(verbosity=2)
