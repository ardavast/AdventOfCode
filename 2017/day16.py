#!/usr/bin/env python3


def dance(programs, moves):
    programs = programs[:]

    for move in moves:
        if move[0] == 's':
            n = int(move[1:])
            programs = programs[-n:] + programs[:-n]
        if move[0] == 'x':
            posA, posB = move[1:].split('/')
            posA, posB = int(posA), int(posB)
            programs[posA], programs[posB] = programs[posB], programs[posA]
        if move[0] == 'p':
            programA, programB = move[1:].split('/')
            posA, posB = programs.index(programA), programs.index(programB)
            programs[posA], programs[posB] = programs[posB], programs[posA]

    return programs


def part1(filename):
    with open(filename) as f:
        line = f.readline()

    programs = 'abcdefghijklmnop'
    programs = list(programs)

    moves = line.split(',')

    programs = dance(programs, moves)

    programs = ''.join(programs)

    print(programs)


def part2(filename):
    with open(filename) as f:
        line = f.readline()

    programs = 'abcdefghijklmnop'
    programs = list(programs)

    moves = line.split(',')

    def findCycle(programs0, moves):
        cycle = 1
        programs = programs0[:]

        while True:
            programs = dance(programs, moves)

            if programs == programs0:
                break

            cycle += 1

        return cycle

    cycle = findCycle(programs, moves)

    for _ in range(1000000000 % cycle):
        programs = dance(programs, moves)

    programs = ''.join(programs)

    print(programs)


if __name__ == '__main__':
    part1('day16input.txt')
    part2('day16input.txt')