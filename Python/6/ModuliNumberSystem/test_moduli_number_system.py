from unittest import TestCase
from unittest import main

from .moduli_number_system import fromNb2Str


class TestModuliNumberSystem(TestCase):
    # Test class of moduli_number_system
    def test_fromNb2Str(self):
        test_patterns = [
            (779, [8, 7, 5, 3], '-3--2--4--2-'),
            (15, [8, 6, 5, 3], 'Not applicable'),
            (3450, [17, 5, 3], 'Not applicable'),
            (3450, [13, 11, 7, 5, 3, 2], '-5--7--6--0--0--0-'),
        ]
        for n, nums, expected in test_patterns:
            with self.subTest(n=n, nums=nums, expected=expected):
                self.assertEqual(fromNb2Str(n=n, modsys=nums), expected)


if __name__ == '__main__':
    main(verbosity=2)
