#!/usr/bin/env python3

import re
from collections import defaultdict


class CPU:
    def __init__(self, instructions, id):
        self.instructions = instructions
        self.regs = defaultdict(int)
        self.regs['p'] = id
        self.ip = 0
        self.sndq = []
        self.rcvq = []
        self.sent = 0
        self.terminated = False
        self.deadlock = 0

    def retrieve(self, opd):
        if re.match(r'^-?\d+$', opd):
            return int(opd)
        else:
            return self.regs[opd]

    def execute(self):
        if self.ip > len(self.instructions):
            self.terminated = True
            return

        instruction = self.instructions[self.ip]

        op, opd1, opd2 = instruction.op, instruction.opd1, instruction.opd2

        if op == 'snd':
            self.sndq.insert(0, self.retrieve(opd1))
            self.sent += 1
            self.ip += 1
        elif instruction.op == 'rcv':
            if len(self.rcvq) > 0:
                self.regs[opd1] = self.rcvq.pop()
                self.ip += 1
            else:
                self.deadlock += 1
        elif instruction.op == 'set':
            self.regs[opd1] = self.retrieve(opd2)
            self.ip += 1
        elif instruction.op == 'add':
            self.regs[opd1] += self.retrieve(opd2)
            self.ip += 1
        elif instruction.op == 'mul':
            self.regs[opd1] *= self.retrieve(opd2)
            self.ip += 1
        elif instruction.op == 'mod':
            self.regs[opd1] %= self.retrieve(opd2)
            self.ip += 1
        elif instruction.op == 'jgz':
            if self.retrieve(opd1) > 0:
                self.ip += self.retrieve(opd2)
            else:
                self.ip += 1


class Instruction:
    def __init__(self, op, opds):
        self.op = op
        self.length = len(opds)
        self.opd1 = opds[0]
        self.opd2 = None
        if self.length > 1:
            self.opd2 = opds[1]


def parse(line):
    line = re.sub('\s+', ' ', line.strip())
    m = re.match(r'^(snd|rcv) (.*)$', line)
    if m:
        op = m.group(1)
        opd1 = m.group(2)
        return op, (opd1)

    m = re.match(r'^(set|add|mul|mod|jgz) (.*) (.*)$', line)
    if m:
        op = m.group(1)
        opd1 = m.group(2)
        opd2 = m.group(3)
        return op, (opd1, opd2)


def part1(filename):
    with open(filename) as f:
        lines = f.readlines()

    instructions = []
    for line in lines:
        op, opds = parse(line)
        instructions.append(Instruction(op, opds))

    cpuA = CPU(instructions, 0)
    cpuB = CPU(instructions, 1)

    while True:
        if cpuA.deadlock > 1000 and cpuB.deadlock > 1000:
            break

        cpuA.execute()
        if len(cpuA.sndq) > 0:
            cpuB.rcvq.insert(0, cpuA.sndq.pop())

        cpuB.execute()
        if len(cpuB.sndq) > 0:
            cpuA.rcvq.insert(0, cpuB.sndq.pop())

    print(cpuB.sent)


def part2(filename):
    pass


if __name__ == '__main__':
    part1('day18input.txt')
    part2('day18input.txt')