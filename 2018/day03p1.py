#!/usr/bin/env python3
# coding: utf8

import re

import numpy as np


def main():
    fabric = np.zeros((1000, 1000), dtype=int)
    overlaps = 0

    with open('day03input.txt') as f:
        for line in f:
            m = re.match(r'^#\d+ @ (\d+),(\d+): (\d+)x(\d+)$', line)
            hpos, vpos, hsize, vsize = map(int, m.groups())

            for i in range(hpos, hpos + hsize):
                for j in range(vpos, vpos + vsize):
                    if fabric[i][j] == 1:
                        overlaps += 1
                    fabric[i][j] += 1

        print(overlaps)


if __name__ == '__main__':
    main()
