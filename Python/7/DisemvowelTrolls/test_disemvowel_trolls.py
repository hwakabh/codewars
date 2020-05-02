from unittest import TestCase
from unittest import main

from disemvowel_trolls import disemvowel


class TestDisemvowelTrolles(TestCase):
    def test_disemvowel(self):
        ptr = [
            ('This website is for losers LOL!', 'Ths wbst s fr lsrs LL!'),
        ]
        for inp, exp in ptr:
            with self.subTest(inp=inp, exp=exp):
                self.assertEqual(disemvowel(string=inp), exp)


if __name__ == "__main__":
    main(verbosity=2)
