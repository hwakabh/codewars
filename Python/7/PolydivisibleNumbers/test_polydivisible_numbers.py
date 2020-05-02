from unittest import TestCase
from unittest import main

from polydivisible_numbers import polydivisible


class TestPolydivisibleNumbers(TestCase):
    def test_polydivisible(self):
        test_patterns = [
            (1232, True),
            (123220, False),
            (0, True),
            (1, True),
            (141, True),
            (1234, False),
            (21234, False),
            (81352, False),
            (987654, True),
            (1020005, True),
            (9876545, True),
            (381654729, True),
            (1073741823, False),
        ]
        for n, expected in test_patterns:
            with self.subTest(n=n, expected=expected):
                self.assertEqual(polydivisible(x=n), expected)


if __name__ == "__main__":
    main(verbosity=2)
