from unittest import TestCase
from unittest import main

from maximum_triplet_sum import max_tri_sum


class TestMaxiumumTripletSum(TestCase):
    def test_max_tri_sum(self):
        test_patterns = [
            ([3, 2, 6, 8, 2, 3], 17),
            ([2, 9, 13, 10, 5, 2, 9, 5], 32),
            ([2, 1, 8, 0, 6, 4, 8, 6, 2, 4], 18),
            ([-3, -27, -4, -2, -27, -2], -9),
            ([-14, -12, -7, -42, -809, -14, -12], -33),
            ([-13, -50, 57, 13, 67, -13, 57, 108 ,67] ,232),
            ([-7, 12, -7, 29, -5, 0, -7, 0, 0, 29], 41),
            ([-2, 0, 2], 0),
            ([-2, -4, 0, -9, 2], 0),
            ([-5, -1, -9, 0, 2], 1),
        ]
        for inp, exp in test_patterns:
            with self.subTest(inp=inp, exp=exp):
                self.assertEqual(max_tri_sum(numbers=inp), exp)


if __name__ == "__main__":
    main(verbosity=2)
