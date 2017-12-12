#!/usr/bin/env python3

import re

import networkx as nx


def parse(line):
    m = re.match(r'(\d+) <-> (.*)', line)
    if m:
        srcVertex = int(m.group(1))

        dstVertices = m.group(2)
        dstVertices = dstVertices.split(', ')
        dstVertices = list(map(int, dstVertices))

        return srcVertex, dstVertices


def part1(filename):
    with open(filename) as f:
        lines = f.readlines()

    G = nx.Graph()
    for line in lines:
        srcVertex, dstVertices = parse(line)
        for dstVertex in dstVertices:
            G.add_edge(srcVertex, dstVertex)

    print(len(nx.bfs_tree(G, 0).nodes()))


def part2(filename):
    with open(filename) as f:
        lines = f.readlines()

    G = nx.Graph()
    for line in lines:
        srcVertex, dstVertices = parse(line)
        for dstVertex in dstVertices:
            G.add_edge(srcVertex, dstVertex)

    vertices = set(G.nodes())
    count = 0
    while vertices:
        vertices -= set(nx.bfs_tree(G, vertices.pop()).nodes())
        count += 1

    print(count)


if __name__ == '__main__':
    part1('day12input.txt')
    part2('day12input.txt')