#!/usr/bin/env python3

import re


def _10to26(n10):
    if n10 == 0:
        return 'a'

    n26 = []
    while n10:
        n26.insert(0, n10 % 26)
        n10 //= 26

    return ''.join(map(lambda n: chr(n + ord('a')), n26))


def _26to10(n26):
    n26 = list(map(lambda n: ord(n) - ord('a'), n26))

    n10 = 0
    for i in range(0, len(n26)):
        n10 += n26[len(n26) - 1 - i] * 26 ** i

    return n10


def isValid(s):
    if re.search(r'[iol]', s):
        return False

    if not re.search(r'(.)\1.*(.)\2', s):
        return False

    s = list(map(ord, s))
    for i in range(0, len(s) - 2):
        if s[i] + 1 == s[i + 1] and s[i] + 2 == s[i + 2]:
            return True

    return False


def part1(filename):
    with open(filename) as f:
        line = f.readline()

    line = line.strip()
    line = _26to10(line)
    while not isValid(_10to26(line)):
        line += 1

    print(_10to26(line))


def part2(filename):
    with open(filename) as f:
        line = f.readline()

    line = line.strip()
    line = _26to10(line)
    while not isValid(_10to26(line)):
        line += 1

    line += 1

    while not isValid(_10to26(line)):
        line += 1

    print(_10to26(line))


if __name__ == '__main__':
    part1('day11input.txt')
    part2('day11input.txt')