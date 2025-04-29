from unittest import TestCase
from unittest import main

from .next_polydivisible_number import next_num


class TestNextPolydivisibleNumber(TestCase):
    def test_next_num(self):
        ptr = [
            # polydivisible numbers
            (0, 1),  # 1 / 1 = 0
            (10, 12), # 1 / 1 = 0, 12 / 2 = 6
            (11, 12),
            (1234, 1236), # 1 / 1 = 0, 12 / 2 = 6, 123 / 3 = 41, 1236 / 4 = 309
            (123220, 123252),
        ]
        for inp, exp in ptr:
            with self.subTest(inp=inp, exp=exp):
                self.assertEqual(next_num(n=inp), exp)


if __name__ == "__main__":
    main(verbosity=2)
