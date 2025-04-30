from unittest import TestCase
from unittest import main

from .what_is_the_real_floor import get_real_floor


class TestWhatIsTheRealFloor(TestCase):
    def test_get_real_floor(self):
        test_patterns = [
            (1, 0),
            (5, 4),
            (15, 13),
        ]
        for inp, exp in test_patterns:
            with self.subTest(inp=inp, exp=exp):
                self.assertEqual(get_real_floor(n=inp), exp)


if __name__ == "__main__":
    main(verbosity=2)
