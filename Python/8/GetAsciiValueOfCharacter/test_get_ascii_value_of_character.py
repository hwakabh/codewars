from unittest import TestCase
from unittest import main

from get_ascii_value_of_character import get_ascii


class TestGetAsciiValueOfCharacter(TestCase):
    def test_get_ascii(self):
        test_patterns = [
            ('A', 65),
            (' ', 32),
            ('!', 33),
        ]
        for inp, exp in test_patterns:
            with self.subTest(inp=inp, exp=exp):
                self.assertEqual(get_ascii(c=inp), exp)


if __name__ == "__main__":
    main(verbosity=2)
