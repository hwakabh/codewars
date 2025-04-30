from unittest import TestCase
from unittest import main

from .form_the_minimum import min_value


class TestFormTheMinimum(TestCase):
    def test_min_value(self):
        test_patterns = [
            ([1, 3, 1], 13),
            ([4, 7, 5, 7], 457),
            ([4, 8, 1, 4], 148),
        ]
        for x, exp in test_patterns:
            with self.subTest(x=x, exp=exp):
                self.assertEqual(min_value(digits=x), exp)


if __name__ == "__main__":
    main(verbosity=2)
