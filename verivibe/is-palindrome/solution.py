def is_palindrome(s: str) -> bool:
    """
    判断 s 去掉空格、忽略大小写后是否回文。

    >>> # TODO: 写你的例子
    >>> is_palindrome("A man, a plan, a canal: Panama")
    True
    >>> is_palindrome("racecar")
    True
    >>> is_palindrome("1221")
    True
    """
    # TODO: 写实现
    cleaned = "".join(ch.lower() for ch 
                      in s if ch.isalnum())
    return cleaned == cleaned[::-1]


# --- 下面别改 ---
if __name__ == "__main__":
    import doctest
    doctest.testmod()
