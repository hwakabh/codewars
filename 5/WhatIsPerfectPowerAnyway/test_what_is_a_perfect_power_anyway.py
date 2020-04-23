from unittest import TestCase
from unittest import main
from random import randint

from what_is_a_perfect_power_anyway import isPP


class TestWhatIsAPerfectPowerAnyway(TestCase):
    def test_isPP(self):
        # static
        ptr = [
            (4, [2, 2]),
            (9, [3, 2]),
            (5, None),
        ]
        for inp, exp in ptr:
            with self.subTest(inp=inp, exp=exp):
                self.assertEqual(isPP(n=inp), exp)


if __name__ == "__main__":
    main(verbosity=2)
