from unittest import TestCase
from unittest import main

from minimum_to_multiple import minimum

class TestMinimumToMultiple(TestCase):
    # Test class of minimum_to_multiple
    def test_minimum(self):
        test_patterns = [
            (1, 1, 0),
            (9, 4, 1),
            (10, 6, 2),
            (60, 45, 15),
            (57, 50, 7),
            (28, 16, 4),
            (84, 80, 4),
            (129, 49, 18),
            (150, 67, 16),
            (121, 46, 17),
            (83, 81, 2),
            (89, 74, 15),
            # (30, 14, 1),    #-> Wrong Case
        ]
        for a, x, expected in test_patterns:
            with self.subTest(a=a, x=x, expected=expected):
                self.assertEqual(minimum(a=a, x=x), expected)


if __name__ == "__main__":
    main(verbosity=2)