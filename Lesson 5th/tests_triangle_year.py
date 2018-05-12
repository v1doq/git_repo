import unittest
from Task7 import triangle
from Task6 import is_year_leap
from Task6 import triangles


class TestTriangle(unittest.TestCase):
    def test_zero(self):
        res = triangle(2, 5, 1)
        self.assertEqual(res, "It is not a triangle")
    def test_one(self):
        res = triangle(2,2,2)
        self.assertEqual(res,'It is a Equilateral triangle')
    def test_two(self):
        res = triangle(2,3,4)
        self.assertEqual(res, 'It is a Versatile triangle')
    def test_three(self):
        res = triangle(2,3,3)
        self.assertEqual(res, 'It is a Isosceles triangle')

class TestYear(unittest.TestCase):
    def test_high_year(self):
        res = is_year_leap(1999)
        self.assertFalse(res)
    def test_low_year(self):
        res = is_year_leap(1996)
        self.assertTrue(res)

class TestTriangles(unittest.TestCase):
    def test_one(self):
        res = triangles(2,5,1)
        self.assertFalse(res)
    def test_two(self):
        res = triangles(5,1,2)
        self.assertTrue(res)