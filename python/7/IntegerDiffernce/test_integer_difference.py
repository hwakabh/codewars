from unittest import TestCase
from unittest import main

from .integer_difference import int_diff


class TestIntegerDifference(TestCase):
    def test_int_diff(self):
        ptr = [
            ([1, 1, 5, 6, 9, 16, 27], 4, 3),
            ([1, 1, 3, 3], 2, 4),
        ]
        for inp, d, exp in ptr:
            with self.subTest(inp=inp, d=d, exp=exp):
                self.assertEqual(int_diff(arr=inp, n=d), exp)


if __name__ == "__main__":
    main(verbosity=2)
