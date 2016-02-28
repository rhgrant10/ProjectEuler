"""Problem 23

Non-abundant sums
=================

A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors of 28
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123 can
be written as the sum of two abundant numbers. However, this upper limit cannot
be reduced any further by analysis even though it is known that the greatest
number that cannot be expressed as the sum of two abundant numbers is less than
this limit.

Find the sum of all the positive integers which cannot be written as the sum of
two abundant numbers.

"""

LIMIT = 28123

def abundant_numbers(limit):
    for n in range(1, limit + 1):
        if sum(proper_divisors(n)) > n:
            yield n

def proper_divisors(n):
    if n < 2:
        return
    yield 1
    for i in range(2, int(n ** 0.5) + 1):
        d, r = divmod(n, i)
        if r == 0:
            yield i
            if d != i:
                yield d

def is_sum_of_two_abundants(n, abundants):
    # print("Testing {}".format(n))
    for a in [x for x in abundants if x < n]:
        # print(" {} - {} in abundants?".format(n, a), end=' ')
        if (n - a) in abundants:
            # print("yes - > {} + {} = {}".format(n - a, a, n))
            # print("TRUE")
            return True
        # print("no".format(n - a, a, n))
    # print("FALSE")
    return False

def answer():
    total = 0
    abundants = list(abundant_numbers(LIMIT + 1))
    for n in range(1, LIMIT + 1):
        if not is_sum_of_two_abundants(n, abundants):
            total += n
    return total

if __name__ == '__main__':
    print(answer())