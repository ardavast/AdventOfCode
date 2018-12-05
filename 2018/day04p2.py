#!/usr/bin/env python3
# coding: utf8

"""
Day 4: Repose Record part 2
https://adventofcode.com/2018/day/4
"""

import re
from collections import defaultdict, Counter


def main():
    guards = defaultdict(list)

    with open('day04input.txt') as f:
        for line in sorted(f):
            m = re.match(r'^\[\d+-\d+-\d+ \d+:(\d+)\] (.*)$', line)
            seconds = int(m.group(1))
            msg = m.group(2)

            m = re.match(r'^Guard #(\d+) begins shift$', msg)
            if m:
                guardID = int(m.group(1))
            elif 'falls' in msg:
                sleepStart = seconds
            elif 'wakes' in msg:
                sleepEnd = seconds
                guards[guardID].append(range(sleepStart, sleepEnd))

    minutes = Counter()
    for guardID in guards:
        for minute in range(60):
            for r in guards[guardID]:
                if minute in r:
                    minutes[(guardID, minute)] += 1

    [((guardID, minute), _)] = minutes.most_common(1)
    print(guardID * minute)


if __name__ == '__main__':
    main()
