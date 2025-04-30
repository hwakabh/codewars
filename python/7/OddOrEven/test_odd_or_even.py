# Test.assert_equals(oddOrEven([0, 1, 2]), 'odd')
# Test.assert_equals(oddOrEven([0, 1, 3]), 'even')
# Test.assert_equals(oddOrEven([1023, 1, 2]), 'even')

from unittest import TestCase
from unittest import main

from .odd_or_even import oddOrEven


class TestOddOrEven(TestCase):
    # Test class of odd_or_even
    def test_oddOrEven(self):
        test_patterns = [
            ([0, 1, 2], 'odd'),
            ([0, 1, 3], 'even'),
            ([1023, 1, 2], 'even'),
            # ([-1, 2, 5], 'odd'),  #-> Wrong Case: -1 + 2 + 5 = 6, expected even
        ]

        for numbers, expected in test_patterns:
            with self.subTest(numbers=numbers, expected=expected):
                self.assertEqual(oddOrEven(arr=numbers), expected)


if __name__ == "__main__":
    main(verbosity=2)
