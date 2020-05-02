from unittest import TestCase
from unittest import main

from what_will_be_the_odd_one_out import odd_one_out


class TestWhatWillBeTheOddOneOut(TestCase):
    # Test class of what_will_be_the_odd_one_out
    def test_odd_one_out(self):
        test_patterns = [
            ('Hello World', ["H", "e", " ", "W", "r", "l", "d"]),
            ('Codewars', ["C", "o", "d", "e", "w", "a", "r", "s"]),
            ('woowee', []),
            ('racecar', ['e']),
            ('Mamma', ['M']),
            ('¼ x 4 = 1', ["¼", "x", "4", "=", "1"]),
            ('¼ x 4 = 1 and ½ x 4 = 2', ["¼", "1", "a", "n", "d", "½", "2"]),
        ]
        for s, expected in test_patterns:
            with self.subTest(s=s, expected=expected):
                self.assertEqual(odd_one_out(s=s), expected)


if __name__ == "__main__":
    main(verbosity=2)
