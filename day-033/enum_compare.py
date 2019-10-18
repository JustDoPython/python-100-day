import unittest
from enum import Enum, IntEnum

class TestEnum(unittest.TestCase):
    class Season(IntEnum):
        SPRING = 1
        SUMMER = 2
        AUTUMN = 3
        WINTER = 4

    def test_comparisons(self):
        season = self.Season

        self.assertEqual(season.SPRING, 1)

        class Part(Enum):
            SPRING = 1
            CLIP = 2
            BARREL = 3

        self.assertNotEqual(Part.SPRING, 1)
        self.assertNotEqual(Part.SPRING, season.SPRING)

TestEnum().test_comparisons()
