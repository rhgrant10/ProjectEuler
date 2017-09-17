""" Problem 3

Largest Prime Factors
=====================

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?

"""

from math import sqrt


NUMBER = 600851475143


def primes(limit):
    is_prime = [False, False] + [True for _ in range(limit - 2)]
    for i in range(2, limit):
        if is_prime[i]:
            for j in range(i + i, limit, i):
                is_prime[j] = False
    return [i for i, is_p in enumerate(is_prime) if is_p]


def prime_factors(n):
    for p in primes(int(sqrt(n) + 1)):
        if n % p == 0:
            yield p


def answer():
    return max(prime_factors(NUMBER))


if __name__ == '__main__':
    print(answer())
