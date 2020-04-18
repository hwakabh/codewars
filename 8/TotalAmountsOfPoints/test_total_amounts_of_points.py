from unittest import TestCase
from unittest import main

from total_amounts_of_points import points


class TestTotalAmountsOfPoints(TestCase):
    def test_points(self):
        ptr = [
            (['1:0', '2:0', '3:0', '4:0', '2:1', '3:1', '4:1', '3:2', '4:2', '4:3'], 30),
            (['1:1', '2:2', '3:3', '4:4', '2:2', '3:3', '4:4', '3:3', '4:4', '4:4'], 10),
            (['0:1', '0:2', '0:3', '0:4', '1:2', '1:3', '1:4', '2:3', '2:4', '3:4'], 0),
            (['1:0', '2:0', '3:0', '4:0', '2:1', '1:3', '1:4', '2:3', '2:4', '3:4'], 15),
            (['1:0', '2:0', '3:0', '4:4', '2:2', '3:3', '1:4', '2:3', '2:4', '3:4'], 12),
        ]
        for inp, exp in ptr:
            with self.subTest(inp=inp, exp=exp):
                self.assertEqual(points(games=inp), exp)


if __name__ == "__main__":
    main(verbosity=2)
