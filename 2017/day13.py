#!/usr/bin/env python3

import re


class Scanner:
    def __init__(self, depth, scannerRange):
        self.depth, self.scannerRange = depth, scannerRange

    def getPosition(self, tick):
        m = tick % (2 * (self.scannerRange - 1))
        if m > self.scannerRange - 1:
            m = 2 * (self.scannerRange - 1) - m
        return m

    def getSeverity(self):
        return self.depth * self.scannerRange


def parse(line):
    m = re.match(r'(\d+): (\d+)', line)
    if m:
        return int(m.group(1)), int(m.group(2))


def part1(filename):
    with open(filename) as f:
        lines = f.readlines()

    scanners = {}
    for line in lines:
        depth, scannerRange = parse(line)
        scanners[depth] = Scanner(depth, scannerRange)

    severity = 0
    for pktPos in range(0, max(scanners.keys()) + 1):
        if pktPos in scanners:
            if scanners[pktPos].getPosition(pktPos) == 0:
                severity += scanners[pktPos].getSeverity()

    print(severity)


def part2(filename):
    with open(filename) as f:
        lines = f.readlines()

    scanners = {}
    for line in lines:
        depth, scannerRange = parse(line)
        scanners[depth] = Scanner(depth, scannerRange)

    delay = 0
    while True:
        if 0 in scanners.keys() and scanners[0].getPosition(delay) == 0:
            delay += 1
            continue

        severity = 0
        for pktPos in range(0, max(scanners.keys()) + 1):
            if pktPos in scanners:
                if scanners[pktPos].getPosition(pktPos + delay) == 0:
                    severity += scanners[pktPos].getSeverity()

        if severity == 0:
            break

        delay += 1

    print(delay)


if __name__ == '__main__':
    part1('day13input.txt')
    part2('day13input.txt')