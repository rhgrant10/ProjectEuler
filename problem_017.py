"""Problem 17

Number letter counts
====================

If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
letters. The use of "and" when writing out numbers is in compliance with British
usage.

"""

TEENS = {
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen'
}

ONES = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine'
}

TENS = {
    0: '',
    1: 'ten',
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety'
}

def text(number):
    words = []
    thousands, hundreds, tens, ones = map(int, "{:04}".format(number))
    if thousands:
        words.append('{} thousand'.format(ONES[thousands]))
    if hundreds:
        words.append('{} hundred'.format(ONES[hundreds]))
    if (thousands or hundreds) and (tens or ones):
        words.append('and')
    if tens == 1 and ones:
        words.append(TEENS[10 * tens + ones])
    else:
        if tens:
            words.append(TENS[tens])
        if ones:
            words.append(ONES[ones])
    return " ".join(words)
    
def answer():
    letter_count = 0
    for n in range(1, 1001):
        letter_count += len(text(n).replace(" ", ""))
    return letter_count


if __name__ == '__main__':
    print(answer())
