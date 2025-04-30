from unittest import TestCase
from unittest import main

from .debug_sum_of_digits_of_a_number import get_sum_of_digits


class TestDebugSumOfDigitsOfANumber(TestCase):
    def test_get_sum_of_digits(self):
        ptr = [
            (123, 6),
            (223, 7),
            (1337, 14),
        ]
        for inp, exp in ptr:
            with self.subTest(inp=inp, exp=exp):
                self.assertEqual(get_sum_of_digits(num=inp), exp)


if __name__ == "__main__":
    main(verbosity=2)
