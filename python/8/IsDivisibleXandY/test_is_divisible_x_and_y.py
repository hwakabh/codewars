from unittest import TestCase
from unittest import main

from .is_divisible_x_and_y import is_divisible


class TestIsDivisibleXAndY(TestCase):
    def test_is_divisible(self):
        test_patterns = [
          (3, 2, 2, False),
          (3, 3, 4, False),
          (12, 3, 4, True),
          (8, 3, 4, False),
        ]
        for n, x, y, exp in test_patterns:
            with self.subTest(n=n, x=x, y=y, exp=exp):
                self.assertEqual(is_divisible(n=n, x=x, y=y), exp)


if __name__ == "__main__":
    main(verbosity=2)
