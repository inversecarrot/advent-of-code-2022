from io import TextIOWrapper
from advent_day import AdventDay
from day9.rope_grid import RopeGrid

class Day9(AdventDay):
    grid: RopeGrid

    def __init__(self, input: TextIOWrapper):
        self.grid = RopeGrid(input)
        super().__init__(input)

    def part1(self) -> str:
        return self.grid.get_tail_visits()

    def part2(self) -> str:
        return ""