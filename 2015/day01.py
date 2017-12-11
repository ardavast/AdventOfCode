#!/usr/bin/env python3


def part1(filename):
    with open(filename) as f:
        line = f.readline()

    floor = 0
    for c in line:
        if c == '(':
            floor += 1
        elif c == ')':
            floor -= 1

    print(floor)


def part2(filename):
    with open(filename) as f:
        line = f.readline()

    floor = 0
    i = None
    for (i, c) in enumerate(line, 1):
        if c == '(':
            floor += 1
        elif c == ')':
            floor -= 1
        if floor == -1:
            break

    print(i)


if __name__ == '__main__':
    part1('day01input.txt')
    part2('day01input.txt')