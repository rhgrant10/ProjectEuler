"""Problem 6

Sum square difference
=====================

The sum of the squares of the first ten natural numbers is,

    1 ** 2 + 2 ** 2 + ... + 10 ** 2 = 385

The square of the sum of the first ten natural numbers is,

    (1 + 2 + ... + 10) ** 2 = 55 ** 2 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.

"""

N = 100

def sum_of_squares(n):
    return sum(x ** 2 for x in n)

def square_of_sum(n):
    return sum(n) ** 2

def answer():
    return square_of_sum(range(N + 1)) - sum_of_squares(range(N + 1))

if __name__ == '__main__':
    print(answer())
