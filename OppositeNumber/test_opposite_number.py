from unittest import TestCase
from unittest import main

from opposite_number import opposite


class TestOppositeNumber(TestCase):
    def test_opposite(self):
        test_patterns = [
            (1, -1),
            (14, -14),
            (-34, 34),
        ]
        for n, expected in test_patterns:
            with self.subTest(n=n, expected=expected):
                self.assertEqual(opposite(number=n), expected)


if __name__ == "__main__":
    main(verbosity=2)
