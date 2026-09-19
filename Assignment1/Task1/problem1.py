from typing import List

# do not modify this function
def sat(li: List[int]):
    return all(i in range(1000) and abs(i - j) >= 10 for i in li for j in li if i != j) and len(set(li)) == 100

def sol():
    """Find a list of one hundred integers between 0 and 999 which all differ by at least ten from one another."""
    """100整数 范围0<=999 任意两个差值>=10"""
    # TODO: your implementation here

    # return [i *10 for i in range(100)]

    # return [999-i*10 for i in range(100)]
    # return [5+i*10 for i in range(100)]
    return [1+i*10 for i in range(100)]
print(sat(sol()))
