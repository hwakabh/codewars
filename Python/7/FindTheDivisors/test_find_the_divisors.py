from unittest import TestCase
from unittest import main

from .find_the_divisors import divisors


class TestFindTheDivisors(TestCase):
    def test_divisors(self):
        ptr = [
            (15, [3, 5]),
            (12, [2, 3, 4, 6]),
            (13, '13 is prime'),
        ]
        for inp, exp in ptr:
            with self.subTest(inp=inp, exp=exp):
                self.assertEqual(divisors(integer=inp), exp)


if __name__ == "__main__":
    main(verbosity=2)
