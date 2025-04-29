from unittest import TestCase
from unittest import main

from .absent_vowel import absent_vowel


class TestAbsentVowel(TestCase):
    # Test class of absent_vowel
    def test_absent_vowel(self):
        test_patterns = [
            ('John Doe hs seven red pples under his bsket', 0),
            ('Bb Smith sent us six neatly arranged range bicycles', 3),
        ]
        for s, expected in test_patterns:
            with self.subTest(s=s, expected=expected):
                self.assertEqual(absent_vowel(x=s), expected)


if __name__ == "__main__":
    main(verbosity=2)
