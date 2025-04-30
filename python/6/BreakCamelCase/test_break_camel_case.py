from unittest import TestCase
from unittest import main

from .break_camel_case import solution


class TestBreakCamelCase(TestCase):
    # Test class of break_camel_case
    def test_solution(self):
        test_patterns = [
            ('helloWorld', 'hello World'),
            ('camelCase', 'camel Case'),
            ('breakCamelCase', 'break Camel Case'),
        ]
        for s, expected in test_patterns:
            with self.subTest(s=s, expected=expected):
                self.assertEqual(solution(s=s), expected)


if __name__ == '__main__':
    main(verbosity=2)
