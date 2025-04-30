from unittest import TestCase
from unittest import main

from .cyclops_numbers import cyclops


class TestCyclopsNumbers(TestCase):
    def test_cyclops(self):
        ptr = [
            (1, False),
            (5, True),
            (3, False),
            (11, False),
            (13, False),
            (23, False),
            (27, True),
        ]
        for inp, exp in ptr:
            with self.subTest(inp=inp, exp=exp):
                self.assertEqual(cyclops(n=inp), exp)


if __name__ == "__main__":
    main(verbosity=2)
