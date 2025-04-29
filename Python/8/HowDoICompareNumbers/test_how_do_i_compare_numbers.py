from unittest import TestCase
from unittest import main

from .how_do_i_compare_numbers import what_is


class TestHowDoICompareNumbers(TestCase):
    def test_what_is(self):
        ptr = [
            (0, 'nothing'),
            (123, 'nothing'),
            (-1, 'nothing'),
            (42, 'everything'),
            (42 * 42, 'everything squared'),
        ]
        for inp, exp in ptr:
            with self.subTest(inp=inp, exp=exp):
                self.assertEqual(what_is(x=inp), exp)


if __name__ == "__main__":
    main(verbosity=2)
