from unittest import TestCase
from unittest import main

from alphabetical_addition import add_letters


class TestAlphabeticalAddition(TestCase):
    # Test class of alphabetical_addition
    def test_add_letters(self):
        test_patterns = [
            (['a', 'b', 'c'], 'f'),
            (['z'], 'z'),
            (['a', 'b'], 'c'),
            (['c'], 'c'),
            (['z', 'a'], 'a'),
            (['y', 'c', 'b'], 'd'),
            ([], 'z'),
        ]
        for l, expected in test_patterns:
            with self.subTest(l=l, expected=expected):
                self.assertEqual(add_letters(letters=l), expected)


if __name__ == "__main__":
    main(verbosity=2)
