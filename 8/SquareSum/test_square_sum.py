from unittest import TestCase
from unittest import main

from square_sum import square_sum


class TestSquareSum(TestCase):
    # Test class of square_sum
    def test_square_sum(self):
        test_patterns = [
            ([1, 2], 5),
            ([0, 3, 4, 5], 50),
            ([12], 144),
            # ([11, 12, 13], 435),  #-> Wrong Case: expected 434
        ]

        for nums, expected in test_patterns:
            with self.subTest(nums=nums, expected=expected):
                self.assertEqual(square_sum(numbers=nums), expected)


if __name__ == "__main__":
    main(verbosity=2)