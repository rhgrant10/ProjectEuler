"""Problem 7

10001st prime
=============

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10001st prime number?

"""
import math


def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def next_prime(after):
    after += 2 if after % 2 else 1
    while not is_prime(after):
        after += 2
    return after
    
def first_primes(count):
    n = 1
    x = 2
    for n in range(count, 0, -1):
        x = next_prime(x)   
    return x
    
def answer():
    return first_primes(10001)
    

if __name__ == '__main__':
    print(answer())
