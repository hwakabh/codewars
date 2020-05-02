from unittest import TestCase
from unittest import main

from removing_elements import remove_every_other


class TestRemovingElements(TestCase):
    def test_remove_every_other(self):
        test_patterns = [
            (['Hello', 'Goodbye', 'Hello Again'], ['Hello', 'Hello Again']),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 3, 5, 7, 9]),
            ([[1, 2]], [[1, 2]]),
            ([['Goodbye'], {'Great': 'Job'}], [['Goodbye']]),
        ]
        for inp, exp in test_patterns:
            with self.subTest(inp=inp, exp=exp):
                self.assertEqual(remove_every_other(my_list=inp), exp)


if __name__ == "__main__":
    main(verbosity=2)
