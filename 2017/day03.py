#!/usr/bin/env python3

from collections import defaultdict


def findRange(n):
    if n == 1:
        return 0, 1, 1

    i = 1
    lo, hi = 2, 9
    while not (lo <= n <= hi):
        i += 1
        lo, hi = hi + 1, hi + i * 8

    return i, lo, hi


def part1(n):
    d, lo, hi = findRange(n)
    mind, maxd = d, d * 2
    d = maxd - 1
    inc = -1
    for i in range(lo, hi + 1):
        if i == n:
            print(d)
        if d == mind or d == maxd:
            inc = -inc
        d += inc


def part2(n):
    d = defaultdict(int)
    d [(0, 0)] = 1

    def sumNeighbors(x, y):
        sum = 0

        sum += d[(x + 1, y)]
        sum += d[(x + 1, y + 1)]
        sum += d[(x, y + 1)]
        sum += d[(x - 1, y + 1)]
        sum += d[(x - 1, y)]
        sum += d[(x - 1 , y - 1)]
        sum += d[(x, y - 1)]
        sum += d[(x + 1, y - 1)]

        return sum

    def fill(x, y):
        sum = sumNeighbors(x, y)
        d[(x, y)] = sum
        return sum

    i = 1
    x, y = 1, 0

    solved = False
    while not solved:
        for y in range(-i + 1, i + 1):
            if fill(x, y) > n:
                solved = True
                break
        if solved:
            break

        for x in range(i - 1, -i - 1, -1):
            if fill(x, y) > n:
                solved = True
                break
        if solved:
            break

        for y in range(i - 1, -i - 1, -1):
            if fill(x, y) > n:
                solved = True
                break
        if solved:
            break

        for x in range(-i + 1, i + 1):
            if fill(x, y) > n:
                solved = True
                break
        if solved:
            break

        i += 1
        x += 1

    print(d[(x, y)])


if __name__ == '__main__':
    part1(368078)
    part2(368078)