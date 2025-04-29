from unittest import TestCase
from unittest import main

from .largest_product_in_a_series import greatest_product


class TestLargestProductInASeries(TestCase):
    def test_greatest_product(self):
        ptr = [
            ('123834539327238239583', 3240),
            ('395831238345393272382', 3240),
            ('92494737828244222221111111532909999', 5292),
            ('02494037820244202221011110532909999', 0),
        ]
        for inp, exp in ptr:
            with self.subTest(inp=inp, exp=exp):
                self.assertEqual(greatest_product(n=inp), exp)


if __name__ == "__main__":
    main(verbosity=2)
