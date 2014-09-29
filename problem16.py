"""Problem 16

Power digit sum
===============

215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

"""

BASE = 2
EXPONENT = 1000


def answer():
	return sum(map(int, str(BASE ** EXPONENT)))
	
if __name__ == '__main__':
	print(answer())
	
