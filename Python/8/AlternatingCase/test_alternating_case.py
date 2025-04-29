from unittest import TestCase
from unittest import main

from .alternating_case import to_alternating_case


class TestAlternatingCase(TestCase):
    def test_to_alternating_case(self):
        ptr = [
            ('hello world', 'HELLO WORLD'),
            ('HELLO WORLD', 'hello world'),
            ('hello WORLD', 'HELLO world'),
            ('HeLLo WoRLD', 'hEllO wOrld'),
            ('12345', '12345'),
            ('1a2b3c4d5e', '1A2B3C4D5E'),
            ('String.prototype.toAlternatingCase', 'sTRING.PROTOTYPE.TOaLTERNATINGcASE'),
        ]
        for inp, exp in ptr:
            with self.subTest(inp=inp, exp=exp):
                self.assertEqual(to_alternating_case(string=inp), exp)


if __name__ == '__main__':
    main(verbosity=2)
