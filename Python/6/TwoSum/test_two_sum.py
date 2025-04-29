from unittest import TestCase
from unittest import main

from .two_sum import two_sum


class TestTwoSum(TestCase):
    def test_two_sum(self):
        test_patterns = [
            ([1, 2, 3], 4, [0,2]),
            ([1234, 5678, 9012], 14690, [1,2]),
            ([2, 2, 3], 4, [0, 1]),
        ]
        for num, t, expected in test_patterns:
            with self.subTest(num=num, t=t, expected=expected):
                self.assertEqual(two_sum(numbers=num, target=t), expected)


if __name__ == "__main__":
    main(verbosity=2)
