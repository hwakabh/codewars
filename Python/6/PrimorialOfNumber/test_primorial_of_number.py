from unittest import TestCase
from unittest import main

from .primorial_of_number import num_primorial


class TestPrimorialOfNumber(TestCase):
    # Test class of primorial_of_number
    def test_num_primorial(self):
        test_patterns = [
          (3, 30),
          (5, 2310),
          (6, 30030),
          # (2, 2), #-> Wrong Case: expected 2 * 3 = 6
        ]

        for n, expected in test_patterns:
            with self.subTest(n=n, expected=expected):
                self.assertEqual(num_primorial(n=n), expected)


if __name__ == "__main__":
    main(verbosity=2)
