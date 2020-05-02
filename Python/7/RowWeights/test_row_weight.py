from unittest import TestCase
from unittest import main

from row_weights import row_weights


class TestRowWeights(TestCase):
    def test_row_weights(self):
        test_patterns = [
            ([80], (80,0)),
            ([100,50], (100,50)),
            ([50,60,70,80], (120,140)),
            ([13,27,49], (62,27)),
            ([70,58,75,34,91], (236,92)),
            ([29,83,67,53,19,28,96], (211,164)),
            ([0], (0,0)),
            ([100,51,50,100], (150,151)),
            ([39,84,74,18,59,72,35,61], (207,235)),
            ([0,1,0], (0,1)),
        ]
        for num, exp in test_patterns:
            with self.subTest(num=num, exp=exp):
                self.assertEqual(row_weights(array=num), exp)


if __name__ == "__main__":
    main(verbosity=2)
