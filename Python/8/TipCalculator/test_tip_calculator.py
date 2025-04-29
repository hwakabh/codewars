from unittest import TestCase
from unittest import main

from .tip_calculator import calculate_tip


class TestTipCalculator(TestCase):
    def test_calculate_tip(self):
        ptr = [
            (30, 'poor', 2),
            (20, 'Excellent', 4),
            (20, 'hi', 'Rating not recognised'),
            (107.65, 'GReat', 17),
            (20, 'great!', 'Rating not recognised'),
        ]
        for inp, rate, exp in ptr:
            with self.subTest(inp=inp, rate=rate, exp=exp):
                self.assertEqual(calculate_tip(amount=inp, rating=rate), exp)


if __name__ == "__main__":
    main(verbosity=2)
