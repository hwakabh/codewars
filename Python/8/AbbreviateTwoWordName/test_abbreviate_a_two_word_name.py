from unittest import TestCase
from unittest import main

from abbreviate_a_two_word_name import abbrevName


class TestAbbreviateATwoWordName(TestCase):
    def test_abbrevName(self):
        ptr = [
            ('Sam Harris', 'S.H'),
            ('Patrick Feenan', 'P.F'),
            ('Evan Cole', 'E.C'),
            ('P Favuzzi', 'P.F'),
            ('David Mendieta', 'D.M'),
        ]
        for inp, exp in ptr:
            with self.subTest(inp=inp, exp=exp):
                self.assertEqual(abbrevName(name=inp), exp)


if __name__ == '__main__':
    main(verbosity=2)
