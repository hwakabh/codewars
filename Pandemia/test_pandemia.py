from unittest import TestCase
from unittest import main

from pandemia import infected


class TestPandemia(TestCase):
    def test_infected(self):
        test_patterns = [
            ("01000000X000X011X0X",73.33333333333333),
            ("01X000X010X011XX", 72.72727272727273),
            ("XXXXX", 0),
            ("00000000X00X0000", 0),
            ("0000000010", 100),
            ("000001XXXX0010X1X00010", 100),
            ("X00X000000X10X0100",42.857142857142854),
        ]
        for m, expected in test_patterns:
            with self.subTest(m=m, expected=expected):
                self.assertEqual(infected(s=m), expected)


if __name__ == "__main__":
    main(verbosity=2)
