from unittest import TestCase
from unittest import main

from grade_book import get_grade


class TestGradeBook(TestCase):
    def test_get_grade(self):
        test_patterns = [
            # Check should return A
            (95, 90, 93, "A"),
            (100, 85, 96, "A"),
            (92, 93, 94, "A"),
            # Check should return B
            (70, 70, 100, "B"),
            (82, 85, 87, "B"),
            (84, 79, 85, "B"),
            # Check should return C
            (70, 70, 70, "C"),
            (75, 70, 79, "C"),
            (60, 82, 76, "C"),
            # Check should return D
            (65, 70, 59, "D"),
            (66, 62, 68, "D"),
            (58, 62, 70, "D"),
            # Check should return F
            (44, 55, 52, "F"),
            (48, 55, 52, "F"),
            (58, 59, 60, "F"),
        ]
        for i, j, k, exp in test_patterns:
            with self.subTest(i=i, j=j, k=k, exp=exp):
                self.assertEqual(get_grade(s1=i, s2=j, s3=k), exp)


if __name__ == "__main__":
    main(verbosity=2)
