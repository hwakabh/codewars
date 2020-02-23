from unittest import  TestCase
from unittest import main

from how_good_are_you_really import better_than_average


class TestHowGoodAreYouReally(TestCase):
    def test_better_than_average(self):
        test_patterns = [
            ([2, 3], 5, True),
            ([100, 40, 34, 57, 29, 72, 57, 88], 75, True),
            ([12, 23, 34, 45, 56, 67, 78, 89, 90], 69, True),
        ]
        for c, y, exp in test_patterns:
            with self.subTest(c=c, y=y, exp=exp):
                self.assertEqual(better_than_average(class_points=c, your_points=y), exp)


if __name__ == "__main__":
    main(verbosity=2)
