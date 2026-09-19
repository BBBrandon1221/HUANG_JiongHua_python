from typing import List

# do not modify this function
def sat(li: List[int]):
    return all([li.count(i) == i for i in range(10)])

def sol():
    """Find a list integers such that the integer i occurs i times, for i = 0, 1, 2, ..., 9."""
    # TODO: your implementation here
    list = []
    for i in range(10):
        list.extend([i]*i)
    return  list# return a list

print(sol())

print(sat(sol()))
