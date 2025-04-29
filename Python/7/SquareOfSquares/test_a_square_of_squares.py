from unittest import TestCase
from unittest import main

from .a_square_of_squares import is_square


class TestASquareOfSquares(TestCase):
    # Test class of a_sqare_of_squares
    def test_is_sqare(self):
        test_patterns = [
            (-1, False),
            (0, True),
            (3, False),
            (4, True),
            (25, True),
            (26, False),
            # (144, False)  #-> Wrong Case: Square Root of 144 should be 12, then return True
        ]

        for num, expected in test_patterns:
            with self.subTest(num=num, expected=expected):
                self.assertEqual(is_square(n=num), expected)


if __name__ == "__main__":
    main(verbosity=2)
