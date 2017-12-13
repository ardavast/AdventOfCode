#!/usr/bin/env python3

import math
import re
import itertools

import networkx as nx


def parse(line):
    m = re.match(r'(\S+) to (\S+) = (\d+)', line)
    if m:
        return m.group(1), m.group(2), int(m.group(3))


def part1(filename):
    with open(filename) as f:
        lines = f.readlines()

    G = nx.Graph()
    for line in lines:
        v0, v1, d = parse(line)
        G.add_edge(v0, v1, distance=d)

    minDistance = math.inf
    for path in itertools.permutations(G.nodes()):
        distance = 0
        for i in range(len(path) - 1):
            distance += G[path[i]][path[i + 1]]['distance']
        if distance < minDistance:
            minDistance = distance
    print(minDistance)


def part2(filename):
    with open(filename) as f:
        lines = f.readlines()

    G = nx.Graph()
    for line in lines:
        v0, v1, d = parse(line)
        G.add_edge(v0, v1, distance=d)

    maxDistance = -math.inf
    for path in itertools.permutations(G.nodes()):
        distance = 0
        for i in range(len(path) - 1):
            distance += G[path[i]][path[i + 1]]['distance']
        if distance > maxDistance:
            maxDistance = distance
    print(maxDistance)


if __name__ == '__main__':
    part1('day09input.txt')
    part2('day09input.txt')