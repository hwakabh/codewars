from unittest import TestCase
from unittest import main

from .number_to_string import to_string


class TestNumberToString(TestCase):
    def test_to_string(self):
        inp = 123
        exp = '123'

        self.assertEqual(to_string(n=inp), exp)


if __name__ == "__main__":
    main(verbosity=2)
