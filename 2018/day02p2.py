#!/usr/bin/env python3
# coding: utf8

from itertools import combinations


def hamming(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))


def commonChars(s1, s2):
    return ''.join(c for c in s1 if c in s2)


def main():
    with open('day02input.txt') as f:
        for s1, s2 in combinations(f, 2):
            s1, s2 = map(str.strip, [s1, s2])
            if hamming(s1, s2) == 1:
                print(commonChars(s1, s2))


if __name__ == '__main__':
    main()
