from unittest import TestCase
from unittest import main

from .vaporcode import vaporcode


class TestVaporcode(TestCase):
    def test_vaporcode(self):
        test_patterns = [
            ("Lets go to the movies", "L  E  T  S  G  O  T  O  T  H  E  M  O  V  I  E  S"),
            ("Why isn't my code working?", "W  H  Y  I  S  N  '  T  M  Y  C  O  D  E  W  O  R  K  I  N  G  ?"),
        ]
        for inp, exp in test_patterns:
            with self.subTest(inp=inp, exp=exp):
                self.assertEqual(vaporcode(s=inp), exp)


if __name__ == "__main__":
    main(verbosity=2)
