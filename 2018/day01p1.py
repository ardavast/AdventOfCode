#!/usr/bin/env python3
# coding: utf8

"""
Day 1: Chronal Calibration part 1
https://adventofcode.com/2018/day/1
"""


def main():
    freq = 0

    with open('day01input.txt') as f:
        for line in f:
            freq += int(line)

    print(freq)


if __name__ == '__main__':
    main()
