from unittest import TestCase
from unittest import main

from .century_from_year import century


class TestCenturyFromYear(TestCase):
    # Test class of century_from_year
    def test_century(self):
        test_patterns = [
            (1705, 18),
            (1900, 19),
            (1601, 17),
            (2000, 20),
            # (386, 3)  #-> Wrong Case
        ]

        for y, expected in test_patterns:
            with self.subTest(y=y, expected=expected):
                self.assertEqual(century(year=y), expected)


if __name__ == "__main__":
    main(verbosity=2)
