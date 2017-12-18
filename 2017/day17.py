#!/usr/bin/env python3


def part1(filename):
    with open(filename) as f:
        line = f.readline()

    step = int(line)

    spinlock = [0]
    currentPos = 0

    for spinlockLen in range(1, 2017 + 1):
        currentPos = (currentPos + step) % spinlockLen + 1
        spinlock.insert(currentPos, spinlockLen)

    print(spinlock[spinlock.index(2017) + 1])


def part2(filename):
    with open(filename) as f:
        line = f.readline()

    step = int(line)

    currentPos = 0

    value = None
    for spinlockLen in range(1, 50000000 + 1):
        currentPos = (currentPos + step) % spinlockLen + 1
        if currentPos == 1:
            value = spinlockLen

    print(value)


if __name__ == '__main__':
    part1('day17input.txt')
    part2('day17input.txt')