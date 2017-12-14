#!/usr/bin/env python3

import re


class Product:
    def __init__(self, name, capacity, durability, flavor, texture, calories):
        self.name, self.capacity, self.durability, self.flavor, self.texture, self.calories = \
          name, capacity, durability, flavor, texture, calories


def parse(line):
    m = re.match(r'(.*): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)', line)
    if m:
        return m.group(1), int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5)), int(m.group(6))


def part1(filename):
    with open(filename) as f:
        lines = f.readlines()

    productList = []
    for line in lines:
        name, capacity, durability, flavor, texture, calories = parse(line)
        productList.append(Product(name, capacity, durability, flavor, texture, calories))

    maxScore = 0
    remaining = 100
    for i in range(0, remaining + 1):
        for j in range(0, remaining - i + 1):
            for k in range(0, remaining - i - j + 1):
                h = remaining - i - j - k

                capacity = (i * productList[0].capacity +
                            j * productList[1].capacity +
                            k * productList[2].capacity +
                            h * productList[3].capacity)
                capacity = max(0, capacity)

                durability = (i * productList[0].durability +
                              j * productList[1].durability +
                              k * productList[2].durability +
                              h * productList[3].durability)
                durability = max(0, durability)

                flavor = (i * productList[0].flavor +
                          j * productList[1].flavor +
                          k * productList[2].flavor +
                          h * productList[3].flavor)
                flavor = max(0, flavor)

                texture = (i * productList[0].texture +
                           j * productList[1].texture +
                           k * productList[2].texture +
                           h * productList[3].texture)
                texture = max(0, texture)

                score = capacity * durability * flavor * texture
                if score > maxScore:
                    maxScore = score

    print(maxScore)


def part2(filename):
    with open(filename) as f:
        lines = f.readlines()

    productList = []
    for line in lines:
        name, capacity, durability, flavor, texture, calories = parse(line)
        productList.append(Product(name, capacity, durability, flavor, texture, calories))

    maxScore = 0
    remaining = 100
    for i in range(0, remaining + 1):
        for j in range(0, remaining - i + 1):
            for k in range(0, remaining - i - j + 1):
                h = remaining - i - j - k

                capacity = (i * productList[0].capacity +
                            j * productList[1].capacity +
                            k * productList[2].capacity +
                            h * productList[3].capacity)
                capacity = max(0, capacity)

                durability = (i * productList[0].durability +
                              j * productList[1].durability +
                              k * productList[2].durability +
                              h * productList[3].durability)
                durability = max(0, durability)

                flavor = (i * productList[0].flavor +
                          j * productList[1].flavor +
                          k * productList[2].flavor +
                          h * productList[3].flavor)
                flavor = max(0, flavor)

                texture = (i * productList[0].texture +
                           j * productList[1].texture +
                           k * productList[2].texture +
                           h * productList[3].texture)
                texture = max(0, texture)

                calories = (i * productList[0].calories +
                            j * productList[1].calories +
                            k * productList[2].calories +
                            h * productList[3].calories)

                if calories != 500:
                    continue

                score = capacity * durability * flavor * texture
                if score > maxScore:
                    maxScore = score

    print(maxScore)


if __name__ == '__main__':
    part1('day15input.txt')
    part2('day15input.txt')