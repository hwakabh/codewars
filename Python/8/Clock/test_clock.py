from unittest import TestCase
from unittest import main

from clock import past


class TestClock(TestCase):
    def test_past(self):
        ptr = [
            (0, 1, 1, 61000),
            (1, 1, 1, 3661000),
            (0, 0, 0, 0),
            (1, 0, 1, 3601000),
            (1, 0, 0, 3600000),
        ]
        for hr, mn, sc, exp in ptr:
            with self.subTest(hr=hr, mn=mn, sc=sc, exp=exp):
                self.assertEqual(past(h=hr, m=mn, s=sc), exp)


if __name__ == "__main__":
    main(verbosity=2)
