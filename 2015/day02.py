#!/usr/bin/env python3


def parse(line):
    line = line.split('x')
    line = map(int, line)
    l, w, h = line

    return l, w, h


def part1(filename):
    with open(filename) as f:
        lines = f.readlines()

    total = 0
    for line in lines:
        l, w, h = parse(line)
        total += 2 * (l * w + w * h + h * l)
        total += min(l * w, w * h, h * l)

    print(total)


def part2(filename):
    with open(filename) as f:
        lines = f.readlines()

    total = 0
    for line in lines:
        l, w, h = parse(line)
        total += min(2 * (l + w), 2 * (w + h), 2 * (h + l))
        total += l * w * h

    print(total)


if __name__ == '__main__':
    import os
    print(os.getcwd())
    part1('../2015/day02input.txt')
    part2('../2015/day02input.txt')