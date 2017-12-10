#!/usr/bin/env python3


def part1():
    checksum = 0

    with open('day02input.txt') as f:
        for line in f:
            line = line.split()
            l = list(map(int, line))
            checksum += max(l) - min(l)

    print(checksum)


def part2():
    checksum = 0

    with open('day02input.txt') as f:
        for line in f:
            line = line.split()
            l = list(map(int, line))
            l.sort(reverse=True)
            solved = False
            for i in range(len(l)):
                for j in range(i + 1, len(l)):
                    if l[i] % l[j] == 0:
                        l = [l[i],  l[j]]
                        checksum += max(l) // min(l)
                        solved = True
                        break
                if solved:
                    break

    print(checksum)

if __name__ == '__main__':
    part1()
    part2()