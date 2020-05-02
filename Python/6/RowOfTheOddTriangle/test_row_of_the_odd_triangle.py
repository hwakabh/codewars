from unittest import TestCase
from unittest import main

from row_of_the_odd_triangle import odd_row


class TestRowOfTheOddTriangle(TestCase):
    # Test class of row_of_the_odd_triangle
    def test_odd_row(self):
        test_patterns = [
            (1, [1]),
            (2, [3, 5]),
            (13, [157, 159, 161, 163, 165, 167, 169, 171, 173, 175, 177, 179, 181]),
            (19, [343, 345, 347, 349, 351, 353, 355, 357, 359, 361, 363, 365, 367, 369, 371, 373, 375, 377, 379]),
            (41, [1641, 1643, 1645, 1647, 1649, 1651, 1653, 1655, 1657, 1659, 1661, 1663, 1665, 1667, 1669, 1671, 1673, 1675, 1677, 1679, 1681, 1683, 1685, 1687, 1689, 1691, 1693, 1695, 1697, 1699, 1701, 1703, 1705, 1707, 1709, 1711, 1713, 1715, 1717, 1719, 1721]),
        ]
        for n, expected in test_patterns:
            with self.subTest(n=n, expected=expected):
                self.assertEqual(odd_row(n=n), expected)


if __name__ == "__main__":
    main(verbosity=2)