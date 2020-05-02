from unittest import TestCase
from unittest import main

from draw_stairs import draw_stairs


class TestDrawStairs(TestCase):
    def test_draw_stairs(self):
        ptr = [
            (3, '''I\n I\n  I'''),
        ]
        for inp, exp in ptr:
            with self.subTest(inp=inp, exp=exp):
                self.assertEqual(draw_stairs(n=inp), exp)


if __name__ == "__main__":
    main(verbosity=2)
