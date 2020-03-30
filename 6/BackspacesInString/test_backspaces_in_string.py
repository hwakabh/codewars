from unittest import TestCase
from unittest import main

from backspaces_in_string import clean_string


class TestBackspacesInString(TestCase):
    def test_clean_string(self):
        ptr = [
            ('a#bc#d', 'bd'),
            ('abc#d##c', 'ac'),
            ('abc####d##c#', ''),
            ('#######', ''),
            ('', ''),
        ]
        for inp, exp in ptr:
            with self.subTest(inp=inp, exp=exp):
                self.assertEqual(clean_string(s=inp), exp)


if __name__ == "__main__":
    main(verbosity=2)
