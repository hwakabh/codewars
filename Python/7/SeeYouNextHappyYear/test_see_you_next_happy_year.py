from unittest import TestCase
from unittest import main

from .see_you_next_happy_year import next_happy_year


class TestSeeYouNextHappyYear(TestCase):
    def test_next_happy_year(self):
        test_patterns = [
            (1001, 1023),
            (1123, 1203),
            (2001, 2013),
            (2334, 2340),
            (3331, 3401),
            (1987, 2013),
            (5555, 5601),
            (7712, 7801),
            (8088, 8091),
            (8999, 9012),
        ]
        for inp, exp in test_patterns:
            with self.subTest(inp=inp, exp=exp):
                self.assertEqual(next_happy_year(year=inp), exp)


if __name__ == "__main__":
    main(verbosity=2)
