#!/usr/bin/env python3

import re
from collections import defaultdict


class Instruction:
    def __init__(self, reg, op, data, preg, pcond, pdata):
        self.reg = reg
        self.op = op
        self.data = data
        self.preg = preg
        self.pcond = pcond
        self.pdata = pdata

    def checkPredicate(self, regs):
        if self.pcond == '==':
            return True if regs[self.preg] == self.pdata else False
        elif self.pcond == '!=':
            return True if regs[self.preg] != self.pdata else False
        elif self.pcond == '>':
            return True if regs[self.preg] > self.pdata else False
        elif self.pcond == '<':
            return True if regs[self.preg] < self.pdata else False
        elif self.pcond == '>=':
            return True if regs[self.preg] >= self.pdata else False
        elif self.pcond == '<=':
            return True if regs[self.preg] <= self.pdata else False
        else:
            return False

    def execute(self, regs):
        if self.checkPredicate(regs):
            if self.op == 'inc':
                regs[self.reg] += self.data
            elif self.op == 'dec':
                regs[self.reg] -= self.data


def parse(line):
    line = re.sub('\s+', ' ', line.strip())
    m = re.match(r'^(\S+) (inc|dec) (\S+) if (\S+) (\S+) (\S+)$', line)
    if m:
        reg = m.group(1)
        op = m.group(2)
        data = int(m.group(3))
        preg = m.group(4)
        pcond = m.group(5)
        pdata = int(m.group(6))

        return reg, op, data, preg, pcond, pdata


def part1(filename):
    regs = defaultdict(int)

    with open(filename) as f:
        for line in f:
            reg, op, data, preg, pcond, pdata = parse(line)
            instruction = Instruction(reg, op, data, preg, pcond, pdata)
            instruction.execute(regs)

    maxData = 0
    for data in regs.values():
        if data > maxData:
            maxData = data

    print(maxData)


def part2(filename):
    regs = defaultdict(int)
    maxData = 0

    with open(filename) as f:
        for line in f:
            reg, op, data, preg, pcond, pdata = parse(line)
            instruction = Instruction(reg, op, data, preg, pcond, pdata)
            instruction.execute(regs)

            for data in regs.values():
                if data > maxData:
                    maxData = data

    print(maxData)


if __name__ == '__main__':
    part1('day08input.txt')
    part2('day08input.txt')