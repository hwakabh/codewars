from unittest import TestCase
from unittest import main

from .count_the_divisor_of_number import divisors


class TestCountTheDivisorOfNumber(TestCase):
    def test_divisors(self):
        test_patterns = [
            (4, 3),
            (5, 2),
            (12, 6),
            (30, 8),
            (4096, 13),
            # (4, 2), #-> Wrong case: expected 3 (1, 2,4)
        ]
        for d, exp in test_patterns:
            with self.subTest(d=d, exp=exp):
                self.assertEqual(divisors(n=d), exp)


if __name__ == "__main__":
    main(verbosity=2)
