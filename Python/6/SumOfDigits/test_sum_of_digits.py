from unittest import TestCase
from unittest import main

from .sum_of_digits import digital_root


class TestSumOfDigits(TestCase):
    def test_digital_root(self):
        test_patterns = [
            (16, 7),
            (456, 6),
            (942, 6),
            (132189, 6),
            (493193, 2),
        ]
        for inp, exp in test_patterns:
            with self.subTest(inp=inp, exp=exp):
                self.assertEqual(digital_root(n=inp), exp)


if __name__ == "__main__":
    main(verbosity=2)
