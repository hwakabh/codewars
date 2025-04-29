from unittest import TestCase
from unittest import main

from .growth_of_population import nb_year


class TestGrowthOfPopulation(TestCase):
    def test_fb_year(self):
        test_patterns = [
            (1500, 5, 100, 5000, 15),
            (1500000, 2.5, 10000, 2000000, 10),
            (1500000, 0.25, 1000, 2000000, 94),
        ]
        for i, p, a, s, exp in test_patterns:
            with self.subTest(i=i, p=p, a=a, s=s, exp=exp):
                self.assertEqual(nb_year(p0=i, percent=p, aug=a, p=s), exp)


if __name__ == "__main__":
    main(verbosity=2)
