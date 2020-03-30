from unittest import TestCase
from unittest import main

from remove_string_spaces import no_space


class TestRemoveStringSpaces(TestCase):
    def test_no_space(self):
        ptr = [
            ('8 j 8   mBliB8g  imjB8B8  jl  B', '8j8mBliB8gimjB8B8jlB'),
            ('8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd', '88Bifk8hB8BB8BBBB888chl8BhBfd'),
            ('8aaaaa dddd r     ', '8aaaaaddddr'),
            ('jfBm  gk lf8hg  88lbe8 ', 'jfBmgklf8hg88lbe8'),
            ('8j aam', '8jaam'),
        ]
        for inp, exp in ptr:
            with self.subTest(inp=inp, exp=exp):
                self.assertEqual(no_space(x=inp), exp)


if __name__ == "__main__":
    main(verbosity=2)
