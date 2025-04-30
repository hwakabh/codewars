from unittest import TestCase
from unittest import main

from .string_letter_counting import string_letter_count


class TestStringLetterCounting(TestCase):
    def test_string_letter_count(self):
        ptr = [
            ('The quick brown fox jumps over the lazy dog.', '1a1b1c1d3e1f1g2h1i1j1k1l1m1n4o1p1q2r1s2t2u1v1w1x1y1z'),
            ('The time you enjoy wasting is not wasted time.', '2a1d5e1g1h4i1j2m3n3o3s6t1u2w2y'),
            ('./4592#{}()', ''),
        ]
        for inp, exp in ptr:
            with self.subTest(inp=inp, exp=exp):
                self.assertEqual(string_letter_count(s=inp), exp)


if __name__ == '__main__':
    main(verbosity=2)
