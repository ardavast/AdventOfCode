#!/usr/bin/env python3

import re


def part1(filename):
    with open(filename) as f:
        lines = f.readlines()
        lines = list(map(str.strip, lines))

    count = 0
    for line in lines:
        len0 = len(line)
        line = line[1:-1]
        line = re.sub(r'\\\\|\\"|\\x[0-9a-f][0-9a-f]', 'Z', line)
        count += (len0 - len(line))

    print(count)


def part2(filename):
    with open(filename) as f:
        lines = f.readlines()
        lines = list(map(str.strip, lines))

    count = 0
    for line in lines:
        len0 = len(line)
        line = 'ZZ' + line + 'ZZ'
        line = re.sub(r'\\\\|\\"', 'ZZZZ', line)
        line = re.sub(r'\\x[0-9a-f][0-9a-f]', 'ZZZZZ', line)
        count += (len(line) - len0)

    print(count)


if __name__ == '__main__':
    part1('day08input.txt')
    part2('day08input.txt')