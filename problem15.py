"""Problem 15

Lattice paths
=============

Starting in the top left corner of a 2×2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

	rrdd
	rdrd
	rddr
	drrd
	drdr
	ddrr

How many such routes are there through a 20×20 grid?

"""

SIZE = 2

def answer():
	return ((SIZE / 2) ** 2 - 1) * 2

if __name__ == '__main__':
	print(answer())
