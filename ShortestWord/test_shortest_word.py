from unittest import TestCase
from unittest import main

from shortest_word import find_short


class TestShortestWord(TestCase):
    def test_find_short(self):
        test_patterns = [
            ('bitcoin take over the world maybe who knows perhaps', 3),
            ('turns out random test cases are easier than writing out basic ones', 3),
            ('lets talk about javascript the best language', 3),
            ('i want to travel the world writing code one day', 1),
            ('Lets all go on holiday somewhere very cold', 2),
        ]
        for p, expected in test_patterns:
            with self.subTest(p=p, expected=expected):
                self.assertEqual(find_short(s=p), expected)


if __name__ == "__main__":
    main(verbosity=2)
