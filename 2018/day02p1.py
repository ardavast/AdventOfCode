#!/usr/bin/env python3
# coding: utf8

"""
Day 2: Inventory Management System part 1
https://adventofcode.com/2018/day/2
"""

from collections import Counter


def main():
    with open('day02input.txt') as f:
        t2 = 0
        t3 = 0

        for line in f:
            counter = Counter(line)
            if 2 in counter.values():
                t2 += 1
            if 3 in counter.values():
                t3 += 1

        print(t2 * t3)


if __name__ == '__main__':
    main()
