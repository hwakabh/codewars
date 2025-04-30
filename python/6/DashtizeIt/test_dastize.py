from unittest import TestCase
from unittest import main

from .dashtize import dashtize


class TestDashtize(TestCase):
    def test_dashtize(self):
        test_patterns = [
            (274, '2-7-4'),
            (5311, '5-3-1-1'),
            (86320, '86-3-20'),
            (974302, '9-7-4-3-02'),
            (0, '0'),
            (-1, '1'),
            (-28369, '28-3-6-9'),
            (None, 'None'),
        ]
        for n, expected in test_patterns:
            with self.subTest(n=n, expected=expected):
                self.assertEqual(dashtize(num=n), expected)


if __name__ == "__main__":
    main(verbosity=2)
