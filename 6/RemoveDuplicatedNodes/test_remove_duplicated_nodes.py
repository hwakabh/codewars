from unittest import TestCase
from unittest import main

from remove_duplicated_nodes import remove_duplicate


class TestRemoveDuplicatedNodes(TestCase):
    def test_remove_duplicate(self):
        inp = [
            {'data': {'id': 'A'}},
            {'data': {'id': 'A'}},
            {'data': {'id': 'B'}},
            {'data': {'id': 'B'}},
            {'data': {'id': 'C'}},
            {'data': {'id': 'C'}},
            {'data': {'id': 'D'}},
        ]
        exp = [
            {'data': {'id': 'A'}},
            {'data': {'id': 'B'}},
            {'data': {'id': 'C'}},
            {'data': {'id': 'D'}},
        ]
        self.assertEqual(remove_duplicate(arr=inp), exp)


if __name__ == "__main__":
    main(verbosity=2)
