from unittest import TestCase
from unittest import main

from breaking_chocolate_problem import breakChocolate


class TestBreakingChocolateProblem(TestCase):
    def test_breakingChocolate(self):
        test_patterns = [
            (5, 5, 24),
            (1, 1, 0),
        ]
        for n, m, exp in test_patterns:
            with self.subTest(n=n, m=m, exp=exp):
                self.assertEqual(breakChocolate(n=n, m=m), exp)


if __name__ == "__main__":
    main(verbosity=2)
