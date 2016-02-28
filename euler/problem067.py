"""Problem 67

Maximum path sum I
==================

By starting at the top of the triangle below and moving to adjacent numbers on
the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in "p067_triangle.txt", a 15K file
containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible
to try every route to solve this problem, as there are 299 altogether! If you
could check one trillion (1012) routes every second it would take over twenty
billion years to check them all. There is an efficient algorithm to solve it.
;o)

    0
   0 1      0(0), 1(0)
  0 1 2     0(0), 1(0, 1), 2(1)
 0 1 2 3    0(0), 1(0, 1), 2(1, 2), 3(2)
0 1 2 3 4   0(0), 1(0, 1), 2(1, 2), 3(2, 3)

The i-th item on row r has parents at i - 1 and i on row r - 1

The i-th item on row r has children at i and i + 1 on row r + 1

"""

INPUT_FILE = './data/problem067.data'

def triangle_sums(triangle):
    for r in range(1, len(triangle)):
        # Do first and last columns (they only have one parent)
        triangle[r][0] += triangle[r - 1][0]
        triangle[r][-1] += triangle[r - 1][-1]
        # Do middle columns
        for c in range(1, len(triangle[r]) - 1):
            triangle[r][c] += max(triangle[r - 1][c - 1:c + 1])
    return triangle

def answer():
    triangle = []
    with open(INPUT_FILE, 'r') as f:
        for line in f:
            triangle.append(list(map(int, line.split())))
    return max(triangle_sums(triangle)[-1])

if __name__ == '__main__':
    print(answer())

