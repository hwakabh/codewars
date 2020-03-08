from unittest import TestCase
from unittest import main

from alternative_capitalization import capitalize


class TestAlternativeCapitalization(TestCase):
    def test_capitalize(self):
        test_patterns = [
            ('abcdef', ['AbCdEf', 'aBcDeF']),
            ('codewars', ['CoDeWaRs', 'cOdEwArS']),
            ('abracadabra', ['AbRaCaDaBrA', 'aBrAcAdAbRa']),
            ('codewarriors', ['CoDeWaRrIoRs', 'cOdEwArRiOrS']),
        ]
        for inp, exp in test_patterns:
            with self.subTest(inp=inp, exp=exp):
                self.assertEqual(capitalize(s=inp), exp)


if __name__ == '__main__':
    main(verbosity=2)
