from unittest import TestCase
from unittest import main

from sum_two_smallest import sum_two_smallest_numbers

class TestSumTwoSmallest(TestCase):
    # Test class of SumTwoSmallest

    def test_sum_two_smallest_numbers(self):
        test_patterns = [
            ([5, 8, 12, 18, 22], 13),   #-> Expect OK
            ([7, 15, 12, 18, 22], 19),  #-> Expect OK
            ([25, 42, 12, 18, 22], 30), #-> Expect OK
            ([19, 5, 42, 2, 77], 7),    #-> Expect OK
            ([10, 343445353, 3453445, 3453545353453], 3453455), #-> Expect OK
            # ([5, 4, 1, 2, 3], 4)    #-> Wrong Case
        ]

        for input_numbers, answer in test_patterns:
            with self.subTest(input_numbers=input_numbers, answer=answer):
                self.assertEqual(sum_two_smallest_numbers(numbers=input_numbers), answer)

if __name__ == '__main__':
    main(verbosity=2)
