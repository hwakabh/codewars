from unittest import TestCase
from unittest import main

from .responsible_drinking import hydrate


class TestResponsibleDrinking(TestCase):
    def test_hydrate(self):
        ptr = [
            ('1 beer', '1 glass of water'),
            ('1 shot, 5 beers, 2 shots, 1 glass of wine, 1 beer', '10 glasses of water'),
        ]
        for inp, exp in ptr:
            with self.subTest(inp=inp, exp=exp):
                self.assertEqual(hydrate(drink_string=inp), exp)


if __name__ == "__main__":
    main(verbosity=2)
