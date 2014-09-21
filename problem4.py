""" Problem 4

Largest palindrome product
==========================

A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""


def is_palindrome(n):
    n = str(n)
    return n == "".join(reversed(n))

def palindromes(start):
    for n in range(start, 100 * 100 - 1, -1):
        if is_palindrome(n):
            yield n

def answer():
    for p in palindromes(999 * 999):
        for d in range(int(p ** 0.5), 100, -1):
            div, m = divmod(p, d)
            if len(str(div)) == 3 and m == 0:
                return p
    return None   

if __name__ == '__main__':
    print(answer())
