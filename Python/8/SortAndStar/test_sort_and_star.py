from unittest import TestCase
from unittest import main

from .sort_and_star import two_sort


class TestSortAndStar(TestCase):
    def test_two_sort(self):
        ptr = [
            (['bitcoin', 'take', 'over', 'the', 'world', 'maybe', 'who', 'knows', 'perhaps'], 'b***i***t***c***o***i***n'),
            (['turns', 'out', 'random', 'test', 'cases', 'are', 'easier', 'than', 'writing', 'out', 'basic', 'ones'], 'a***r***e'),
            (['lets', 'talk', 'about', 'javascript', 'the', 'best', 'language'], 'a***b***o***u***t'),
            (['i', 'want', 'to', 'travel', 'the', 'world', 'writing', 'code', 'one', 'day'], 'c***o***d***e'),
            (['Lets', 'all', 'go', 'on', 'holiday', 'somewhere', 'very', 'cold'], 'L***e***t***s'),
        ]
        for inp, exp in ptr:
            with self.subTest(inp=inp, exp=exp):
                self.assertEqual(two_sort(array=inp), exp)


if __name__ == "__main__":
    main(verbosity=2)
