import unittest
from enum import Enum


class TestOrder(unittest.TestCase):

    def test_same_members(self):
        class Color(Enum):
            _order_ = 'red green blue'
            red = 1
            green = 2
            blue = 3

    def test_same_members_with_aliases(self):
        class Color(Enum):
            _order_ = 'red green blue'
            red = 1
            green = 2
            blue = 3
            verde = green

    def test_same_members_wrong_order(self):
        with self.assertRaisesRegex(TypeError, 'member order does not match _order_'):
            class Color(Enum):
                _order_ = 'red green blue'
                red = 1
                blue = 3
                green = 2

    def test_order_has_extra_members(self):
        with self.assertRaisesRegex(TypeError, 'member order does not match _order_'):
            class Color(Enum):
                _order_ = 'red green blue purple'
                red = 1
                green = 2
                blue = 3

    def test_order_has_extra_members_with_aliases(self):
        with self.assertRaisesRegex(TypeError, 'member order does not match _order_'):
            class Color(Enum):
                _order_ = 'red green blue purple'
                red = 1
                green = 2
                blue = 3
                verde = green

    def test_enum_has_extra_members(self):
        with self.assertRaisesRegex(TypeError, 'member order does not match _order_'):
            class Color(Enum):
                _order_ = 'red green blue'
                red = 1
                green = 2
                blue = 3
                purple = 4

    def test_enum_has_extra_members_with_aliases(self):
        with self.assertRaisesRegex(TypeError, 'member order does not match _order_'):
            class Color(Enum):
                _order_ = 'red green blue'
                red = 1
                green = 2
                blue = 3
                purple = 4
                verde = green
