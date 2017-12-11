#!/usr/bin/env python3


def part1(filename):
    with open(filename) as f:
        line = f.readline()

    skip = False
    inGroup = 0
    inGarbage = False
    nGroups = 0

    for c in line:
        if skip:
            skip = False
            continue

        if c == '!':
            skip = True
        elif not inGarbage:
            if c == '{':
                inGroup += 1
            elif c == '}':
                nGroups += inGroup
                inGroup -= 1
            elif c == '<':
                inGarbage = True
        elif c == '>':
            inGarbage = False

    print(nGroups)


def part2(filename):
    with open(filename) as f:
        line = f.readline()

    skip = False
    inGroup = False
    inGarbage = False
    nGarbage = 0

    for c in line:
        if skip:
            skip = False
            continue

        if c == '!':
            skip = True
        elif not inGarbage:
            if c == '{':
                inGroup = True
            elif c == '}':
                inGroup = False
            elif c == '<':
                inGarbage = True
        elif c == '>':
            inGarbage = False
        elif inGarbage:
            nGarbage += 1

    print(nGarbage)

if __name__ == '__main__':
    part1('day09input.txt')
    part2('day09input.txt')