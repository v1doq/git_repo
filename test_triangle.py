import unittest
from Task7 import triangle


class test_triangle(unittest.TestCase):
    def test_zero(self):
        res = triangle(2, 5, 1)
        self.assertEqual(res, "It is not a triangle")
