from unittest import TestCase
from unittest import main

from remove_duplicate_words import remove_duplicate_words


class TestRemoveDuplicateWords(TestCase):
    # Test class of remove_duplicate_words
    def test_remove_duplicate_words(self):
        test_patterns = [
            ('alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta', 'alpha beta gamma delta'),
            ('my cat is my cat fat', 'my cat is fat'),
            # ('alpha bravo charie charie', 'alpha bravo charie charie'), #-> Wrong case
        ]

        for words, expected in test_patterns:
            with self.subTest(words=words, expected=expected):
                self.assertEqual(remove_duplicate_words(s=words), expected)


if __name__ == "__main__":
    main(verbosity=2)