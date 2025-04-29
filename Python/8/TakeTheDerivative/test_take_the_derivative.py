from unittest import TestCase
from unittest import main

from .take_the_derivative import derive


class TestTakeTheDerivative(TestCase):
    def test_derive(self):
        ptr = [
            (7, 8, '56x^7'),
            (5, 9, '45x^8'),
        ]
        for c, e, exp in ptr:
            with self.subTest(c=c, e=e, exp=exp):
                self.assertEqual(derive(coefficient=c, exponent=e), exp)


if __name__ == "__main__":
    main(verbosity=2)
