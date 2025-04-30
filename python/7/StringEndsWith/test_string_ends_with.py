from unittest import TestCase
from unittest import main

from .string_ends_with import solution


class TestStringEndsWith(TestCase):
    def test_solution(self):
        test_patterns = [
            ('abcde', 'cde', True),
            ('abcde', 'abc', False),
            ('abcde', '', True),
        ]
        for s, e, exp in test_patterns:
            with self.subTest(s=s, e=e, exp=exp):
                self.assertEqual(solution(string=s, ending=e), exp)


if __name__ == "__main__":
    main(verbosity=2)
