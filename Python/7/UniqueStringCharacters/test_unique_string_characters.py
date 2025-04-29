from unittest import TestCase
from unittest import main

from .unique_string_characters import solve


class TestUniqueStringCharacters(TestCase):
    def test_solve(self):
        ptr = [
            ('xyab', 'xzca', 'ybzc'),
            ('xyabb', 'xzca', 'ybbzc'),
            ('abcd', 'xyz', 'abcdxyz'),
            ('xxx', 'xzca', 'zca'),
        ]
        for x, y, exp in ptr:
            with self.subTest(x=x, y=y, exp=exp):
                self.assertEqual(solve(a=x, b=y), exp)


if __name__ == '__main__':
    main(verbosity=2)
