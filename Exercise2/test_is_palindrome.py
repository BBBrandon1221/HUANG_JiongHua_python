import unittest

try:
    from Exercise2.is_palindrome import is_palindrome
except ImportError:
    from is_palindrome import is_palindrome


class TestIsPalindrome(unittest.TestCase):
    """Lecture07 Exercise 2 Task1：用这些测试找出 is_palindrome 里的错误。"""

    def test_odd_length_palindrome(self):
        self.assertTrue(is_palindrome("racecar"), msg="'racecar' 是回文，应返回 True")

    def test_even_length_palindrome(self):
        self.assertTrue(is_palindrome("abba"), msg="'abba' 是回文，应返回 True")

    def test_ignore_case_and_spaces(self):
        self.assertTrue(is_palindrome("A man a plan a canal Panama"),
                        msg="忽略大小写和空格后是回文，应返回 True")

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("hello"), msg="'hello' 不是回文，应返回 False")

    def test_digits(self):
        self.assertTrue(is_palindrome("1221"), msg="'1221' 是回文，应返回 True")


if __name__ == "__main__":
    unittest.main()
