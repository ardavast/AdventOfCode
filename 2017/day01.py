#!/usr/bin/env python3


def part1(filename):
    with open(filename) as f:
        line = f.readline()

    line += line[0]

    sum = 0

    for i in range(0, len(line) - 1):
        if line[i] == line[i + 1]:
            sum += int(line[i])

    print(sum)


def part2(filename):
    with open(filename) as f:
        line = f.readline()

    sum = 0
    length = len(line)

    for i in range(0, length):
        if line[i] == line[(i + length // 2) % length]:
            sum += int(line[i])

    print(sum)


if __name__ == '__main__':
    part1('day01input.txt')
    part2('day01input.txt')