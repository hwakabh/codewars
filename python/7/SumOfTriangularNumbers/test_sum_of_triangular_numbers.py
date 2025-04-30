from unittest import TestCase
from unittest import main

from .sum_of_triangular_numbers import sum_triangular_numbers


class TestSumOfTriangularNumbers(TestCase):
    def test_sum_triangular_numbers(self):
        test_patterns = [
            (6, 56),
            (34, 7140),
            (-291, 0),
            (943, 140205240),
            (-971, 0),
        ]
        for n, exp in test_patterns:
            with self.subTest(n=n, exp=exp):
                self.assertEqual(sum_triangular_numbers(n=n), exp)


if __name__ == "__main__":
    main(verbosity=2)
