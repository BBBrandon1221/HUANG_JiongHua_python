def is_prime(number: int) -> bool:
    """
    Return True if number is a prime. Integers less than 2 are not prime.
    
    >>> #TODO: your testcase here
    >>> is_prime(3)
    True
    >>> is_prime(4)
    False
    >>> is_prime(7)
    True
    """
    #TODO: your implementation here
    if number < 2:
        return False
    for i in range(2, int(number**0.5)+1):
        if number%i == 0:
            return False
    return True

# --- DON'T MODIFY BELOW THIS LINE ---
if __name__ == "__main__":
    import doctest
    doctest.testmod()
