#!/usr/bin/env python3


def part1(filename):
    l = []
    ip = 0
    count = 0

    with open(filename) as f:
        for line in f:
            l.append(int(line))

    while True:
        try:
            oldIp = ip
            ip += l[ip]
            l[oldIp] += 1
            count += 1
        except IndexError:
            print(count)
            break


def part2(filename):
    l = []
    ip = 0
    count = 0

    with open(filename) as f:
        for line in f:
            l.append(int(line))

    while True:
        try:
            oldIp = ip
            ip += l[ip]
            if l[oldIp] >= 3:
                l[oldIp] -= 1
            else:
                l[oldIp] += 1

            count += 1
        except IndexError:
            print(count)
            break


if __name__ == '__main__':
    part1('day05input.txt')
    part2('day05input.txt')