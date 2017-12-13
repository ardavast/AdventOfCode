#!/usr/bin/env python3

import re


def parse(line):
    m = re.match(r'(\S+) -> (\S+)', line)
    if m:
        return [m.group(1)], 'wire', m.group(2)

    m = re.match(r'NOT (\S+) -> (\S+)', line)
    if m:
        return [m.group(1)], 'not', m.group(2)

    m = re.match(r'(\S+) (AND|OR|LSHIFT|RSHIFT) (\S+) -> (\S+)', line)
    if m:
        return [m.group(1), m.group(3)], m.group(2).lower(), m.group(4)


def execute(src, op, dst, wires):
    def getSignal(src):
        if src in wires:
            return wires[src]
        else:
            try:
                return int(src)
            except ValueError:
                return None

    if op in ['wire', 'not']:
        s0 = getSignal(src[0])
        if s0 is None:
            return False

        if op == 'wire':
            wires[dst] = s0
        elif op == 'not':
            wires[dst] = ~s0

    elif op in ['and', 'or', 'lshift', 'rshift']:
        s0 = getSignal(src[0])
        s1 = getSignal(src[1])
        if s0 is None or s1 is None:
            return False

        if op == 'and':
            wires[dst] = s0 & s1
        elif op == 'or':
            wires[dst] = s0 | s1
        elif op == 'lshift':
            wires[dst] = s0 << s1
        elif op == 'rshift':
            wires[dst] = s0 >> s1

    wires[dst] &= 0xffff

    return True


def part1(filename):
    with open(filename) as f:
        lines = f.readlines()

    wires = {}

    while lines:
        processedLines = []
        for line in lines:
            src, op, dst = parse(line)
            if execute(src, op, dst, wires):
                processedLines.append(line)

        for line in processedLines:
            lines.remove(line)

    print(wires['a'])


def part2(filename):
    with open(filename) as f:
        lines = f.readlines()
        savedLines = lines[:]

    wires = {}

    while lines:
        processedLines = []
        for line in lines:
            src, op, dst = parse(line)
            if execute(src, op, dst, wires):
                processedLines.append(line)

        for line in processedLines:
            lines.remove(line)

    lines = savedLines
    for i, line in enumerate(lines):
        if re.search('-> b$', line):
            lines[i] = '{0} -> b'.format(wires['a'])

    wires = {}

    while lines:
        processedLines = []
        for line in lines:
            src, op, dst = parse(line)
            if execute(src, op, dst, wires):
                processedLines.append(line)

        for line in processedLines:
            lines.remove(line)

    print(wires['a'])


if __name__ == '__main__':
    part1('day07input.txt')
    part2('day07input.txt')