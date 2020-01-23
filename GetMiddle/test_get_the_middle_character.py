from unittest import TestCase
from unittest import main

from get_the_middle_character import get_middle

class TestGetMiddle(TestCase):
    # Test Class of get_middle()
    def test_get_middle(self):
        test_patterns = [
            ('test', 'es'),
            ('testing', 't'),
            ('middle', 'dd'),
            ('A', 'A'),
            # ('abc', 'c') #-> Wrong Case
        ]

        for word, ans in test_patterns:
            with self.subTest(word=word, ans=ans):
                self.assertEqual(get_middle(s=word), ans)

if __name__ == '__main__':
    main(verbosity=2)
