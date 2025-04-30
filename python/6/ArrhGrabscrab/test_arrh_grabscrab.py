from unittest import TestCase
from unittest import main

from .arrh_grabscrab import grabscrab


class TestArrhGrabscrab(TestCase):
    # Test class of arrh_grabscrab
    def test_grabscrab(self):
        test_patterns = [
            ("trisf", ["first"], ["first"]),
            ("oob", ["bob", "baobab"], []),
            ("ainstuomn", ["mountains", "hills", "mesa"], ["mountains"]),
            ("oolp", ["donkey", "pool", "horse", "loop"], ["pool", "loop"]),
            ("ortsp", ["sport", "parrot", "ports", "matey"], ["sport", "ports"]),
            ("ourf", ["one","two","three"], []),
        ]
        for w, words, expected in test_patterns:
            with self.subTest(w=w, words=words, expected=expected):
                self.assertEqual(grabscrab(word=w, possible_words=words), expected)


if __name__ == "__main__":
    main(verbosity=2)
