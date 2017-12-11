#!/usr/bin/env python3


def hexMove(p, step):
    p = p[:]

    if step == 'ne':
        p[0] += 1
        p[2] -= 1
    elif step == 'n':
        p[1] += 1
        p[2] -= 1
    elif step == 'nw':
        p[0] -= 1
        p[1] += 1
    elif step == 'sw':
        p[0] -= 1
        p[2] += 1
    elif step == 's':
        p[1] -= 1
        p[2] += 1
    elif step == 'se':
        p[0] += 1
        p[1] -= 1

    return p


def hexDistance(p0, p1):
    return max(abs(p1[0] - p0[0]), abs(p1[1] - p0[1]), abs(p1[2] - p0[2]))


def part1(filename):
    with open(filename) as f:
        line = f.readline().split(',')

    p0 = [0, 0, 0]
    p1 = p0[:]
    for move in line:
        p1 = hexMove(p1, move)

    print(hexDistance(p1, p0))


def part2(filename):
    with open(filename) as f:
        line = f.readline().split(',')

    p0 = [0, 0, 0]
    p1 = p0[:]
    maxDistance = 0
    for move in line:
        p1 = hexMove(p1, move)
        if hexDistance(p1, p0) > maxDistance:
            maxDistance = hexDistance(p1, p0)

    print(maxDistance)


if __name__ == '__main__':
    part1('day11input.txt')
    part2('day11input.txt')