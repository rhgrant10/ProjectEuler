"""Problem 9

Special Pythagorean triplet
===========================

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

    a^2 + b^2 = c^2
    
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""

# a^2 + b^2 = c^2
# a + b + c = 1000
# a * b * c = ?

def gcd(a, b):
    b, a = sorted([a, b])
    while b != 0:
        a, b = b, a % b
    return a

def is_coprime(a, b):
    return gcd(a, b) == 1
    
def primitive_triple(m, n):
    mm = m * m
    nn = n * n
    return mm - nn, 2 * m * n, mm + nn

def pairs_with(m):
    start = 1 if m % 2 == 0 else 2
    for n in range(start, m, 2):
        if is_coprime(m, n):
            yield n

def triples():
    for m in range(2, 1000):
        for n in pairs_with(m):
            yield primitive_triple(m, n)
            
def find_triple():
    for a, b, c in triples():
        d, r = divmod(1000, a + b + c)
        if r == 0:
            return d * a, d * b, d * c
        
def answer():
    a, b, c = find_triple()
    return a * b * c
    
if __name__ == '__main__':
    print(answer())