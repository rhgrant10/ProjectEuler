"""Problem 14

Longest Collatz sequence
========================

The following iterative sequence is defined for the set of positive integers:

	n → n/2 (n is even)
	n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

	13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

"""

LIMIT = 10 ** 6

def collatz_length(n):
	c = 1
	while n != 1:
		d, r = divmod(n, 2)
		n = 3 * n + 1 if r else d
		c += 1
	return c

def answer():
	C = N = 1
	for n in range(2, LIMIT):
		c = collatz_length(n)
		if c > C:
			N = n
			C = c
	return N, C

if __name__ == '__main__':
	print(answer())
