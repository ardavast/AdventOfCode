#!/usr/bin/env python3


def redistribute(banks):
    length = len(banks)
    biggest = 0

    for i in range(length - 1, -1, -1):
        if banks[i] >= banks[biggest]:
            biggest = i

    nBlocks = banks[biggest]
    banks[biggest] = 0
    for i in range(1, nBlocks + 1):
        banks[(biggest + i) % length] += 1


def part1(filename):
    seen = []
    counter = 1

    with open(filename) as f:
        banks = f.readline().split()
        banks = list(map(int, banks))

    seen.append(banks[:])

    while True:
        redistribute(banks)
        if banks in seen:
            break
        seen.append(banks[:])
        counter += 1

    print(counter)


def part2(filename):
    seen = []
    counter = 1

    with open(filename) as f:
        banks = f.readline().split()
        banks = list(map(int, banks))

    seen.append(banks[:])

    while True:
        redistribute(banks)
        if banks in seen:
            break
        seen.append(banks[:])
        counter += 1

    print(counter - seen.index(banks))


if __name__ == '__main__':
    part1('day06input.txt')
    part2('day06input.txt')