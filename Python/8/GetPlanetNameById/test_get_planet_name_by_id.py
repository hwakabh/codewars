from unittest import TestCase
from unittest import main

from .get_planet_name_by_id import get_planet_name


class TestGetPlanetNameById(TestCase):
    def test_get_planet_name(self):
        ptr = [
            (2, 'Venus'),
            (5, 'Jupiter'),
            (3, 'Earth'),
            (4, 'Mars'),
            (8, 'Neptune'),
            (1, 'Mercury'),
        ]
        for inp, exp in ptr:
            with self.subTest(inp=inp, exp=exp):
                self.assertEqual(get_planet_name(id=inp), exp)


if __name__ == "__main__":
    main(verbosity=2)
