"""Problem 21

Amicable numbers
================

Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n). If d(a) = b and d(b) = a, where a ≠ b, then a and
b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and
142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000

"""


def divisors(n, memo={}):
    if n in memo:
        yield from memo[n]
    else:
        memo[n] = [1]
        yield 1
        for i in range(2, int(n ** 0.5) + 1):
            d, r = divmod(n, i)
            if r == 0:
                memo[n].extend([i, d])
                yield i
                yield d


def answer():
    amicables = set()
    for a in range(1, 10000):
        b = sum(divisors(a))
        if a != b and sum(divisors(b)) == a:
            amicables.update([a, b])
    return sum(amicables)


if __name__ == '__main__':
    print(answer())
