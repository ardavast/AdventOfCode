#!/usr/bin/env python3

from functools import reduce
from itertools import cycle, islice
from operator import xor


def knotRound(l, lengths, curPos, skipSize):
    l = l[:]

    for length in lengths:
        sl = list(reversed(list(islice(cycle(l), curPos, curPos + length))))
        ctr = 0
        for i in range(curPos, curPos + len(l)):
            i %= len(l)
            if ctr < length:
                l[i] = sl[ctr]
            ctr += 1
        curPos += (length + skipSize) % len(l)
        skipSize += 1

    return l, curPos, skipSize


def part1(filename):
    with open(filename) as f:
        lengths = list(map(int, f.readline().split(',')))

    l = list(range(256))
    curPos = 0
    skipSize = 0

    l, curPos, skipSize = knotRound(l, lengths, curPos, skipSize)

    print(l[0] * l[1])


def part2(filename):
    with open(filename) as f:
        lengths = list(map(ord, f.readline()))
        lengths += [17, 31, 73, 47, 23]

    l = list(range(256))
    curPos = 0
    skipSize = 0

    sparseHash = l
    for i in range(64):
        sparseHash, curPos, skipSize = knotRound(sparseHash, lengths, curPos, skipSize)

    denseHash = []
    for i in range(0, 256, 16):
        denseHash.append(reduce(xor, sparseHash[i:i + 16]))

    knotHash = ''
    for byte in denseHash:
        knotHash += ('{0:0{1}x}'.format(byte, 2))

    print(knotHash)


if __name__ == '__main__':
    part1('day10input.txt')
    part2('day10input.txt')