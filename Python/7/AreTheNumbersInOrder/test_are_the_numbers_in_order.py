from unittest import TestCase
from unittest import main

from are_the_numbers_in_order import in_asc_order


class TestAreTheNumbersInOrder(TestCase):
    def test_in_asc_order(self):
        ptr = [
            ([1, 2], True),
            ([2, 1], False),
            ([1, 2, 3], True),
            ([1, 3, 2], False),
            ([1, 4, 13, 97, 508, 1047, 20058], True),
            ([56, 98, 123, 67, 742, 1024, 32, 90969], False),
        ]
        for inp, exp in ptr:
            with self.subTest(inp=inp, exp=exp):
                self.assertEqual(in_asc_order(arr=inp), exp)


if __name__ == "__main__":
    main(verbosity=2)
