from unittest import TestCase
from unittest import main

from .factorial import factorial


class TestFactorial(TestCase):
    def test_factorial(self):
        test_patterns = [
            (0, 1),
            (1, 1),
            (2, 2),
            (3, 6),
            (4, 24),
            (5, 120),
            (6, 720),
            (7, 5040),
        ]
        for x, exp in test_patterns:
            with self.subTest(x=x, exp=exp):
                self.assertEqual(factorial(n=x), exp)


if __name__ == "__main__":
    main(verbosity=2)
