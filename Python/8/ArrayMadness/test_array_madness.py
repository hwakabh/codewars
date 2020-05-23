from unittest import TestCase
from unittest import main

from array_madness import array_madness


class TestArrayMadness(TestCase):
    def test_array_madness(self):
        ptr = [
            ([4, 5, 6], [1, 2, 3], True),
            ([1, 2, 3],[4, 5, 6], False),
        ]
        for x, y, exp in ptr:
            with self.subTest(x=x, y=y, exp=exp):
                self.assertEqual(array_madness(a=x, b=y), exp)


if __name__ == "__main__":
    main(verbosity=2)
