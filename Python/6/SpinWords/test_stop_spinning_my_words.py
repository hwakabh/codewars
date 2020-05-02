from unittest import TestCase
from unittest import main

from stop_spinning_my_words import spin_words

class TestStopSpinningMyWords(TestCase):
    # Test Class of stop_spinning_my_words
    def test_spin_words(self):
        test_patterns = [
            ('Hey fellow warriors', 'Hey wollef sroirraw'),
            ('This is a test', 'This is a test'),
            ('This is another test', 'This is rehtona test'),
            ('Welcome', 'emocleW'),
            # ('spinning', 'spinning')    #-> Wrong Case
        ]

        for s, expected in test_patterns:
            with self.subTest(s=s, expected=expected):
                self.assertEqual(spin_words(sentence=s), expected)

if __name__ == '__main__':
    main(verbosity=2)
