from unittest import TestCase
from unittest import main

from .how_many_urinals_are_free import get_free_urinals


class TestHowManyUrinalsAreFree(TestCase):
    def test_ge_free_urinals(self):
        test_patterns = [
            ("10001", 1),
            ("1001", 0),
            ("00000", 3),
            ("0000", 2),
            ("01000", 1),
            ("00010", 1),
            ("10000", 2),
            ("0100000", 2),
            ("1", 0),
            ("0", 1),
            ("10", 0),
        ]
        for u, expected in test_patterns:
            with self.subTest(u=u, expected=expected):
                self.assertEqual(get_free_urinals(urinals=u), expected)


if __name__ == "__main__":
    main(verbosity=2)
