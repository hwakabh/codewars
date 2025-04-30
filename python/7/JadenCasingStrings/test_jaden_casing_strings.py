from unittest import TestCase
from unittest import main

from .jaden_casing_strings import toJadenCase


class TestJadenCasingStrings(TestCase):
    # Test class of jaden_casing_strings
    def test_toJadenCase(self):
        test_pattern = [
            ('How can mirrors be real if our eyes aren\'t real', 'How Can Mirrors Be Real If Our Eyes Aren\'t Real'),
            ('I need someone to fabricate a shipping container for me', 'I Need Someone To Fabricate A Shipping Container For Me')
        ]

        for sentence, expected in test_pattern:
            with self.subTest(sentence=sentence, expected=expected):
                self.assertEqual(toJadenCase(string=sentence), expected)

if __name__ == "__main__":
    main(verbosity=2)
