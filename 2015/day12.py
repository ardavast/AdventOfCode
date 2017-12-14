#!/usr/bin/env python3

import operator
import re
import json
from functools import reduce


def part1(filename):
    with open(filename) as f:
        line = f.readline()

    numbers = map(int, re.findall(r'-?\d+', line))
    total = reduce(operator.add, numbers)

    print(total)


def part2(filename):
    with open(filename) as f:
        lines = f.readlines()

    def count(node, total=0):
        if isinstance(node, dict) and 'red' in node.values():
            return 0

        if isinstance(node, dict):
            elems = node.values()
        elif isinstance(node, list):
            elems = node

        for elem in elems:
            if isinstance(elem, int):
                total += elem
            if isinstance(elem, (dict, list)):
                total += count(elem)

        return total

    for line in lines:
        root = json.loads(line)
        print(count(root))


if __name__ == '__main__':
    part1('day12input.txt')
    part2('day12input.txt')