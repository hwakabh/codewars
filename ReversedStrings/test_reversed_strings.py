from unittest import TestCase
from unittest import main

from reversed_strings import solutions


class TestReversedStrings(TestCase):
    # Test class of reversed_strings
    def test_solutions(self):
        test_patterns = [
            ('world', 'dlrow'),
            ('hello', 'olleh'),
            ('', ''),
            ('h', 'h'),
            # ('abc', 'acb'), #-> Wrong Case: expected 'cba'
        ]

        for s, expected in test_patterns:
            with self.subTest(s=s, expected=expected):
                self.assertEqual(solutions(string=s), expected)


if __name__ == "__main__":
    main(verbosity=2)