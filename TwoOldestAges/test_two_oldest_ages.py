from unittest import TestCase
from unittest import main

from two_oldest_ages import two_oldest_ages


class TestTwoOldestAges(TestCase):
    def test_two_oldest_ages(self):
        test_patterns = [
            ([1, 5, 87, 45, 8, 8], [45, 87]),
            ([6, 5, 83, 5, 3, 18], [18, 83]),
            ([10, 1], [1, 10]),
        ]
        for a, expected in test_patterns:
            with self.subTest(a=a, expected=expected):
                self.assertEqual(two_oldest_ages(ages=a), expected)


if __name__ == "__main__":
    main(verbosity=2)
