from unittest import TestCase
from unittest import main

from return_negative import make_nagative


class TestReturnNegative(TestCase):
    def test_make_nagative(self):
        test_patterns = [
            (1, -1),
            (-5, -5),
            (0, 0),
            (42, -42),
        ]
        for x, exp in test_patterns:
            with self.subTest(x=x, exp=exp):
                self.assertEqual(make_nagative(number=x), exp)


if __name__ == "__main__":
    main(verbosity=2)
