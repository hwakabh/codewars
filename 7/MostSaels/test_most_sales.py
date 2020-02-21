from unittest import TestCase
from unittest import main

from most_sales import top3


class TestMostSales(TestCase):
    # Test class of most_sales
    def test_top3(self):
        test_patterns = [
            (
                ['Computer', 'Cell Phones', 'Vacuum Cleaner'], [3,24,8], [199,299,399],
                ['Cell Phones', 'Vacuum Cleaner', 'Computer']
            ),(
                ['Cell Phones', 'Vacuum Cleaner', 'Computer', 'Autos', 'Gold', 'Fishing Rods', 'Lego', ' Speakers'], [5, 25, 2, 7, 10, 3, 2, 24], [51, 225, 22, 47, 510, 83, 82, 124],
                ['Vacuum Cleaner', 'Gold', ' Speakers']
            ),(
                ['Cell Phones', 'Vacuum Cleaner', 'Computer', 'Autos', 'Gold', 'Fishing Rods', 'Lego', ' Speakers'], [0, 12, 24, 17, 19, 23, 120, 8], [9, 24, 29, 31, 51, 8, 120, 14],
                ['Lego', 'Gold', 'Computer']
            )
        ]

        for product, amount, price, expected in test_patterns:
            with self.subTest(product=product, amount=amount, price=price, expected=expected):
                self.assertEqual(top3(products=product, amounts=amount, prices=price), expected)


if __name__ == "__main__":
    main(verbosity=2)