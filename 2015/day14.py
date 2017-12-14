#!/usr/bin/env python3

import re


class Reindeer:
    def __init__(self, name, speed, flyTime, restTime):
        self.name, self.speed, self.flyTime, self.restTime = \
          name, speed, flyTime, restTime

        self.action = 'fly'
        self.flyTicks = self.flyTime
        self.restTicks = self.restTime
        self.distance = 0
        self.points = 0

    def fly(self):
        self.distance += self.speed
        self.flyTicks -= 1

    def rest(self):
        self.restTicks -= 1

    def toggleAction(self):
        if self.action == 'fly':
            self.action = 'rest'
            self.restTicks = self.restTime
        elif self.action == 'rest':
            self.action = 'fly'
            self.flyTicks = self.flyTime

    def tick(self):
        if self.action == 'fly':
            self.fly()
            if self.flyTicks == 0:
                self.toggleAction()
        elif self.action == 'rest':
            self.rest()
            if self.restTicks == 0:
                self.toggleAction()


def parse(line):
    m = re.match(r'(.*) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.', line)
    if m:
        name = m.group(1)
        speed = int(m.group(2))
        flyTime = int(m.group(3))
        restTime = int(m.group(4))
        return name, speed, flyTime, restTime


def part1(filename):
    with open(filename) as f:
        lines = f.readlines()

    reindeerList = []
    for line in lines:
        name, speed, flyTime, restTime = parse(line)
        reindeerList.append(Reindeer(name, speed, flyTime, restTime))

    for _ in range(2503):
        for reindeer in reindeerList:
            reindeer.tick()

    maxDistance = 0
    for reindeer in reindeerList:
        if reindeer.distance > maxDistance:
            maxDistance = reindeer.distance

    print(maxDistance)


def part2(filename):
    with open(filename) as f:
        lines = f.readlines()

    reindeerList = []
    for line in lines:
        name, speed, flyTime, restTime = parse(line)
        reindeerList.append(Reindeer(name, speed, flyTime, restTime))

    for _ in range(2503):
        for reindeer in reindeerList:
            reindeer.tick()

        maxDistance = 0
        for reindeer in reindeerList:
            if reindeer.distance > maxDistance:
                maxDistance = reindeer.distance

        winners = []
        for reindeer in reindeerList:
            if reindeer.distance == maxDistance:
                reindeer.points += 1

    maxPoints = 0
    for reindeer in reindeerList:
        if reindeer.points > maxPoints:
            maxPoints = reindeer.points

    print(maxPoints)


if __name__ == '__main__':
    part1('day14input.txt')
    part2('day14input.txt')