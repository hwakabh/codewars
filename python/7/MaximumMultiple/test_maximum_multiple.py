from unittest import TestCase
from unittest import main

from .maximum_multiple import max_multiple


class TestMaximumMultiple(TestCase):
    def test_max_multiple(self):
        test_patterns = [
            (2, 7, 6),
            (3, 10, 9),
            (7, 17, 14),
            (10, 50, 50),
            (37, 200, 185),
            (7, 100, 98),
        ]
        for d, b, exp in test_patterns:
            with self.subTest(d=d, b=b, exp=exp):
                self.assertEqual(max_multiple(divisor=d, bound=b), exp)


if __name__ == "__main__":
    main(verbosity=2)
