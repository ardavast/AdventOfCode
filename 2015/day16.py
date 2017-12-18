#!/usr/bin/env python3

import re

d = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}


def parse(line):
    m = re.match(r'Sue (\d+): (.*): (\d+), (.*): (\d+), (.*): (\d+)', line)
    if m:
        d = {}
        d[m.group(2)] = int(m.group(3))
        d[m.group(4)] = int(m.group(5))
        d[m.group(6)] = int(m.group(7))
        return d


def part1(filename):
    with open(filename) as f:
        lines = f.readlines()

    for i, line in enumerate(lines, 1):
        aunt = parse(line)
        points = 0
        for item in aunt.keys():
            if item in d.keys():
                if aunt[item] == d[item]:
                    points += 1
        if points == 3:
            print(i)


def part2(filename):
    with open(filename) as f:
        lines = f.readlines()

    for i, line in enumerate(lines, 1):
        aunt = parse(line)
        points = 0
        for item in aunt.keys():
            if item in d.keys():
                if item in ['cats', 'trees']:
                    if aunt[item] > d[item]:
                        points += 1
                elif item in ['pomeranians', 'goldfish']:
                    if aunt[item] < d[item]:
                        points += 1
                else:
                    if aunt[item] == d[item]:
                        points += 1
        if points == 3:
            print(i)


if __name__ == '__main__':
    part1('day16input.txt')
    part2('day16input.txt')
