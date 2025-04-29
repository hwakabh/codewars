from unittest import TestCase
from unittest import main

from .convert_number_to_reversed_array_of_digits import digitize


class TestConvertNumberToReversedArrayOfDigits(TestCase):
    # Test class of convert_number_to_reversed_array_of_digits
    def test_digitize(self):
        test_patterns = [
            (35231, [1, 3, 2, 5, 3]),
            (348597, [7, 9, 5, 8, 4, 3]),
            # (4869, [4, 8, 6, 9]), #-> Wrong Case
        ]

        for num, expected in test_patterns:
            with self.subTest(num=num, expected=expected):
                self.assertEqual(digitize(n=num), expected)


if __name__ == "__main__":
    main(verbosity=2)
