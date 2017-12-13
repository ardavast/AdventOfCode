#!/usr/bin/env python3


def lookAndSee(s):
    ls = ''

    c = s[0]
    count = 1
    for i in range(1, len(s)):
        if s[i] == c:
            count += 1
        else:
            ls += str(count) + c
            c = s[i]
            count = 1
    ls += str(count) + c

    return ls


def part1(filename):
    with open(filename) as f:
        line = f.readline()

    lsSeq = line
    for i in range(40):
        lsSeq = lookAndSee(lsSeq)

    print(len(lsSeq))


def part2(filename):
    with open(filename) as f:
        line = f.readline()

    lsSeq = line
    for i in range(50):
        lsSeq = lookAndSee(lsSeq)

    print(len(lsSeq))


if __name__ == '__main__':
    part1('day10input.txt')
    part2('day10input.txt')