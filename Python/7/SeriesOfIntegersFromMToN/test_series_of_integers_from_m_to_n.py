from unittest import TestCase
from unittest import main

from .series_of_integers_from_m_to_n import generate_integers


class TestSeriesOfIntegersFromMToN(TestCase):
    def test_generate_integers(self):
        ptr = [
            (2, 5, [2, 3, 4, 5]),
            (3, 7, [3, 4, 5, 6, 7])
        ]
        for s, e, exp in ptr:
            with self.subTest(s=s, e=e, exp=exp):
                self.assertEqual(generate_integers(m=s, n=e), exp)


if __name__ == "__main__":
    main(verbosity=2)
