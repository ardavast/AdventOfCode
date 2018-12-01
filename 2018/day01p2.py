#!/usr/bin/env python3
# coding: utf8

from itertools import cycle


def main():
    freq = 0
    freqs_seen = set([freq])

    with open('day01input.txt') as f:
        f = cycle(f)
        for line in f:
            freq += int(line)
            if freq in freqs_seen:
                print(freq)
                break
            freqs_seen.add(freq)


if __name__ == '__main__':
    main()
