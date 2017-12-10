#!/usr/bin/env python3


def part1(filename):
    valid = 0

    with open(filename) as f:
        for line in f:
            line = line.split()
            if len(line) == len(set(line)):
                valid += 1

    print(valid)


def part2(filename):
    valid = 0

    with open(filename) as f:
        for line in f:
            line = line.split()
            words = []
            for word in line:
                words.append(''.join(sorted(word)))
            if len(words) == len(set(words)):
                valid += 1

    print(valid)

if __name__ == '__main__':
    part1('day04input.txt')
    part2('day04input.txt')