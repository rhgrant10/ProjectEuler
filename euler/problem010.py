"""Problem 10

Summation of primes
===================

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""

def primes(limit):
    seive = [True for i in range(limit)]
    seive[:2] = [False, False]
    for i, n in enumerate(seive):
        if n:
            for x in range(i + i, limit, i):
                seive[x] = False
    return (i for i, x in enumerate(seive) if x)

def answer():
    return sum(primes(2000000))

if __name__ == '__main__':
    print(answer())