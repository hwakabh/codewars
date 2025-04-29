from unittest import TestCase
from unittest import main

from .school_paperwork import paperwork


class TestSchoolPaperwork(TestCase):
    def test_paperwork(self):
        ptr = [
            (5, 5, 25),
            (5, -5, 0),
            (-5, -5, 0),
            (5, 0, 0),
        ]
        for s, p, exp in ptr:
            with self.subTest(s=s, p=p, exp=exp):
                self.assertEqual(paperwork(n=s, m=p), exp)


if __name__ == "__main__":
    main(verbosity=2)
