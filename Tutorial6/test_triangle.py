import unittest

try:
    from Tutorial6.triangle import Triangle, TriangleType
except ImportError:
    from triangle import Triangle, TriangleType


class TestTriangle(unittest.TestCase):
    """规则：三边为数字(int/float, 非 bool)且 >0；任意两边之和严格大于第三边；
    get_type 返回等边/等腰/不等边或 None；get_area 用 Heron 公式保留 4 位。"""

    def test_valid_triangle(self):
        self.assertTrue(Triangle(3, 4, 5).is_valid())

    def test_sides_false(self):
        self.assertFalse(Triangle("3", 4, 5).is_valid())    # 非数字
        self.assertFalse(Triangle(True, 4, 5).is_valid())   # bool 不算数字
        self.assertFalse(Triangle(0, 4, 5).is_valid())      # 边长必须 > 0
        self.assertFalse(Triangle(-3, 4, 5).is_valid())

    def test_invalid_triangle_returns_none(self):
        t = Triangle(1, 2, 3)          # 1+2 == 3，不满足严格大于
        self.assertFalse(t.is_valid())
        self.assertIsNone(t.get_type())
        self.assertIsNone(t.get_area())

    def test_valid_types_returns_kind(self):
        self.assertEqual(Triangle(3, 3, 3).get_type(), TriangleType.EQUILATERAL)
        self.assertEqual(Triangle(3, 3, 4).get_type(), TriangleType.ISOSCELES)
        self.assertEqual(Triangle(3, 4, 5).get_type(), TriangleType.SCALENE)

    def test_area_heron_rounded_4(self):
        self.assertEqual(Triangle(3, 4, 5).get_area(), 6.0)
        self.assertEqual(Triangle(2, 3, 4).get_area(), 2.9047)


if __name__ == "__main__":
    unittest.main()
