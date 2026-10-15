def sleep_in(weekday: bool, vacation: bool) -> bool:
    """
    weekday 为 True 表示工作日，vacation 为 True 表示在休假。不是工作日，或者正在休假，就可以睡懒觉。可以睡懒觉时返回
    True。

    >>> # TODO: 写你的例子
    >>> sleep_in(True,False)
    False
    >>> sleep_in(False,True)
    True
    """
    # TODO: 写实现
    if(weekday!=True):
        if(vacation == True):
            return True
    return False


# --- 下面别改 ---
if __name__ == "__main__":
    import doctest
    doctest.testmod()
