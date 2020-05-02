from unittest import TestCase
from unittest import main

from difference_of_two import twos_differnece


class TestDiffernceOfTwo(TestCase):
    def test_twos_differnces(self):
        ptr = [
            ([1, 2, 3, 4], [(1, 3), (2, 4)]),
            ([1, 3, 4, 6], [(1, 3), (4, 6)]),
            ([0, 3, 1, 4], [(1, 3)]),
            ([4, 1, 2, 3], [(1, 3), (2, 4)]),
            ([6, 3, 4, 1, 5], [(1, 3), (3, 5), (4, 6)]),
            ([3, 1, 6, 4], [(1, 3), (4, 6)]),
            ([1, 3, 5, 6, 8, 10, 15, 32, 12, 14, 56], [(1, 3), (3, 5), (6, 8), (8, 10), (10, 12), (12, 14)]),
            ([1, 4, 7, 10], []),
            ([], []),
        ]
        for inp, exp in ptr:
            with self.subTest(inp=inp, exp=exp):
                self.assertEqual(twos_differnece(lst=inp), exp)


if __name__ == "__main__":
    main(verbosity=2)
