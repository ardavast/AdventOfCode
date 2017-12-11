#!/usr/bin/env python3

import hashlib


def md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()


def part1(filename):
    with open(filename) as f:
        line = f.readline()

    i = 0
    while True:
        fingerprint = md5(line + str(i))
        if fingerprint[0:5] == '00000':
            break
        i += 1

    print(i)


def part2(filename):
    with open(filename) as f:
        line = f.readline()

    i = 0
    while True:
        fingerprint = md5(line + str(i))
        if fingerprint[0:6] == '000000':
            break
        i += 1

    print(i)


if __name__ == '__main__':
    part1('day04input.txt')
    part2('day04input.txt')