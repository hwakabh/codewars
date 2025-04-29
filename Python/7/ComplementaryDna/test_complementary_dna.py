from unittest import TestCase
from unittest import main

from .complementary_dna import DNA_stand


class TestComplementaryDna(TestCase):
    # Test class of complementary_dna
    def test_DNA_stand(self):
        test_patterns = [
            ('AAAA', 'TTTT'),
            ('ATTGC', 'TAACG'),
            ('GTAT', 'CATA'),
            # ('GGCC', 'GGCC') #-> Wrong Case
        ]

        for d, expected in test_patterns:
            with self.subTest(d=d, expected=expected):
                self.assertEqual(DNA_stand(dna=d), expected)


if __name__ == "__main__":
    main(verbosity=2)
