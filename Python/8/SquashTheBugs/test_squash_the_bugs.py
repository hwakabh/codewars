from unittest import TestCase
from unittest import main

from squash_the_bugs import find_longest


class SquashTheBugs(TestCase):
    def test_find_longest(self):
        test_patterns = [
            ('The quick white fox jumped around the massive dog', 7),
            ('Take me to tinseltown with you', 10),
            ('Sausage chops', 7),
            ('Wind your body and wiggle your belly', 6),
            ('Lets all go on holiday', 7),
        ]
        for s, exp in test_patterns:
            with self.subTest(s=s, exp=exp):
                self.assertEqual(find_longest(string=s), exp)


if __name__ == "__main__":
    main(verbosity=2)
