from unittest import TestCase
from unittest import main

from .expressions_matter import expression_matter


class TestExpressionsMatter(TestCase):
    def test_expression_matter(self):
        test_patterns = [
            # Small value patterns
            (2, 1, 2, 6),
            (2, 1, 1, 4),
            (1, 1, 1, 3),
            (1, 2, 3, 9),
            (1, 3, 1, 5),
            (2, 2, 2, 8),
            # Medium value patterns
            (5, 1, 3, 20),
            (3, 5, 7, 105),
            (5, 6, 1, 35),
            (1, 6, 1, 8),
            (2, 6, 1, 14),
            (6, 7, 1, 48),
            # Mized value pattern
            (2, 10, 3, 60),
            (1, 8, 3, 27),
            (9, 7, 2, 126),
            (1, 1, 10, 20),
            (9, 1, 1, 18),
            (10, 5, 6, 300),
            (1, 10, 1, 12),
        ]
        for a, b, c, exp in test_patterns:
            with self.subTest(a=a, b=b, c=c, exp=exp):
                self.assertEqual(expression_matter(a=a, b=b, c=c), exp)


if __name__ == "__main__":
    main(verbosity=2)
