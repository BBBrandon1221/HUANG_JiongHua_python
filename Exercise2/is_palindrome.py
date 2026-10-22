# Lecture07 Exercise 2 —— PPT 原始"带 bug"版本（Task 1 用测试找出这里的错）
# 已知 bug：镜像索引 s[-i] 应为 s[-i-1]（Task 2 时自己修，别提前看答案）

def is_palindrome(s):
    s = s.lower()
    s = s.replace(" ", "")
    for i in range(len(s) // 2):
        if s[i] != s[-i-1]:
            return False
    return True
