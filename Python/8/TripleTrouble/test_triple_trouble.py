from unittest import TestCase
from unittest import main

from .triple_trouble import triple_trouble


class TestTripleTrouble(TestCase):
    def test_triple_trouble(self):
        test_patterns = [
            ('aaa', 'bbb', 'ccc', 'abcabcabc'),
            ('aaaaaa', 'bbbbbb', 'cccccc', 'abcabcabcabcabcabc'),
            ('burn', 'reds', 'roll', 'brrueordlnsl'),
            ('Bm', 'aa', 'tn', 'Batman'),
            ('LLh', 'euo', 'xtr', 'LexLuthor'),
        ]
        for x, y, z, exp in test_patterns:
            with self.subTest(x=x, y=y, z=z, exp=exp):
                self.assertEqual(triple_trouble(one=x, two=y, three=z), exp)


if __name__ == '__main__':
    main(verbosity=2)
