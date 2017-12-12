#!/usr/bin/env python3

import re


def parse(line):
    m = re.match(r'(.*) (\d+),(\d+) through (\d+),(\d+)', line)
    if m:
        op = m.group(1)
        p0 = [int(m.group(2)), int(m.group(3))]
        p1 = [int(m.group(4)), int(m.group(5))]

        return op, p0, p1


def part1(filename):
    with open(filename) as f:
        lines = f.readlines()

    grid = [[0] * 1000 for _ in range(1000)]

    for line in lines:
        op, p0, p1 = parse(line)
        for i in range(p0[0], p1[0] + 1):
            for j in range(p0[1], p1[1] + 1):
                if op == 'turn on':
                    grid[i][j] = 1
                elif op == 'turn off':
                    grid[i][j] = 0
                elif op == 'toggle':
                    grid[i][j] = int(not grid[i][j])

    count = 0
    for i in range(1000):
        for j in range(1000):
            if grid[i][j] == 1:
                count += 1

    print(count)


def part2(filename):
    with open(filename) as f:
        lines = f.readlines()

    grid = [[0] * 1000 for _ in range(1000)]

    for line in lines:
        op, p0, p1 = parse(line)
        for i in range(p0[0], p1[0] + 1):
            for j in range(p0[1], p1[1] + 1):
                if op == 'turn on':
                    grid[i][j] += 1
                elif op == 'turn off':
                    grid[i][j] = max(0, grid[i][j] - 1)
                elif op == 'toggle':
                    grid[i][j] += 2

    count = 0
    for i in range(1000):
        for j in range(1000):
            count += grid[i][j]

    print(count)


if __name__ == '__main__':
    part1('day06input.txt')
    part2('day06input.txt')