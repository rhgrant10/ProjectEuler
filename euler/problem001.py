""" Problem 1

Multiples of 3 and 5
--------------------

If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def answer():
	return sum(set(range(3, 1000, 3) + range(5, 1000, 5)))


if __name__ == '__main__':
	print(answer())
