import unittest

try:
    from Tutorial6.parking_fee import ParkingFeeCalculator
except ImportError:
    from parking_fee import ParkingFeeCalculator


class TestValidHours(unittest.TestCase):
    """规则：首小时免费；之后每小时 $10（不足一小时进一）；每 24h 封顶 $80；
    超 24h = 整天数 × $80 + 余量费用；返回保留 2 位小数。"""

    def setUp(self):
        self.calc = ParkingFeeCalculator()

    def test_first_day_calculator_readme_table(self):
        self.assertEqual(self.calc.calculate_fee(1), 0.0)
        self.assertEqual(self.calc.calculate_fee(1.5), 10.0)
        self.assertEqual(self.calc.calculate_fee(2), 10.0)
        self.assertEqual(self.calc.calculate_fee(9), 80.0)
        self.assertEqual(self.calc.calculate_fee(26), 90.0)

    def test_first_hour_free(self):
        self.assertEqual(self.calc.calculate_fee(0.5), 0.0)

    def test_partial_hour_rounded_up(self):
        self.assertEqual(self.calc.calculate_fee(2.2), 20.0)   # 1.2h 计费 → 进一为 2h

    def test_daily_cap_80(self):
        self.assertEqual(self.calc.calculate_fee(12), 80.0)
        self.assertEqual(self.calc.calculate_fee(24), 80.0)

    def test_multi_day(self):
        self.assertEqual(self.calc.calculate_fee(25), 80.0)    # 80 + 首小时免费
        self.assertEqual(self.calc.calculate_fee(48), 160.0)


class TestZeroOrNegativeHours(unittest.TestCase):
    """规则：hours 必须是正数（int/float，非 bool），否则返回 None。"""

    def setUp(self):
        self.calc = ParkingFeeCalculator()

    def test_zero_or_negative_hours_return_none(self):
        self.assertIsNone(self.calc.calculate_fee(0))
        self.assertIsNone(self.calc.calculate_fee(-3))

    def test_bool_returns_none(self):
        self.assertIsNone(self.calc.calculate_fee(True))
        self.assertIsNone(self.calc.calculate_fee(False))

    def test_not_number_returns_none(self):
        self.assertIsNone(self.calc.calculate_fee("5"))
        self.assertIsNone(self.calc.calculate_fee(None))


if __name__ == "__main__":
    unittest.main()
