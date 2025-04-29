from unittest import TestCase
from unittest import main

from .sum_of_minimals import sum_of_minimals


class TestSumOfMinimals(TestCase):
    # Test class of sum_of_minimals
    def test_sum_of_minimals(self):
        test_patterns = [
            ([[7, 9, 8, 6, 2 ], [6, 3, 5,4, 3], [5, 8, 7, 4, 5] ],9),
            ([[11, 12, 14, 54], [67, 89, 90, 56], [7, 9, 4, 3], [9, 8, 6, 7]],76),
        ]
        for nums, expected in test_patterns:
            with self.subTest(nums=nums, expected=expected):
                self.assertEqual(sum_of_minimals(numbers=nums), expected)


if __name__ == "__main__":
    main(verbosity=2)
