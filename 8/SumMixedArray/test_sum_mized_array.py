from unittest import TestCase
from unittest import main

from sum_mixed_array import sum_mix


class TestSumMixedArray(TestCase):
    # Test class of sum_mixed_array
    def test_sum_mix(self):
        test_patterns = [
            ([9, 3, '7', '3'], 22),
            (['5', '0', 9, 3, 2, 1, '9', 6, 7], 42),
            (['3', 6, 6, 0, '5', 8, 5, '6', 2,'0'], 41),
            (['1', '5', '8', 8, 9, 9, 2, '3'], 45),
            ([8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7], 61),
        ]
        for i, expected in test_patterns:
            with self.subTest(i=i, expected=expected):
                self.assertEqual(sum_mix(arr=i), expected)


if __name__ == "__main__":
    main(verbosity=2)