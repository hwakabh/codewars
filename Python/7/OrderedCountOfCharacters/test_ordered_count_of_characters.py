from unittest import TestCase
from unittest import main

from ordered_count_of_characters import ordered_count


class TestOrderedCountOfCharacters(TestCase):
    def test_ordered_count(self):
        ptr = [
            ('abracadabra', [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]),
            ('Code Wars', [('C', 1), ('o', 1), ('d', 1), ('e', 1), (' ', 1), ('W', 1), ('a', 1), ('r', 1), ('s', 1)]),
        ]
        for inp, exp in ptr:
            with self.subTest(inp=inp, exp=exp):
                self.assertEqual(ordered_count(inp=inp), exp)


if __name__ == "__main__":
    main(verbosity=2)
