#!/usr/bin/env python3
# coding: utf8

import re

import numpy as np


def main():
    fabric = np.zeros((1000, 1000), int)

    with open('day03input.txt') as f:
        for line in f:
            m = re.match(r'^#\d+ @ (\d+),(\d+): (\d+)x(\d+)$', line)
            hpos, vpos, hsize, vsize = map(int, m.groups())

            for i in range(hpos, hpos + hsize):
                for j in range(vpos, vpos + vsize):
                    fabric[i][j] += 1

        f.seek(0)

        for line in f:
            m = re.match(r'^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$', line)
            claimID, hpos, vpos, hsize, vsize = map(int, m.groups())

            if (fabric[hpos:hpos+hsize, vpos:vpos+vsize] == 1).all():
                print(claimID)
                break


if __name__ == '__main__':
    main()
