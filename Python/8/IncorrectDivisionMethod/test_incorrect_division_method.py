from unittest import TestCase
from unittest import main

from .incorrect_division_method import divide_numbers


class TestIncorrectDivisionMethod(TestCase):
    def test_divide_numbers(self):
        test_patterns = [
            (4, 2, 2),
            (10, 2, 5),
            (9, 4, 2.25),
            (21, 5, 4.2),
            (9, 3, 3),
            (1, 100, 0.01),
        ]
        for i, j, exp in test_patterns:
            with self.subTest(i=i, j=j, exp=exp):
                self.assertEqual(divide_numbers(x=i, y=j), exp)


if __name__ == "__main__":
    main(verbosity=2)
