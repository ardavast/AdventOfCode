#!/usr/bin/env python3

import re


class Generator:
    def __init__(self, seed, factor, mul):
        self.seed, self.factor, self.mul = seed, factor, mul
        self.value = self.seed

    def gen(self):
        self.value *= self.factor
        self.value %= 0x7fffffff
        while self.value % self.mul != 0:
            self.value *= self.factor
            self.value %= 0x7fffffff

        return self.value


def parse(line):
    m = re.match(r'Generator .* starts with (\d+)', line)
    if m:
        return int(m.group(1))


def part1(filename):
    with open(filename) as f:
        lines = f.readlines()

    seed = parse(lines[0])
    generatorA = Generator(seed, 16807, 1)
    seed = parse(lines[1])
    generatorB = Generator(seed, 48271, 1)

    total = 0
    for i in range(40000000):
        if generatorA.gen() & 0xffff == generatorB.gen() & 0xffff:
            total += 1

    print(total)


def part2(filename):
    with open(filename) as f:
        lines = f.readlines()

    seed = parse(lines[0])
    generatorA = Generator(seed, 16807, 4)
    seed = parse(lines[1])
    generatorB = Generator(seed, 48271, 8)

    total = 0
    for i in range(5000000):
        if generatorA.gen() & 0xffff == generatorB.gen() & 0xffff:
            total += 1

    print(total)

if __name__ == '__main__':
    part1('day15input.txt')
    part2('day15input.txt')