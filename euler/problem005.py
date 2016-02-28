""" Problem 5

Smallest multiple
=================

2520 is the smallest number that can be divided by each of the numbers from 1 to
10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?

"""

def answer():
	n = 20
	while any(n % d for d in range(20, 0, -1)):
		n += 20
	return n

if __name__ == '__main__':
	print(answer())
