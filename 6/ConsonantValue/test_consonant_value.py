from unittest import TestCase
from unittest import main

from consonant_value import solve


class TestConsonantValue(TestCase):
    def test_solve(self):
        test_patterns = [
            ('zodiac', 26),
            ('chruschtschov', 80),
            ('khrushchev', 38),
            ('strength', 57),
            ('catchphrase', 73),
            ('twelfthstreet', 103),
            ('mischtschenkoana', 80),
        ]
        for inp, exp in test_patterns:
            with self.subTest(inp=inp, exp=exp):
                self.assertEqual(solve(s=inp), exp)


if __name__ == '__main__':
    main(verbosity=2)
