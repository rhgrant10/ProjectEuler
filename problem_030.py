"""Problem 30

Digit fifth powers
==================

Surprisingly there are only three numbers that can be written as the sum
of fourth powers of their digits:

    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth
powers of their digits.
"""


def dpow(power):
    return lambda x: int(x) ** power


def get_digit_power_sum(number, power):
    return sum([int(d) ** power for d in str(number)])


def print_digit_power_sums(power):
    # This is super lame... I can't see how to know when to stop considering
    # numbers, so instead we just print the work being done and the user can
    # cancel this with a signal.
    print('Press ctrl+c when you are satisfied with the answer')
    n = 2
    total = 0
    numbers = []
    while True:
        s = get_digit_power_sum(n, power)
        print(f'\rn={n:<10} {total:>10} = sum({numbers})', end='', flush=True)
        if s == n:
            numbers.append(n)
            total += n
        n += 1


def answer():
    try:
        print_digit_power_sums(power=5)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    answer()
