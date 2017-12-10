#!/usr/bin/env python3

import re
from collections import defaultdict, Counter


class Node:
    def __init__(self, name, weight, children):
        self.name = name
        self.weight = weight
        self.cumulativeWeight = weight
        self.children = children


def parse(line):
    programRegex = re.compile('^(\S+) \((\d+)\)(?: -> (.*))?$')
    line = line.strip()
    m = re.match(programRegex, line)
    if m:
        name = m.group(1)
        weight = int(m.group(2))
        if m.group(3):
            children = m.group(3).split(', ')
        else:
            children = None
    return name, weight, children


def findRoot(filename):
    programs = defaultdict(int)

    with open(filename) as f:
        for line in f:
            name, weight, children = parse(line)
            programs[name] += 1
            if children:
                for name in children:
                   programs[name] += 1

    for name in programs.keys():
        if programs[name] == 1:
            return name


def part1(filename):
    print(findRoot(filename))


def part2(filename):
    def isUnbalanced(node):
        if node.children:
            weights = []
            for name in node.children:
                weights.append(programs[name].cumulativeWeight)
            if len(set(weights)) != 1:
                return True
            else:
                return False

    def getUnbalancerData(node):
        if node.children:
            weights = []
            for name in node.children:
                weights.append(programs[name].cumulativeWeight)
            if len(set(weights)) != 1:
                ctr = Counter(weights)
                balancedWeight, _ = ctr.most_common()[0]
                unbalancedWeight, _ = ctr.most_common()[-1]
                for name in node.children:
                    if programs[name].cumulativeWeight == unbalancedWeight:
                        return name, unbalancedWeight, balancedWeight

    def computeCumulativeWeights(node):
        if node.children:
            for name in node.children:
                node.cumulativeWeight += computeCumulativeWeights(programs[name])
        return node.cumulativeWeight

    def findUnbalancer(node, unbalancer=None, weight=None, correctWeight=None):
        if isUnbalanced(node):
            name, weight, correctWeight = getUnbalancerData(node)
            unbalancer = name
            if node.children:
                for name in node.children:
                    unbalancer, weight, correctWeight = \
                      findUnbalancer(programs[name], unbalancer, weight, correctWeight)
        return unbalancer, weight, correctWeight

    programs = {}

    with open(filename) as f:
        for line in f:
            name, weight, children = parse(line)
            programs[name] = Node(name, weight, children)

    root = programs[findRoot(filename)]
    computeCumulativeWeights(root)
    unbalancer, weight, correctWeight = findUnbalancer(root)
    if unbalancer:
        if weight > correctWeight:
            print(unbalancer, programs[unbalancer].weight - (weight - correctWeight))
        else:
            print(unbalancer, programs[unbalancer].weight + (correctWeight - weight))


if __name__ == '__main__':
    part1('day07input.txt')
    part2('day07input.txt')