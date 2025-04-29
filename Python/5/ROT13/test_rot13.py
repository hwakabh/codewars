from unittest import TestCase
from unittest import main

from .rot13 import rot13


class TestRot13(TestCase):
    def test_rot13(self):
        ptr = [
            ('EBG13 rknzcyr.', 'ROT13 example.'),
            ('ROT13 example.', 'EBG13 rknzcyr.'),
        ]
        for inp, exp in ptr:
            with self.subTest(inp=inp, exp=exp):
                self.assertEqual(rot13(message=inp), exp)


if __name__ == "__main__":
    main(verbosity=2)
