from unittest import TestCase
from unittest import main

from array_diff import array_diff


class TestArrayDiff(TestCase):
    # Test class of array_diff
    def test_array_diff(self):
        test_patterns = [
            ([1, 2], [1], [2]),
            ([1, 2, 2], [1], [2, 2]),
            ([1, 2, 2], [2], [1]),
            ([1, 2, 2], [], [1, 2, 2]),
            ([], [1, 2], [])
        ]
        
        for first, second, expected in test_patterns:
            with self.subTest(first=first, second=second, expected=expected):
                self.assertEqual(array_diff(a=first, b=second), expected)


if __name__ == "__main__":
    main(verbosity=2)