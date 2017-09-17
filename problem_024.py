"""Problem 24

Lexicographic permutations
=============

A permutation is an ordered arrangement of objects. For example, 3124 is one
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
are listed numerically or alphabetically, we call it lexicographic order. The
lexicographic permutations of 0, 1 and 2 are:

    012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits
0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?



     0 0123
     1 0132
    ----
     2 0213
     3 0231
    ----
     4 0312
     5 0321

     6 1023
     7 1032
    ----
     8 1203
     9 1230
    ----
    10 1302
    11 1320

    12 2013
    13 2031
    ----
    14 2103
    15 2130
    ----
    16 2301
    17 2310

    18 3012
--> 19 3021
    ----
    20 3102
    21 3120
    ----
    22 3201
    23 3210

N = 4
Total permutations = F(4) = 24

digit | items
------+------
   0  |  24 / 4 = 6
   1  |  6 / 3 = 2
   x  |  F(N - x - 1)

N = 5
Total permutations = F(5) = 120

digit | items
------+------
   1  |  120 / 5 = 24
   2  |  24 / 4 = 6
   3  |  6 / 3 = 2
   3  |  2 / 2 = 1


Suppose N = 4 and I = 20.

digits = [0, 1, 2, 3]
spread = [24]
spread = [6, 6, 6, 6]
spread = [2, 2, 2]

24
i=3     6 6 6 6
i=2     2 2 2 2 2 2 2 2 2 2 2 2
i=1     1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
i=0     1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1

24


[24/4, 6/3, 2/2, 1/1]           => [6, 2, 1, 1]
[120/5, 24/4, 6/3, 2/2, 1/1]    => [24, 6, 2, 1, 1]

"""

from math import factorial

N = 10
I = 10 ** 6

def answer():
    digits = list(range(N))
    item = ''
    items_per_digit = list(reversed([factorial(i) for i in range(N)]))
    index = I - 1
    for i in items_per_digit:
        d = index // i
        index -= d * i
        item += str(digits.pop(d))
    return item

if __name__ == '__main__':
    print(answer())
