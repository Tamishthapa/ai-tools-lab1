def is_prime(n):
    """Return True if n is a prime number, otherwise False.

    Prime numbers are integers greater than 1 that have no divisors other
    than 1 and themselves. Values less than 2 are not prime.
    """
    if n < 2:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 2

    return True
print(is_prime(2))
print(is_prime(7))
print(is_prime(1))
print(is_prime(12))