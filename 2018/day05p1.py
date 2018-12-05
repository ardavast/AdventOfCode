#!/usr/bin/env python3
# coding: utf8

"""
Day 5: Alchemical Reduction part 1
https://adventofcode.com/2018/day/5
"""

from string import ascii_lowercase


def reactPolymer(polymer):
    pats = []
    pats += [c + c.upper() for c in ascii_lowercase]
    pats += [c.upper() + c for c in ascii_lowercase]

    reactedPolymer = polymer

    while True:
        for pat in pats:
            reactedPolymer = reactedPolymer.replace(pat, '')
        if polymer == reactedPolymer:
            break
        else:
            polymer = reactedPolymer

    return reactedPolymer


def main():
    with open('day05input.txt') as f:
        line = f.readline()
        line = line.strip()

    print(len(reactPolymer(line)))


if __name__ == '__main__':
    main()
