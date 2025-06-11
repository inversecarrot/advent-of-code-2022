from io import TextIOWrapper
import logging
from typing import List, Tuple
from advent_day import AdventDay
from day14.cave import Cave

log = logging.getLogger(__name__)

class Day14(AdventDay):
    input: TextIOWrapper
    lines: List[List[Tuple[int, int]]]
    min_x: int = -1
    max_x: int = -1
    max_y: int = -1

    def __init__(self, input: TextIOWrapper):
        super().__init__(input)
        self.input = input
        self._parse_input(input)

    def _parse_input(self, input: TextIOWrapper):
        lines = []
        for line in input:
            line = line.strip("\n")
            if line != "":
                points = []
                str_points = line.split(" -> ")
                for point in str_points:
                    pt = point.split(",")
                    x = int(pt[0])
                    y = int(pt[1])
                    if x < self.min_x or self.min_x == -1:
                        self.min_x = x
                    if x > self.max_x:
                        self.max_x = x
                    if y > self.max_y:
                        self.max_y = y
                    points.append((x, y))
                lines.append(points)
        self.lines = lines
      
    def part1(self):
        cave = Cave(self.min_x, self.max_x, self.max_y, self.lines)
        count = 0
        while cave.spawnSand() == True:
            count += 1
        return str(count)

    def part2(self):
        newmax = self.max_y + 2
        newlines = self.lines + [[(0, newmax), (1000, newmax)]]
        cave = Cave(0, 1000, newmax, newlines)
        count = 0
        while cave.spawnSand() == True:
            count += 1
        return str(count)