""" Problem 3

Largest Prime Factors
---------------------

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
from math import sqrt, ceil


def is_prime(n):
    if n < 3:
        return n == 2
    for i in range(2, ceil(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def primes(limit):
    if limit >= 2:
        yield 2
        n = 3
        while n < limit:
            if is_prime(n):
                yield n
            n += 2

def prime_factors(n):
    for p in primes(sqrt(n) + 1):
        if n % p == 0:
            yield p

def answer():
    return max(prime_factors(600851475143))


if __name__ == '__main__':
    print(answer())
