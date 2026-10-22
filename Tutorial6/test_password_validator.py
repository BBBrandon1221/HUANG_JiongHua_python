import unittest

try:
    from Tutorial6.password_validator import validate_password
except ImportError:
    from password_validator import validate_password


class TestPasswordValidator(unittest.TestCase):
    """规则：str；长度 8-20（含边界）；无空白；必含大写+小写+数字+特殊字符。"""

    def test_valid_input_returns_true(self):
        self.assertTrue(validate_password("Abcdef1!"))

    def test_length_boundary_8_and_20_valid(self):
        self.assertTrue(validate_password("Aa1!Aa1!"))                    # 8 位
        self.assertTrue(validate_password("Aa1!Aa1!Aa1!Aa1!Aa1!"))        # 20 位

    def test_not_string_returns_false(self):
        self.assertFalse(validate_password(12345678))
        self.assertFalse(validate_password(None))
        self.assertFalse(validate_password(["Aa1!Aa1!"]))

    def test_invalid_length_returns_false(self):
        self.assertFalse(validate_password("Ab1!Ab1"))                     # 7 位
        self.assertFalse(validate_password("Aa1!Aa1!Aa1!Aa1!Aa1!Aa"))      # 22 位

    def test_with_space_returns_false(self):
        self.assertFalse(validate_password("Abcde f1!"))
        self.assertFalse(validate_password("Abcdef1!\t"))                  # 制表符也算空白

    def test_missing_uppercase_returns_false(self):
        self.assertFalse(validate_password("abcdef1!"))

    def test_missing_lowercase_returns_false(self):
        self.assertFalse(validate_password("ABCDEF1!"))

    def test_missing_digit_returns_false(self):
        self.assertFalse(validate_password("Abcdefg!"))

    def test_missing_special_returns_false(self):
        self.assertFalse(validate_password("Abcdef12"))


if __name__ == "__main__":
    unittest.main()
