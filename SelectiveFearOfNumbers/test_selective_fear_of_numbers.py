from unittest import TestCase
from unittest import main

from selective_fear_of_numbers import am_I_afraid


class TestSelectiveFearOfNumbers(TestCase):
    def test_selective_fear_of_numbers(self):
        test_patterns = [
            ('Monday', 13, False),
            ('Sunday', -666, True),
            ('Tuesday', 2, False),
            ('Tuesday', 965, True),
            ('Friday', 2, True),
        ]
        for d, n, expected in test_patterns:
            with self.subTest(d=d, n=n, expected=expected):
                self.assertEqual(am_I_afraid(day=d, num=n), expected)


if __name__ == "__main__":
    main(verbosity=2)
