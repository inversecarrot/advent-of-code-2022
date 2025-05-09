
from io import TextIOWrapper
from advent_day import AdventDay
from day8.forest import Forest

class Day8(AdventDay):

    forest: Forest

    def __init__(self, input: TextIOWrapper):
        self.forest = Forest(input)

    def part1(self) -> str:
        return self.forest.calculate_cover()

    def part2(self) -> str:
        return self.forest.find_max_visibility()
