from unittest import TestCase
from unittest import main

from sum_of_angles import angle


class TestSumOfAngles(TestCase):
    # Test class of sum_of_angles
    def test_angle(self):
        test_patterns = [
            (3, 180),
            (4, 360),
        ]
        for n, expected in test_patterns:
            with self.subTest(n=n, expected=expected):
                self.assertEqual(angle(n=n), expected)


if __name__ == "__main__":
    main(verbosity=2)
