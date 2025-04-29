from unittest import TestCase
from unittest import main

from .split_strings import solution


class TestSplitStrings(TestCase):
    def test_solution(self):
        test_patterns = [
            ('asdfadsf', ['as', 'df', 'ad', 'sf']),
            ('asdfads', ['as', 'df', 'ad', 's_']),
            ('', []),
            ('x', ['x_']),
        ]
        for w, exp in test_patterns:
            with self.subTest(w=w, exp=exp):
                self.assertEqual(solution(s=w), exp)


if __name__ == "__main__":
    main(verbosity=2)
