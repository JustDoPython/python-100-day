import unittest
from enum import Enum


class EnumExtend(unittest.TestCase):

    def test_extending(self):
        class Color(Enum):
            red = 1
            green = 2
            blue = 3

        # TypeError: Cannot extend enumerations
        with self.assertRaises(TypeError):
            class MoreColor(Color):
                cyan = 4
                magenta = 5
                yellow = 6

    def test_extending2(self):
        class Shade(Enum):
            def shade(self):
                print(self.name)

        class Color(Shade):
            red = 1
            green = 2
            blue = 3
        with self.assertRaises(TypeError):
            class MoreColor(Color):
                cyan = 4
                magenta = 5
                yellow = 6

    def test_extending3(self):
        class Shade(Enum):
            def shade(self):
                return self.name

        class Color(Shade):
            def hex(self):
                return '%s nice!' % self.value

        class MoreColor(Color):
            cyan = 4
            magenta = 5
            yellow = 6
        self.assertEqual(MoreColor.magenta.shade(), 'magenta')
        self.assertEqual(MoreColor.magenta.hex(), '5 nice!')

