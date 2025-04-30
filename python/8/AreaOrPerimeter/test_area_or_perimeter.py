from unittest import TestCase
from unittest import main

from .area_or_perimeter import area_or_perimeter


class TestAreaOrParameter(TestCase):
    def test_are_or_parameter(self):
        test_patterns = [
            (4, 4, 16),
            (6, 10, 32),
        ]
        for x, y, exp in test_patterns:
            with self.subTest(x=x, y=y, exp=exp):
                self.assertEqual(area_or_perimeter(l=x, w=y), exp)


if __name__ == "__main__":
    main(verbosity=2)
