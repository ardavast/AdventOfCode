#!/usr/bin/env python3

from day10 import knotHash


def part1(filename):
    with open(filename) as f:
        line = f.readline()

    used = 0
    for i in range(0, 128):
        hashHex = knotHash(line + '-' + str(i))
        hashBin = bin(int(hashHex, 16))[2:].zfill(128)
        used += hashBin.count('1')

    print(used)


def part2(filename):
    with open(filename) as f:
        line = f.readline()

    grid = []
    for i in range(0, 128):
        hashHex = knotHash(line + '-' + str(i))
        hashBin = bin(int(hashHex, 16))[2:].zfill(128)
        grid.append(list(hashBin))

    def getNeighbors(grid, i, j):
        neighbors = []

        if j < len(grid[i]):
            k = j + 1
            while k < len(grid[i]) and grid[i][k] == '1':
                neighbors.append((i, k))
                k += 1
        if j > 0:
            k = j - 1
            while k >= 0 and grid[i][k] == '1':
                neighbors.append((i, k))
                k -= 1
        if i < len(grid):
            k = i + 1
            while k < len(grid) and grid[k][j] == '1':
                neighbors.append((k, j))
                k += 1
        if i > 0:
            k = i - 1
            while k >= 0 and grid[k][j] == '1':
                neighbors.append((k, j))
                k -= 1

        return neighbors

    def removeGroup(grid, i, j):
        grid[i][j] = 'x'
        for i, j in getNeighbors(grid, i, j):
            removeGroup(grid, i, j)

    groups = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '1':
                removeGroup(grid, i, j)
                groups += 1

    print(groups)


if __name__ == '__main__':
    part1('day14input.txt')
    part2('day14input.txt')