from unittest import TestCase
from unittest import main

from is_he_gonna_suvive import hero


class TestIsHeGonnaSuvive(TestCase):
    def test_hero(self):
        test_patterns = [
            (10, 5, True),
            (7, 4, False),
            (4, 5, False),
            (100, 40, True),
            (1500, 751, False),
            (0, 1, False),
        ]
        for b, d, exp in test_patterns:
            with self.subTest(b=b, d=d, exp=exp):
                self.assertEqual(hero(bullets=b, dragons=d), exp)


if __name__ == "__main__":
    main(verbosity=2)
