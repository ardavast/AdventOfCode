#!/usr/bin/env python3

import re


def part1(filename):
    with open(filename) as f:
        lines = f.readlines()

    nice = 0
    for line in lines:
        if re.search(r'(?:ab|cd|pq|xy)', line):
            continue
        if not re.search(r'(.)\1', line):
            continue
        if len(re.findall(r'[aeiou]', line)) < 3:
            continue
        nice += 1

    print(nice)


def part2(filename):
    with open(filename) as f:
        lines = f.readlines()

    nice = 0
    for line in lines:
        if len(re.findall(r'(..).*\1', line)) < 1:
            continue
        if not re.search(r'(.).\1', line):
            continue
        nice += 1

    print(nice)


if __name__ == '__main__':
    part1('day05input.txt')
    part2('day05input.txt')