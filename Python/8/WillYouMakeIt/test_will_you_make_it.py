from unittest import TestCase
from unittest import main

from .will_you_make_it import zero_fuel


class TestWillYouMakeIt(TestCase):
    def test_zero_fuel(self):
        test_patterns = [
            (50, 25, 2, True),
            (100, 50, 1, False),
        ]
        for d, m, f, exp in test_patterns:
            with self.subTest(d=d, m=m, f=f, exp=exp):
                self.assertEqual(zero_fuel(distance_to_pump=d, mpg=m, fuel_left=f), exp)


if __name__ == "__main__":
    main(verbosity=2)
