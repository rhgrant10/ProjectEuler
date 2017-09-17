"""
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain
1000 digits?
"""


def fib(n, memo={}):
    memo.update({1: 1, 2: 1})
    if n in memo:
        return memo[n]
    if n < 1:
        raise ValueError('undefined for {}'.format(n))

    term = fib(n - 1) + fib(n - 2)
    memo[n] = term
    return term


def answer():
    n = 1
    while True:
        print('f({}) = '.format(n), end='', flush=True)
        term = fib(n)
        print(term)
        if len(str(term)) >= 1000:
            return n
        n += 1


if __name__ == '__main__':
    answer()
