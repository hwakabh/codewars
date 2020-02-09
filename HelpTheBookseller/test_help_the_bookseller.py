from unittest import TestCase
from unittest import main

from help_the_bookseller import stock_list


class TestHelpTheBookseller(TestCase):
    # Test class of help_the_bookseller
    def test_stock_list(self):
        test_patterns = [
            (["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"], ["A", "B"], "(A : 200) - (B : 1140)"),
        ]
        for l, m, expected in test_patterns:
            with self.subTest(l=l, m=m, expected=expected):
                self.assertEqual(stock_list(listOfArt=l, listOfCat=m), expected)


if __name__ == "__main__":
    main(verbosity=2)
