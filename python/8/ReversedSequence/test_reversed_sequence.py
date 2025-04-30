from unittest import TestCase
from unittest import main

from .reversed_sequence import reverse_seq


class TestReversedSequence(TestCase):
    # Test Class of reversed_sequence
    def test_reverse_seq(self):
        nums = 5
        expected = [5,4,3,2,1]
        self.assertEqual(reverse_seq(n=nums), expected)


if __name__ == "__main__":
    main(verbosity=2)
