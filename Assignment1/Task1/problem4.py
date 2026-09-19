# do not modify this function
def sat(prod: int, n=14235764939971075543215213):
    for c in str(n):
        i = int(c)
        if i % 2 == 1:
            assert prod % i == 0
            prod //= i
    return prod == any(int(c) % 2 for c in str(n))

def sol(n=14235764939971075543215213):
    """Return the product of the odd digits in n, or 0 if there aren't any

    12345 => 15
    """
    s = str(n)
    x=1
    for i in range(len(s)):
        char = s[i]
        digit = int(char)
        if digit % 2 == 1:
            x *= digit

    # TODO: your implementation here
    return  x# return an integer
print(sol())
print(sat(sol()))
