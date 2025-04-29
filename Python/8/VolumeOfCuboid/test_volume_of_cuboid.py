from unittest import TestCase
from unittest import main

from .volume_of_cuboid import getVolumeOfCuboid


class TestVolumeOfCuboid(TestCase):
    def test_getVolumeOfCuboid(self):
        test_patterns = [
            (1, 2, 2, 4),
            (6.3, 2, 5, 63),
        ]
        for l, w, h, expected in test_patterns:
            with self.subTest(l=l, w=w, h=w, expected=expected):
                self.assertEqual(getVolumeOfCuboid(length=l, width=w, height=h), expected)


if __name__ == "__main__":
    main(verbosity=2)
