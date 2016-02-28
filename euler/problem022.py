"""Problem 22

Names scores
============

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into
alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a name
score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

"""

INPUT_FILE = './data/problem022.data'


def alphabetical_value(letter):
    return ord(letter) - ord('A') + 1

def name_score(name, position):
    return sum(map(alphabetical_value, name)) * position

def read_names(filepath):
    with open(filepath, 'r') as f:
        names = f.read().split(',')
        for n in names:
            yield n.replace('"', '')

def answer():
    names = sorted(read_names(INPUT_FILE))
    total = 0
    for i, name in enumerate(names, 1):
        total += name_score(name, i)
    return total

if __name__ == '__main__':
    print(answer())
