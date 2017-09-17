"""Problem 18

Maximum path sum I
==================

By starting at the top of the triangle below and moving to adjacent numbers on
the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

               75
              95 64
             17 47 82
            18 35 87 10
           20  4 82 47 65
          19  1 23 75  3 34
         88  2 77 73  7 63 67
        99 65  4 28  6 16 70 92
       41 41 26 56 83 40 80 70 33
      41 48 72 33 47 32 37 16 94 29
     53 71 44 65 25 43 91 52 97 51 14
    70 11 33 28 77 73 17 78 39 68 17 57
   91 71 52 38 17 14 91 43 58 50 27 29 48
  63 66  4 68 89 53 67 30 73 16 69 87 40 31
 4 62 98 27 23  9 70 98 73 93 38 53 60  4 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by
trying every route. However, Problem 67, is the same challenge with a triangle
containing one-hundred rows; it cannot be solved by brute force, and requires a
clever method! ;o)

    0
   0 1      0(0), 1(0)
  0 1 2     0(0), 1(0, 1), 2(1)
 0 1 2 3    0(0), 1(0, 1), 2(1, 2), 3(2)
0 1 2 3 4   0(0), 1(0, 1), 2(1, 2), 3(2, 3)

The i-th item on row r has parents at i - 1 and i on row r - 1

The i-th item on row r has children at i and i + 1 on row r + 1

"""


TRIANGLE = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20,  4, 82, 47, 65],
    [19,  1, 23, 75,  3, 34],
    [88,  2, 77, 73,  7, 63, 67],
    [99, 65,  4, 28,  6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23]
]


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
    return max(triangle_sums(TRIANGLE)[-1])


if __name__ == '__main__':
    print(answer())

