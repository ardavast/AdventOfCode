#!/usr/bin/env python3


def move(p, step):
    p = list(p)

    if step == '>':
        p[0] += 1
    elif step == '^':
        p[1] += 1
    elif step == '<':
        p[0] -= 1
    elif step == 'v':
        p[1] -= 1

    return tuple(p)


def uniquePositions(line):
    positions = set()

    p = [0, 0]
    positions.add(tuple(p))
    for step in line:
        p = move(p, step)
        positions.add(tuple(p))

    return positions


def part1(filename):
    with open(filename) as f:
        line = f.readline()

    positions = uniquePositions(line)

    print(len(positions))


def part2(filename):
    with open(filename) as f:
        line = f.readline()

    positions = set()
    positions = positions.union(uniquePositions(line[0::2]))
    positions = positions.union(uniquePositions(line[1::2]))

    print(len(positions))


if __name__ == '__main__':
    part1('day03input.txt')
    part2('day03input.txt')