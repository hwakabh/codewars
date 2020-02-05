from unittest import TestCase
from unittest import main

from regexp_basics import is_vowel


class TestRegexpBasics(TestCase):
    # Test class of regexp_basics
    def test_is_vowel(self):
        test_patterns = [
            ('', False),
            ('a', True),
            ('E', True),
            ('ou', False),
            ('z', False),
            ('lol', False),
            # ('code', True), #-> Wrong Case
        ]
        for s, expected in test_patterns:
            with self.subTest(s=s, expected=expected):
                self.assertEqual(is_vowel(s=s), expected)


if __name__ == "__main__":
    main(verbosity=2)