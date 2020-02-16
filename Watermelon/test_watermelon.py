from unittest import TestCase
from unittest import main

from watermelon import divide


class TestWatermelon(TestCase):
    def test_watermelon(self):
        test_patterns = [
            (4, True),
            (2, False),
            (5, False),
            (88, True),
            (100, True),
            (67, False),
            (90, True),
            (10, True),
            (99, False),
            (32, True),
        ]
        for w, expected in test_patterns:
            with self.subTest(w=w, expected=expected):
                self.assertEqual(divide(weight=w), expected)


if __name__ == "__main__":
    main(verbosity=2)
