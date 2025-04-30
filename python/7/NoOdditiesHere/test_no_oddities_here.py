from unittest import TestCase
from unittest import main

from .no_oddities_here import no_odds


class TestNoOdditiesHere(TestCase):
    def test_no_odds(self):
        test_patterns = [
            ([0, 1], [0]),
            ([0, 1, 2, 3], [0, 2]),
            ([1, 3, 5, 7, 9], []),
            ([0, 2, 4, 6, 8, 10], [0, 2, 4, 6, 8, 10]),
            ([-1, -3, -5, -7, -9], []),
            ([2, 4, 8, 6, 0], [2, 4, 8, 6, 0]),
            ([], []),
        ]
        for inp, exp in test_patterns:
            with self.subTest(inp=inp, exp=exp):
                self.assertEqual(no_odds(values=inp), exp)


if __name__ == "__main__":
    main(verbosity=2)
