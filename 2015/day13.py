#!/usr/bin/env python3

import math
import itertools
import re

from collections import defaultdict


def parse(line):
    m = re.match(r'(.*) would (gain|lose) (\d+) happiness units by sitting next to (.*).$', line)
    if m:
        points = int(m.group(3))
        if m.group(2) == 'lose':
            points = -points
        return m.group(1), m.group(4), points


def computeHappiness(arrangement, happinessDict):
    happiness = 0
    for i in range(0, len(arrangement)):
        person = arrangement[i]
        prevPerson = arrangement[i - 1]
        nextPerson = arrangement[(i + 1) % len(arrangement)]
        happiness += happinessDict[person][prevPerson]
        happiness += happinessDict[person][nextPerson]

    return happiness


def part1(filename):
    with open(filename) as f:
        lines = f.readlines()

    happinessDict = defaultdict(dict)
    for line in lines:
        person0, person1, points = parse(line)
        happinessDict[person0][person1] = points

    maxHappiness = -math.inf
    persons = list(happinessDict.keys())
    for arrangement in itertools.permutations(persons):
        happiness = computeHappiness(arrangement, happinessDict)
        if happiness > maxHappiness:
            maxHappiness = happiness

    print(maxHappiness)


def part2(filename):
    with open(filename) as f:
        lines = f.readlines()

    happinessDict = defaultdict(dict)
    for line in lines:
        person0, person1, points = parse(line)
        happinessDict[person0][person1] = points
        happinessDict[person0]['me'] = 0
        happinessDict['me'][person0] = 0

    maxHappiness = -math.inf
    persons = list(happinessDict.keys())
    for arrangement in itertools.permutations(persons):
        happiness = computeHappiness(arrangement, happinessDict)
        if happiness > maxHappiness:
            maxHappiness = happiness

    print(maxHappiness)


if __name__ == '__main__':
    part1('day13input.txt')
    part2('day13input.txt')