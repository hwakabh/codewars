from unittest import TestCase
from unittest import main

from what_dominates_your_array import dominator


class TestWhatDominamtesYourArray(TestCase):
    def test_dominator(self):
        ptr = [
            ([3, 4, 3, 2, 3, 1, 3, 3], 3),
            ([1, 2, 3, 4, 5], -1),
            ([1, 1, 1, 2, 2, 2], -1),
            ([1, 1, 1, 2, 2, 2, 2], 2),
            ([], -1),
        ]
        for inp, exp in ptr:
            with self.subTest(inp=inp, exp=exp):
                self.assertEqual(dominator(arr=inp), exp)


if __name__ == "__main__":
    main(verbosity=2)
