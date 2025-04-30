from unittest import TestCase
from unittest import main

from .square_every_digit import square_digits

class TestSquareEveryDigit(TestCase):
    # Test class of square_every_digit
    def test_square_digits(self):
        test_patters = [
            (9119, 811181),
            (783, 49649),
            (23415, 4916125),
            # (1234, 1234)  #-> Wrong Case: Expected 14916
        ]

        for n, expected in test_patters:
            with self.subTest(n=n, expected=expected):
                self.assertEqual(square_digits(num=n), expected)


if __name__ == "__main__":
    main(verbosity=2)
