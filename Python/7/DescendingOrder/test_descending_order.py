from unittest import TestCase
from unittest import main

from descending_order import descending_order


class TestDescendingOrder(TestCase):
    def test_descending_order(self):
        test_patterns = [
            (0, 0),
            (15, 51),
            (123456789, 987654321),
        ]
        for inp, exp in test_patterns:
            with self.subTest(inp=inp, exp=exp):
                self.assertEqual(descending_order(num=inp), exp)


if __name__ == "__main__":
    main(verbosity=2)
