from unittest import TestCase
from unittest import main

from is_it_even import is_even


class TestIsItEven(TestCase):
    def test_is_it_even(self):
        ptr = [
            (0, True),
            (0.5, False),
            (1, False),
            (2, True),
            (-4, True),
            (15, False),
            (20, True),
            (220, True),
            (222222221, False),
            (500000000, True),
        ]
        for inp, exp in ptr:
            with self.subTest(inp=inp, exp=exp):
                self.assertEqual(is_even(n=inp), exp)


if __name__ == "__main__":
    main(verbosity=2)
